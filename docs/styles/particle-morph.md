# 21 · Particle Morph · 粒子聚散造型

[All styles](README.md) · [← Impressionist Oil (Monet)](monet-impressionist.md) · [White-model Projection →](white-model-projection.md)

<img src="../../assets/previews/particle-morph.webp" width="100%" alt="Particle Morph">

<sub>Preview: our render (layer B), MIT. 预览是我们渲染的 B，MIT 许可。</sub>

**Status 状态:** Implemented, one scene · 单场景实做

## Prompt (copy this)

Paste into Claude, GPT or any coding model. Swap *your topic* for your own subject.

```text
Make a particle animation: hundreds of thousands of glowing particles gather on a dark background into the shape and text of your topic, then scatter and become the next shape. Key visuals: hundreds of thousands of glowing particles, gather into shape then scatter, deep blue-black background, lines connecting into a relationship network, big number counter, one English conclusion line as subtitle. Watch out: Too few particles or no target shape, and the form cannot be read. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
```

## 提示语（复制这段）

发给 Opus 5.5 或任意能写代码的模型，把你的主题换成自己的内容。

```text
做一支粒子动画，几十万发光粒子在深色背景上聚成你的主题的形状和文字，再散开变成下一个形状。画面要点：数十万发光粒子、聚拢成形再散开、深蓝黑底、连线成关系网络、大数字计数器、一句英文结论字幕。注意：粒子太少或不给目标形状，就读不出造型。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
```

## What the two examples show · 两个示例

| | English | 中文 |
|---|---|---|
| A | Millions of particles gather into an object on a deep blue background and scatter again, with a counter ticking in the top right. | 深蓝底上几百万粒子聚成物体又散开，右上角计数在跳。 |
| B | Our render: an English explainer version, the story's ending. 60,000 particles gather into the village, curl into a vortex, then gather into a reaching person and a seated cat, and the particles spell MAYBE... THE CAT CHOSE US. | 我们做的英文讲解版，故事收尾。6 万粒子聚成村子，卷成漩涡，再聚成伸手的人和坐着的猫，粒子拼出 MAYBE… THE CAT CHOSE US。 |

## Where it usually breaks · 容易失败的点

Too few particles or no target shape and the form cannot be read; provide a defined shape and enough particles; the gathering and scattering needs rhythm, so do not let them drift all the time.

粒子太少或没给目标形状就读不出造型；要给定形状并让粒子够多；聚和散要有节奏，别一直飘。

## Key visuals · 画面要点

hundreds of thousands of glowing particles, gather into shape then scatter, deep blue-black background, lines connecting into a relationship network, big number counter, one English conclusion line as subtitle

数十万发光粒子、聚拢成形再散开、深蓝黑底、连线成关系网络、大数字计数器、一句英文结论字幕

Palette 主色：`#3e6cb8` `#b88a3e`

## References · 参考来源

| Layer | Title | Source | License |
|---|---|---|---|
| A | Drone Emprit：粒子地图与关系网络 | [prompt-motion.com](https://prompt-motion.com/ismailfahmi-557268) | link only |
| B | carl-motion | [this repo](../../skills/carl-motion/scenes/particle-morph) · story idea: [en.yasue.org](https://en.yasue.org/article/pushing-opus-5-5-video-generation-limits) | MIT |

## Reproduce · 复现

Source that rendered the B clip: [`skills/carl-motion/scenes/particle-morph`](../../skills/carl-motion/scenes/particle-morph) (Python (NumPy + OpenCV + Pillow)). Check dependencies first with `python3 skills/carl-motion/scripts/doctor.py particle-morph`.

```bash
cd skills/carl-motion/scenes/particle-morph
./render.sh /tmp/particle-morph
python3 ../../scripts/deliver.py --frames /tmp/particle-morph/frames --out particle-morph.mp4
```

渲染 B 的完整源码在 [`skills/carl-motion/scenes/particle-morph`](../../skills/carl-motion/scenes/particle-morph)（Python (NumPy + OpenCV + Pillow)），渲染命令写在它的 README 里。
