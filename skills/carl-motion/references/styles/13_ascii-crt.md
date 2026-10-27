# 13 · ASCII Character Visuals · ASCII字符视觉 (`ascii-crt`)

## Status · 状态

**Upstream implementation, link only · 上游实做，只给链接.** LemoLab built it; we only link their code. Read their recipe, then build.

Engine: none in this skill. Upstream code and recipe: see the source column in INDEX.md.

## Prompt · 提示语

EN: Build your topic from a monospace character grid on an amber monochrome CRT phosphor screen, with scanlines and glow, and do the camera push and pull by changing the font size. Key visuals: monospace character grid, amber or green phosphor monochrome, CRT scanlines and barrel distortion, bloom glow, character density gradient, blinking cursor, push and pull by changing font size, typewriter subtitles. Watch out: Every bright spot must be a real character in the grid; applying an ASCII filter to the whole image gives it away. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用等宽字符网格拼出你的主题，琥珀色单色 CRT 荧光屏，加扫描线和辉光，推拉镜头靠改字号来做。画面要点：monospace 字符网格、琥珀或绿色荧光单色、CRT 扫描线与桶形畸变、bloom 辉光、字符密度梯度、光标闪烁、改字号推拉、打字机字幕。注意：每一处亮点都得是网格里的真字符，整图套 ASCII 滤镜会露馅。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#151515`

## Pipeline · 管线

No engine yet. Build it from these visual keys, one pass per element:

monospace character grid, amber or green phosphor monochrome, CRT scanlines and barrel distortion, bloom glow, character density gradient, blinking cursor, push and pull by changing font size, typewriter subtitles

monospace 字符网格、琥珀或绿色荧光单色、CRT 扫描线与桶形畸变、bloom 辉光、字符密度梯度、光标闪烁、改字号推拉、打字机字幕

## Beats · 节拍

—

## Pitfalls · 踩到的坑

- Applying an ASCII filter to the whole image looks like a filter at a glance; every pixel must come from a real character in the grid; too small a character set blurs the image.
- 整张图套 ASCII 滤镜一看就是滤镜；每个像素都要来自网格里的真字符；字符集太少画面会糊。

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
