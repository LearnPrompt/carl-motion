#!/usr/bin/env bash
# S27 点云测绘／剥层 B —— 完整复现：Blender 5.2 渲染原始帧 → 后期叠字 → 编码
set -euo pipefail
cd "$(dirname "$0")"
WORK="${WORK:-../../../work/frames}"
blender -b -P scene.py -- "$WORK/S27_raw"
python3 overlay.py "$WORK/S27_raw" "$WORK/S27"
# 点云噪点多，用 CRF 19（其余参数与 ../../pipeline/encode.sh 相同），规格不变
ffmpeg -hide_banner -loglevel error -y -framerate 30 -start_number 1 -i "$WORK/S27/%04d.png" \
  -frames:v 240 -vf "scale=1920:1080:flags=lanczos,format=yuv420p" -an \
  -c:v libx264 -preset slow -crf 19 -profile:v high -r 30 -movflags +faststart ../../../out/S27_B_8s.mp4
