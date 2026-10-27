# carl-motion style reference (29 styles)

Generated from data/styles.*.json. Each entry: English and Chinese prompt, key visuals, watch-out line, common failures, palette, references, and the scene folder when the repo ships source.

## 01 Retro Paper Collage · 复古纸张拼贴 (`retro-paper-collage`)

- Use when: the user wants retro paper collage / 复古纸张拼贴.
- Prompt (EN): Use HTML to turn your topic into a retro paper collage: cut-out assets with white scissor edges and halftone dots, motion dropped to 12 fps, with a slight hand jitter. Key visuals: newspaper and kraft paper background, cut-outs with a 2 to 4px white scissor edge, halftone dots, 12fps down to 6fps, plus or minus 2px hand-moved jitter, slap-on and page-flip transitions, red and black constructivist type, ransom-note lettering. Watch out: Full-frame smooth motion loses the handmade feel; drop to 12 fps and add 2px of jitter. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用 HTML 做你的主题的复古纸张拼贴，素材抠图加白色剪刀边和半调网点，运动降到 12 帧，加轻微手抖。画面要点：报纸牛皮纸底、抠图加 2 到 4px 白剪刀边、halftone 网点、12fps 乃至 6fps、正负 2px 手摆抖动、拍上来与翻页转场、红黑构成主义字、勒索信拼字。注意：满帧顺滑就没有手作感，降到 12 帧再加 2px 抖动。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: Full-frame smooth motion looks like PowerPoint animation; drop to 12 fps and add a light jitter on every beat. Cut-outs without torn edges and drop shadows fall back to flat vector. Using only one typeface loses the ransom-note collage feel.
- 容易失败: 满帧顺滑运动像 PPT 动画，要降到 12 帧再加每拍轻抖；剪片缺撕边和投影就退成扁平矢量；字体只用一种就没有勒索信的拼贴味。
- Palette: #b88a3e, #3e8ab8
- Scene source: templates/scenes/retro-paper-collage
- References: A Vincentwei1021 · mg-styles-15 https://vincentwei1021.github.io/mg-styles-15/?lang=zh#06-collage; B carl-motion

## 02 Product UI 2.5D Camera · 产品界面2.5D运镜 (`product-ui-2-5d`)

- Use when: the user wants product ui 2.5d camera / 产品界面2.5D运镜.
- Prompt (EN): Use Remotion to turn real screenshots of your product's pages into a promo video: tilt the screenshots in 3D for a 2.5D camera move, and hold key information for more than one second. Key visuals: Remotion, real page screenshots, 2.5D page camera, pages tilted then layered, beat-synced cuts, number roll-ups, flash frames, key information held for one second. Watch out: Pacing that is too fast, with the whole screen shaking on every beat, looks cheap; slow it down one notch. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用 Remotion 把你的产品真实页面截图做成宣传片，截图 3D 倾斜做 2.5D 运镜，关键信息停留一秒以上。画面要点：Remotion、真实页面截图、2.5D 页面相机、页面倾斜后分层、卡点剪辑、数字滚动、闪帧、关键信息停留一秒。注意：节奏太快、整屏一拍一抖会廉价，放慢一档。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: Fast pacing with the whole screen shaking together looks cheap; slow it down one notch. UI text must be real and readable, since gray blurred bars look like placeholders. A perspective angle that keeps changing causes dizziness.
- 容易失败: 节奏快、整屏一起抖会显廉价，要放慢一档；界面字要真实可读，糊成灰条就像占位图；透视角度来回变会晕。
- Palette: #d2d2d2
- Scene source: none, build from the prompt
- References: A Vincentwei1021 · video-shotcraft https://vincentwei1021.github.io/video-shotcraft/showcase.html; B Vincentwei1021 · video-shotcraft https://vincentwei1021.github.io/video-shotcraft/showcase.html

## 03 Neon Synthwave · 霓虹复古Synthwave (`neon-synthwave`)

- Use when: the user wants neon synthwave / 霓虹复古Synthwave.
- Prompt (EN): Make your topic into an 80s Synthwave: a one-point-perspective neon grid rolling forward, a layered sunset on the horizon, double-layer glow on the lines, with scanlines and chromatic aberration on top. Key visuals: one-point-perspective grid scrolling, multi-layer gradient sunset, double-layer glow, scanlines and RGB color shift, chrome lettering, palm tree silhouettes, tape stutter at 15fps in selected spots. Watch out: Without the grid rolling there is no sense of speed; the camera must keep rushing forward. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 做你的主题的 80 年代 Synthwave，一点透视霓虹网格往前滚，地平线放分层落日，线条双层辉光，叠扫描线和色偏。画面要点：一点透视网格滚动、多层渐变落日、双层辉光、扫描线与 RGB 色偏、镀铬字、棕榈剪影、局部抽到 15fps 的磁带卡顿。注意：网格不滚就没速度感，镜头要一直往前冲。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: A grid that does not roll forward becomes a static wallpaper; colors outside magenta, cyan and orange look muddy; stacking too many glow layers blurs everything together.
- 容易失败: 网格不往前滚就成了静态壁纸；颜色跑出品红、青、橙会发脏；辉光叠太多层会糊成一片。
- Palette: #b83ea8
- Scene source: templates/scenes/neon-synthwave
- References: A Vincentwei1021 · mg-styles-15 https://vincentwei1021.github.io/mg-styles-15/?lang=zh#10-synthwave; B carl-motion

## 04 Hand-drawn Paper Notes · 纸面手绘笔记 (`hand-drawn-notes`)

