# 16 · Iridescent Psychedelic Shader · 虹彩迷幻Shader

[All styles](README.md) · [← Van Gogh Impasto](van-gogh-impasto.md) · [Claymation Stop-motion →](claymation.md)

<img src="../../assets/posters/psychedelic-shader.jpg" width="100%" alt="Iridescent Psychedelic Shader">

<sub>No redistributable clip. Watch it at the source link. 没有可随仓库分发的片段，去来源链接看。</sub>

**Status 状态:** Research recipe, prompt only · 研究配方，只有提示语

## Prompt (copy this)

Paste into Claude, GPT or any coding model. Swap *your topic* for your own subject.

```text
Use a shader to make a psychedelic hypnosis animation with your topic as the subject: concentric lines and kaleidoscope symmetry rotating continuously, with iridescent color flowing along the edges. Key visuals: psychedelic hypnosis, concentric lines, kaleidoscope mirror symmetry, vortex tunnel, iridescent thin-film color flowing along edges, high-saturation clashing colors, VJ loop. Watch out: Just writing psychedelic falls back to a plain gradient; spell out the symmetry and the motion. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
```

## 提示语（复制这段）

发给 Opus 5.5 或任意能写代码的模型，把你的主题换成自己的内容。

```text
用 shader 做一支迷幻催眠动画，主题是你的主题，同心线和万花筒对称一直旋转，虹彩色沿边缘流动。画面要点：psychedelic 催眠、同心线、万花筒镜像对称、旋涡隧道、虹彩薄膜色沿边缘流动、高饱和撞色、VJ 循环。注意：只写迷幻两个字会退成普通渐变，要写清对称方式和运动方式。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
```

## What the two examples show · 两个示例

| | English | 中文 |
|---|---|---|
| A | After a black opening, an iridescent eye lights up and the pupil radiates into a tunnel of light beams. | 黑场后亮起一只虹彩眼睛，瞳孔放射成光束隧道。 |
| B | A magenta, cyan and yellow-green kaleidoscope rotates symmetrically and finally turns into a geometric tunnel. | 品红、青、黄绿万花筒对称旋转，最后变成几何隧道。 |

## Where it usually breaks · 容易失败的点

The source is only one sentence and easily falls back to a plain gradient background; specify how many-fold the symmetry is, how it rotates and which colors to use; the first 0.5 seconds of A is black, so avoid it when cutting.

来源只有一句话，容易退成普通渐变背景；要写清几重对称、怎么转、用哪几种色；A 的前 0.5 秒是黑场，剪的时候注意避开。

## Key visuals · 画面要点

psychedelic hypnosis, concentric lines, kaleidoscope mirror symmetry, vortex tunnel, iridescent thin-film color flowing along edges, high-saturation clashing colors, VJ loop

psychedelic 催眠、同心线、万花筒镜像对称、旋涡隧道、虹彩薄膜色沿边缘流动、高饱和撞色、VJ 循环

Palette 主色：`#3ea8b8` `#6c3eb8` `#8ab83e`

## References · 参考来源

| Layer | Title | Source | License |
|---|---|---|---|
| A | 虹彩眼睛与同心线催眠 | [prompt-motion.com](https://prompt-motion.com/monokern-ade5b6) | link only |
| B | 万花筒与彩色旋涡 VJ | [X post](https://x.com/yama_kiyo/status/2103740786177134910) | link only |

## Reproduce · 复现

No source in this repo yet. The prompt above is enough to build it from scratch.

本仓库暂时没有这个画风的源码，直接用上面的提示语就能从零做出来。
