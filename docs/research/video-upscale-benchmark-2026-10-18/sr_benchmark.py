"""Free/open-source upscaling with Real-ESRGAN models (CPU, PyTorch).

Research benchmark script (2026-10-18). NOT a canonical route of the skill;
the canonical experimental route lives in src/ai-creative-skill/media/runtime/.

Weights are NOT committed (third-party, BSD-3 Real-ESRGAN). Download into ./w/:
  https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesr-general-x4v3.pth
  https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth
  https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.1/RealESRGAN_x2plus.pth
Requires: torch, opencv-python, numpy, ffmpeg on PATH.

Usage:
  python3 sr.py image MODEL in.png out.png
  python3 sr.py video MODEL in.mp4 out.mp4 [max_frames]
MODEL: general (realesr-general-x4v3), x4plus (RealESRGAN_x4plus), x2plus (RealESRGAN_x2plus)
Output is resized (Lanczos) to exactly 1080x1920.
"""
import sys, time, subprocess, os
import numpy as np, cv2, torch
import torch.nn as nn, torch.nn.functional as F

W = os.path.join(os.path.dirname(os.path.abspath(__file__)), "w")
torch.set_num_threads(os.cpu_count())

class SRVGGNetCompact(nn.Module):
    def __init__(self, num_in_ch=3, num_out_ch=3, num_feat=64, num_conv=32, upscale=4):
        super().__init__()
        self.upscale = upscale
        self.body = nn.ModuleList()
        self.body.append(nn.Conv2d(num_in_ch, num_feat, 3, 1, 1))
        self.body.append(nn.PReLU(num_parameters=num_feat))
        for _ in range(num_conv):
            self.body.append(nn.Conv2d(num_feat, num_feat, 3, 1, 1))
            self.body.append(nn.PReLU(num_parameters=num_feat))
        self.body.append(nn.Conv2d(num_feat, num_out_ch * upscale * upscale, 3, 1, 1))
        self.upsampler = nn.PixelShuffle(upscale)
    def forward(self, x):
        out = x
        for m in self.body:
            out = m(out)
        out = self.upsampler(out)
        return out + F.interpolate(x, scale_factor=self.upscale, mode="nearest")

class RDB(nn.Module):
    def __init__(self, nf=64, gc=32):
        super().__init__()
        self.conv1 = nn.Conv2d(nf, gc, 3, 1, 1)
        self.conv2 = nn.Conv2d(nf + gc, gc, 3, 1, 1)
        self.conv3 = nn.Conv2d(nf + 2 * gc, gc, 3, 1, 1)
        self.conv4 = nn.Conv2d(nf + 3 * gc, gc, 3, 1, 1)
        self.conv5 = nn.Conv2d(nf + 4 * gc, nf, 3, 1, 1)
        self.lrelu = nn.LeakyReLU(0.2, True)
    def forward(self, x):
        x1 = self.lrelu(self.conv1(x))
        x2 = self.lrelu(self.conv2(torch.cat((x, x1), 1)))
        x3 = self.lrelu(self.conv3(torch.cat((x, x1, x2), 1)))
        x4 = self.lrelu(self.conv4(torch.cat((x, x1, x2, x3), 1)))
        x5 = self.conv5(torch.cat((x, x1, x2, x3, x4), 1))
        return x5 * 0.2 + x

class RRDB(nn.Module):
    def __init__(self, nf, gc=32):
        super().__init__()
        self.rdb1, self.rdb2, self.rdb3 = RDB(nf, gc), RDB(nf, gc), RDB(nf, gc)
    def forward(self, x):
        return self.rdb3(self.rdb2(self.rdb1(x))) * 0.2 + x

class RRDBNet(nn.Module):
    def __init__(self, scale=4, nf=64, nb=23, gc=32):
        super().__init__()
        self.scale = scale
        in_ch = 3 * (16 if scale == 1 else 4 if scale == 2 else 1)
        self.conv_first = nn.Conv2d(in_ch, nf, 3, 1, 1)
        self.body = nn.Sequential(*[RRDB(nf, gc) for _ in range(nb)])
        self.conv_body = nn.Conv2d(nf, nf, 3, 1, 1)
        self.conv_up1 = nn.Conv2d(nf, nf, 3, 1, 1)
        self.conv_up2 = nn.Conv2d(nf, nf, 3, 1, 1)
        self.conv_hr = nn.Conv2d(nf, nf, 3, 1, 1)
        self.conv_last = nn.Conv2d(nf, 3, 3, 1, 1)
        self.lrelu = nn.LeakyReLU(0.2, True)
    def forward(self, x):
        if self.scale == 2:
            x = F.pixel_unshuffle(x, 2)
        feat = self.conv_first(x)
        feat = feat + self.conv_body(self.body(feat))
        feat = self.lrelu(self.conv_up1(F.interpolate(feat, scale_factor=2, mode="nearest")))
        feat = self.lrelu(self.conv_up2(F.interpolate(feat, scale_factor=2, mode="nearest")))
        return self.conv_last(self.lrelu(self.conv_hr(feat)))

def load(name):
    if name == "general":
        net, f = SRVGGNetCompact(), "realesr-general-x4v3.pth"
    elif name == "x4plus":
        net, f = RRDBNet(4), "RealESRGAN_x4plus.pth"
    elif name == "x2plus":
        net, f = RRDBNet(2), "RealESRGAN_x2plus.pth"
    else:
        raise SystemExit("unknown model")
    sd = torch.load(os.path.join(W, f), map_location="cpu", weights_only=True)
    sd = sd.get("params_ema", sd.get("params", sd))
    net.load_state_dict(sd, strict=True)
    return net.eval()

@torch.inference_mode()
def run(net, bgr):
    x = torch.from_numpy(cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)).permute(2, 0, 1).float().div(255).unsqueeze(0)
    y = net(x).clamp(0, 1).squeeze(0).permute(1, 2, 0).mul(255).round().byte().numpy()
    y = cv2.cvtColor(y, cv2.COLOR_RGB2BGR)
    return cv2.resize(y, (1080, 1920), interpolation=cv2.INTER_LANCZOS4)

if __name__ == "__main__":
    mode, model, src, dst = sys.argv[1:5]
    net = load(model)
    if mode == "image":
        t = time.time(); out = run(net, cv2.imread(src)); cv2.imwrite(dst, out)
        print(f"{model}: {time.time()-t:.1f}s")
    else:
        maxf = int(sys.argv[5]) if len(sys.argv) > 5 else None
        cap = cv2.VideoCapture(src)
        fps = cap.get(cv2.CAP_PROP_FPS); n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24",
            "-s", "1080x1920", "-r", str(fps), "-i", "-", "-i", src, "-map", "0:v", "-map", "1:a?",
            "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p", "-c:a", "copy",
            "-shortest", "-movflags", "+faststart", dst], stdin=subprocess.PIPE)
        i, t0 = 0, time.time()
        while True:
            ok, fr = cap.read()
            if not ok or (maxf and i >= maxf):
                break
            enc.stdin.write(run(net, fr).tobytes()); i += 1
            if i % 24 == 0:
                el = time.time() - t0
                print(f"{i}/{n} frames, {el/i:.2f}s/frame, eta {(n-i)*el/i/60:.1f} min", flush=True)
        enc.stdin.close(); enc.wait()
        print(f"done {i} frames in {(time.time()-t0)/60:.1f} min")