- Use when: the user wants hand-drawn paper notes / 纸面手绘笔记.
- Prompt (EN): Use HTML to make a step-by-step animation of your topic on off-white paper: hand-drawn thin lines draw the equipment, and each time something is added, its name and amount pop up in sync. Key visuals: off-white paper, hand-drawn thin-line equipment, handwritten titles and amounts, numbered step cards, from empty to finished, tick marks, explainer pacing. Watch out: If text and action are out of sync there is no explainer feel; every step appears on the same beat. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用 HTML 在米白纸面上做你的主题的步骤动画，手绘细线画器物，每加一样东西就同步跳出名称和用量。画面要点：米白纸面、手绘细线器物、手写体标题与用量、步骤编号卡、从空到成品、刻度线、讲解节奏。注意：字和动作不同步就没有讲解感，每一步同一拍出现。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: If the label and the pouring action are not on the same beat there is no explainer feel; lines that are too regular look like an icon library; too many colors kill the hand-drawn feel.
- 容易失败: 标签和倒酒动作不在同一拍就没有讲解感；线条太规整会像图标库；颜色一多就压掉手绘感。
- Palette: #ededed
- Scene source: none, build from the prompt
- References: A prompt-motion.com https://prompt-motion.com/ror-fly-9950f1; B prompt-motion.com https://prompt-motion.com/sarut0bisasuke-cefa43

## 05 Watercolor · 水彩手绘 (`watercolor`)

- Use when: the user wants watercolor / 水彩手绘.
- Prompt (EN): Use Canvas to draw a watercolor journal page that colors itself, with your topic as the subject: transparent strokes layered one on another, dry-brush skips, and paper white kept for highlights. Key visuals: warm cotton paper fibers, transparent wash that deepens as it layers, dry-brush skips, paper white as highlight, handwritten notes with leader lines, stroke-by-stroke coloring, mist-wipe transition, low-saturation ochre and gray-blue. Watch out: Vector shapes with a watercolor texture look fake; use variable-width strokes plus bristle trails. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用 Canvas 画一页会自己上色的水彩手账，主题是你的主题，透明笔触一层层叠，干笔飞白，纸白留作高光。画面要点：暖色棉纸纤维、透明 wash 越叠越深、dry-brush 飞白、纸白当高光、手写批注加引线、逐笔上色、薄雾擦除转场、赭石灰蓝低饱和。注意：矢量图贴水彩纹理会假，要用变宽笔触加毛刷轨迹。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: Vector shapes with a watercolor texture look fake at a glance; use variable-width strokes and bristle edges, leave paper white in the highlights, and do not fill whole areas with color.
- 容易失败: 矢量形状贴水彩纹理一眼就假；要用变宽笔触和毛刷边，亮部留纸白；颜色别填满整块。
- Palette: #b88a3e
- Scene source: templates/scenes/watercolor
- References: A LemoLab · lemo-opuscar https://github.com/lemomo-ai/lemo-opuscar/tree/main/styles/watercolor; B carl-motion

## 06 Black-and-white Woodcut · 黑白木刻版画 (`woodcut`)

- Use when: the user wants black-and-white woodcut / 黑白木刻版画.
- Prompt (EN): Turn your topic into a black-and-white woodcut print: a solid black block, highlights are white lines cut away by the knife, the image is carved out one cut at a time, with at most one red. Key visuals: white lines cut into a black block, light is carved out, image appears cut by cut with no fade-in, bold cuts in front and fine lines behind, cut lines follow the form, at most one color, paper margin left white, mirrored-lettering print-out transition. Watch out: Hatching on every surface looks like fur and rain; cut only three to six strokes on the lit edge. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 把你的主题做成黑白木刻版画，整块黑版，亮部是刀刻掉的白线，画面一刀一刀刻出来，最多留一种红。画面要点：黑版白刻、光是刻出来的、画面逐刀刻出不淡入、粗刀在前细线在后、刀线顺形体走、最多一种颜色、纸边留白、反字印出转场。注意：每个面都排线会像毛和雨，只在受光边刻三到六刀。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: Hatching on every surface looks like fur and rain, so cut only three to six strokes on the lit edge; if the image fades in it no longer looks carved; keep at most one color.
- 容易失败: 每个面都排线会像毛和雨，只在受光边刻三到六刀；画面用淡入出现就不像刻的；颜色最多留一种。
- Palette: #565656
- Scene source: templates/scenes/woodcut
- References: A LemoLab · lemo-opuscar https://github.com/lemomo-ai/lemo-opuscar/tree/main/styles/woodcut; B carl-motion

## 07 Soft Inflatable 3D · 软体充气3D (`soft-inflatable-3d`)

- Use when: the user wants soft inflatable 3d / 软体充气3D.
- Prompt (EN): Use Blender to make your topic as soft inflatable 3D: candy-colored soft rubber with subsurface scattering, squashing flat on landing then bouncing back fast, studio three-point lighting, shallow depth of field. Key visuals: SSS soft rubber, candy colors, AO plus HDRI three-point lighting, cloner arrays, soft-body collision squash, long-tail easing, shallow depth of field and motion blur, 24fps cinematic frame rate. Watch out: A slow rebound has no weight: accelerate on the fall, squash on contact, and bounce back fast. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用 Blender 做你的主题的软体充气 3D，糖果色软胶带次表面散射，落地压扁再快速弹起，棚拍三点光，浅景深。画面要点：SSS 软胶、糖果色、AO 加 HDRI 三点光、克隆阵列、软体碰撞挤压、长尾缓动、浅景深与运动模糊、24fps 电影帧率。注意：回弹一慢就没重量，下落加速、触地压扁、弹起要快。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: A slow rebound has no weight; a material without subsurface scattering looks like hard plastic; flat lighting looks like a web illustration.
- 容易失败: 回弹一慢就没重量；材质缺次表面散射会像硬塑料；光打平了就像网页插图。
- Palette: #b83e6c, #b86c3e
- Scene source: templates/scenes/soft-inflatable-3d
- References: A Vincentwei1021 · mg-styles-15 https://vincentwei1021.github.io/mg-styles-15/?lang=zh#04-3d-render; B carl-motion

## 08 Point-cloud Survey · 点云测绘／剥层 (`point-cloud-survey`)

