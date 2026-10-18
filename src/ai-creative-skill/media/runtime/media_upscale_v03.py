"""AI Creative Skill Media Upscale v0.3 experimental.

Adds a portable local Real-ESRGAN VIDEO route for reproducible short clips,
reusing v0.2 image/FFmpeg/ledger helpers. Every output is TECHNICAL_ONLY.
NO network, account access, paid execution, automatic download or publication.
"""
from __future__ import annotations
import argparse, fcntl, hashlib, json, os, shutil, subprocess, sys
from dataclasses import asdict, replace
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
from PIL import Image
from media_upscale_v02 import (MediaRequest, MediaError, IMAGE_CONV, IMAGE_NEURAL,
                               VIDEO_CONV, sha, quote as old_quote, run_image, run_video,
                               torch_status, video_probe, save_atomic, ts, neural_image, route_registry as legacy_registry)
import video_backend_v02 as baseline
ROOT = Path(__file__).resolve().parents[1]
V03_REGISTRY = ROOT/'registry/provider_capabilities_v0.3.json'
VIDEO_NEURAL_V03='local.realesrgan.srvgg.video.v0.3'
VERSION='0.3.0-EXPERIMENTAL'


def registry():
    doc=json.loads(V03_REGISTRY.read_text())
    st=(torch_status() if (ROOT/'models'/'realesr-general-wdn-x4v3.pth').is_file() else {'installed':False,'mps':False,'cuda':False})
    legacy={r['id']:r for r in legacy_registry()['routes']}
    for route in doc['routes']:
        if route['id']==VIDEO_NEURAL_V03:
            route['host_available']=(bool(shutil.which('ffmpeg') and shutil.which('ffprobe'))
                and st['installed'] and (ROOT/'models'/'realesr-general-wdn-x4v3.pth').is_file())
        else:
            route['host_available']=legacy.get(route['id'],{}).get('host_available',False)
    return doc


def preflight_video_neural(req:MediaRequest):
    if req.media_kind!='VIDEO' or req.route_id!=VIDEO_NEURAL_V03:
        raise MediaError('NEURAL_VIDEO_ROUTE_KIND_MISMATCH')
    if type(req.target_width)!=int or type(req.target_height)!=int or req.target_width<16 or req.target_height<16:
        raise MediaError('INVALID_TARGET_DIMENSIONS')
    if req.allow_paid_submission or req.allow_external_transfer or req.max_additional_cash_usd!='0.00':
        raise MediaError('PAID_OR_EXTERNAL_TRANSFER_BLOCKED')
    if req.device not in ('cpu','mps','cuda'):raise MediaError('DEVICE_UNSUPPORTED')
    if not 0 < req.neural_blend <=1:raise MediaError('INVALID_BLEND')
    source=Path(req.source)
    if not source.is_file():raise MediaError('SOURCE_UNAVAILABLE')
    if source.suffix.lower() not in ('.mp4','.mov','.mkv'):raise MediaError('UNSUPPORTED_INPUT_TYPE')
    r=next(x for x in registry()['routes'] if x['id']==VIDEO_NEURAL_V03)
    if not r['host_available']:raise MediaError('ROUTE_UNAVAILABLE_ON_HOST')
    st=torch_status()
    if req.device=='mps' and not st['mps']:raise MediaError('MPS_UNAVAILABLE')
    if req.device=='cuda' and not st['cuda']:raise MediaError('CUDA_UNAVAILABLE')
    p=baseline.probe(source)
    if p['sar'] not in ('1:1','N/A'):raise MediaError('NON_SQUARE_PIXEL_SOURCE_UNSUPPORTED')
    if p['subtitle_streams'] or p['audio_streams']>1:raise MediaError('MULTI_STREAM_SOURCE_UNSUPPORTED')
    if p['fps']<=0 or p['fps']>60 or abs(p['fps']-p['r_fps'])>.005:raise MediaError('NON_CONSTANT_FPS_UNSUPPORTED')
    if p['width']>req.target_width or p['height']>req.target_height:raise MediaError('TARGET_NOT_UPSCALE')
    if req.target_width%2 or req.target_height%2:raise MediaError('OUTPUT_DIMENSIONS_MUST_BE_EVEN')
    if req.target_width*req.target_height>r['max_pixels']:raise MediaError('ROUTE_PIXEL_CAP_EXCEEDED')
    if abs((req.target_width/req.target_height)/(p['width']/p['height'])-1)>.001:
        raise MediaError('ASPECT_RATIO_MISMATCH')
    if p['duration']>r['max_duration_seconds']+.001:raise MediaError('DURATION_LIMIT_EXCEEDED')
    if req.device=='cpu':
        if p['width']*p['height']>r['cpu_max_source_pixels'] or req.target_width*req.target_height>320*480:
            raise MediaError('CPU_NEURAL_DIMENSIONS_EXCEEDED')
    else:
        if p['width']*p['height']>r['max_source_pixels']:raise MediaError('NEURAL_SOURCE_DIMENSIONS_EXCEEDED')
    # count_frames on a short video, not trusting unverified header nb_frames
    z=subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-count_frames','-show_entries','stream=nb_read_frames','-of','default=noprint_wrappers=1:nokey=1',str(source)],capture_output=True,text=True,check=True)
    try:count=int(z.stdout.strip())
    except ValueError:raise MediaError('FRAME_COUNT_UNAVAILABLE')
    maximum=r['cpu_max_frames'] if req.device=='cpu' else (r['mps_max_frames'] if req.device=='mps' else r['cuda_max_frames'])
    if count>maximum:raise MediaError('DEVICE_FRAME_LIMIT_EXCEEDED')
    if count==0:raise MediaError('EMPTY_VIDEO')
    return r,p,count


