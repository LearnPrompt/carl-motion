# 18 · Pixel Game · 像素游戏

[All styles](README.md) · [← Claymation Stop-motion](claymation.md) · [Flat Vector →](flat-vector.md)

<img src="../../assets/posters/pixel-game.jpg" width="100%" alt="Pixel Game">

<sub>No redistributable clip. Watch it at the source link. 没有可随仓库分发的片段，去来源链接看。</sub>

**Status 状态:** Research recipe, prompt only · 研究配方，只有提示语

## Prompt (copy this)

Paste into Claude, GPT or any coding model. Swap *your topic* for your own subject.

```text
Use Canvas with a 320×180 internal resolution to draw your topic, upscale 6x with nearest neighbor, limit to 16 to 32 colors, animate sprites in stepped frames, and layer the background with parallax. Key visuals: low-resolution big pixels, limited 16 to 32 color palette, nearest-neighbour integer upscaling, 8 to 12fps sprite frames, parallax scrolling, steps() stepped timing, dithering, game HUD type. Watch out: Smooth scaling or smooth easing blurs it; keep all coordinates and offsets as integers. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
```

## 提示语（复制这段）

发给 Opus 5.5 或任意能写代码的模型，把你的主题换成自己的内容。

```text
用 Canvas 320×180 内部分辨率画你的主题，最近邻放大 6 倍，限定 16 到 32 色，精灵按阶梯帧动，背景分层视差。画面要点：低分辨率大像素、16 到 32 色有限色板、nearest-neighbour 整数放大、8 到 12fps 精灵帧、视差卷轴、steps() 阶梯时序、dithering、游戏 HUD 字。注意：一用平滑缩放或平滑缓动就糊，坐标和位移全取整数。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
```

## What the two examples show · 两个示例

| | English | 中文 |
|---|---|---|
| A | A pixel city on Mid-Autumn night, a rabbit pounding medicine in the moon, rainbow light strips, and HAPPY CHUSEOK in pixel type. | 中秋夜的像素城市，月亮里兔子捣药，彩虹灯带，HAPPY CHUSEOK 像素字。 |
| B | A pixel-game battle over a night lake: a wizard casts meteors and a fire dragon while the score ticks up. | 夜晚湖面上的像素游戏战斗，巫师放出陨石和火龙，分数在跳。 |

## Where it usually breaks · 容易失败的点

Scaling interpolation or easing smears the pixels into a blur; use integer coordinates everywhere and upscale with nearest neighbor; keep the palette within 16 to 32 colors.

缩放插值或缓动会把像素糊成马赛克；坐标全取整数，用最近邻放大；调色板限在 16 到 32 色。

## Key visuals · 画面要点

low-resolution big pixels, limited 16 to 32 color palette, nearest-neighbour integer upscaling, 8 to 12fps sprite frames, parallax scrolling, steps() stepped timing, dithering, game HUD type

低分辨率大像素、16 到 32 色有限色板、nearest-neighbour 整数放大、8 到 12fps 精灵帧、视差卷轴、steps() 阶梯时序、dithering、游戏 HUD 字

Palette 主色：`#4e3eb8`

## References · 参考来源

| Layer | Title | Source | License |
|---|---|---|---|
| A | 中秋像素夜景 | [prompt-motion.com](https://prompt-motion.com/hoyoyoda-3a5c08) | link only |
| B | 像素巫师施法 | [prompt-motion.com](https://prompt-motion.com/0xevinho-3777d8) | link only |

## Reproduce · 复现

No source in this repo yet. The prompt above is enough to build it from scratch.

本仓库暂时没有这个画风的源码，直接用上面的提示语就能从零做出来。
