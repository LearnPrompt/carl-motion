---
name: carl-motion
description: 29 motion-graphics styles (paper collage, synthwave, ink wash, woodcut, point cloud, claymation, risograph, glassmorphism, blueprint, pixel game, particles, HUD and more), each with a tested copy-paste prompt, known failure points and, for 20 styles, the source code that rendered an 8-second example. Use when the user wants an animated clip, explainer or motion graphic in a named visual style, asks which style fits a topic, wants to restyle an existing animation, or says carl-motion / 动效画风 / 画风盘点 / 用某某画风做动画.
---

# carl-motion

A style library for code-rendered motion graphics. Every entry in `references/styles.md` has a prompt in English and Chinese, the visual keywords, one watch-out line, the failures that usually break the look, its palette, upstream references, and a scene folder when this repo ships source.

## Workflow

1. **Pick the style.** If the user names one, find it in `references/styles.md` (English name, Chinese name or slug). If they describe a feel instead (flat, warm, hand-made, techy, dreamy), offer the two or three closest entries with one line each and let them choose. Ask only when the request truly fits several.

2. **Fill the prompt.** Take that entry's prompt in the user's language and replace *your topic* / 你的主题 with their subject. Keep every number in it (fps, px, colour count, hex values): those are what make the look hold.

3. **Check the failure list before building.** Read the entry's *Breaks when* line and design against each point up front. These come from real renders that went wrong, so treat them as requirements.

4. **Start from source when it exists.** If the entry lists a scene folder (`templates/scenes/<slug>`), read its README and adapt that engine: change the subject, keep the rendering technique. If there is none, build from the prompt in the stack it names.

5. **Render to the house spec.** 1920×1080, 30 fps, exactly 240 frames (8 s), H.264 yuv420p, no audio. `templates/pipeline/encode.sh <frames> <out.mp4>` encodes PNG frames to that spec, and `templates/pipeline/qa.py` checks format, black frames and jump cuts.

6. **Review before calling it done.** Pull frames at 0.5, 2, 4, 6 and 7.5 s and look at them. Compare against the failure list again and say plainly which points still show.

## Output

Return the filled prompt as one copy-pasteable block, the style name and slug, and the failure points you designed against. When you render, also give the MP4 path and the contact sheet, and list anything that did not pass.

## Language

Answer in the user's language. Both prompt versions are in the reference, so either works without translating.

See `references/workflow.md` for the A/B method, colour ordering and the 9:16 explainer layout.
