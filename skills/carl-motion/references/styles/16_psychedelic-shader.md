# 16 · Iridescent Psychedelic Shader · 虹彩迷幻Shader (`psychedelic-shader`)

## Status · 状态

**Research recipe, prompt only · 研究配方，只有提示语.** No implementation yet. Show the user a still frame before animating.

Engine: none in this skill. Build from the prompt; show a still frame before animating.

## Prompt · 提示语

EN: Use a shader to make a psychedelic hypnosis animation with your topic as the subject: concentric lines and kaleidoscope symmetry rotating continuously, with iridescent color flowing along the edges. Key visuals: psychedelic hypnosis, concentric lines, kaleidoscope mirror symmetry, vortex tunnel, iridescent thin-film color flowing along edges, high-saturation clashing colors, VJ loop. Watch out: Just writing psychedelic falls back to a plain gradient; spell out the symmetry and the motion. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用 shader 做一支迷幻催眠动画，主题是你的主题，同心线和万花筒对称一直旋转，虹彩色沿边缘流动。画面要点：psychedelic 催眠、同心线、万花筒镜像对称、旋涡隧道、虹彩薄膜色沿边缘流动、高饱和撞色、VJ 循环。注意：只写迷幻两个字会退成普通渐变，要写清对称方式和运动方式。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#3ea8b8`, `#6c3eb8`, `#8ab83e`

## Pipeline · 管线

No engine yet. Build it from these visual keys, one pass per element:

psychedelic hypnosis, concentric lines, kaleidoscope mirror symmetry, vortex tunnel, iridescent thin-film color flowing along edges, high-saturation clashing colors, VJ loop

psychedelic 催眠、同心线、万花筒镜像对称、旋涡隧道、虹彩薄膜色沿边缘流动、高饱和撞色、VJ 循环

## Beats · 节拍

—

## Pitfalls · 踩到的坑

- The source is only one sentence and easily falls back to a plain gradient background; specify how many-fold the symmetry is, how it rotates and which colors to use; the first 0.5 seconds of A is black, so avoid it when cutting.
- 来源只有一句话，容易退成普通渐变背景；要写清几重对称、怎么转、用哪几种色；A 的前 0.5 秒是黑场，剪的时候注意避开。

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
