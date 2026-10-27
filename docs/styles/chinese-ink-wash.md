# 12 · Chinese Ink Wash · 中国水墨

[All styles](README.md) · [← Feature-film 3D Character](feature-3d-character.md) · [ASCII Character Visuals →](ascii-crt.md)

<img src="../../assets/previews/chinese-ink-wash.webp" width="100%" alt="Chinese Ink Wash">

<sub>Preview: our render (layer B), MIT. 预览是我们渲染的 B，MIT 许可。</sub>

**Status 状态:** Implemented, one scene · 单场景实做

## Prompt (copy this)

Paste into Claude, GPT or any coding model. Swap *your topic* for your own subject.

```text
Use code to draw an ink-wash animation of your topic on rice paper, with only five ink tones, more than half left blank, brushstrokes drawn one stroke at a time, and a single vermilion seal stamped. Key visuals: freehand xieyi style, procedural rice-paper texture, five tones of ink, boneless strokes with ink load, dry-brush skips, 60 to 80 percent blank space, ink-bleed transition, one vermilion seal. Watch out: Do not draw closed outlines; use brush strokes with an ink load that runs dry. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
```

## 提示语（复制这段）

发给 Opus 5.5 或任意能写代码的模型，把你的主题换成自己的内容。

```text
用代码在宣纸上画你的主题的水墨动画，只用五档墨色，留白过半，笔触一笔一笔画出来，只盖一枚朱红印章。画面要点：写意、程序宣纸纹理、墨分五色、没骨带墨量笔触、飞白干笔、留白六到八成、墨晕转场、一枚朱红印章。注意：别画闭合描边轮廓，要用带墨量会枯的毛笔笔触。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
```

## What the two examples show · 两个示例

| | English | 中文 |
|---|---|---|
| A | On rice paper with large blank areas, a bird skims the water, with reeds and ripples and an English poem as subtitles. | 大片留白的宣纸上，一只鸟掠过水面，芦苇和涟漪，英文诗句字幕。 |
| B | Our render: an English explainer version. A villager puts down a broom and reaches out, a cat curls up by the stove, the moon comes out, a red seal lands, and the subtitle PEOPLE DID NOT CHASE IT AWAY changes to THE CAT STAYED. | 我们做的英文讲解版。村民放下扫帚伸出手，猫在灶边蜷起，月亮出来、红印落下，字幕 PEOPLE DID NOT CHASE IT AWAY 换成 THE CAT STAYED。 |

## Where it usually breaks · 容易失败的点

Vector outlines plus a brush texture look fake; use brush strokes with ink load and no closed outlines; with less blank space it becomes a colorful illustration.

矢量描边加笔刷贴图会很假；要带墨量的毛笔笔触，不画闭合轮廓；留白一少就成了彩色插画。

## Key visuals · 画面要点

freehand xieyi style, procedural rice-paper texture, five tones of ink, boneless strokes with ink load, dry-brush skips, 60 to 80 percent blank space, ink-bleed transition, one vermilion seal

写意、程序宣纸纹理、墨分五色、没骨带墨量笔触、飞白干笔、留白六到八成、墨晕转场、一枚朱红印章

Palette 主色：`#d8d8d8`

## References · 参考来源

| Layer | Title | Source | License |
|---|---|---|---|
| A | 持剑者与墨浪 | [LemoLab · lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar/tree/main/styles/ink-wash) | prompts/code MIT, demo video CC BY 4.0 |
| B | carl-motion | [this repo](../../skills/carl-motion/scenes/chinese-ink-wash) · story idea: [en.yasue.org](https://en.yasue.org/article/pushing-opus-5-5-video-generation-limits) | MIT |

## Reproduce · 复现

Source that rendered the B clip: [`skills/carl-motion/scenes/chinese-ink-wash`](../../skills/carl-motion/scenes/chinese-ink-wash) (Python (NumPy + OpenCV + Pillow)). Check dependencies first with `python3 skills/carl-motion/scripts/doctor.py chinese-ink-wash`.

```bash
cd skills/carl-motion/scenes/chinese-ink-wash
./render.sh /tmp/chinese-ink-wash
python3 ../../scripts/deliver.py --frames /tmp/chinese-ink-wash/frames --out chinese-ink-wash.mp4
```

渲染 B 的完整源码在 [`skills/carl-motion/scenes/chinese-ink-wash`](../../skills/carl-motion/scenes/chinese-ink-wash)（Python (NumPy + OpenCV + Pillow)），渲染命令写在它的 README 里。
