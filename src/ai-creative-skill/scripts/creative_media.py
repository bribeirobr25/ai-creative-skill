#!/usr/bin/env python3
"""Portable Media Upscale CLI. Local only, does not submit paid jobs."""
from pathlib import Path
import os,sys,runpy
root=Path(__file__).resolve().parents[1]/'media'/'runtime'
sys.path.insert(0,str(root))
if __name__=='__main__': runpy.run_path(str(root/'media_upscale_v03.py'),run_name='__main__')
