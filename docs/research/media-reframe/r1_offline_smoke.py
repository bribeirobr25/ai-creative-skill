#!/usr/bin/env python3
"""R1 research-only smoke: deterministic crop/pad and FFmpeg scene-conditioned crop.
Synthetic content only, no cloud calls, no commercial routes, no production claims.
Run: python r1_offline_smoke.py --out /tmp/reframe-r1
"""
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageOps, __version__ as PIL_VERSION

SRC_W, SRC_H = 640, 360


def cmd(*args):
    p = subprocess.run(list(map(str,args)), check=True, text=True, capture_output=True)
    return p.stdout


def probe(path):
    return json.loads(cmd('ffprobe', '-v', 'error', '-show_entries',
                          'stream=codec_type,width,height,avg_frame_rate,nb_frames,duration:format=duration',
                          '-of', 'json', path))


def ratio(s):
    a,b=map(int,s.split('/'))
    return a/b


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def protected_inside(box, crop):
    x0,y0,x1,y1=box; cx,cy,cw,ch=crop
    return cx <= x0 and cy <= y0 and cx+cw >= x1 and cy+ch >= y1


def subject_image(path, double=False):
    im=Image.new('RGB',(SRC_W,SRC_H),(231,231,231)); d=ImageDraw.Draw(im)
    # Synthetic face / product / label proxies, not a face-perception test.
    d.ellipse((480,85,555,160),fill=(170,40,55))
    d.rectangle((475,160,610,315),fill=(30,95,175))
    d.rectangle((500,210,595,242),fill=(248,248,248))
    d.text((515,216),'BRAND',fill=(10,10,10))
    if double:
        d.ellipse((55,85,130,160),fill=(60,140,70))
        d.rectangle((50,160,165,315),fill=(50,130,70))
    im.save(path)
    return im


def test_images(out):
    source=out/'single_source.png'; single=subject_image(source)
    # 9:16 on 640x360 requires crop width ~202. Preserve the off-centre product.
    crop=(438,0,202,360)
    assert protected_inside((475,85,610,315), crop)
    kept=single.crop((crop[0],crop[1],crop[0]+crop[2],crop[1]+crop[3]))
    kept.resize((360,640),Image.Resampling.LANCZOS).save(out/'single_crop_9x16.png')
    two=out/'two_subjects_source.png'; both=subject_image(two,double=True)
    required=(50,85,610,315)
    assert not protected_inside(required,crop)
    full=ImageOps.pad(both,(360,640),method=Image.Resampling.LANCZOS,color=(24,25,27))
    full.save(out/'two_subjects_pad_9x16.png')
    full2=ImageOps.pad(both,(500,400),method=Image.Resampling.LANCZOS,color=(24,25,27))
    full2.save(out/'two_subjects_pad_5x4.png')
    # Inverted aspect stress: vertical source -> ultrawide, no pixels cropped.
    vert=Image.new('RGB',(360,640),(55,85,130)); d=ImageDraw.Draw(vert)
    d.rectangle((45,90,315,550),outline=(240,240,240),width=12)
    vert.save(out/'portrait_source.png')
    ImageOps.pad(vert,(840,360),method=Image.Resampling.LANCZOS,color=(20,20,20)).save(out/'portrait_pad_21x9.png')
    assert full.size==(360,640) and full2.size==(500,400)
    return {'status':'PASS', 'checks':['single subject protected box fits crop',
                                      'two-subject crop detected unsafe, switched to pad',
                                      '16:9->9:16, 16:9->5:4, 9:16->21:9 output dimensions'],
            'files':[p.name for p in [source,out/'single_crop_9x16.png',two,out/'two_subjects_pad_9x16.png',out/'two_subjects_pad_5x4.png',out/'portrait_pad_21x9.png']]}


