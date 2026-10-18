"""Experimental provider-neutral VIDEO_UPSCALE slice. Only FFmpeg local is executable.

Design boundary: imports no Higgsfield/fal/cloud SDK; paid routes are deliberately unimplemented.
Not a neural model and not a production-ready distributed job orchestrator.
"""
from __future__ import annotations
import argparse
import contextlib
import dataclasses
from decimal import Decimal
import fcntl
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from datetime import datetime, timezone, timedelta

VERSION = '0.2.0-route-cap-experimental'
ROUTE = 'local.ffmpeg.lanczos.video.v0.2'

class UpscaleError(Exception):
    pass


def digest(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        while block:=f.read(1024*1024):h.update(block)
    return h.hexdigest()


def iso():return datetime.now(timezone.utc).isoformat()


def command(args, timeout=90):
    try:
        return subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True,timeout=timeout)
    except (FileNotFoundError,subprocess.CalledProcessError,subprocess.TimeoutExpired) as e:
        err=(e.stderr or b'').decode(errors='replace')[-1800:] if isinstance(e,subprocess.CalledProcessError) else str(e)
        raise UpscaleError(f'Command failed: {args[0]}: {err}') from e


def probe(path):
    output=command(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(path)])
    val=json.loads(output.stdout)
    vs=[s for s in val.get('streams',[]) if s.get('codec_type')=='video']
    aud=[s for s in val.get('streams',[]) if s.get('codec_type')=='audio']
    if len(vs)!=1:raise UpscaleError('MVP supports exactly one video stream')
    v=vs[0]
    def fraction(s):
        p=str(s).split('/')
        try:return float(p[0])/float(p[1]) if len(p)==2 else float(s)
        except (ValueError,ZeroDivisionError):return 0.0
    info={
        'width':int(v['width']),'height':int(v['height']),
        'fps':fraction(v.get('avg_frame_rate','0/0')),
        'r_fps':fraction(v.get('r_frame_rate','0/0')),
        'fps_raw':v.get('avg_frame_rate'),
        'frame_count':int(v['nb_frames']) if v.get('nb_frames','').isdigit() else None,
        'duration':float(v.get('duration',val.get('format',{}).get('duration',0))),
        'sar':v.get('sample_aspect_ratio','1:1'),
        'codec':v.get('codec_name'),'audio_streams':len(aud),
        'audio_codecs':[a.get('codec_name') for a in aud],
        'subtitle_streams':len([s for s in val.get('streams',[]) if s.get('codec_type')=='subtitle']),
        'total_streams':len(val.get('streams',[])),
    }
    return info


@dataclasses.dataclass(frozen=True)
class Request:
    source: str
    target_width: int
    target_height: int
    provider: str = ROUTE
    max_additional_cash_usd: str = '0.00'
    allow_paid_submission: bool = False
    preserve_audio: bool = True
    preserve_fps: bool = True
    def validate(self):
        if not Path(self.source).is_file():raise UpscaleError('Local source file absent: '+self.source)
        if Path(self.source).suffix.lower() not in {'.mp4','.mov','.mkv'}:raise UpscaleError('Unsupported input extension')
        if self.target_width<16 or self.target_height<16 or self.target_width%2 or self.target_height%2:raise UpscaleError('Dimensions must be even and >=16')
        
        route_doc=json.loads((Path(__file__).resolve().parents[1]/'registry/provider_capabilities_v0.2.json').read_text())
        route_spec=next(r for r in route_doc['routes'] if r['id']==ROUTE)
        if self.target_width*self.target_height>route_spec['max_pixels']:raise UpscaleError('ROUTE_PIXEL_CAP_EXCEEDED')
        try:limit=Decimal(self.max_additional_cash_usd)
        except Exception as e:raise UpscaleError('Invalid cash budget') from e
        if not limit.is_finite() or limit<0:raise UpscaleError('Invalid cash budget')
        if self.allow_paid_submission:raise UpscaleError('PAID_SUBMISSION_BLOCKED: paid routes are not implemented in MVP')
        if self.provider!=ROUTE:raise UpscaleError('EXECUTABLE_PROVIDER_UNAVAILABLE: only local FFmpeg is implemented')
        if not self.preserve_fps or not self.preserve_audio:raise UpscaleError('MVP only supports strict temporal and audio preservation')
        x=probe(self.source)
        if x['sar'] not in ('1:1','N/A'):raise UpscaleError('Non-square pixels require a different route')
        if x['fps']<=0 or abs(x['fps']-x['r_fps'])>0.005:raise UpscaleError('Variable/unknown frame rate unsupported for strict-preservation MVP')
        if x['fps']>60:raise UpscaleError('MVP source FPS above 60 not supported')
        if x['duration']>30:raise UpscaleError('MVP input duration above 30 seconds not supported')
        if Path(self.source).stat().st_size>100_000_000:raise UpscaleError('MVP input above 100 MB not supported')
        if x['width']>self.target_width or x['height']>self.target_height:raise UpscaleError('Upscale target smaller than original')
        a=x['width']/x['height'];b=self.target_width/self.target_height
        if abs(a-b)/a>.005:raise UpscaleError('ASPECT_MISMATCH: no cropping, padding or stretching without separate approval')
        if x['subtitle_streams']:raise UpscaleError('MVP does not preserve subtitles')
        if x['audio_streams']>1:raise UpscaleError('MVP supports at most one audio stream')
        return x


