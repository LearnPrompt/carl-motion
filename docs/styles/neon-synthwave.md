# 03 · Neon Synthwave · 霓虹复古Synthwave

[All styles](README.md) · [← Product UI 2.5D Camera](product-ui-2-5d.md) · [Hand-drawn Paper Notes →](hand-drawn-notes.md)

<img src="../../assets/previews/neon-synthwave.webp" width="100%" alt="Neon Synthwave">

<sub>Preview: our render (layer B), MIT. 预览是我们渲染的 B，MIT 许可。</sub>

**Status 状态:** Implemented, one scene · 单场景实做

## Prompt (copy this)

Paste into Claude, GPT or any coding model. Swap *your topic* for your own subject.

```text
Make your topic into an 80s Synthwave: a one-point-perspective neon grid rolling forward, a layered sunset on the horizon, double-layer glow on the lines, with scanlines and chromatic aberration on top. Key visuals: one-point-perspective grid scrolling, multi-layer gradient sunset, double-layer glow, scanlines and RGB color shift, chrome lettering, palm tree silhouettes, tape stutter at 15fps in selected spots. Watch out: Without the grid rolling there is no sense of speed; the camera must keep rushing forward. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
```

## 提示语（复制这段）

发给 Opus 5.5 或任意能写代码的模型，把你的主题换成自己的内容。

```text
做你的主题的 80 年代 Synthwave，一点透视霓虹网格往前滚，地平线放分层落日，线条双层辉光，叠扫描线和色偏。画面要点：一点透视网格滚动、多层渐变落日、双层辉光、扫描线与 RGB 色偏、镀铬字、棕榈剪影、局部抽到 15fps 的磁带卡顿。注意：网格不滚就没速度感，镜头要一直往前冲。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
```

## What the two examples show · 两个示例

| | English | 中文 |
|---|---|---|
| A | A magenta-purple grid floor rolls forward, a striped sunset sits on the horizon, a sports car drives toward it, and NEON DRIVE Midnight chrome lettering slams in. | 紫红网格地面往前滚，条纹落日，跑车开向地平线，NEON DRIVE Midnight 镀铬字砸出。 |
| B | Our render: A neon tape recorder hops to the beat on the grid, the sun rises, and a chrome NEON TAPE title slams in at the end. | 我们做的。霓虹录音机在网格上跟拍子跳，太阳升起，结尾砸出 NEON TAPE 镀铬标题。 |

## Where it usually breaks · 容易失败的点

A grid that does not roll forward becomes a static wallpaper; colors outside magenta, cyan and orange look muddy; stacking too many glow layers blurs everything together.

网格不往前滚就成了静态壁纸；颜色跑出品红、青、橙会发脏；辉光叠太多层会糊成一片。

## Key visuals · 画面要点

one-point-perspective grid scrolling, multi-layer gradient sunset, double-layer glow, scanlines and RGB color shift, chrome lettering, palm tree silhouettes, tape stutter at 15fps in selected spots

一点透视网格滚动、多层渐变落日、双层辉光、扫描线与 RGB 色偏、镀铬字、棕榈剪影、局部抽到 15fps 的磁带卡顿

Palette 主色：`#b83ea8`

## References · 参考来源

| Layer | Title | Source | License |
|---|---|---|---|
| A | NEON DRIVE棕榈公路小车 | [Vincentwei1021 · mg-styles-15](https://vincentwei1021.github.io/mg-styles-15/?lang=zh#10-synthwave) | prompts/code MIT; demo video not redistributed |
| B | carl-motion | [this repo](../../skills/carl-motion/scenes/neon-synthwave) | MIT |

## Reproduce · 复现

Source that rendered the B clip: [`skills/carl-motion/scenes/neon-synthwave`](../../skills/carl-motion/scenes/neon-synthwave) (Blender + Python). Check dependencies first with `python3 skills/carl-motion/scripts/doctor.py neon-synthwave`.

```bash
cd skills/carl-motion/scenes/neon-synthwave
./render.sh /tmp/neon-synthwave
python3 ../../scripts/deliver.py --frames /tmp/neon-synthwave/frames --out neon-synthwave.mp4
```

渲染 B 的完整源码在 [`skills/carl-motion/scenes/neon-synthwave`](../../skills/carl-motion/scenes/neon-synthwave)（Blender + Python），渲染命令写在它的 README 里。
