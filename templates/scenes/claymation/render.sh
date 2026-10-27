#!/usr/bin/env bash
# S12 黏土定格 B：渲染 240 帧 → 编码 1920×1080/8s/30fps/静音 MP4
set -euo pipefail
cd "$(dirname "$0")"
FR="${FRAMES:-../../../work/frames/S12}"
blender -b --factory-startup -P scene.py -- "$FR" 1 240 1 100
../../pipeline/encode.sh "$FR" ../../../out/S12_B_8s.mp4