def fingerprint(request,source_hash,ffmpeg_version='ffmpeg'):
    data={**dataclasses.asdict(request),'source':str(Path(request.source).resolve()),'sha256':source_hash,'version':VERSION,'route':ROUTE,'engine':ffmpeg_version}
    return hashlib.sha256(json.dumps(data,sort_keys=True).encode()).hexdigest()


def available_routes():
    ff=shutil.which('ffmpeg') and shutil.which('ffprobe')
    vulkan=shutil.which('vulkaninfo') is not None
    return [
        {'id':ROUTE,'transport':'LOCAL_CLI','neural':False,'available':bool(ff),'implemented':True,'provider_fee_usd':'0.00','total_operational_cost_usd':None},
        {'id':'local.video2x.realesrgan.v0','transport':'LOCAL_CLI','neural':True,'available':bool(shutil.which('video2x') and vulkan),'implemented':False,'reason':'capability probe only; no validated recipe or weights/license/QA'},
        {'id':'mock.fal.bytedance.v0','transport':'MOCK','neural':True,'available':False,'implemented':False,'reason':'simulation only; zero paid calls'},
        {'id':'mock.byteplus.direct.v0','transport':'MOCK','neural':True,'available':False,'implemented':False,'reason':'simulation only; zero paid calls'},
        {'id':'mock.bfl.direct.v0','transport':'MOCK','neural':True,'available':False,'implemented':False,'reason':'simulation only; zero paid calls'},
    ]


def quote(req):
    info=req.validate()
    src_hash=digest(req.source)
    engine_version=command(['ffmpeg','-version'],timeout=10).stdout.decode(errors='replace').splitlines()[0]
    fp=fingerprint(req,src_hash,engine_version)
    return {'engine_version':engine_version,'quote_id':fp[:24],'fingerprint':fp,'source_sha256':src_hash,'route':req.provider,
            'neural':False,'classification':'CONVENTIONAL_RESAMPLE_NOT_AI_SUPER_RESOLUTION',
            'cash_incremental_usd':'0.00','imputed_subscription_cost_usd':'0.00',
            'provider_fee_usd':'0.00','estimated_total_operational_cost_usd':None,
            'cost_confidence':'PARTIAL_OPERATIONS_NOT_MEASURED',
            'cost_limit_usd':req.max_additional_cash_usd,'billing_authorization_required':False,
            'third_party_upload':False,'source_info':info,'generated_at':iso()}