- Use when: the user wants point-cloud survey / 点云测绘／剥层.
- Prompt (EN): Use Three.js to turn your location into a laser point cloud: real measured points floating on black, a scan plane passes and the points solidify into solid terrain, then peel apart layer by layer by ground, vegetation and buildings. Key visuals: real airborne lidar points, near-black background, scan line or section plane advancing, points condense into a solid lit at grazing angle, layers peeled by ground, vegetation and building classes, hairline measurement readouts, one designed camera move. Watch out: From afar a point cloud looks like a flat carpet; the camera must fly low and close. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用 Three.js 把你的地点做成激光点云，黑底悬浮真实测量点，扫描面经过后凝成实体地形，再按地面植被建筑逐层剥开。画面要点：真实机载激光点、近黑底、扫描线或剖切面推进、点凝成掠射光实体、按地面植被建筑分类剥层、发丝线测量读数、一条设计好的运镜。注意：远看点云像平地毯，镜头要贴低穿过去。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: From afar a point cloud looks like a flat carpet, so the camera must fly low and close; points that are too sparse cannot read as terrain; peel the layers by ground, vegetation and building class.
- 容易失败: 远看点云像平铺地毯，镜头要贴低穿过去；点太稀读不出地形；剥层要按地面、植被、建筑分类。
- Palette: #777777
- Scene source: templates/scenes/point-cloud-survey
- References: A LemoLab · lemo-opuscar https://github.com/lemomo-ai/lemo-opuscar/tree/main/styles/lidar-survey; B carl-motion

## 09 Blueprint Drawing · 蓝图工程制图 (`blueprint`)

- Use when: the user wants blueprint drawing / 蓝图工程制图.
- Prompt (EN): Use Canvas to draw your topic on Prussian-blue blueprint paper in thin white lines, in drawing order, with dimension lines, numbered balloons and a drawing frame. Key visuals: cyanotype blueprint paper, thin white engineering lines, layer-by-layer drawing order, dimension lines and leader lines, numbered balloons, title block frame, section hatching, pan and zoom of the whole sheet. Watch out: Keep it a 2D line drawing in blue and white only; once it becomes 3D or a glowing wireframe it no longer fits. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用 Canvas 在普鲁士蓝晒图纸上，用白色细线按绘图顺序画出你的主题，配尺寸线、编号气泡和图框。画面要点：cyanotype 蓝晒纸、白色工程细线、逐层绘制顺序、尺寸线与引线、编号气泡、title block 图框、剖面线、整张图纸平移缩放。注意：只用蓝白两色的 2D 线稿，一做成 3D 或发光线框就不像了。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: Once it becomes 3D or a glowing wireframe it no longer fits; use a 2D line drawing in blue and white only; if all lines appear at once the sense of drawing is lost.
- 容易失败: 做成 3D 或发光线框就不像了；只用蓝白两色的 2D 线稿；线条一次全出现会丢掉绘制感。
- Palette: #3e6cb8
- Scene source: templates/scenes/blueprint
- References: A LemoLab · lemo-opuscar https://github.com/lemomo-ai/lemo-opuscar/tree/main/styles/blueprint; B carl-motion

## 10 Die-cut Sticker Explainer · 贴纸科普 (`sticker-explainer`)

- Use when: the user wants die-cut sticker explainer / 贴纸科普.
- Prompt (EN): Use HTML on a large canvas to make a science-explainer animation of your topic: photo cut-outs with a 10px white border become stickers, a blue-gray background uses only two or three colors, and the camera pans and zooms across the canvas. Key visuals: photo cut-out stickers with white outline, blue-gray and off-white background, two or three colors plus one accent, flat icons with precise charts, oversized canvas, long-eased pan and zoom, bar growth and number roll-ups. Watch out: With too many colors or inaccurate chart proportions, the science-explainer seriousness is lost. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用 HTML 大画布做你的主题的科普动画，照片抠图加 10px 白边做成贴纸，蓝灰底只用两三种颜色，镜头在画布上平移缩放。画面要点：照片抠图白描边贴纸、蓝灰米白底、两三色加一个强调色、扁平图标配精确图表、超大画布、长缓动平移缩放、柱状生长与数字滚动。注意：配色一多、图表比例不准，就没有科普的严肃感。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: More than three colors falls apart; bar heights and numbers must be proportionally accurate or the seriousness is lost; stickers without a white border and drop shadow are just ordinary cut-outs.
- 容易失败: 配色超过三种就散；柱高和数字比例要准，不然没有科普的严肃感；贴纸缺白边和投影就是普通抠图。
- Palette: #b88a3e
- Scene source: templates/scenes/sticker-explainer
- References: A Vincentwei1021 · mg-styles-15 https://vincentwei1021.github.io/mg-styles-15/?lang=zh#19-paperclip; B carl-motion

## 11 Feature-film 3D Character · 动画电影式3D角色 (`feature-3d-character`)

- Use when: the user wants feature-film 3d character / 动画电影式3D角色.
- Prompt (EN): Use the best technology you can think of to make an animated short, with your topic as the protagonist: cinematic lighting, shallow depth of field, a character with expression and performance, as complex and refined as you can make it. Key visuals: one-shot animated short, tech stack of your choice, cinematic backlight and sunset, shallow depth of field, character expression and performance, a small story told shot by shot, cinematic subtitle bar. Watch out: Just saying make a character falls back to a crude stick figure; explicitly ask for the most complex and refined result. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用你认为最好的技术做一支动画短片，主角是你的主题，电影布光、浅景深、角色有表情有表演，做到你能做到的最复杂最精致。画面要点：one-shot 动画短片、自选技术栈、电影级逆光与夕阳、浅景深、角色表情与表演、按镜头讲小故事、电影字幕条。注意：只说做个角色会退成简陋小人，要明确要求最复杂最精致。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: Just saying make a character falls back to a crude SVG figure; state that it should be made as complex as possible and open up Three.js or Blender; without depth of field and rim light it does not look like an animated film.
- 容易失败: 只说做个角色会退成简陋的 SVG 小人；要写明往最复杂了做，放开 Three.js 或 Blender；没有景深和轮廓光就不像动画电影。
- Palette: #b86c3e
- Scene source: none, build from the prompt
- References: A prompt-motion.com https://prompt-motion.com/axtonliu-0b861d; B prompt-motion.com https://prompt-motion.com/faroukzy-9ff23e

