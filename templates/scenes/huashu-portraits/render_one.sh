#!/usr/bin/env bash
# 用法: ./render_one.sh <场景名> <编号 S22|S23|S24|S25>  → 渲染 240 帧并编码到 完成片/<编号>_B_8s.mp4
set -euo pipefail
cd "$(dirname "$0")"
FR="${FRAMES_ROOT:-../../../work/frames}/$2"
rm -rf "$FR"
node render.cjs "$1" "$FR"
../../pipeline/encode.sh "$FR" "../../../out/$2_B_8s.mp4"