def pcm_digest(path, audio_index=0):
    # Raw PCM decoded from the first audio track; compares samples rather than compressed packet framing.
    p=subprocess.Popen(['ffmpeg','-v','error','-i',str(path),'-map',f'0:a:{audio_index}',
        '-acodec','pcm_s16le','-f','s16le','pipe:1'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    h=hashlib.sha256()
    while True:
        block=p.stdout.read(65536)
        if not block:break
        h.update(block)
    err=p.stderr.read().decode(errors='replace')
    code=p.wait()
    p.stdout.close()
    p.stderr.close()
    if code!=0:raise UpscaleError('Cannot decode audio for QA: '+err[-500:])
    return h.hexdigest()


def inspect_result(source, output, planned, out_file=None):
    a=probe(source);b=probe(output)
    fps_tol=0.0001
    checks={
        'dimensions_exact':b['width']==planned['target_width'] and b['height']==planned['target_height'],
        'fps_preserved':abs(a['fps']-b['fps'])<fps_tol,
        'duration_within_one_frame':abs(a['duration']-b['duration']) <= (1/a['fps'])+0.001,
        'frame_count_equal_when_known':a['frame_count'] is None or b['frame_count']==a['frame_count'],
        'audio_streams_equal':a['audio_streams']==b['audio_streams'],
        'aspect_preserved':abs((a['width']/a['height'])-(b['width']/b['height']))/(a['width']/a['height'])<=0.005,
    }
    audio_evidence=None
    if checks['audio_streams_equal'] and a['audio_streams']>0:
        src_audio=pcm_digest(source);out_audio=pcm_digest(output)
        audio_evidence={'source_decoded_pcm_sha256':src_audio,'output_decoded_pcm_sha256':out_audio}
        checks['decoded_audio_bit_identical']=src_audio==out_audio
    else:checks['decoded_audio_bit_identical']=a['audio_streams']==0 and b['audio_streams']==0
    checks['output_changed_source_unchanged']=digest(source)!=digest(output)
    out={
        'kind':'TECHNICAL_QA_ONLY','status':'PASS' if all(checks.values()) else 'FAIL',
        'source':a,'output':b,'checks':checks,'audio_evidence':audio_evidence,
        'limitations':['No face/product/label preservation QA','No flicker or perceptual quality QA','No neural detail reconstruction','No HDR/color-space validation','No subtitles/attachments support','Not proof of user satisfaction'],
        'assessed_at':iso()
    }
    if out_file:Path(out_file).write_text(json.dumps(out,indent=2,ensure_ascii=False))
    return out


def ledger_write(path, payload):
    temp=Path(str(path)+'.tmp')
    temp.write_text(json.dumps(payload,ensure_ascii=False,indent=2))
    os.replace(temp,path)


def run_ffmpeg(req, target_dir):
    q=quote(req)
    target_dir=Path(target_dir).resolve();target_dir.mkdir(parents=True,exist_ok=True)
    src=Path(req.source).resolve();source_hash=q['source_sha256'];fp=q['fingerprint']
    out=target_dir/(src.stem+'_lanczos_'+fp[:10]+'.mp4')
    if out==src:raise UpscaleError('Output cannot overwrite input')
    ledger=target_dir/'execution_ledger.json'
    lock=target_dir/'execution_ledger.lock'
    with open(lock,'a+b') as lock_f:
        fcntl.flock(lock_f.fileno(),fcntl.LOCK_EX)
        state=json.loads(ledger.read_text()) if ledger.exists() else {}
        old=state.get(fp)
        if old:
            if old.get('state')=='COMPLETE':
                result_file=Path(old['result_path'])
                if result_file.exists() and digest(result_file)==old['result_sha256']:
                    return {'status':'IDEMPOTENT_REUSE','output':str(result_file),'quote':q,'qa':old['qa'],'ledger_state':old}
                raise UpscaleError('RECOVERY_REQUIRED: completed result changed/missing; never submit another job silently')
            raise UpscaleError('RECOVERY_REQUIRED: existing job state '+old.get('state','UNKNOWN')+'; never submit twice')
        # Same output pathname for different request is blocked rather than overwritten.
        if out.exists():raise UpscaleError('OUTPUT_COLLISION: refusing overwrite')
        state[fp]={'state':'SUBMITTING','route':ROUTE,'source_sha256':source_hash,'created_at':iso(),
                  'request':dataclasses.asdict(req),'quote':q,'result_path':str(out)}
        ledger_write(ledger,state)
        partial=target_dir/(out.stem+'.partial.mp4')
        if partial.exists():
            state[fp]['state']='UNKNOWN';ledger_write(ledger,state)
            raise UpscaleError('PARTIAL_COLLISION: manual reconciliation required')
        # No shell: avoid arbitrary command/string injection. One video; optional audio, copy encoded audio.
        cmd=['ffmpeg','-hide_banner','-nostdin','-loglevel','error','-i',str(src),
             '-map','0:v:0','-map','0:a?','-map_metadata','0','-map_chapters','0',
             '-vf',f'scale={req.target_width}:{req.target_height}:flags=lanczos,setsar=1',
             '-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p',
             '-c:a','copy','-movflags','+faststart','-fps_mode','passthrough','-n',str(partial)]
        try:
            command(cmd,timeout=150)
            if digest(src)!=source_hash:raise UpscaleError('INPUT_MUTATED_DURING_JOB')
            preqa=inspect_result(src,partial,{'target_width':req.target_width,'target_height':req.target_height})
            if preqa['status']!='PASS':
                state[fp].update({'state':'QA_FAILED','qa':preqa,'partial_path':str(partial)})
                ledger_write(ledger,state)
                raise UpscaleError('Technical QA failed; result not promoted')
            os.replace(partial,out)
            state[fp].update({'state':'COMPLETE','completed_at':iso(),'result_sha256':digest(out),
                'qa':preqa,'actual_cash_incremental_usd':'0.00',
                'actual_operational_cost_usd':None,'classification':'CONVENTIONAL_UPSCALE'})
            ledger_write(ledger,state)
        except Exception:
            if state[fp]['state'] not in ('QA_FAILED',):
                # Conservative: a subprocess error does NOT prove nothing happened. Preserve evidence.
                state[fp].update({'state':'UNKNOWN','last_error_at':iso(),'partial_path':str(partial)})
                ledger_write(ledger,state)
            raise
        return {'status':'EXECUTED_TECHNICAL_QA_PASS','output':str(out),'quote':q,'qa':preqa,'ledger_state':state[fp]}


def mock_route_decision(routes,preferred,max_incremental_cash='0',consent=False):
    """Offline routing policy simulation. Never makes network requests."""
    limit=Decimal(str(max_incremental_cash))
    for name in preferred:
        c=routes.get(name)
        if not c or not c.get('available') or not c.get('implemented'):continue
        cost=c.get('cash_incremental_usd')
        if cost is None:continue
        cost=Decimal(str(cost))
        if not cost.is_finite() or cost<0 or not limit.is_finite() or limit<0:continue
        if cost>limit:continue
        if cost>0 and not consent:continue
        if c.get('needs_third_party_upload') and not c.get('data_transfer_consent'):continue
        return {'status':'ELIGIBLE_SIMULATED','route':name}
    return {'status':'BLOCKED_PROVIDER_UNAVAILABLE_OR_UNAUTHORIZED','route':None}


def main():
    p=argparse.ArgumentParser(description='Provider-neutral video upscale pilot; FFmpeg conventional only')
    p.add_argument('operation',choices=['routes','quote','run'])
    p.add_argument('--source')
    p.add_argument('--width',type=int)
    p.add_argument('--height',type=int)
    p.add_argument('--out-dir',default='outputs')
    args=p.parse_args()
    if args.operation=='routes':r=available_routes()
    else:
        if not args.source or not args.width or not args.height:p.error('--source --width --height required')
        req=Request(args.source,args.width,args.height)
        r=quote(req) if args.operation=='quote' else run_ffmpeg(req,args.out_dir)
    print(json.dumps(r,indent=2,ensure_ascii=False))

if __name__=='__main__':
    try:main()
    except UpscaleError as e:
        print(json.dumps({'status':'BLOCKED_OR_FAILED','reason':str(e)}),file=sys.stderr)
        sys.exit(2)