## 12 Chinese Ink Wash · 中国水墨 (`chinese-ink-wash`)

- Use when: the user wants chinese ink wash / 中国水墨.
- Prompt (EN): Use code to draw an ink-wash animation of your topic on rice paper, with only five ink tones, more than half left blank, brushstrokes drawn one stroke at a time, and a single vermilion seal stamped. Key visuals: freehand xieyi style, procedural rice-paper texture, five tones of ink, boneless strokes with ink load, dry-brush skips, 60 to 80 percent blank space, ink-bleed transition, one vermilion seal. Watch out: Do not draw closed outlines; use brush strokes with an ink load that runs dry. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用代码在宣纸上画你的主题的水墨动画，只用五档墨色，留白过半，笔触一笔一笔画出来，只盖一枚朱红印章。画面要点：写意、程序宣纸纹理、墨分五色、没骨带墨量笔触、飞白干笔、留白六到八成、墨晕转场、一枚朱红印章。注意：别画闭合描边轮廓，要用带墨量会枯的毛笔笔触。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: Vector outlines plus a brush texture look fake; use brush strokes with ink load and no closed outlines; with less blank space it becomes a colorful illustration.
- 容易失败: 矢量描边加笔刷贴图会很假；要带墨量的毛笔笔触，不画闭合轮廓；留白一少就成了彩色插画。
- Palette: #d8d8d8
- Scene source: templates/scenes/chinese-ink-wash
- References: A LemoLab · lemo-opuscar https://github.com/lemomo-ai/lemo-opuscar/tree/main/styles/ink-wash; B carl-motion

## 13 ASCII Character Visuals · ASCII字符视觉 (`ascii-crt`)

- Use when: the user wants ascii character visuals / ASCII字符视觉.
- Prompt (EN): Build your topic from a monospace character grid on an amber monochrome CRT phosphor screen, with scanlines and glow, and do the camera push and pull by changing the font size. Key visuals: monospace character grid, amber or green phosphor monochrome, CRT scanlines and barrel distortion, bloom glow, character density gradient, blinking cursor, push and pull by changing font size, typewriter subtitles. Watch out: Every bright spot must be a real character in the grid; applying an ASCII filter to the whole image gives it away. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用等宽字符网格拼出你的主题，琥珀色单色 CRT 荧光屏，加扫描线和辉光，推拉镜头靠改字号来做。画面要点：monospace 字符网格、琥珀或绿色荧光单色、CRT 扫描线与桶形畸变、bloom 辉光、字符密度梯度、光标闪烁、改字号推拉、打字机字幕。注意：每一处亮点都得是网格里的真字符，整图套 ASCII 滤镜会露馅。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: Applying an ASCII filter to the whole image looks like a filter at a glance; every pixel must come from a real character in the grid; too small a character set blurs the image.
- 容易失败: 整张图套 ASCII 滤镜一看就是滤镜；每个像素都要来自网格里的真字符；字符集太少画面会糊。
- Palette: #151515
- Scene source: none, build from the prompt
- References: A LemoLab · lemo-opuscar https://github.com/lemomo-ai/lemo-opuscar/tree/main/styles/ascii-crt; B prompt-motion.com https://prompt-motion.com/rames-jusso-589f80

## 14 Isometric 2.5D World · 等轴2.5D世界 (`isometric-world`)

- Use when: the user wants isometric 2.5d world / 等轴2.5D世界.
- Prompt (EN): Use Canvas or a Three.js orthographic camera to turn your topic into an isometric miniature world, with flat three-tone shading on every face and small icons with leader lines labeling the data. Key visuals: true isometric 30 degrees, flat three-tone shading per face, floating base with cross-section, Isotype icon counting, label leader lines, cutaway, buildings growing with overshoot, camera following a route. Watch out: Keep a fixed 30 degree isometric; adding perspective or outlines turns it into low-poly 3D. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用 Canvas 或 Three.js 正交相机把你的主题做成等轴测微缩世界，每个面三色调平涂，用小图标和引线标数据。画面要点：true isometric 30 度、每面三色调平涂、悬浮底座带剖面、Isotype 图标计数、标签引线、剖开 cutaway、建筑生长带过冲、沿路线带镜头。注意：固定 30 度等轴，一加透视或描边就变成低多边形 3D。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: Slipping in perspective turns it into low-poly 3D; use a fixed 30 degree projection with no outlines; a camera that spins around breaks the isometric feel.
- 容易失败: 夹带透视就变成低多边形 3D；固定 30 度投影、不描边；镜头乱转会破坏等轴感。
- Palette: #6cb83e, #b84e3e
- Scene source: none, build from the prompt
- References: A LemoLab · lemo-opuscar https://github.com/lemomo-ai/lemo-opuscar/tree/main/styles/iso-infographic; B Vincentwei1021 · mg-styles-15 https://vincentwei1021.github.io/mg-styles-15/?lang=zh#03-isometric

## 15 Van Gogh Impasto · 梵高厚涂油画 (`van-gogh-impasto`)

