"""Builds side-by-side crop panels (same frame, all routes) for human fidelity QA.

Expects, in this script's directory: <frame>.png (480p source frame) and
<frame>_<route>.png for each route (general, x2plus, x4plus, topaz).
Crop boxes are in 1080x1920 coordinates and are specific to the 2026-10-18 test
clip; adjust them for other material. Output PNGs contain project media and must
NOT be committed to this public repository.
"""
import cv2, numpy as np, sys, os
S = os.path.dirname(os.path.abspath(__file__))
os.chdir(S)
names = [("lanczos", "Lanczos (sem IA)"), ("general", "Real-ESRGAN general-v3"),
         ("x2plus", "Real-ESRGAN x2plus"), ("x4plus", "Real-ESRGAN x4plus"), ("topaz", "Topaz slp-2.5 (Higgsfield)")]

def get(frame, n):
    if n == "lanczos":
        return cv2.resize(cv2.imread(f"{frame}.png"), (1080, 1920), interpolation=cv2.INTER_LANCZOS4)
    im = cv2.imread(f"{frame}_{n}.png")
    return cv2.resize(im, (1080, 1920), interpolation=cv2.INTER_LANCZOS4) if im.shape[:2] != (1920, 1080) else im

def panel(frame, box, zoom, out):
    x0, y0, x1, y1 = box
    tiles = []
    for n, label in names:
        c = get(frame, n)[y0:y1, x0:x1]
        c = cv2.resize(c, None, fx=zoom, fy=zoom, interpolation=cv2.INTER_CUBIC) if zoom != 1 else c
        bar = np.full((40, c.shape[1], 3), 245, np.uint8)
        cv2.putText(bar, label, (8, 28), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (30, 30, 30), 2, cv2.LINE_AA)
        tiles.append(np.vstack([bar, c]))
    sep = np.full((tiles[0].shape[0], 8, 3), 255, np.uint8)
    row = tiles[0]
    for t in tiles[1:]:
        row = np.hstack([row, sep, t])
    cv2.imwrite(out, row)

panel("f085", (360, 495, 810, 945), 1, "cmp_face.png")
panel("f085", (420, 590, 700, 760), 1.6, "cmp_eyes.png")
panel("f138", (560, 1385, 810, 1540), 1.8, "cmp_label.png")
panel("f138", (300, 1150, 700, 1450), 1, "cmp_fabric.png")
