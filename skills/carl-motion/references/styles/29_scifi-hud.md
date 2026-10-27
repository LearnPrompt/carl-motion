# 29 · Sci-fi Scan HUD · 科幻扫描HUD (`scifi-hud`)

## Status · 状态

**Upstream implementation, link only · 上游实做，只给链接.** LemoLab built it; we only link their code. Read their recipe, then build.

Engine: none in this skill. Upstream code and recipe: see the source column in INDEX.md.

## Prompt · 提示语

EN: Use Three.js wireframes to scan your topic into a glowing holographic volume: target boxes lock onto parts and then pull them apart, numbers roll from garbled characters to true values, in a single color with glow. Key visuals: glowing wireframe, projection base, scan plane growth, target-lock boxes, local teardown, garbled digits rolling down to settle, one cool color plus one warm accent, near-black stage, bloom. Watch out: Do not put text directly over the wireframe; put it on a dark backing plate, and keep the parts connected. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用 Three.js 线框把你的主题扫描成发光全息体，目标框锁定部件再拆开，数字从乱码滚到真值，单色加辉光。画面要点：发光 wireframe、投影底座、扫描面生长、目标锁定框、局部拆解、乱码数字滚动落定、单冷色加一个暖色强调、近黑舞台、bloom。注意：文字别直接压在线框上，放进暗底板，部件之间要连着。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#3ea8b8`

## Pipeline · 管线

No engine yet. Build it from these visual keys, one pass per element:

glowing wireframe, projection base, scan plane growth, target-lock boxes, local teardown, garbled digits rolling down to settle, one cool color plus one warm accent, near-black stage, bloom

发光 wireframe、投影底座、扫描面生长、目标锁定框、局部拆解、乱码数字滚动落定、单冷色加一个暖色强调、近黑舞台、bloom

## Beats · 节拍

—

## Pitfalls · 踩到的坑

- Text laid directly over a wireframe is hard to read, so put it on a dark backing plate; floating parts look fake, so keep them connected; too many colors get messy.
- 线框上直接叠字会看不清，字要放暗底板；部件悬空会假，要连在一起；颜色一多就乱。

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
