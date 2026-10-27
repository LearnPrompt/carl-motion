#!/usr/bin/env bash
# S29 B v2 复现命令（Blender 5.2.x、Python3 + numpy + Pillow、ffmpeg）
set -euo pipefail
cd "$(dirname "$0")"
WORK=${WORK:-../../../work/frames}
TEX="$WORK/S29_tex"; RAW="$WORK/S29_raw"; FR="$WORK/S29"
python3 pcb_tex.py "$TEX"                                            # 主板 8K / 感光板 4K 版图贴图 + 元件摆放表
blender -b -P scene.py -- "$RAW" "$TEX" 0 239 1 100 40               # 交付版：100% 分辨率、40 采样
python3 post.py "$RAW" "$FR"
../../pipeline/encode.sh "$FR" ../../../out/S29_B_8s.mp4
