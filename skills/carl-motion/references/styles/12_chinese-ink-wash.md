# 12 · Chinese Ink Wash · 中国水墨 (`chinese-ink-wash`)

## Status · 状态

**Implemented, one scene · 单场景实做.** Our engine rendered the B clip. Start from it and change the subject.

Engine: `scenes/chinese-ink-wash/` (Python (NumPy + OpenCV + Pillow)). Run `./render.sh <work_dir>`, then `scripts/deliver.py --frames <work_dir>/frames --out clip.mp4`. Deterministic: not verified.

## Prompt · 提示语

EN: Use code to draw an ink-wash animation of your topic on rice paper, with only five ink tones, more than half left blank, brushstrokes drawn one stroke at a time, and a single vermilion seal stamped. Key visuals: freehand xieyi style, procedural rice-paper texture, five tones of ink, boneless strokes with ink load, dry-brush skips, 60 to 80 percent blank space, ink-bleed transition, one vermilion seal. Watch out: Do not draw closed outlines; use brush strokes with an ink load that runs dry. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用代码在宣纸上画你的主题的水墨动画，只用五档墨色，留白过半，笔触一笔一笔画出来，只盖一枚朱红印章。画面要点：写意、程序宣纸纹理、墨分五色、没骨带墨量笔触、飞白干笔、留白六到八成、墨晕转场、一枚朱红印章。注意：别画闭合描边轮廓，要用带墨量会枯的毛笔笔触。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#d8d8d8`

## Pipeline · 管线

- 笔触引擎和 S19 同源：变宽墨带加刷毛轨迹，每根刷毛有自己的墨量和枯竭点，笔尾刷毛先后断掉，出飞白。门柱、陶罐、人、猫都是几笔拼出来的，没有闭合描边。
- 墨分五色：焦 1.8、浓 1.0、重 0.62、淡 0.32、清 0.13（浓度倍数），按透射叠加，墨叠墨更深。
- 宣纸：暖白底、两千多根长纤维、低频云斑；湿笔顺着纤维洇开，淡墨边缘积墨；远山山脚化进雾里。
- 留白：画面上半部和中间大片空着，主体压在下方一条地平线上。
- 烘云托月：月亮本身是纸白，外圈清墨烘进来。
- 唯一的红色是右上角的朱红印章，白文猫爪印，按下时略大再落定，印泥不匀、边缘毛。印章里没有文字。
- 字幕用 Baskerville SemiBold，大写、加字距，右上角竖排短行，右对齐，逐行写出；字幕和印章不跟镜头推，保证在安全区内。

## Beats · 节拍

0–0.7 s 宣纸上清墨远山从两侧洇开，中间留白｜0.2–1.0 s 屋檐侧锋一刷、门楣和两根门柱、门洞一层清墨｜0.4–1.6 s 右上角竖排短行逐行写出 PEOPLE / DID NOT / CHASE IT / AWAY｜0.55–1.2 s 拿着扬起扫帚的村民逐笔画出｜0.75–1.5 s 陶罐没骨画出，灶石和柴｜1.0 s 灶火起，灶烟开始往上飘｜1.0–1.7 s 坐着的虎斑猫逐笔画出，罐边几片兰叶草｜1.9–2.9 s 村民把扫帚放到地上，左手向猫伸出，猫转头看他｜2.7–3.7 s 猫在灶边蜷成一团、闭眼｜3.9–4.4 s 字幕墨晕化开，4.35 s 起写出 THE CAT / STAYED｜4.4–5.6 s 村民像墨被水洗淡一样隐去｜4.7–5.7 s 清墨从外往里烘出一轮月亮，5.2 s 淡墨一笔不闭合的圆｜6.2 s 朱红印章按下｜6.3–8 s 猫随呼吸起伏，火苗和灶烟在动，镜头朝猫推近 6%。

## Pitfalls · 踩到的坑

- Vector outlines plus a brush texture look fake; use brush strokes with ink load and no closed outlines; with less blank space it becomes a colorful illustration.
- 矢量描边加笔刷贴图会很假；要带墨量的毛笔笔触，不画闭合轮廓；留白一少就成了彩色插画。
- No jump frames flagged; there are no cuts, and subtitle changes, fade-outs and the moon are all gradual (max frame difference 0.73).
- Frames 1-2 are almost still (difference below 0.02): blank rice paper before the mountains start; only 2 frames.
- Mean frame difference is 0.27, well below the reference A at 2.29; large white space and few moving parts are part of the style.
- The villager and cat are a few loose brush-stroke pieces; the cat going from sitting to curled is one stroke set deforming, not frame-by-frame drawing.
- The clear-ink wash inside the doorway has vertical brush marks that can read as a bamboo blind from afar.

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
