# 15 · Van Gogh Impasto · 梵高厚涂油画

[All styles](README.md) · [← Isometric 2.5D World](isometric-world.md) · [Iridescent Psychedelic Shader →](psychedelic-shader.md)

<img src="../../assets/previews/van-gogh-impasto.webp" width="100%" alt="Van Gogh Impasto">

<sub>Preview: our render (layer B), MIT. 预览是我们渲染的 B，MIT 许可。</sub>

**Status 状态:** Implemented on an upstream library · 基于上游库实做

## Prompt (copy this)

Paste into Claude, GPT or any coding model. Swap *your topic* for your own subject.

```text
Use Canvas 2D to draw your topic: lay down flat base colors first, then fill short thick impasto strokes following a flow field, a dozen-plus hues per region, with the strokes changing eight times per second. Key visuals: flat-color underpainting plus flow-field strokes, walls vertical and floor along perspective, starry sky swirling around vortexes, region palettes of a dozen-plus hues, short thick impasto, dark blue outlines, 8fps stroke boil, small objects on their own layers. Watch out: Lay strokes in three separate passes for wall, floor and figure; one parameter set for the whole image blurs into a carpet. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
```

## 提示语（复制这段）

发给 Opus 5.5 或任意能写代码的模型，把你的主题换成自己的内容。

```text
用 Canvas 2D 画你的主题，先平涂底色，再顺着流场铺短粗厚涂笔触，每块区域十几种色相，笔触每秒换八次。画面要点：平涂底稿加流场笔触、墙竖地沿透视星空绕漩涡、区域色板十几种色相、短粗厚涂、深蓝描边、8fps 笔触沸腾、小物件单独成层。注意：墙、地、人物分三遍铺笔触，一套参数跑全图会糊成地毯。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
```

## What the two examples show · 两个示例

| | English | 中文 |
|---|---|---|
| A | A girl and a cat in Van Gogh's bedroom, with the wall, floor and figures all made of short impasto strokes. | 少女与猫在梵高卧室里，墙、地板、人物都是短促的厚涂笔触。 |
| B | Our render: Carl walks through a wheat field, with a swirling starry sky and cypress trees overhead. | 我们做的制作。卡尔走过麦田，头顶星空漩涡和柏树。 |

## Where it usually breaks · 容易失败的点

Changing only colors without laying strokes is just an ordinary illustration; wall, floor and figure need separate layers with their own strokes; strokes shaking across the whole screen cause dizziness.

只换颜色不铺笔触就是普通插画；墙、地、人物要分层分别铺笔触；全屏笔触一起抖会晕。

## Key visuals · 画面要点

flat-color underpainting plus flow-field strokes, walls vertical and floor along perspective, starry sky swirling around vortexes, region palettes of a dozen-plus hues, short thick impasto, dark blue outlines, 8fps stroke boil, small objects on their own layers

平涂底稿加流场笔触、墙竖地沿透视星空绕漩涡、区域色板十几种色相、短粗厚涂、深蓝描边、8fps 笔触沸腾、小物件单独成层

Palette 主色：`#3e6cb8` `#b84e3e`

## References · 参考来源

| Layer | Title | Source | License |
|---|---|---|---|
| A | 少女与猫喝茶 · 梵高厚涂油画 | [alchaincyf · huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | MIT (re-rendered from source) |
| B | carl-motion | [this repo](../../skills/carl-motion/scenes/huashu-portraits) | MIT |

## Reproduce · 复现

Source that rendered the B clip: [`skills/carl-motion/scenes/huashu-portraits`](../../skills/carl-motion/scenes/huashu-portraits) (Node + Canvas / headless Chrome). Check dependencies first with `python3 skills/carl-motion/scripts/doctor.py huashu-portraits`.

```bash
cd skills/carl-motion/scenes/huashu-portraits
./render.sh /tmp/van-gogh-impasto s23_wheat
python3 ../../scripts/deliver.py --frames /tmp/van-gogh-impasto/frames --out van-gogh-impasto.mp4
```

渲染 B 的完整源码在 [`skills/carl-motion/scenes/huashu-portraits`](../../skills/carl-motion/scenes/huashu-portraits)（Node + Canvas / headless Chrome），渲染命令写在它的 README 里。