def neural_quote(req):
    r,p,count=preflight_video_neural(req)
    weight=ROOT/'models'/'realesr-general-wdn-x4v3.pth'
    canonical={'request':{k:v for k,v in asdict(req).items() if k!='source'},'source_sha256':sha(req.source),
        'weight_sha256':sha(weight),'recipe_sha256':sha(__file__),'arch_sha256':sha(ROOT/'runtime/srvgg_arch.py'),
        'registry_sha256':sha(V03_REGISTRY),'version':VERSION,'source_video':p,'frames':count}
    fp=hashlib.sha256(json.dumps(canonical,sort_keys=True).encode()).hexdigest()
    return {'route':VIDEO_NEURAL_V03,'fingerprint':fp,'source_sha256':canonical['source_sha256'],'weight_sha256':canonical['weight_sha256'],
      'target':[req.target_width,req.target_height],'frames':count,'source_video':p,
      'cash_incremental_usd':'0.00','estimated_operational_cost_usd':None,'third_party_transfer':False,
      'status':'LOCAL_EXECUTABLE_PREFLIGHT', 'quality_status':'UNVERIFIED_VISUAL', 'classification':r['classification']}


def _read_exact(reader,count):
    blocks=[];total=0
    while total<count:
        chunk=reader.read(count-total)
        if not chunk:break
        blocks.append(chunk);total+=len(chunk)
    if total==0:return None
    if total!=count:raise MediaError('TRUNCATED_RAW_VIDEO_FRAME')
    return b''.join(blocks)