- Use when: the user wants van gogh impasto / 梵高厚涂油画.
- Prompt (EN): Use Canvas 2D to draw your topic: lay down flat base colors first, then fill short thick impasto strokes following a flow field, a dozen-plus hues per region, with the strokes changing eight times per second. Key visuals: flat-color underpainting plus flow-field strokes, walls vertical and floor along perspective, starry sky swirling around vortexes, region palettes of a dozen-plus hues, short thick impasto, dark blue outlines, 8fps stroke boil, small objects on their own layers. Watch out: Lay strokes in three separate passes for wall, floor and figure; one parameter set for the whole image blurs into a carpet. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用 Canvas 2D 画你的主题，先平涂底色，再顺着流场铺短粗厚涂笔触，每块区域十几种色相，笔触每秒换八次。画面要点：平涂底稿加流场笔触、墙竖地沿透视星空绕漩涡、区域色板十几种色相、短粗厚涂、深蓝描边、8fps 笔触沸腾、小物件单独成层。注意：墙、地、人物分三遍铺笔触，一套参数跑全图会糊成地毯。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: Changing only colors without laying strokes is just an ordinary illustration; wall, floor and figure need separate layers with their own strokes; strokes shaking across the whole screen cause dizziness.
- 容易失败: 只换颜色不铺笔触就是普通插画；墙、地、人物要分层分别铺笔触；全屏笔触一起抖会晕。
- Palette: #3e6cb8, #b84e3e
- Scene source: templates/scenes/huashu-portraits
- References: A alchaincyf · huashu-art-motion https://github.com/alchaincyf/huashu-art-motion; B carl-motion

## 16 Iridescent Psychedelic Shader · 虹彩迷幻Shader (`psychedelic-shader`)

- Use when: the user wants iridescent psychedelic shader / 虹彩迷幻Shader.
- Prompt (EN): Use a shader to make a psychedelic hypnosis animation with your topic as the subject: concentric lines and kaleidoscope symmetry rotating continuously, with iridescent color flowing along the edges. Key visuals: psychedelic hypnosis, concentric lines, kaleidoscope mirror symmetry, vortex tunnel, iridescent thin-film color flowing along edges, high-saturation clashing colors, VJ loop. Watch out: Just writing psychedelic falls back to a plain gradient; spell out the symmetry and the motion. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用 shader 做一支迷幻催眠动画，主题是你的主题，同心线和万花筒对称一直旋转，虹彩色沿边缘流动。画面要点：psychedelic 催眠、同心线、万花筒镜像对称、旋涡隧道、虹彩薄膜色沿边缘流动、高饱和撞色、VJ 循环。注意：只写迷幻两个字会退成普通渐变，要写清对称方式和运动方式。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: The source is only one sentence and easily falls back to a plain gradient background; specify how many-fold the symmetry is, how it rotates and which colors to use; the first 0.5 seconds of A is black, so avoid it when cutting.
- 容易失败: 来源只有一句话，容易退成普通渐变背景；要写清几重对称、怎么转、用哪几种色；A 的前 0.5 秒是黑场，剪的时候注意避开。
- Palette: #3ea8b8, #6c3eb8, #8ab83e
- Scene source: none, build from the prompt
- References: A prompt-motion.com https://prompt-motion.com/monokern-ade5b6; B X post https://x.com/yama_kiyo/status/2103740786177134910

## 17 Claymation Stop-motion · 黏土定格 (`claymation`)

- Use when: the user wants claymation stop-motion / 黏土定格.
- Prompt (EN): Use Blender to make a clay stop-motion animation of your topic, with fingerprints and dents on the surface, a pose change every two frames played at 12 fps, and soft studio lighting with shallow depth of field. Key visuals: clay material with fingerprints and dents, on twos 12fps, slight shape change boil on every beat, soft studio light, shallow-depth macro, handmade jump-cut rhythm. Watch out: Smooth motion looks like CG; drop frames on purpose and change the shape slightly on every beat. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用 Blender 做你的主题的黏土定格动画，表面留指纹和压痕，两帧换一个姿势按 12 帧播放，柔光棚拍浅景深。画面要点：黏土材质指纹压痕、on twos 12fps、每拍形状微变 boil、柔光棚拍、浅景深微距、手工跳切节奏。注意：动作一顺滑就像 CG，要故意抽帧，形状每一拍都微微变。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: Motion that is too smooth looks like 3D animation; drop frames to get a stop-motion feel; a material without fingerprints and dents is just plastic; the light should look like a real tabletop shoot.
- 容易失败: 动作太顺就像 3D 动画，要抽帧做出定格感；材质没有指纹和压痕就是塑料；光要像桌面实拍。
- Palette: #b8a83e
- Scene source: templates/scenes/claymation
- References: A prompt-motion.com https://prompt-motion.com/davidshulmanfl-371638; B carl-motion

## 18 Pixel Game · 像素游戏 (`pixel-game`)

- Use when: the user wants pixel game / 像素游戏.
- Prompt (EN): Use Canvas with a 320×180 internal resolution to draw your topic, upscale 6x with nearest neighbor, limit to 16 to 32 colors, animate sprites in stepped frames, and layer the background with parallax. Key visuals: low-resolution big pixels, limited 16 to 32 color palette, nearest-neighbour integer upscaling, 8 to 12fps sprite frames, parallax scrolling, steps() stepped timing, dithering, game HUD type. Watch out: Smooth scaling or smooth easing blurs it; keep all coordinates and offsets as integers. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用 Canvas 320×180 内部分辨率画你的主题，最近邻放大 6 倍，限定 16 到 32 色，精灵按阶梯帧动，背景分层视差。画面要点：低分辨率大像素、16 到 32 色有限色板、nearest-neighbour 整数放大、8 到 12fps 精灵帧、视差卷轴、steps() 阶梯时序、dithering、游戏 HUD 字。注意：一用平滑缩放或平滑缓动就糊，坐标和位移全取整数。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: Scaling interpolation or easing smears the pixels into a blur; use integer coordinates everywhere and upscale with nearest neighbor; keep the palette within 16 to 32 colors.
- 容易失败: 缩放插值或缓动会把像素糊成马赛克；坐标全取整数，用最近邻放大；调色板限在 16 到 32 色。
- Palette: #4e3eb8
- Scene source: none, build from the prompt
- References: A prompt-motion.com https://prompt-motion.com/hoyoyoda-3a5c08; B prompt-motion.com https://prompt-motion.com/0xevinho-3777d8

