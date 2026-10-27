#!/usr/bin/env bash
# S33 积木玩具 B：渲染 240 帧 → 叠字幕 → 编码 1920×1080/8s/30fps/静音 MP4
set -euo pipefail
cd "$(dirname "$0")"
FR="${FRAMES:-../../../work/frames/S33}"
blender -b --factory-startup -P scene.py -- "$FR" 1 240 1 100
python3 caption.py "$FR" "${FR}_final"
../../pipeline/encode.sh "${FR}_final" ../../../out/S33_B_8s.mp4
