#!/usr/bin/env bash
# S34 B 复现命令（Blender 5.2.x、Python3 + Pillow、ffmpeg）
set -euo pipefail
cd "$(dirname "$0")"
RAW=${1:-../../../work/frames/S34_raw}
FR=${2:-../../../work/frames/S34}
blender -b -P scene.py -- "$RAW" --samples 48
python3 post.py "$RAW" "$FR"
../../pipeline/encode.sh "$FR" ../../../out/S34_B_8s.mp4
