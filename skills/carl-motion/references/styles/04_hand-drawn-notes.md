# 04 · Hand-drawn Paper Notes · 纸面手绘笔记 (`hand-drawn-notes`)

## Status · 状态

**Research recipe, prompt only · 研究配方，只有提示语.** No implementation yet. Show the user a still frame before animating.

Engine: none in this skill. Build from the prompt; show a still frame before animating.

## Prompt · 提示语

EN: Use HTML to make a step-by-step animation of your topic on off-white paper: hand-drawn thin lines draw the equipment, and each time something is added, its name and amount pop up in sync. Key visuals: off-white paper, hand-drawn thin-line equipment, handwritten titles and amounts, numbered step cards, from empty to finished, tick marks, explainer pacing. Watch out: If text and action are out of sync there is no explainer feel; every step appears on the same beat. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用 HTML 在米白纸面上做你的主题的步骤动画，手绘细线画器物，每加一样东西就同步跳出名称和用量。画面要点：米白纸面、手绘细线器物、手写体标题与用量、步骤编号卡、从空到成品、刻度线、讲解节奏。注意：字和动作不同步就没有讲解感，每一步同一拍出现。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#ededed`

## Pipeline · 管线

No engine yet. Build it from these visual keys, one pass per element:

off-white paper, hand-drawn thin-line equipment, handwritten titles and amounts, numbered step cards, from empty to finished, tick marks, explainer pacing

米白纸面、手绘细线器物、手写体标题与用量、步骤编号卡、从空到成品、刻度线、讲解节奏

## Beats · 节拍

—

## Pitfalls · 踩到的坑

- If the label and the pouring action are not on the same beat there is no explainer feel; lines that are too regular look like an icon library; too many colors kill the hand-drawn feel.
- 标签和倒酒动作不在同一拍就没有讲解感；线条太规整会像图标库；颜色一多就压掉手绘感。

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
