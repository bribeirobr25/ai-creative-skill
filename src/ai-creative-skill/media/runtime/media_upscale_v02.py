"""AI Creative Skill Media Upscale v0.2: experimental, provider-neutral offline slice.

IMAGE_UPSCALE: executable Pillow Lanczos and optional local Real-ESRGAN SRVGG.
VIDEO_UPSCALE: existing v0.1 FFmpeg route retained; v0.2 flexible-route quote layer.
No cloud calls, subscriptions, paid inference, or implicit model downloads.
TECHNICAL_QA_PASS is never a claim of faithful recovered detail.
"""
from __future__ import annotations
import argparse
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
import hashlib, json, os, subprocess, sys, fcntl, shutil
from PIL import Image, ImageOps
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
REGISTRY_PATH=ROOT/'registry/provider_capabilities_v0.2.json'
VERSION='0.2.0-EXPERIMENTAL'
IMAGE_CONV='local.pillow.lanczos.image.v0.2'
IMAGE_NEURAL='local.realesrgan.srvgg.image.v0.2'
VIDEO_CONV='local.ffmpeg.lanczos.video.v0.2'
VIDEO_NEURAL='local.realesrgan.srvgg.mps.video.v0.2'

class MediaError(Exception): pass

def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        while b:=f.read(1<<20): h.update(b)
    return h.hexdigest()

def ts():return datetime.now(timezone.utc).isoformat()

def save_atomic(path,data):
    path=Path(path); tmp=path.with_name(path.name+'.tmp')
    tmp.write_text(json.dumps(data,ensure_ascii=False,indent=2,sort_keys=True),encoding='utf-8')
    os.replace(tmp,path)

def torch_status():
    try:
        import torch
        return {'installed':True,'mps':bool(hasattr(torch.backends,'mps') and torch.backends.mps.is_available()),'cuda':bool(torch.cuda.is_available()),'version':torch.__version__}
    except ImportError:return {'installed':False,'mps':False,'cuda':False}

def route_registry():
    doc=json.loads(REGISTRY_PATH.read_text())
    for route in doc['routes']:
        if route['id']==IMAGE_CONV:route['host_available']=True
        elif route['id']==VIDEO_CONV:route['host_available']=bool(shutil.which('ffmpeg') and shutil.which('ffprobe'))
        elif route['id']==IMAGE_NEURAL:route['host_available']=all((ROOT/'models'/n).is_file() for n in route['weight_names']) and torch_status()['installed']
        else:route['host_available']=False # Work-verified route has not been generalized to this host/package.
    return doc

