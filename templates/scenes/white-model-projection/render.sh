#!/usr/bin/env bash
# S28 实体白模投影 B —— 完整复现：投影图 → Blender 5.2 两遍渲染 → 合成叠字 → 编码
set -euo pipefail
cd "$(dirname "$0")"
WORK="${WORK:-../../../work/frames}"
python3 project.py "$WORK/S28_proj"
blender -b -P scene.py -- "$WORK/S28_raw" "$WORK/S28_proj" 0 239 1 100 32   # 交付版：100% 分辨率、32 采样
python3 overlay.py "$WORK/S28_raw" "$WORK/S28"
../../pipeline/encode.sh "$WORK/S28" ../../../out/S28_B_8s.mp4
