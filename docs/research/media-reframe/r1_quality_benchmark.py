#!/usr/bin/env python3
"""R1 reframe quality benchmark. Synthetic-only, not commercial certification.

Run: python r1_quality_benchmark.py --output-dir /tmp/r1-quality
No provider calls. Pillow and numpy required; FFmpeg optional for video.
"""
import argparse
import hashlib
import json
import math
import shutil
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps, __version__ as PIL_VERSION

TARGET = (1080, 1920)
MASTER = (3840, 2160)
CROP_X = 2420
PROTECTED_MASTER = (2640, 750, 3420, 1690)


def synthetic_master():
    """Artificial fine texture, product and text surrogate; never a real person or brand."""
    w, h = MASTER
    xx = np.arange(w, dtype=np.float32)[None, :]
    yy = np.arange(h, dtype=np.float32)[:, None]
    red = 120 + 32 * np.sin(xx / 18.0) + 16 * np.cos(yy / 17.0)
    green = 120 + 40 * np.sin((xx + yy) / 8.5)
    blue = 135 + 44 * np.cos((xx - yy) / 11.0)
    rgb = np.stack(np.broadcast_arrays(red, green, blue), axis=-1)
    im = Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8), 'RGB')
    d = ImageDraw.Draw(im)
    d.rounded_rectangle(PROTECTED_MASTER, radius=55, fill=(208, 172, 139),
                        outline=(40, 27, 20), width=10)
    d.ellipse((2750, 805, 3050, 1130), fill=(80, 55, 53), outline=(30, 30, 30), width=7)
    d.rectangle((2710, 1180, 3325, 1610), fill=(57, 75, 93), outline='white', width=6)
    for idx in range(55):
        x = 2715 + idx * 11
        d.line((x, 1200, x, 1565), fill=(95, 130, 151) if idx % 2 else (15, 31, 49), width=2)
    try:
        font = ImageFont.truetype('DejaVuSans.ttf', 45)
        small = ImageFont.truetype('DejaVuSans.ttf', 18)
    except OSError:
        font = ImageFont.load_default()
        small = font
    d.rectangle((2790, 1360, 3260, 1450), fill='white')
    d.text((2820, 1378), 'DEMO PRODUCT', fill='black', font=font)
    d.text((2800, 1500), 'synthetic fine text 2026', fill='white', font=small)
    # Separate left subject; impossible to retain both in the intended crop.
    d.ellipse((500, 660, 900, 1060), fill=(35, 140, 95))
    d.rectangle((520, 1080, 910, 1810), fill=(60, 110, 65))
    return im


def crop_at_resolution(image, original_size=MASTER):
    w, h = image.size
    left = round(CROP_X * w / original_size[0])
    crop_w = round(h * TARGET[0] / TARGET[1])
    left = max(0, min(w - crop_w, left))
    cropped = image.crop((left, 0, left + crop_w, h))
    return cropped.resize(TARGET, Image.Resampling.LANCZOS), (left, 0, crop_w, h)


def psnr(a, b):
    a = np.asarray(a, dtype=np.float32)
    b = np.asarray(b, dtype=np.float32)
    mse = float(np.mean((a - b) ** 2))
    return None if mse == 0 else round(10 * math.log10(255.0 ** 2 / mse), 3)


def proxy_ssim(a, b):
    """Nonstandard global SSIM-like proxy. NOT windowed SSIM, VMAF or an acceptance score."""
    a = np.asarray(a.convert('L'), dtype=np.float64)[::4, ::4]
    b = np.asarray(b.convert('L'), dtype=np.float64)[::4, ::4]
    am, bm = float(a.mean()), float(b.mean())
    av, bv = float(a.var()), float(b.var())
    cov = float(np.mean((a - am) * (b - bm)))
    c1, c2 = (0.01 * 255) ** 2, (0.03 * 255) ** 2
    return round(((2 * am * bm + c1) * (2 * cov + c2)) /
                 ((am ** 2 + bm ** 2 + c1) * (av + bv + c2)), 5)


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def pixel_box_retained(box, crop):
    left, top, width, height = crop
    return (left <= box[0] and top <= box[1] and
            left + width >= box[2] and top + height >= box[3])