@dataclass(frozen=True)
class MediaRequest:
    source: str
    target_width: int
    target_height: int
    route_id: str = IMAGE_CONV
    media_kind: str = 'IMAGE'
    allow_paid_submission: bool = False
    max_additional_cash_usd: str = '0.00'
    allow_external_transfer: bool = False
    device: str = 'cpu'  # Explicit: cpu, mps, cuda. No silent device change.
    neural_blend: float = 1.0  # 1.0 neural; 0.35 D-inspired blend, NOT image quality approved
    def validate(self):
        p=Path(self.source)
        if not p.is_file():raise MediaError('SOURCE_UNAVAILABLE')
        if self.media_kind not in ('IMAGE','VIDEO'):raise MediaError('UNSUPPORTED_MEDIA_KIND')
        if type(self.target_width)!=int or type(self.target_height)!=int:raise MediaError('INVALID_DIMENSIONS')
        if min(self.target_width,self.target_height)<16:raise MediaError('INVALID_DIMENSIONS')
        if not isinstance(self.allow_paid_submission,bool) or self.allow_paid_submission:raise MediaError('PAID_SUBMISSION_BLOCKED')
        if self.allow_external_transfer:raise MediaError('THIRD_PARTY_TRANSFER_BLOCKED')
        try:d=Decimal(self.max_additional_cash_usd)
        except (InvalidOperation,ValueError,TypeError):raise MediaError('INVALID_BUDGET')
        if not d.is_finite() or d<0:raise MediaError('INVALID_BUDGET')
        if not (0.0<self.neural_blend<=1.0):raise MediaError('INVALID_NEURAL_BLEND')
        options=[r for r in route_registry()['routes'] if r['id']==self.route_id]
        if not options:raise MediaError('ROUTE_UNKNOWN')
        r=options[0]
        if r['media_kind']!=self.media_kind:raise MediaError('ROUTE_KIND_MISMATCH')
        if r['status'] not in ('EXECUTABLE_EXPERIMENTAL','EXECUTABLE_BASELINE'):raise MediaError('ROUTE_NOT_PACKAGED_EXECUTABLE')
        if not r['host_available']:raise MediaError('ROUTE_UNAVAILABLE_ON_HOST')
        if self.target_width*self.target_height>r['max_pixels']:raise MediaError('ROUTE_PIXEL_CAP_EXCEEDED')
        if r.get('even_dimensions') and (self.target_width%2 or self.target_height%2):raise MediaError('ROUTE_REQUIRES_EVEN_DIMENSIONS')
        if self.media_kind=='IMAGE':
            if p.suffix.lower() not in ('.png','.jpg','.jpeg','.webp','.tif','.tiff'):raise MediaError('UNSUPPORTED_IMAGE_TYPE')
            with Image.open(p) as x:
                if getattr(x,'n_frames',1)!=1:raise MediaError('ANIMATED_IMAGE_NOT_SUPPORTED')
                sx=ImageOps.exif_transpose(x);w,h=sx.size
                if self.target_width<w or self.target_height<h:raise MediaError('TARGET_NOT_UPSCALE')
                if abs((self.target_width/self.target_height)/(w/h)-1)>0.005:raise MediaError('ASPECT_RATIO_MISMATCH')
            if self.route_id==IMAGE_NEURAL:
                if self.device not in ('cpu','cuda','mps'):raise MediaError('DEVICE_UNSUPPORTED')
                st=torch_status()
                if self.device=='mps' and not st['mps']:raise MediaError('MPS_UNAVAILABLE')
                if self.device=='cuda' and not st['cuda']:raise MediaError('CUDA_UNAVAILABLE')
                if self.device=='cpu' and self.target_width*self.target_height>r['cpu_max_pixels']:raise MediaError('CPU_NEURAL_CAP_EXCEEDED')
                if self.device=='mps' and self.target_width*self.target_height>r['mps_max_pixels']:raise MediaError('MPS_NEURAL_CAP_EXCEEDED')
        else:
            if p.suffix.lower() not in ('.mp4','.mov','.mkv'):raise MediaError('UNSUPPORTED_VIDEO_TYPE')
            if self.route_id!=VIDEO_CONV:raise MediaError('NEURAL_VIDEO_RECIPE_NOT_PACKAGED_EXECUTABLE')
            meta=video_probe(p)
            if meta['duration']>r['max_duration_seconds']:raise MediaError('ROUTE_DURATION_LIMIT')
            if meta['width']>self.target_width or meta['height']>self.target_height:raise MediaError('TARGET_NOT_UPSCALE')
            if abs((self.target_width/self.target_height)/(meta['width']/meta['height'])-1)>0.005:raise MediaError('ASPECT_RATIO_MISMATCH')
            if meta['fps']>60 or meta['fps']<=0:raise MediaError('INVALID_SOURCE_FPS')
        return r

def video_probe(path):
    z=subprocess.run(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(path)],capture_output=True,check=True)
    val=json.loads(z.stdout);v=next(s for s in val['streams'] if s['codec_type']=='video')
    fps=[float(x) for x in v['avg_frame_rate'].split('/')]
    return {'width':v['width'],'height':v['height'],'fps':fps[0]/fps[1],'duration':float(v.get('duration',val['format']['duration'])),'frames':int(v.get('nb_frames') or 0),'audio_count':sum(s['codec_type']=='audio' for s in val['streams']),'subtitle_count':sum(s['codec_type']=='subtitle' for s in val['streams']),'sar':v.get('sample_aspect_ratio','1:1')}