## 19 Flat Vector · 扁平矢量 (`flat-vector`)

- Use when: the user wants flat vector / 扁平矢量.
- Prompt (EN): Use SVG plus GSAP to make a flat vector explainer of your topic: solid colors with no gradients, five or six high-saturation colors, elements entering with springy motion, in one continuous shot. Key visuals: SVG plus GSAP, large solid color blocks, five-or-six-color high-saturation palette, overshoot elastic easing, anticipation then burst then rebound, about 10% squash and stretch, stagger of two to four frames, shape-wipe transitions. Watch out: Adding gradients or moving several subjects at once falls apart; move only one hero at any moment. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用 SVG 加 GSAP 做你的主题的扁平矢量讲解，纯色无渐变，五六种高饱和色，元素弹性入场，一镜到底。画面要点：SVG 加 GSAP、纯色大色块、五六色高饱和色板、overshoot 弹性缓动、预备冲出回弹、约 10% 挤压拉伸、stagger 两到四帧、形状擦除转场。注意：加渐变或几个主体同时动就散了，同一时刻只动一个主角。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: Adding gradients or moving several subjects at once falls apart; let only one hero move at a time; keep solid colors to five or six.
- 容易失败: 加了渐变或几个主体同时动就散；一次只让一个主角动；纯色控制在五六种以内。
- Palette: #b88a3e, #3eb8a8
- Scene source: templates/scenes/flat-vector
- References: A Vincentwei1021 · mg-styles-15 https://vincentwei1021.github.io/mg-styles-15/?lang=zh#01-flat-vector; B carl-motion

## 20 Impressionist Oil (Monet) · 印象派油画／莫奈 (`monet-impressionist`)

- Use when: the user wants impressionist oil (monet) / 印象派油画／莫奈.
- Prompt (EN): Use Canvas 2D to draw your topic with no outlines, short horizontal strokes for the water, warm yellow layered on the lit side and pale purple on the shadow side, with light flecks that flicker. Key visuals: impressionist with no outlines, horizontal water strokes, colored shadows with warm yellow in light and pale purple in shade, bright short-stroke light flecks trembling, 6fps local stroke boil, water lily and Japanese bridge motifs. Watch out: Boiling across the whole screen turns into full-screen noise; keep large areas like the floor and bridge still. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用 Canvas 2D 画你的主题，不勾边，水面用横向短笔触，受光侧叠暖黄、背光侧叠淡紫，光斑一闪一闪。画面要点：印象派不勾边、横向水面笔触、受光暖黄背光淡紫的色彩阴影、亮色短笔光斑颤动、6fps 局部笔触沸腾、睡莲日本桥母题。注意：全屏一起沸腾会变满屏噪点，地板和桥这类大面保持不动。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: Strokes shaking across the whole screen cause dizziness, so animate only the water and light flecks; strokes that are too large blur the figures; juxtapose complementary colors and do not mix them into gray.
- 容易失败: 全屏笔触一起抖会晕，只让水面和光斑动；笔触太大人物会糊掉；颜色要补色并置，别调成灰。
- Palette: #b86c3e, #3e6cb8
- Scene source: templates/scenes/huashu-portraits
- References: A alchaincyf · huashu-art-motion https://github.com/alchaincyf/huashu-art-motion; B carl-motion

## 21 Particle Morph · 粒子聚散造型 (`particle-morph`)

- Use when: the user wants particle morph / 粒子聚散造型.
- Prompt (EN): Make a particle animation: hundreds of thousands of glowing particles gather on a dark background into the shape and text of your topic, then scatter and become the next shape. Key visuals: hundreds of thousands of glowing particles, gather into shape then scatter, deep blue-black background, lines connecting into a relationship network, big number counter, one English conclusion line as subtitle. Watch out: Too few particles or no target shape, and the form cannot be read. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 做一支粒子动画，几十万发光粒子在深色背景上聚成你的主题的形状和文字，再散开变成下一个形状。画面要点：数十万发光粒子、聚拢成形再散开、深蓝黑底、连线成关系网络、大数字计数器、一句英文结论字幕。注意：粒子太少或不给目标形状，就读不出造型。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: Too few particles or no target shape and the form cannot be read; provide a defined shape and enough particles; the gathering and scattering needs rhythm, so do not let them drift all the time.
- 容易失败: 粒子太少或没给目标形状就读不出造型；要给定形状并让粒子够多；聚和散要有节奏，别一直飘。
- Palette: #3e6cb8, #b88a3e
- Scene source: templates/scenes/particle-morph
- References: A prompt-motion.com https://prompt-motion.com/ismailfahmi-557268; B carl-motion

## 22 White-model Projection · 实体白模投影 (`white-model-projection`)

- Use when: the user wants white-model projection / 实体白模投影.
- Prompt (EN): Use Three.js to make a white-model city: pure white blocks on a dark-room display plinth, with data added only as projected light layer by layer, soft light edges spilling over the base. Key visuals: pure white block model, dark-room plinth, data as projected light, only faces toward the projector light up, soft light edges spilling over the base, one question per layer, lights on and off as opener and closer, real building data. Watch out: Do not paint color into the material; warm ambient light will also tint the white model yellow. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用 Three.js 做你的城市白模，纯白体块放在暗房展台上，数据只以投影光一层层打上去，光边柔和、溢出底座。画面要点：纯白体块模型、暗房展台、数据即投影光、只亮朝向投影仪的面、柔和光边溢出底座、一层一个问题、开灯关灯作开场收尾、真实建筑数据。注意：颜色别画进材质，暖色环境光还会把白模染黄。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: If the white model carries its own color it is no longer a projection; color may only come from the projected light; text should be projected onto the model, not float on the screen.
- 容易失败: 白模本身带了颜色就不是投影了，颜色只能来自投影光；字要投在模型上，别浮在屏幕上。
- Palette: #3e6cb8, #b86c3e
- Scene source: templates/scenes/white-model-projection
- References: A LemoLab · lemo-opuscar https://github.com/lemomo-ai/lemo-opuscar/tree/main/styles/white-model; B carl-motion

