# 05 · Watercolor · 水彩手绘

[All styles](README.md) · [← Hand-drawn Paper Notes](hand-drawn-notes.md) · [Black-and-white Woodcut →](woodcut.md)

<img src="../../assets/previews/watercolor.webp" width="100%" alt="Watercolor">

<sub>Preview: our render (layer B), MIT. 预览是我们渲染的 B，MIT 许可。</sub>

**Status 状态:** Implemented, one scene · 单场景实做

## Prompt (copy this)

Paste into Claude, GPT or any coding model. Swap *your topic* for your own subject.

```text
Use Canvas to draw a watercolor journal page that colors itself, with your topic as the subject: transparent strokes layered one on another, dry-brush skips, and paper white kept for highlights. Key visuals: warm cotton paper fibers, transparent wash that deepens as it layers, dry-brush skips, paper white as highlight, handwritten notes with leader lines, stroke-by-stroke coloring, mist-wipe transition, low-saturation ochre and gray-blue. Watch out: Vector shapes with a watercolor texture look fake; use variable-width strokes plus bristle trails. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
```

## 提示语（复制这段）

发给 Opus 5.5 或任意能写代码的模型，把你的主题换成自己的内容。

```text
用 Canvas 画一页会自己上色的水彩手账，主题是你的主题，透明笔触一层层叠，干笔飞白，纸白留作高光。画面要点：暖色棉纸纤维、透明 wash 越叠越深、dry-brush 飞白、纸白当高光、手写批注加引线、逐笔上色、薄雾擦除转场、赭石灰蓝低饱和。注意：矢量图贴水彩纹理会假，要用变宽笔触加毛刷轨迹。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
```

## What the two examples show · 两个示例

| | English | 中文 |
|---|---|---|
| A | A watercolor of an Australian eucalyptus forest, with bleeding distant hills and a paper-white sky, a rainfall reading changing in the top right, and bilingual subtitles at the bottom. | 澳洲桉树林水彩，远山晕染、纸白天空，右上角雨量读数在变，底部双语字幕。 |
| B | Our render: an English explainer version, part two of the cat-moves-into-the-village story. Adobe houses and clay jars are brushed in stroke by stroke, mice shift toward the grain pile, a tabby wildcat steps out of the reeds, and the subtitle STORED GRAIN DREW MICE changes to THEN CAME THE WILDCAT. | 我们做的英文讲解版，猫进村故事第二段。土坯房、陶罐一笔笔刷出来，老鼠挪向谷堆，虎斑野猫从芦苇里走出，字幕 STORED GRAIN DREW MICE 换成 THEN CAME THE WILDCAT。 |

## Where it usually breaks · 容易失败的点

Vector shapes with a watercolor texture look fake at a glance; use variable-width strokes and bristle edges, leave paper white in the highlights, and do not fill whole areas with color.

矢量形状贴水彩纹理一眼就假；要用变宽笔触和毛刷边，亮部留纸白；颜色别填满整块。

## Key visuals · 画面要点

warm cotton paper fibers, transparent wash that deepens as it layers, dry-brush skips, paper white as highlight, handwritten notes with leader lines, stroke-by-stroke coloring, mist-wipe transition, low-saturation ochre and gray-blue

暖色棉纸纤维、透明 wash 越叠越深、dry-brush 飞白、纸白当高光、手写批注加引线、逐笔上色、薄雾擦除转场、赭石灰蓝低饱和

Palette 主色：`#b88a3e`

## References · 参考来源

| Layer | Title | Source | License |
|---|---|---|---|
| A | 澳洲树木与水彩地图 | [LemoLab · lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar/tree/main/styles/watercolor) | prompts/code MIT, demo video CC BY 4.0 |
| B | carl-motion | [this repo](../../skills/carl-motion/scenes/watercolor) · story idea: [en.yasue.org](https://en.yasue.org/article/pushing-opus-5-5-video-generation-limits) | MIT |

## Reproduce · 复现

Source that rendered the B clip: [`skills/carl-motion/scenes/watercolor`](../../skills/carl-motion/scenes/watercolor) (Python (NumPy + OpenCV + Pillow)). Check dependencies first with `python3 skills/carl-motion/scripts/doctor.py watercolor`.

```bash
cd skills/carl-motion/scenes/watercolor
./render.sh /tmp/watercolor
python3 ../../scripts/deliver.py --frames /tmp/watercolor/frames --out watercolor.mp4
```

渲染 B 的完整源码在 [`skills/carl-motion/scenes/watercolor`](../../skills/carl-motion/scenes/watercolor)（Python (NumPy + OpenCV + Pillow)），渲染命令写在它的 README 里。
