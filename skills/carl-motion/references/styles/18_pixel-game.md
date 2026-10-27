# 18 · Pixel Game · 像素游戏 (`pixel-game`)

## Status · 状态

**Research recipe, prompt only · 研究配方，只有提示语.** No implementation yet. Show the user a still frame before animating.

Engine: none in this skill. Build from the prompt; show a still frame before animating.

## Prompt · 提示语

EN: Use Canvas with a 320×180 internal resolution to draw your topic, upscale 6x with nearest neighbor, limit to 16 to 32 colors, animate sprites in stepped frames, and layer the background with parallax. Key visuals: low-resolution big pixels, limited 16 to 32 color palette, nearest-neighbour integer upscaling, 8 to 12fps sprite frames, parallax scrolling, steps() stepped timing, dithering, game HUD type. Watch out: Smooth scaling or smooth easing blurs it; keep all coordinates and offsets as integers. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用 Canvas 320×180 内部分辨率画你的主题，最近邻放大 6 倍，限定 16 到 32 色，精灵按阶梯帧动，背景分层视差。画面要点：低分辨率大像素、16 到 32 色有限色板、nearest-neighbour 整数放大、8 到 12fps 精灵帧、视差卷轴、steps() 阶梯时序、dithering、游戏 HUD 字。注意：一用平滑缩放或平滑缓动就糊，坐标和位移全取整数。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#4e3eb8`

## Pipeline · 管线

No engine yet. Build it from these visual keys, one pass per element:

low-resolution big pixels, limited 16 to 32 color palette, nearest-neighbour integer upscaling, 8 to 12fps sprite frames, parallax scrolling, steps() stepped timing, dithering, game HUD type

低分辨率大像素、16 到 32 色有限色板、nearest-neighbour 整数放大、8 到 12fps 精灵帧、视差卷轴、steps() 阶梯时序、dithering、游戏 HUD 字

## Beats · 节拍

—

## Pitfalls · 踩到的坑

- Scaling interpolation or easing smears the pixels into a blur; use integer coordinates everywhere and upscale with nearest neighbor; keep the palette within 16 to 32 colors.
- 缩放插值或缓动会把像素糊成马赛克；坐标全取整数，用最近邻放大；调色板限在 16 到 32 色。

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
