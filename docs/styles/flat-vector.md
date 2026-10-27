# 19 · Flat Vector · 扁平矢量

[All styles](README.md) · [← Pixel Game](pixel-game.md) · [Impressionist Oil (Monet) →](monet-impressionist.md)

<img src="../../assets/previews/flat-vector.webp" width="100%" alt="Flat Vector">

<sub>Preview: our render (layer B), MIT. 预览是我们渲染的 B，MIT 许可。</sub>

**Status 状态:** Implemented, one scene · 单场景实做

## Prompt (copy this)

Paste into Claude, GPT or any coding model. Swap *your topic* for your own subject.

```text
Use SVG plus GSAP to make a flat vector explainer of your topic: solid colors with no gradients, five or six high-saturation colors, elements entering with springy motion, in one continuous shot. Key visuals: SVG plus GSAP, large solid color blocks, five-or-six-color high-saturation palette, overshoot elastic easing, anticipation then burst then rebound, about 10% squash and stretch, stagger of two to four frames, shape-wipe transitions. Watch out: Adding gradients or moving several subjects at once falls apart; move only one hero at any moment. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
```

## 提示语（复制这段）

发给 Opus 5.5 或任意能写代码的模型，把你的主题换成自己的内容。

```text
用 SVG 加 GSAP 做你的主题的扁平矢量讲解，纯色无渐变，五六种高饱和色，元素弹性入场，一镜到底。画面要点：SVG 加 GSAP、纯色大色块、五六色高饱和色板、overshoot 弹性缓动、预备冲出回弹、约 10% 挤压拉伸、stagger 两到四帧、形状擦除转场。注意：加渐变或几个主体同时动就散了，同一时刻只动一个主角。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
```

## What the two examples show · 两个示例

| | English | 中文 |
|---|---|---|
| A | A computer screen flies in, a red dot bounces, and the popwise brand wordmark on blue closes it out. | 电脑屏幕飞入，红点弹跳，最后蓝底上 popwise 品牌字收尾。 |
| B | Our render: an English explainer version, the start of the story. 10,000 YEARS AGO pops up, field rows and wheat grow, a farmer waves, the camera pans to three clay jars, and grain is poured in. | 我们做的英文讲解版，故事开头。10,000 YEARS AGO 弹出，田垄和麦子长出，农夫招手，镜头摇到三只陶罐，谷子倒进去。 |

## Where it usually breaks · 容易失败的点

Adding gradients or moving several subjects at once falls apart; let only one hero move at a time; keep solid colors to five or six.

加了渐变或几个主体同时动就散；一次只让一个主角动；纯色控制在五六种以内。

## Key visuals · 画面要点

SVG plus GSAP, large solid color blocks, five-or-six-color high-saturation palette, overshoot elastic easing, anticipation then burst then rebound, about 10% squash and stretch, stagger of two to four frames, shape-wipe transitions

SVG 加 GSAP、纯色大色块、五六色高饱和色板、overshoot 弹性缓动、预备冲出回弹、约 10% 挤压拉伸、stagger 两到四帧、形状擦除转场

Palette 主色：`#b88a3e` `#3eb8a8`

## References · 参考来源

| Layer | Title | Source | License |
|---|---|---|---|
| A | 城市与电脑前的人物 | [Vincentwei1021 · mg-styles-15](https://vincentwei1021.github.io/mg-styles-15/?lang=zh#01-flat-vector) | prompts/code MIT; demo video not redistributed |
| B | carl-motion | [this repo](../../skills/carl-motion/scenes/flat-vector) · story idea: [en.yasue.org](https://en.yasue.org/article/pushing-opus-5-5-video-generation-limits) | MIT |

## Reproduce · 复现

Source that rendered the B clip: [`skills/carl-motion/scenes/flat-vector`](../../skills/carl-motion/scenes/flat-vector) (Python (NumPy + OpenCV + Pillow)). Check dependencies first with `python3 skills/carl-motion/scripts/doctor.py flat-vector`.

```bash
cd skills/carl-motion/scenes/flat-vector
./render.sh /tmp/flat-vector
python3 ../../scripts/deliver.py --frames /tmp/flat-vector/frames --out flat-vector.mp4
```

渲染 B 的完整源码在 [`skills/carl-motion/scenes/flat-vector`](../../skills/carl-motion/scenes/flat-vector)（Python (NumPy + OpenCV + Pillow)），渲染命令写在它的 README 里。
