# 01 · Retro Paper Collage · 复古纸张拼贴 (`retro-paper-collage`)

## Status · 状态

**Implemented, one scene · 单场景实做.** Our engine rendered the B clip. Start from it and change the subject.

Engine: `scenes/retro-paper-collage/` (Python (NumPy + OpenCV + Pillow)). Run `./render.sh <work_dir>`, then `scripts/deliver.py --frames <work_dir>/frames --out clip.mp4`. Deterministic: not verified.

## Prompt · 提示语

EN: Use HTML to turn your topic into a retro paper collage: cut-out assets with white scissor edges and halftone dots, motion dropped to 12 fps, with a slight hand jitter. Key visuals: newspaper and kraft paper background, cut-outs with a 2 to 4px white scissor edge, halftone dots, 12fps down to 6fps, plus or minus 2px hand-moved jitter, slap-on and page-flip transitions, red and black constructivist type, ransom-note lettering. Watch out: Full-frame smooth motion loses the handmade feel; drop to 12 fps and add 2px of jitter. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用 HTML 做你的主题的复古纸张拼贴，素材抠图加白色剪刀边和半调网点，运动降到 12 帧，加轻微手抖。画面要点：报纸牛皮纸底、抠图加 2 到 4px 白剪刀边、halftone 网点、12fps 乃至 6fps、正负 2px 手摆抖动、拍上来与翻页转场、红黑构成主义字、勒索信拼字。注意：满帧顺滑就没有手作感，降到 12 帧再加 2px 抖动。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#b88a3e`, `#3e8ab8`

## Pipeline · 管线

- 每个元素是一张剪纸：形状遮罩模糊后加噪声阈值，得到撕纸毛边；主体外面再撕一圈白纸边；底下一层软投影。
- 纸材是 512 平铺的周期纹理：牛皮纸、带小字的旧报纸、蓝天和太阳的半调网点、稻草斜纹、陶土网点、方格纸、蓝白条纹胶带。
- 勒索信字：每个字母单独一块纸片，十种字体、九种底色、各自 ±7° 的角度，按拍砸上来，第一拍放大 1.14。
- 元素动作按 12 fps 走，撕边每拍换一张，三张循环（定格的 boil）；镜头每拍手持微抖，8 秒推近约 1%；整体加左上偏亮的翻拍光和每拍纸面噪点。

## Beats · 节拍

0–2.4 s 牛皮纸桌面上，勒索信字逐个拍上来：WHY DID CATS / MOVE IN WITH US?，一只纸老鼠从底部窜过｜2.4–2.75 s 标题纸整张往左抽走｜2.55 s 左上角拍上 10,000 YEARS AGO｜2.9–4.1 s 四只老鼠依次跑向陶罐前的谷堆，字幕 STORED GRAIN DREW MICE｜4.6–6.1 s 虎斑野猫从右侧走进，5.2 s 字幕换成 ...AND MICE DREW WILDCATS｜6.0 s 老鼠四散｜6.2 s 猫抬头｜6.4 s 贴上 WILDCAT 黑标签和红箭头，6.75 s 补一条 Felis lybica 学名，停到 8 s。

## Pitfalls · 踩到的坑

- Full-frame smooth motion looks like PowerPoint animation; drop to 12 fps and add a light jitter on every beat. Cut-outs without torn edges and drop shadows fall back to flat vector. Using only one typeface loses the ransom-note collage feel.
- 满帧顺滑运动像 PPT 动画，要降到 12 帧再加每拍轻抖；剪片缺撕边和投影就退成扁平矢量；字体只用一种就没有勒索信的拼贴味。
- The cat and mice are paper cut-out assemblies with simple swinging legs and no fine expressions.
- The jump frames 73, 75, 78 and 155 flagged by the automated check are the title paper being pulled away and caption changes: by design.
- At 12 fps stop-motion, frame differences within a beat are close to 0; the style requires it.

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