## 23 Ancient Egyptian Mural · 古埃及壁画 (`egyptian-mural`)

- Use when: the user wants ancient egyptian mural / 古埃及壁画.
- Prompt (EN): Use Canvas 2D to paint your topic as an ancient Egyptian tomb mural: figures with profile faces and frontal eyes, register bands composed with hieroglyph columns, flat ochre and lapis fills with black outlines. Key visuals: profile-face frontal-eye convention, column-divided horizontal registers, hieroglyph columns, flat fills of ochre, lapis, peacock green and earth yellow, black outlines, small hands at the ends of sun rays, lime plaster wall texture. Watch out: A mural is flat, so add no perspective or shadows, and animate the river and light so it is not too static. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用 Canvas 2D 把你的主题画成古埃及墓室壁画，人物侧脸正眼，分栏横带构图配象形文字栏，赭石青金平涂加黑描边。画面要点：侧脸正眼程式、分栏横带 register、象形文字栏、赭石青金孔雀绿土黄平涂、黑色描边、太阳光线末端小手、墙面石灰质感。注意：壁画是平的，别加透视和阴影，再让河水和光线动起来免得太静。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: Adding perspective and shadows no longer looks like a mural; figures must use the canonical pose with frontal torso and profile head; use only mineral colors such as ochre red, earth yellow and blue-green.
- 容易失败: 加透视和阴影就不像壁画；人物要正身侧脸的规范姿势；颜色只用赭红、土黄、青绿这类矿物色。
- Palette: #b88a3e
- Scene source: templates/scenes/huashu-portraits
- References: A alchaincyf · huashu-art-motion https://github.com/alchaincyf/huashu-art-motion; B carl-motion

## 24 Product Exploded View · 产品爆炸拆解 (`exploded-view`)

- Use when: the user wants product exploded view / 产品爆炸拆解.
- Prompt (EN): Use Blender to make an exploded teardown of your product: parts lift evenly spaced in layers along one axis, studio key light plus a cool rim light, leader lines labeling real specs, and everything closes back into one piece at the end. Key visuals: real CAD/PCB/BOM, evenly spaced layers along one axis, PBR studio key light plus cool rim light, HDRI reflections, leader lines and dimension lines, camera moving between layers, closing back together at the end. Watch out: Annotate only numbers that appear in the drawings; never estimate dimensions. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用 Blender 做你的产品爆炸拆解，零件沿一根轴等距分层抬起，棚拍主光加冷色轮廓光，引线标真实参数，最后合回一体。画面要点：真实 CAD／PCB／BOM、沿一轴等距分层、PBR 棚拍主光加冷轮廓光、HDRI 反射、引线与尺寸线、镜头在层间穿行、最后合拢。注意：标注只写图纸里有的数，尺寸不许估。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: Made-up model numbers and figures give it away; parts must separate along the assembly axis; materials must distinguish metal, plastic and PCB.
- 容易失败: 型号和数字瞎编会露馅；零件要沿装配轴拆开；材质要分出金属、塑料和 PCB。
- Palette: #4eb83e, #b88a3e
- Scene source: templates/scenes/exploded-view
- References: A LemoLab · lemo-opuscar https://github.com/lemomo-ai/lemo-opuscar/tree/main/styles/teardown; B carl-motion

## 25 Editorial Paper Data Story · 纸面编辑式数据叙事 (`editorial-dataviz`)

- Use when: the user wants editorial paper data story / 纸面编辑式数据叙事.
- Prompt (EN): Use Canvas to draw the real data of your topic on beige dot-grid paper, with red and blue pencils plotting point by point, handwritten notes pinned beside the data points, and the chart itself acting as the camera. Key visuals: beige dot-grid paper, real data drawn point by point, red and blue pencil strokes, handwritten notes pinned to data points, RdBu diverging color scale, chart as camera, chart type chosen by the data. Watch out: Do not turn it into a dashboard or slide deck; make one point at a time. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用 Canvas 在米色点阵纸上画你的主题的真实数据，红蓝铅笔逐点画出，手写批注钉在数据点旁，图表本身当镜头。画面要点：米色点阵纸、真实数据逐点绘制、红蓝铅笔笔触、手写批注钉在数据点、RdBu 发散色阶、图表即镜头、按数据选图型。注意：别做成仪表盘或幻灯片，一次只讲一个观点。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: Turning it into a dashboard or slide deck loses the editorial feel; make one point at a time; use only changes in the chart itself as transitions.
- 容易失败: 做成仪表盘或幻灯片就丢了编辑感；一次只讲一个观点；转场只用图表本身的变化。
- Palette: #cfcfcf
- Scene source: none, build from the prompt
- References: A LemoLab · lemo-opuscar https://github.com/lemomo-ai/lemo-opuscar/tree/main/styles/dataviz; B X post https://x.com/maxescu/status/2104898184442962277

## 26 Glassmorphism UI · 玻璃拟态UI (`glassmorphism-ui`)