def test_video(out):
    if not shutil.which('ffmpeg') or not shutil.which('ffprobe'):
        return {'status':'BLOCKED', 'reason':'ffmpeg or ffprobe absent'}
    frames=out/'frames'; frames.mkdir(exist_ok=True)
    for i in range(36):
        t=i/12
        scene=0 if i<18 else 1
        pos=round(50+80*t) if scene==0 else round(450-70*(t-1.5))
        im=Image.new('RGB',(640,360),(220,220,220) if scene==0 else (44,44,70))
        d=ImageDraw.Draw(im)
        d.rectangle((pos,140,pos+80,220),fill=(200,30,50) if scene==0 else (25,225,230))
        d.rectangle((pos+14,160,pos+65,192),fill='white')
        d.text((pos+18,167),'LOGO',fill='black')
        im.save(frames/f'frame_{i:03}.png')
    src=out/'synthetic_source_16x9.mp4'; dst=out/'synthetic_reframed_9x16.mp4'
    cmd('ffmpeg','-y','-loglevel','error','-framerate','12','-i',frames/'frame_%03d.png',
        '-f','lavfi','-i','sine=frequency=440:sample_rate=48000:duration=3',
        '-map','0:v:0','-map','1:a:0','-c:v','mpeg4','-q:v','2','-c:a','aac','-shortest',src)
    # Manually specified motion trajectories. This is NOT automatic subject tracking.
    # t is frame timestamp; scene jump is intentional at hard cut t=1.5.
    expression="crop=202:360:x='if(lt(t,1.5),max(0,50+80*t+40-101),min(438,450-70*(t-1.5)+40-101))':y=0,scale=360:640"
    cmd('ffmpeg','-y','-loglevel','error','-i',src,'-map','0:v:0','-map','0:a:0',
        '-vf',expression,'-c:v','mpeg4','-q:v','2','-c:a','copy',dst)
    before,after=probe(src),probe(dst)
    def video(p):return next(s for s in p['streams'] if s['codec_type']=='video')
    assert (video(before)['width'],video(before)['height']) == (640,360)
    assert (video(after)['width'],video(after)['height']) == (360,640)
    assert ratio(video(after)['avg_frame_rate']) == ratio(video(before)['avg_frame_rate']) == 12
    assert any(s['codec_type']=='audio' for s in after['streams'])
    d1=float(before['format']['duration']); d2=float(after['format']['duration'])
    assert abs(d1-d2)<0.12,(d1,d2)
    # Check encoded frames, not only metadata; synthetic colored subject should stay visible.
    try:
        import cv2
        import numpy as np
        cap=cv2.VideoCapture(str(dst)); seen=[]
        for i in range(36):
            ok,frame=cap.read()
            assert ok, f'missing decoded frame {i}'
            if i<18:
                count=int(((frame[:,:,2]>120)&(frame[:,:,1]<100)&(frame[:,:,0]<120)).sum())
            else:
                count=int(((frame[:,:,0]>120)&(frame[:,:,1]>120)&(frame[:,:,2]<100)).sum())
            seen.append(count)
        cap.release()
        assert min(seen)>100, {'minimum_subject_pixels':min(seen)}
        decoded='PASS'
    except ImportError:
        decoded='NOT_RUN: cv2 / numpy unavailable'
    return {'status':'PASS','source_dimensions':[640,360],'output_dimensions':[360,640],
            'fps_before_after':[video(before)['avg_frame_rate'],video(after)['avg_frame_rate']],
            'duration_seconds_before_after':[d1,d2], 'audio_preserved':True,
            'encoded_frames_subject_visible':decoded,
            'semantic_QA':'NOT_TESTED: synthetic geometry does not validate real faces, logo fidelity, temporal perceptual QA or scene coherence',
            'tracking':'manual scene-conditioned trajectory, not vision-based auto tracking',
            'source_sha256':sha(src),'reframed_sha256':sha(dst)}


def main():
    p=argparse.ArgumentParser();p.add_argument('--out',default='/tmp/media-reframe-r1')
    args=p.parse_args();out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    report={'benchmark':'R1 deterministic offline, synthetic-only','cost_paid_usd':0,
            'image_lib':'Pillow '+PIL_VERSION, 'environment':{'ffmpeg':cmd('ffmpeg','-version').splitlines()[0]},
            'images':test_images(out),'video':test_video(out)}
    (out/'report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(report,indent=2,ensure_ascii=False))

if __name__=='__main__':main()