def quote(req):
    route=req.validate()
    source_hash=sha(req.source)
    # hash route manifest and model checkpoints so changed weights/limits invalidate old approvals
    weights={n:sha(ROOT/'models'/n) for n in route.get('weight_names',[])}
    request_semantics=asdict(req); request_semantics.pop('source')  # identity from content hash, not host-local path
    canonical={'request':request_semantics,'source_sha256':source_hash,'route':route['id'],'registry_sha256':sha(REGISTRY_PATH),'weights':weights,'implementation_sha256':sha(__file__),'version':VERSION}
    fp=hashlib.sha256(json.dumps(canonical,sort_keys=True).encode()).hexdigest()
    return {'quote_id':fp[:24],'fingerprint':fp,'route':route['id'],'source_sha256':source_hash,'weights_sha256':weights,'classification':route['classification'],'media_kind':req.media_kind,
        'cash_incremental_usd':'0.00','imputed_subscription_usd':'0.00','operational_total_cost_usd':None,'cost_confidence':'PROVIDER_FEE_ONLY_NOT_ENERGY',
        'third_party_transfer':False,'status':'LOCAL_EXECUTABLE_PREFLIGHT' ,'quality_verdict':'UNVERIFIED','created_at':ts(), 'target':[req.target_width,req.target_height]}

def neural_image(source_image,req,weights_dir=ROOT/'models'):
    import torch
    from srvgg_arch import SRVGGNetCompact
    # Only official bundled weights verified by SHA in quote; no unsafe remote pickle execution.
    torch.set_num_threads(2)
    n=SRVGGNetCompact(num_in_ch=3,num_out_ch=3,num_feat=64,num_conv=32,upscale=4,act_type='prelu')
    # Conservative WDN model used in Work profile C; does NOT certify text/brand fidelity.
    blob=torch.load(weights_dir/'realesr-general-wdn-x4v3.pth',map_location='cpu',weights_only=True)
    state=blob.get('params_ema',blob.get('params'))
    if state is None:raise MediaError('WEIGHTS_INVALID')
    n.load_state_dict(state,strict=True)
    n.eval().to(req.device)
    img=source_image.convert('RGB')
    arr=np.asarray(img)
    x=torch.from_numpy(arr.copy()).permute(2,0,1).float().unsqueeze(0).div(255).to(req.device)
    with torch.inference_mode():
        y=n(x)
    y=y.squeeze(0).clamp(0,1).float().cpu().permute(1,2,0).numpy()
    if not np.isfinite(y).all():raise MediaError('NONFINITE_NEURAL_OUTPUT')
    full=Image.fromarray(np.uint8(np.clip(y*255+0.5,0,255)))
    neural=full.resize((req.target_width,req.target_height),Image.Resampling.LANCZOS)
    if req.neural_blend<1.0:
        conv=img.resize((req.target_width,req.target_height),Image.Resampling.LANCZOS)
        neural=Image.blend(conv,neural,req.neural_blend)
    return neural

def inspect_image(src,result,req):
    with Image.open(src) as im:
        ori=ImageOps.exif_transpose(im); source_size=ori.size;alpha='A' in ori.getbands()
    with Image.open(result) as out:
        output_size=out.size;out_alpha='A' in out.getbands();type_ok=out.format=='PNG'
    checks={'dimensions_exact':output_size==(req.target_width,req.target_height),'aspect_ratio_preserved':abs((output_size[0]/output_size[1])/(source_size[0]/source_size[1])-1)<=.005,
            'image_decodes':type_ok,'source_unchanged':sha(src)!=sha(result),'alpha_preserved_if_present':not alpha or out_alpha,'larger_than_original':output_size[0]>=source_size[0] and output_size[1]>=source_size[1]}
    return {'status':'TECHNICAL_QA_PASS' if all(checks.values()) else 'TECHNICAL_QA_FAIL','checks':checks,'source_size':source_size,'output_size':output_size,
            'fidelity_verdict':'UNVERIFIED','limits':['No recovery of true details proven','Brand logo/label not validated','No hallucination/face assessment','No calibrated color delta E evaluation'],
            'output_sha256':sha(result),'source_sha256':sha(src)}