- Use when: the user wants glassmorphism ui / 玻璃拟态UI.
- Prompt (EN): Use HTML to make a glassmorphism animation of your topic: three to five large Gaussian-blurred color blobs drift slowly underneath, with frosted glass cards floating on top, with a 1px translucent white border. Key visuals: aurora color blobs with blur 80 to 150px, backdrop-filter frosted cards, white fill at 5 to 10%, 1px white border, two or three adjacent hues, 3 to 5% noise to prevent banding, sine breathing easing. Watch out: Clashing colors get muddy and fast motion looks cheap; keep a slow breathing pace throughout. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用 HTML 做你的主题的玻璃拟态动画，底层三到五个大色斑高斯模糊慢慢漂，上面浮磨砂玻璃卡片，1px 半透明白描边。画面要点：aurora 大色斑 blur 80 到 150px、backdrop-filter 磨砂卡片、白色 5 到 10% 填充、1px 白描边、邻近色两三色、3 到 5% 噪点防色带、sine 呼吸缓动。注意：撞色会脏，动作一快就廉价，全程慢呼吸。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: Contrasting colors look cheap, so use only adjacent hues; keep motion slow; glass without a 1px translucent white edge and background blur looks like an ordinary card.
- 容易失败: 用对比色会显廉价，只用邻近色；动作要慢；玻璃缺 1px 半透明白边和背景模糊就像普通卡片。
- Palette: #3e4eb8
- Scene source: templates/scenes/glassmorphism-ui
- References: A Vincentwei1021 · mg-styles-15 https://vincentwei1021.github.io/mg-styles-15/?lang=zh#12-aurora-glass; B carl-motion

## 27 Brick Toy · 积木玩具 (`brick-toy`)

- Use when: the user wants brick toy / 积木玩具.
- Prompt (EN): Use Blender to make a toy-brick stop-motion of your topic, macro-shot on a real wooden table, glossy plastic with studs, characters posed on twos, with a smooth camera. Key visuals: real tabletop, macro shallow depth of field, glossy ABS rectangular highlights, studs on top faces, contact shadows in the seams, characters stop-motion on twos, camera smooth frame by frame, neutral studio HDRI. Watch out: No brand names or minifigure silhouettes; build the characters out of bricks. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用 Blender 做你的主题的积木定格，真实木桌上微距拍，亮面塑料带凸点，角色两帧一拍定格，镜头保持顺滑。画面要点：真实桌面、微距浅景深、亮面 ABS 矩形高光、顶面凸点、缝隙接触阴影、角色 on twos 定格、镜头逐帧顺滑、中性棚拍 HDRI。注意：别出现品牌字样和小人轮廓，角色用积木拼出来。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: Using branded minifigures carries copyright risk; bricks need studs and plastic highlights; deep depth of field no longer looks like a real macro shot.
- 容易失败: 用品牌小人会有版权风险；积木要有凸点和塑料高光；景深一深就不像微距实拍。
- Palette: #4eb83e, #b86c3e
- Scene source: templates/scenes/brick-toy
- References: A LemoLab · lemo-opuscar https://github.com/lemomo-ai/lemo-opuscar/tree/main/styles/brick-toy; B carl-motion

## 28 Risograph Print · Risograph孔版套印 (`risograph`)

- Use when: the user wants risograph print / Risograph孔版套印.
- Prompt (EN): Use code to simulate risograph-style stencil printing of your topic: two or three spot colors multiplied together, with halftone dots and slight misregistration, and color blocks with no outlines. Key visuals: two or three spot ink colors, multiply to produce a third color, misregistration, halftone dots, grain and pinholes, warm white paper, outline-free color blocks, characters at 12fps and camera at 24fps. Watch out: Vector art plus noise does not count; every color must come from separated overprinted plates. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用代码模拟孔版印刷做你的主题，两三种专色正片叠底，带半调网点和轻微套印错位，色块不描边。画面要点：两三种 spot ink 专色、multiply 叠出第三色、套印错位、halftone 网点、颗粒针孔、暖白纸、无轮廓色块、角色 12fps 镜头 24fps。注意：矢量图加噪点不算，每块颜色都得来自分版叠印。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: Vector art plus noise does not count, every color must come from separated overprinted plates; without misregistration it does not look right; the screen angles of the three plates must be offset.
- 容易失败: 矢量图加噪点不算，每块颜色都要来自分版叠印；没有套印错位就不像；三块版的网角要错开。
- Palette: #a8b83e, #b83e6c
- Scene source: templates/scenes/risograph
- References: A LemoLab · lemo-opuscar https://github.com/lemomo-ai/lemo-opuscar/tree/main/styles/risograph; B carl-motion

## 29 Sci-fi Scan HUD · 科幻扫描HUD (`scifi-hud`)

- Use when: the user wants sci-fi scan hud / 科幻扫描HUD.
- Prompt (EN): Use Three.js wireframes to scan your topic into a glowing holographic volume: target boxes lock onto parts and then pull them apart, numbers roll from garbled characters to true values, in a single color with glow. Key visuals: glowing wireframe, projection base, scan plane growth, target-lock boxes, local teardown, garbled digits rolling down to settle, one cool color plus one warm accent, near-black stage, bloom. Watch out: Do not put text directly over the wireframe; put it on a dark backing plate, and keep the parts connected. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
- 提示语（中）: 用 Three.js 线框把你的主题扫描成发光全息体，目标框锁定部件再拆开，数字从乱码滚到真值，单色加辉光。画面要点：发光 wireframe、投影底座、扫描面生长、目标锁定框、局部拆解、乱码数字滚动落定、单冷色加一个暖色强调、近黑舞台、bloom。注意：文字别直接压在线框上，放进暗底板，部件之间要连着。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
- Breaks when: Text laid directly over a wireframe is hard to read, so put it on a dark backing plate; floating parts look fake, so keep them connected; too many colors get messy.
- 容易失败: 线框上直接叠字会看不清，字要放暗底板；部件悬空会假，要连在一起；颜色一多就乱。
- Palette: #3ea8b8
- Scene source: none, build from the prompt
- References: A LemoLab · lemo-opuscar https://github.com/lemomo-ai/lemo-opuscar/tree/main/styles/hologram-hud; B Vincentwei1021 · mg-styles-15 https://vincentwei1021.github.io/mg-styles-15/?lang=zh#22-hud