def _neural_encode(src,dst,req,info,frames,logdir):
    """Decode original motion frames once; reconstruct each and reuse source audio packets."""
    w,h=info['width'],info['height'];W,H=req.target_width,req.target_height
    # Streaming subprocesses with bounded memory; no shell or external URLs.
    rawframe=w*h*3
    demux=subprocess.Popen(['ffmpeg','-v','error','-nostdin','-i',str(src),'-map','0:v:0','-pix_fmt','rgb24',
             '-vsync','0','-f','rawvideo','pipe:1'],stdout=subprocess.PIPE,stderr=(logdir/'decode.err').open('wb'))
    silent=logdir/'silent_video.mp4'
    encode=subprocess.Popen(['ffmpeg','-v','error','-nostdin','-f','rawvideo','-pixel_format','rgb24',
             '-video_size',f'{W}x{H}','-framerate',str(info['fps_raw']),
             '-i','pipe:0','-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p',
             '-movflags','+faststart','-y',str(silent)],stdin=subprocess.PIPE,stderr=(logdir/'encode.err').open('wb'))
    # Load weights ONCE per job, not once per frame. Avoid unbounded device allocations.
    import torch
    from srvgg_arch import SRVGGNetCompact
    torch.set_num_threads(2)
    model=SRVGGNetCompact(num_in_ch=3,num_out_ch=3,num_feat=64,num_conv=32,upscale=4,act_type='prelu')
    blob=torch.load(ROOT/'models'/'realesr-general-wdn-x4v3.pth',map_location='cpu',weights_only=True)
    params=blob.get('params_ema',blob.get('params'))
    if params is None:raise MediaError('MODEL_WEIGHTS_INVALID')
    model.load_state_dict(params,strict=True)
    model.eval().to(req.device)
    seen=0
    try:
        while True:
            raw=_read_exact(demux.stdout,rawframe)
            if raw is None:break
            im=Image.fromarray(np.frombuffer(raw,dtype=np.uint8).reshape(h,w,3).copy(),'RGB')
            tensor=torch.from_numpy(np.asarray(im).copy()).permute(2,0,1).float().unsqueeze(0).div(255).to(req.device)
            with torch.inference_mode(): inferred=model(tensor)
            arr=inferred.squeeze(0).clamp(0,1).float().cpu().permute(1,2,0).numpy()
            if not np.isfinite(arr).all():raise MediaError('NONFINITE_VIDEO_FRAME')
            full=Image.fromarray(np.uint8(np.clip(arr*255+0.5,0,255)))
            scaled=full.resize((W,H),Image.Resampling.LANCZOS)
            if req.neural_blend<1:
                conventional=im.resize((W,H),Image.Resampling.LANCZOS)
                scaled=Image.blend(conventional,scaled,req.neural_blend)
            encode.stdin.write(scaled.tobytes())
            seen+=1
        encode.stdin.close();encode.stdin=None
        if demux.wait()!=0 or encode.wait()!=0 or seen!=frames:
            raise MediaError('ENCODE_DECODE_COUNT_MISMATCH')
        cmd=['ffmpeg','-v','error','-nostdin','-i',str(silent),'-i',str(src),'-map','0:v:0']
        if info['audio_streams']:
            cmd+=['-map','1:a:0']
        cmd+=['-c:v','copy','-c:a','copy','-movflags','+faststart','-y',str(dst)]
        x=subprocess.run(cmd,capture_output=True,timeout=90)
        if x.returncode!=0:raise MediaError('FINAL_MUX_FAILED')
    finally:
        if demux.poll() is None:demux.kill();demux.wait()
        if encode.poll() is None:encode.kill();encode.wait()
    return seen