def run_image(req,output_dir):
    if req.media_kind!='IMAGE':raise MediaError('IMAGE_ONLY_EXECUTOR')
    q=quote(req); folder=Path(output_dir).resolve();folder.mkdir(parents=True,exist_ok=True)
    src=Path(req.source).resolve();fp=q['fingerprint']; result=folder/(src.stem+'_'+req.route_id.replace('.','_')+'_'+fp[:10]+'.png')
    if result==src:raise MediaError('DO_NOT_OVERWRITE_SOURCE')
    ledger=folder/'image_execution_ledger.json'
    with (folder/'image_execution_ledger.lock').open('a+b') as lock:
        fcntl.flock(lock.fileno(),fcntl.LOCK_EX)
        state=json.loads(ledger.read_text()) if ledger.exists() else {}
        if fp in state:
            x=state[fp]
            if x.get('state')=='COMPLETE':
                stored=folder/x['output_file'] if 'output_file' in x else Path(x.get('output',''))
                if stored.is_file() and sha(stored)==x['output_sha256']:
                    return {'state':'IDEMPOTENT_REUSE','output':str(stored),'qa':x['qa'],'quote':q}
            raise MediaError('RECOVERY_REQUIRED_NEVER_RESUBMIT_UNKNOWN')
        if result.exists():raise MediaError('OUTPUT_COLLISION')
        state[fp]={'state':'SUBMITTING','started_at':ts(),'source_sha256':q['source_sha256'],'route_id':req.route_id,'output_file':result.name};save_atomic(ledger,state)
        partial=folder/(result.stem+'.partial.png')
        try:
            with Image.open(src) as original:
                x=ImageOps.exif_transpose(original)
                color_profile=x.info.get('icc_profile')
                if req.route_id==IMAGE_CONV:
                    if x.mode not in ('RGB','RGBA','L','LA'):x=x.convert('RGB')
                    result_image=x.resize((req.target_width,req.target_height),Image.Resampling.LANCZOS)
                else:
                    if 'A' in x.getbands():raise MediaError('NEURAL_ALPHA_NOT_SUPPORTED')
                    result_image=neural_image(x,req)
                options={'icc_profile':color_profile} if color_profile else {}
                # Strip EXIF by design: avoid leaking location/GPS data. Correct orientation first.
                result_image.save(partial,format='PNG',**options)
            if sha(src)!=q['source_sha256']:raise MediaError('INPUT_MUTATED_DURING_EXECUTION')
            qa=inspect_image(src,partial,req)
            if qa['status']!='TECHNICAL_QA_PASS':raise MediaError('TECHNICAL_QA_FAILED')
            os.replace(partial,result)
            state[fp].update({'state':'COMPLETE','completed_at':ts(),'output_sha256':sha(result),'qa':qa,'quality_verdict':'UNVERIFIED','cash_incremental_usd':'0.00','energy_cost_usd':None})
            save_atomic(ledger,state)
            return {'state':'EXECUTED_TECHNICAL_QA_PASS','output':str(result),'qa':qa,'quote':q}
        except Exception as e:
            state[fp].update({'state':'UNKNOWN','exception_class':e.__class__.__name__,'failed_at':ts()});save_atomic(ledger,state)
            raise

def run_video(req, output_dir):
    """Reuses the prior v0.1 FFmpeg execution/QA/ledger, with route-specific pixel caps."""
    if req.media_kind != 'VIDEO': raise MediaError('VIDEO_ONLY_EXECUTOR')
    quote(req)  # stricter media and capabilities preflight
    import video_backend_v02 as vb
    legacy=vb.Request(source=req.source,target_width=req.target_width,target_height=req.target_height,provider=VIDEO_CONV)
    try: return vb.run_ffmpeg(legacy,output_dir)
    except vb.UpscaleError as e: raise MediaError(str(e)) from e

def main():
    p=argparse.ArgumentParser();p.add_argument('operation',choices=['routes','quote','run']);p.add_argument('--source');p.add_argument('--width',type=int);p.add_argument('--height',type=int);p.add_argument('--media-kind',choices=['IMAGE','VIDEO'],default='IMAGE');p.add_argument('--route',default=IMAGE_CONV);p.add_argument('--device',default='cpu');p.add_argument('--blend',type=float,default=1.0);p.add_argument('--output-dir',default='outputs')
    a=p.parse_args()
    if a.operation=='routes':print(json.dumps(route_registry(),indent=2));return
    if not a.source or not a.width or not a.height:p.error('source, width and height required')
    req=MediaRequest(source=a.source,target_width=a.width,target_height=a.height,media_kind=a.media_kind,route_id=a.route,device=a.device,neural_blend=a.blend)
    if a.operation=='quote':x=quote(req)
    elif req.media_kind=='IMAGE':x=run_image(req,a.output_dir)
    else:x=run_video(req,a.output_dir)
    print(json.dumps(x,indent=2))
if __name__=='__main__':
    try:main()
    except MediaError as e:
        print(json.dumps({'status':'BLOCKED','code':str(e)}),file=sys.stderr);sys.exit(2)