def image_matrix(folder):
    master = synthetic_master()
    ground, _ = crop_at_resolution(master)
    ground.save(folder / 'reference_from_4k.png')
    def target_box(box):
        return (round((box[0] - CROP_X) * TARGET[0] / 1215),
                round(box[1] * TARGET[1] / 2160),
                round((box[2] - CROP_X) * TARGET[0] / 1215),
                round(box[3] * TARGET[1] / 2160))
    product_roi = target_box(PROTECTED_MASTER)
    microtext_roi = target_box((2790, 1490, 3260, 1560))
    result = []
    for label, sz in [('2160p', (3840, 2160)), ('1080p', (1920, 1080)),
                      ('720p', (1280, 720)), ('480p', (854, 480))]:
        src = master if sz == MASTER else master.resize(sz, Image.Resampling.LANCZOS)
        candidate, crop = crop_at_resolution(src)
        candidate.save(folder / ('reframe_' + label + '.png'))
        # For tuple (x0,y0,x1,y1), index parity distinguishes x from y.
        bbox_scaled = tuple(round(v * sz[i % 2] / MASTER[i % 2])
                            for i, v in enumerate(PROTECTED_MASTER))
        crop_w, crop_h = crop[2:]
        result.append({
            'source_label': label, 'source_dimensions': list(sz),
            'crop_pixels': [crop_w, crop_h], 'target_dimensions': list(TARGET),
            'linear_upscale_required': round(max(TARGET[0] / crop_w, TARGET[1] / crop_h), 3),
            'protected_box_retained_geometry': pixel_box_retained(bbox_scaled, crop),
            'psnr_db_vs_aligned_4k_reference': psnr(candidate, ground),
            'product_roi_psnr_db': psnr(candidate.crop(product_roi), ground.crop(product_roi)),
            'microtext_roi_psnr_db': psnr(candidate.crop(microtext_roi), ground.crop(microtext_roi)),
            'global_ssim_like_proxy_not_standard_ssim': proxy_ssim(candidate, ground),
            'status': 'TECHNICAL_ONLY__HUMAN_VISUAL_QA_REQUIRED'
        })
    second = (500, 660, 910, 1810)
    right = (CROP_X, 0, round(MASTER[1] * 9 / 16), MASTER[1])
    two_subjects_feasible = (pixel_box_retained(PROTECTED_MASTER, right)
                             and pixel_box_retained(second, right))
    assert not two_subjects_feasible
    ImageOps.pad(master, TARGET, method=Image.Resampling.LANCZOS,
                 color=(30, 30, 32)).save(folder / 'both_subjects_pad.png')
    return {'comparisons': result, 'two_subject_crop_safely_possible': two_subjects_feasible,
            'fallback': 'PAD; actual creative acceptability unverified',
            'reference_sha256': sha256(folder / 'reference_from_4k.png')}


def run_ffmpeg(*args):
    return subprocess.run(['ffmpeg', '-nostdin', '-hide_banner', '-loglevel', 'error',
                           '-y', *map(str, args)], check=True, capture_output=True, text=True)


def audio_pcm_digest(path):
    pcm = subprocess.run(
        ['ffmpeg', '-nostdin', '-hide_banner', '-loglevel', 'error', '-i', str(path),
         '-map', '0:a:0', '-vn', '-f', 's16le', '-acodec', 'pcm_s16le', '-'],
        check=True, capture_output=True).stdout
    return hashlib.sha256(pcm).hexdigest()


def probe(path):
    result = subprocess.run(
        ['ffprobe', '-v', 'error', '-show_entries',
         'stream=codec_type,width,height,avg_frame_rate,nb_frames:format=duration',
         '-of', 'json', str(path)],
        capture_output=True, text=True, check=True)
    return json.loads(result.stdout)


