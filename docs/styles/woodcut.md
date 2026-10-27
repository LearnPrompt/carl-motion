# 06 · Black-and-white Woodcut · 黑白木刻版画

[All styles](README.md) · [← Watercolor](watercolor.md) · [Soft Inflatable 3D →](soft-inflatable-3d.md)

<img src="../../assets/previews/woodcut.webp" width="100%" alt="Black-and-white Woodcut">

<sub>Preview: our render (layer B), MIT. 预览是我们渲染的 B，MIT 许可。</sub>

**Status 状态:** Implemented, one scene · 单场景实做

## Prompt (copy this)

Paste into Claude, GPT or any coding model. Swap *your topic* for your own subject.

```text
Turn your topic into a black-and-white woodcut print: a solid black block, highlights are white lines cut away by the knife, the image is carved out one cut at a time, with at most one red. Key visuals: white lines cut into a black block, light is carved out, image appears cut by cut with no fade-in, bold cuts in front and fine lines behind, cut lines follow the form, at most one color, paper margin left white, mirrored-lettering print-out transition. Watch out: Hatching on every surface looks like fur and rain; cut only three to six strokes on the lit edge. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
```

## 提示语（复制这段）

发给 Opus 5.5 或任意能写代码的模型，把你的主题换成自己的内容。

```text
把你的主题做成黑白木刻版画，整块黑版，亮部是刀刻掉的白线，画面一刀一刀刻出来，最多留一种红。画面要点：黑版白刻、光是刻出来的、画面逐刀刻出不淡入、粗刀在前细线在后、刀线顺形体走、最多一种颜色、纸边留白、反字印出转场。注意：每个面都排线会像毛和雨，只在受光边刻三到六刀。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
```

## What the two examples show · 两个示例

| | English | 中文 |
|---|---|---|
| A | White cuts on a black block: an iron pot, a ring and a blacksmith's forge are carved out cut by cut, with English subtitles at the bottom. | 黑版白刻，铁锅、戒指、铁匠炉一刀一刀刻出来，底部英文字幕。 |
| B | Our render: a sailboat at sea after a storm raises its sails again, the waves are knife-cut hatching, the sun rises out of the cut lines, with Chinese and English subtitles. | 我们做的制作。风暴后的海上帆船重新升帆，海浪是刀刻排线，太阳从刻线里升起，中英字幕。 |

## Where it usually breaks · 容易失败的点

Hatching on every surface looks like fur and rain, so cut only three to six strokes on the lit edge; if the image fades in it no longer looks carved; keep at most one color.

每个面都排线会像毛和雨，只在受光边刻三到六刀；画面用淡入出现就不像刻的；颜色最多留一种。

## Key visuals · 画面要点

white lines cut into a black block, light is carved out, image appears cut by cut with no fade-in, bold cuts in front and fine lines behind, cut lines follow the form, at most one color, paper margin left white, mirrored-lettering print-out transition

黑版白刻、光是刻出来的、画面逐刀刻出不淡入、粗刀在前细线在后、刀线顺形体走、最多一种颜色、纸边留白、反字印出转场

Palette 主色：`#565656`

## References · 参考来源

| Layer | Title | Source | License |
|---|---|---|---|
| A | 木刻版画：The Bell Founder | [LemoLab · lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar/tree/main/styles/woodcut) | prompts/code MIT, demo video CC BY 4.0 |
| B | carl-motion | [this repo](../../skills/carl-motion/scenes/woodcut) | MIT |

## Reproduce · 复现

Source that rendered the B clip: [`skills/carl-motion/scenes/woodcut`](../../skills/carl-motion/scenes/woodcut) (Python (NumPy + OpenCV + Pillow)). Check dependencies first with `python3 skills/carl-motion/scripts/doctor.py woodcut`.

```bash
cd skills/carl-motion/scenes/woodcut
./render.sh /tmp/woodcut
python3 ../../scripts/deliver.py --frames /tmp/woodcut/frames --out woodcut.mp4
```

渲染 B 的完整源码在 [`skills/carl-motion/scenes/woodcut`](../../skills/carl-motion/scenes/woodcut)（Python (NumPy + OpenCV + Pillow)），渲染命令写在它的 README 里。
