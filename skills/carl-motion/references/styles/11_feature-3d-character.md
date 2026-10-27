# 11 · Feature-film 3D Character · 动画电影式3D角色 (`feature-3d-character`)

## Status · 状态

**Research recipe, prompt only · 研究配方，只有提示语.** No implementation yet. Show the user a still frame before animating.

Engine: none in this skill. Build from the prompt; show a still frame before animating.

## Prompt · 提示语

EN: Use the best technology you can think of to make an animated short, with your topic as the protagonist: cinematic lighting, shallow depth of field, a character with expression and performance, as complex and refined as you can make it. Key visuals: one-shot animated short, tech stack of your choice, cinematic backlight and sunset, shallow depth of field, character expression and performance, a small story told shot by shot, cinematic subtitle bar. Watch out: Just saying make a character falls back to a crude stick figure; explicitly ask for the most complex and refined result. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用你认为最好的技术做一支动画短片，主角是你的主题，电影布光、浅景深、角色有表情有表演，做到你能做到的最复杂最精致。画面要点：one-shot 动画短片、自选技术栈、电影级逆光与夕阳、浅景深、角色表情与表演、按镜头讲小故事、电影字幕条。注意：只说做个角色会退成简陋小人，要明确要求最复杂最精致。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#b86c3e`

## Pipeline · 管线

No engine yet. Build it from these visual keys, one pass per element:

one-shot animated short, tech stack of your choice, cinematic backlight and sunset, shallow depth of field, character expression and performance, a small story told shot by shot, cinematic subtitle bar

one-shot 动画短片、自选技术栈、电影级逆光与夕阳、浅景深、角色表情与表演、按镜头讲小故事、电影字幕条

## Beats · 节拍

—

## Pitfalls · 踩到的坑

- Just saying make a character falls back to a crude SVG figure; state that it should be made as complex as possible and open up Three.js or Blender; without depth of field and rim light it does not look like an animated film.
- 只说做个角色会退成简陋的 SVG 小人；要写明往最复杂了做，放开 Three.js 或 Blender；没有景深和轮廓光就不像动画电影。

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