def video_checks(folder):
    if not (shutil.which('ffmpeg') and shutil.which('ffprobe')):
        return {'status': 'BLOCKED_NO_FFMPEG', 'technical_verified': False}
    frames = folder / 'frames'
    frames.mkdir(exist_ok=True)
    for i in range(48):
        shot = 0 if i < 24 else 1
        x = 360 + i * 3 if shot == 0 else 460 - (i - 24) * 2
        im = Image.new('RGB', (640, 360), (60, 65, 72) if shot == 0 else (170, 174, 180))
        d = ImageDraw.Draw(im)
        d.rectangle((x, 90, x + 70, 250), fill=(250, 70, 55) if shot == 0 else (25, 110, 230))
        d.text((x + 8, 150), 'BOX', fill='white')
        im.save(frames / f'{i:03d}.png')
    src = folder / 'motion_source_24fps.mp4'
    dest = folder / 'motion_reframe_24fps.mp4'
    run_ffmpeg('-framerate', '24', '-i', frames / '%03d.png',
               '-f', 'lavfi', '-i', 'sine=frequency=550:sample_rate=48000:duration=2',
               '-map', '0:v:0', '-map', '1:a:0', '-c:v', 'mpeg4',
               '-q:v', '2', '-c:a', 'aac', '-shortest', src)
    # Explicit scene-dependent crop. NOT automatic visual tracking.
    expression = ("crop=202:360:x='if(lt(t,1),min(438,360+3*24*t+35-101),"
                  "min(438,460-2*24*(t-1)+35-101))':y=0,scale=360:640")
    run_ffmpeg('-i', src, '-map', '0:v:0', '-map', '0:a:0', '-vf', expression,
               '-c:v', 'mpeg4', '-q:v', '2', '-c:a', 'copy', dest)
    p1, p2 = probe(src), probe(dest)
    v1 = next(x for x in p1['streams'] if x['codec_type'] == 'video')
    v2 = next(x for x in p2['streams'] if x['codec_type'] == 'video')
    duration_delta = abs(float(p1['format']['duration']) - float(p2['format']['duration']))
    a1, a2 = audio_pcm_digest(src), audio_pcm_digest(dest)
    checks = {'width_height': (v2['width'], v2['height']) == (360, 640),
              'fps_stable': v1['avg_frame_rate'] == v2['avg_frame_rate'] == '24/1',
              'frame_count': int(v1['nb_frames']) == int(v2['nb_frames']) == 48,
              'duration_within_one_frame': duration_delta <= 1 / 24,
              'decoded_audio_pcm_sha256_equal': a1 == a2}
    if not all(checks.values()):
        raise AssertionError(checks)
    return {'status': 'PASS_TECHNICAL_ONLY', 'checks': checks,
            'source_sha256': sha256(src), 'output_sha256': sha256(dest),
            'source_duration_s': p1['format']['duration'],
            'output_duration_s': p2['format']['duration'],
            'source_audio_pcm_sha256': a1, 'output_audio_pcm_sha256': a2,
            'temporal_smoothness': 'NOT_MEASURED',
            'real_face_product_logo_quality': 'NOT_TESTED'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', default='/tmp/r1-quality')
    args = parser.parse_args()
    folder = Path(args.output_dir)
    folder.mkdir(exist_ok=True, parents=True)
    images, video = image_matrix(folder), video_checks(folder)
    report = {'benchmark': 'MEDIA_REFRAME R1 spatial quality/resolution and video integrity',
              'reference': 'aligned synthetic 4K → 1080x1920; not native-shot creative master',
              'calibration': ('synthetic signal and global SSIM-like proxy; '
                              'do not use as commercial accept/reject score'),
              'provider_calls': 0, 'paid_cost_usd': 0,
              'versions': {'pillow': PIL_VERSION, 'numpy': np.__version__},
              'images': images, 'video': video,
              'production_quality_status': 'UNVERIFIED_REQUIRE_REAL_ASSET_AND_HUMAN_QA'}
    (folder / 'r1_quality_results.json').write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
