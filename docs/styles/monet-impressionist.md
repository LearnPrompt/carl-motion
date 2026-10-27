# 20 · Impressionist Oil (Monet) · 印象派油画／莫奈

[All styles](README.md) · [← Flat Vector](flat-vector.md) · [Particle Morph →](particle-morph.md)

<img src="../../assets/previews/monet-impressionist.webp" width="100%" alt="Impressionist Oil (Monet)">

<sub>Preview: our render (layer B), MIT. 预览是我们渲染的 B，MIT 许可。</sub>

## Prompt (copy this)

Paste into Claude, GPT or any coding model. Swap *your topic* for your own subject.

```text
Use Canvas 2D to draw your topic with no outlines, short horizontal strokes for the water, warm yellow layered on the lit side and pale purple on the shadow side, with light flecks that flicker. Key visuals: impressionist with no outlines, horizontal water strokes, colored shadows with warm yellow in light and pale purple in shade, bright short-stroke light flecks trembling, 6fps local stroke boil, water lily and Japanese bridge motifs. Watch out: Boiling across the whole screen turns into full-screen noise; keep large areas like the floor and bridge still. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
```

## 提示语（复制这段）

发给 Opus 5.5 或任意能写代码的模型，把你的主题换成自己的内容。

```text
用 Canvas 2D 画你的主题，不勾边，水面用横向短笔触，受光侧叠暖黄、背光侧叠淡紫，光斑一闪一闪。画面要点：印象派不勾边、横向水面笔触、受光暖黄背光淡紫的色彩阴影、亮色短笔光斑颤动、6fps 局部笔触沸腾、睡莲日本桥母题。注意：全屏一起沸腾会变满屏噪点，地板和桥这类大面保持不动。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
```

## What the two examples show · 两个示例

| | English | 中文 |
|---|---|---|
| A | A girl and a cat in front of Monet's water lily window, the whole frame in broken dabs of strokes. | 少女与猫在莫奈睡莲窗前，全画面碎点笔触。 |
| B | Our render: Carl walks onto a green Japanese bridge, with water lilies floating on the water below. | 我们做的制作。卡尔走上绿色日本桥，桥下水面浮着睡莲。 |

## Where it usually breaks · 容易失败的点

Strokes shaking across the whole screen cause dizziness, so animate only the water and light flecks; strokes that are too large blur the figures; juxtapose complementary colors and do not mix them into gray.

全屏笔触一起抖会晕，只让水面和光斑动；笔触太大人物会糊掉；颜色要补色并置，别调成灰。

## Key visuals · 画面要点

impressionist with no outlines, horizontal water strokes, colored shadows with warm yellow in light and pale purple in shade, bright short-stroke light flecks trembling, 6fps local stroke boil, water lily and Japanese bridge motifs

印象派不勾边、横向水面笔触、受光暖黄背光淡紫的色彩阴影、亮色短笔光斑颤动、6fps 局部笔触沸腾、睡莲日本桥母题

Palette 主色：`#b86c3e` `#3e6cb8`

## References · 参考来源

| Layer | Title | Source | License |
|---|---|---|---|
| A | 少女与猫喝茶 · 印象派油画／莫奈 | [alchaincyf · huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | MIT (re-rendered from source) |
| B | carl-motion | [this repo](../../templates/scenes/huashu-portraits) | MIT |

## Reproduce · 复现

Source that rendered the B clip: [`templates/scenes/huashu-portraits`](../../templates/scenes/huashu-portraits) (Canvas / HTML + Node). Its README has the exact render command.

渲染 B 的完整源码在 [`templates/scenes/huashu-portraits`](../../templates/scenes/huashu-portraits)（Canvas / HTML + Node），渲染命令写在它的 README 里。