def run_neural_video(req,output_dir):
    q=neural_quote(req)
    src=Path(req.source).resolve();folder=Path(output_dir).resolve();folder.mkdir(parents=True,exist_ok=True)
    fp=q['fingerprint']; target=folder/(src.stem+'_neural_'+fp[:12]+'.mp4')
    if target==src:raise MediaError('SOURCE_OVERWRITE_FORBIDDEN')
    ledger=folder/'video_neural_ledger.json'
    with (folder/'video_neural_ledger.lock').open('a+b') as lf:
        fcntl.flock(lf.fileno(),fcntl.LOCK_EX)
        state=json.loads(ledger.read_text()) if ledger.exists() else {}
        if fp in state:
            item=state[fp];stored=folder/item['output_file']
            if item['state']=='COMPLETE' and stored.is_file() and sha(stored)==item['output_sha256']:
                return {'status':'IDEMPOTENT_REUSE','output':str(stored),'qa':item['qa'],'quote':q}
            raise MediaError('RECOVERY_REQUIRED_NEVER_REPEAT_UNKNOWN')
        if target.exists():raise MediaError('OUTPUT_COLLISION')
        state[fp]={'state':'SUBMITTING','output_file':target.name,'requested_at':ts(),'route':VIDEO_NEURAL_V03,
                   'source_sha256':q['source_sha256'],'device':req.device};save_atomic(ledger,state)
        tmp=folder/('.partial_'+fp[:12]);tmp.mkdir(exist_ok=False)
        partial=tmp/'result.mp4'
        try:
            r,info,frames=preflight_video_neural(req)
            n=_neural_encode(src,partial,req,info,frames,tmp)
            if sha(src)!=q['source_sha256']:raise MediaError('SOURCE_CHANGED_DURING_PROCESS')
            qa=baseline.inspect_result(src,partial,{'target_width':req.target_width,'target_height':req.target_height})
            # Additional whole-decode check to detect trailing decoder errors.
            dec=subprocess.run(['ffmpeg','-v','error','-xerror','-i',str(partial),'-f','null','-'],capture_output=True,timeout=90)
            qa['checks']['full_decode_success']=dec.returncode==0
            qa['checks']['frames_processed_match']=n==q['frames']
            qa['status']='PASS' if all(qa['checks'].values()) else 'FAIL'
            qa['quality_verdict']='UNVERIFIED';qa['route_classification']='NEURAL_FRAME_BY_FRAME'
            qa['limits']=['No perceptual video fidelity proven','No motion-compensated flicker test','No logo/label identity verification','Work Mac MPS quality result still PARTIAL']
            if qa['status']!='PASS':raise MediaError('NEURAL_VIDEO_TECHNICAL_QA_FAILED')
            os.replace(partial,target)
            state[fp].update({'state':'COMPLETE','completed_at':ts(),'output_sha256':sha(target),'qa':qa,
                 'quality_verdict':'UNVERIFIED','provider_fee_usd':'0.00','energy_cost_usd':None});save_atomic(ledger,state)
            shutil.rmtree(tmp)
            return {'status':'EXECUTED_TECHNICAL_QA_PASS','output':str(target),'qa':qa,'quote':q}
        except Exception as e:
            state[fp].update({'state':'UNKNOWN','error_type':e.__class__.__name__,'failed_at':ts()});save_atomic(ledger,state)
            raise


def main():
    p=argparse.ArgumentParser()
    p.add_argument('operation',choices=['routes','quote','run'])
    p.add_argument('--source');p.add_argument('--width',type=int);p.add_argument('--height',type=int)
    p.add_argument('--kind',choices=['IMAGE','VIDEO'],default='IMAGE');p.add_argument('--route');p.add_argument('--device',default='cpu')
    p.add_argument('--blend',type=float,default=0.35);p.add_argument('--output-dir',default='outputs')
    a=p.parse_args()
    if a.operation=='routes':print(json.dumps(registry(),indent=2));return
    if not a.source or not a.width or not a.height:p.error('--source --width --height required')
    rid=a.route or (IMAGE_CONV if a.kind=='IMAGE' else VIDEO_CONV)
    req=MediaRequest(a.source,a.width,a.height,route_id=rid,media_kind=a.kind,device=a.device,neural_blend=a.blend)
    if rid==VIDEO_NEURAL_V03:
        result=neural_quote(req) if a.operation=='quote' else run_neural_video(req,a.output_dir)
    elif a.operation=='quote':result=old_quote(req)
    elif a.kind=='IMAGE':result=run_image(req,a.output_dir)
    else:result=run_video(req,a.output_dir)
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    try:main()
    except MediaError as e:
        print(json.dumps({'status':'BLOCKED','reason':str(e)}),file=sys.stderr);sys.exit(2)
