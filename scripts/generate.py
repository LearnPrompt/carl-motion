#!/usr/bin/env python3
"""Build every generated file from data/styles.*.json.

    python3 scripts/generate.py

Writes README.md, README_zh.md, docs/styles/<slug>.md, docs/styles/README.md,
agents/skills/carl-motion/references/styles.md, and a text tile for each style
that has no redistributable preview (assets/posters/<slug>.jpg).
Edit the data or this file, never the generated output.
"""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = 'LearnPrompt/carl-motion'
ZH = json.load(open(os.path.join(ROOT, 'data/styles.zh.json')))
EN = {e['id']: e for e in json.load(open(os.path.join(ROOT, 'data/styles.en.json')))}
N = len(ZH)
OURS = [s for s in ZH if s['scene']]
MOVING = [s for s in ZH if s['preview']]


def w(rel, text):
    p = os.path.join(ROOT, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w').write(text.rstrip('\n') + '\n')


def stack(scene):
    """Guess the render stack from the files in a scene folder."""
    d = os.path.join(ROOT, scene); fs = os.listdir(d)
    txt = ' '.join(open(os.path.join(d, f)).read() for f in fs if f.endswith(('.sh', '.md')))
    if 'blender' in txt.lower(): return 'Blender + Python'
    if 'three' in txt.lower(): return 'Three.js + Node'
    if any(f.endswith('.cjs') for f in fs): return 'Canvas / HTML + Node'
    return 'Python (NumPy + OpenCV + Pillow)'


def tool(card):
    m = re.match(r'Use (.+?) (?:to|on|with) ', card)
    return m.group(1) if m and len(m.group(1)) < 40 else 'any stack'


def img(s, prefix):
    ext = 'webp' if s['preview'] else 'jpg'
    folder = 'previews' if s['preview'] else 'posters'
    return f'{prefix}assets/{folder}/{s["slug"]}.{ext}'


def credit(s, lang):
    p = s['preview']
    if not p: return 'No redistributable clip. Watch it at the source link.' if lang == 'en' else '没有可随仓库分发的片段，去来源链接看。'
    if p['by'] == 'carl-motion': return 'Preview: our render (layer B), MIT.' if lang == 'en' else '预览是我们渲染的 B，MIT 许可。'
    return f'Preview: layer A by {p["by"]}, CC BY 4.0.' if lang == 'en' else f'预览是 {p["by"]} 的 A，CC BY 4.0。'


# ---------- text tiles for styles without a clip ----------
def text_tiles():
    try:
        from PIL import Image, ImageDraw, ImageFont
        fnt = lambda n, b=True: ImageFont.truetype('/System/Library/Fonts/HelveticaNeue.ttc', n, index=1 if b else 0)
    except Exception:
        return
    for s in ZH:
        if s['preview']: continue
        im = Image.new('RGB', (480, 270), (17, 17, 17)); d = ImageDraw.Draw(im)
        d.rectangle([0, 0, 479, 269], outline=(70, 70, 70)); d.rectangle([24, 28, 60, 33], fill=(255, 84, 20))
        d.text((24, 52), f'{s["order"]:02d}', font=fnt(30), fill=(255, 84, 20))
        line, y = '', 100
        for word in s['name_en'].split():
            if fnt(34).getlength(line + ' ' + word) > 430 and line: d.text((24, y), line, font=fnt(34), fill=(242, 239, 232)); y += 42; line = word
            else: line = (line + ' ' + word).strip()
        d.text((24, y), line, font=fnt(34), fill=(242, 239, 232))
        d.text((24, 228), 'prompt + source link', font=fnt(20, False), fill=(150, 150, 146))
        os.makedirs(os.path.join(ROOT, 'assets/posters'), exist_ok=True)
        im.save(os.path.join(ROOT, f'assets/posters/{s["slug"]}.jpg'), quality=86)


# ---------- per-style pages ----------
def ref_rows(s, lang):
    rows = []
    for r in s['refs']:
        if r['by'] == 'carl-motion':
            src = f'[{"this repo" if lang == "en" else "本仓库"}](../../{s["scene"]})'
            note = r.get('inspired_by') and (f' · story idea: [{host(r["inspired_by"])}]({r["inspired_by"]})' if lang == 'en' else f' · 故事灵感来自 [{host(r["inspired_by"])}]({r["inspired_by"]})') or ''
            rows.append(f'| {r["layer"]} | carl-motion | {src}{note} | MIT |')
        else:
            title = r['title'] or '—'
            rows.append(f'| {r["layer"]} | {title} | [{r["by"]}]({r["url"]}) | {r["license"]} |' if r['url'] else f'| {r["layer"]} | {title} | — | — |')
    return '\n'.join(rows)


def host(u):
    return re.sub(r'^https?://(www\.)?', '', u).split('/')[0]


def scene_block(s, lang):
    if not s['scene']:
        return ('No source in this repo yet. The prompt above is enough to build it from scratch.' if lang == 'en'
                else '本仓库暂时没有这个画风的源码，直接用上面的提示语就能从零做出来。')
    head = (f'Source that rendered the B clip: [`{s["scene"]}`](../../{s["scene"]}) ({stack(s["scene"])}). Its README has the exact render command.'
            if lang == 'en' else
            f'渲染 B 的完整源码在 [`{s["scene"]}`](../../{s["scene"]})（{stack(s["scene"])}），渲染命令写在它的 README 里。')
    return head


def page(s):
    e = EN[s['id']]; prev = img(s, '../../')
    chips = ' '.join(f'`{c}`' for c in s['palette'])
    nav_i = ZH.index(s); prv, nxt = ZH[nav_i - 1], ZH[(nav_i + 1) % N]
    return f'''# {s["order"]:02d} · {s["name_en"]} · {s["name_zh"]}

[All styles](README.md) · [← {prv["name_en"]}]({prv["slug"]}.md) · [{nxt["name_en"]} →]({nxt["slug"]}.md)

<img src="{prev}" width="100%" alt="{s["name_en"]}">

<sub>{credit(s, "en")} {credit(s, "zh")}</sub>

## Prompt (copy this)

Paste into Claude, GPT or any coding model. Swap *your topic* for your own subject.

```text
{e["full_prompt"]}
```

## 提示语（复制这段）

发给 Opus 5.5 或任意能写代码的模型，把你的主题换成自己的内容。

```text
{s["full_prompt"]}
```

## What the two examples show · 两个示例

| | English | 中文 |
|---|---|---|
| A | {e["fx_a"]} | {s["fx_a"]} |
| B | {e["fx_b"]} | {s["fx_b"]} |

## Where it usually breaks · 容易失败的点

{e["fail"]}

{s["fail"]}

## Key visuals · 画面要点

{e["keywords"]}

{s["keywords"]}

Palette 主色：{chips}

## References · 参考来源

| Layer | Title | Source | License |
|---|---|---|---|
{ref_rows(s, "en")}

## Reproduce · 复现

{scene_block(s, "en")}

{scene_block(s, "zh")}
'''


# ---------- gallery ----------
def gallery(lang, prefix, page_prefix):
    cells = []
    for s in ZH:
        e = EN[s['id']]
        name = f'<b>{s["order"]:02d} · {s["name_en"]}</b><br><sub>{s["name_zh"]}</sub>' if lang == 'en' else f'<b>{s["order"]:02d} · {s["name_zh"]}</b><br><sub>{s["name_en"]}</sub>'
        tag = ('source included' if lang == 'en' else '含源码') if s['scene'] else (tool(e['card']) if lang == 'en' else '提示语加来源')
        if s['scene'] and lang == 'en': tag += f' · {tool(e["card"])}'
        cells.append(f'<td width="33%" valign="top" align="center"><a href="{page_prefix}{s["slug"]}.md"><img src="{img(s, prefix)}" width="260" alt="{s["name_en"]}"></a><br>{name}<br><sub>{tag}</sub></td>')
    rows = ['<tr>\n' + '\n'.join(cells[i:i + 3]) + '\n</tr>' for i in range(0, len(cells), 3)]
    return '<table>\n' + '\n'.join(rows) + '\n</table>'


def scene_table(lang):
    seen, rows = set(), []
    for s in OURS:
        if s['scene'] in seen: continue
        seen.add(s['scene']); ids = [x for x in OURS if x['scene'] == s['scene']]
        names = ' / '.join(x['name_en'] if lang == 'en' else x['name_zh'] for x in ids)
        rows.append(f'| [`{s["scene"].split("/")[-1]}`]({s["scene"]}) | {names} | {stack(s["scene"])} |')
    head = '| Folder | Style | Stack |' if lang == 'en' else '| 目录 | 画风 | 技术栈 |'
    return head + '\n|---|---|---|\n' + '\n'.join(rows)


INSTALL = f'''```bash
npx skills add {REPO}
```'''

UPSTREAM_EN = '''| Upstream | What we took from it | License |
|---|---|---|
| [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) | Style recipes and demo films for 13 of the 29 styles (blueprint, watercolor, ink wash, woodcut, point cloud, white model, teardown, brick toy, risograph, ASCII, isometric, dataviz, HUD) | prompts and code MIT, demo films CC BY 4.0 |
| [Vincentwei1021/mg-styles-15](https://github.com/Vincentwei1021/mg-styles-15) | Style prompts for collage, flat vector, sticker explainer, glass UI, synthwave, soft 3D, isometric, HUD | MIT (prompts and code) |
| [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | Painter engines for Egyptian mural, Van Gogh and Monet; our A clips are re-rendered from its source | MIT |
| [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | Product-UI promo and risograph misregistration references | see upstream |
| [prompt-motion.com](https://prompt-motion.com) | Public references for pixel game, claymation, 3D character, hand-drawn notes, shader, particles, ASCII | link only |
| [yasue.org: Pushing Opus 5.5 video generation limits](https://en.yasue.org/article/pushing-opus-5-5-video-generation-limits) | The cats-move-into-the-village story our seven English explainer clips retell | link only |'''

UPSTREAM_ZH = '''| 上游 | 我们用了什么 | 许可 |
|---|---|---|
| [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) | 29 个画风里 13 个的配方和演示片：蓝图、水彩、水墨、木刻、点云、白模、拆解、积木、孔版、ASCII、等轴、数据叙事、HUD | 提示语和代码 MIT，演示片 CC BY 4.0 |
| [Vincentwei1021/mg-styles-15](https://github.com/Vincentwei1021/mg-styles-15) | 拼贴、扁平矢量、贴纸科普、玻璃拟态、Synthwave、软体 3D、等轴、HUD 的风格提示语 | MIT（提示语和代码） |
| [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | 古埃及、梵高、莫奈的绘画引擎，我们的 A 用它的源码重渲染 | MIT |
| [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | 产品界面宣传片和孔版错位的参考 | 以上游为准 |
| [prompt-motion.com](https://prompt-motion.com) | 像素、黏土、3D 角色、手绘笔记、Shader、粒子、ASCII 的公开参考 | 只放链接 |
| [yasue.org 的 Opus 5.5 视频生成极限文章](https://en.yasue.org/article/pushing-opus-5-5-video-generation-limits) | 七支英文讲解 B 复述的猫进村故事 | 只放链接 |'''

AUTHOR_EN = '''**Carl (@卡尔的AI沃茨)** started GoodCase and maintains this repo. Six years of large-model R&D at ByteDance, Alibaba and Baidu before turning to AI video, then a run of AI shorts that made it onto Chinese TV. 500k+ followers across platforms. Follow along on [X @aiwarts](https://x.com/aiwarts) or the WeChat official account [卡尔的AI沃茨](https://mp.weixin.qq.com/s/bNtxe27sQfGVig40VCAd_Q). Questions and collaborations: [carl@goodcase.ai](mailto:carl@goodcase.ai).'''

AUTHOR_ZH = '''**卡尔（@卡尔的AI沃茨）** 是 GoodCase 的发起人，也维护这个仓库。在字节、阿里、百度做了六年大模型研发后转做 AI 视频，几部 AI 短片上过央视和卫视，全网 50 万以上关注。可以在 [X @aiwarts](https://x.com/aiwarts) 或公众号 [卡尔的AI沃茨](https://mp.weixin.qq.com/s/bNtxe27sQfGVig40VCAd_Q) 找到他，合作和勘误发 [carl@goodcase.ai](mailto:carl@goodcase.ai)。'''


def readme_en():
    return f'''**[English](./README.md)** | [中文](./README_zh.md)

<img src="./assets/style-wall.webp" width="100%" alt="carl-motion style wall: 29 motion-graphics styles playing at once">

# carl-motion

**{N} motion-graphics styles, one copy-paste prompt each.** Paper collage, synthwave, ink wash, woodcut, point cloud, claymation, risograph, glass UI and more. Every style comes with an 8-second example, the prompt, the mistakes that usually break it, and for {len(OURS)} of them the full source code that rendered the clip.

Install the Skill, then tell your agent *make my topic in the risograph style*:

{INSTALL}

Claude Code also works as a plugin: `/plugin marketplace add {REPO}` then `/plugin install carl-motion@carl-motion`.

## Contents

- [Start here](#start-here)
- [The {N} styles](#the-{N}-styles)
- [Skill](#skill)
- [Templates and source](#templates-and-source)
- [How the examples were made](#how-the-examples-were-made)
- [Upstream skills and references](#upstream-skills-and-references)
- [Media and licenses](#media-and-licenses)
- [Acknowledgements](#acknowledgements)
- [Author](#author)

## Start here

Nothing to install for the first try. Pick a look in the gallery below and open its page. Copy the prompt block and replace *your topic* with your own subject. Paste it into Claude, ChatGPT or any model that writes code, and ask for a 1920×1080, 30 fps, 8-second MP4. If the result looks off, read that page's **Where it usually breaks** section and run it again.

## The {N} styles

The order follows the video we cut from them: neighbouring styles sit on roughly complementary colors, so each cut reads as a clear change. {len(MOVING)} of the {N} play here. The other {N - len(MOVING)} only have third-party examples we can't redistribute, so their pages link to the source instead.

{gallery("en", "./", "./docs/styles/")}

## Skill

`carl-motion` turns this library into something your coding agent can use. Ask for a style by name or by look (*flat, warm, hand-made*). The agent picks the closest entry, fills the prompt with your topic, checks it against the known failure points, and when the style ships source code here, it starts from that engine instead of a blank file.

| | Prompt pages | Skill |
|---|---|---|
| For | Anyone, no install | Claude Code, Codex and other coding agents |
| How | Copy, swap your topic, paste | `npx skills add {REPO}`, then just ask |
| You get | One prompt | A prompt, a render plan and a check against known failures |

## Templates and source

**Scene engines.** {len(OURS)} styles ship the code that rendered their B clip, all at 1920×1080, 30 fps, 240 frames. Each folder has a README with the render command and the known limits.

{scene_table("en")}

**9:16 explainer layout.** [`templates/pipeline/script_layout.py`](templates/pipeline/script_layout.py) stacks two clips of the same style (A over B), adds a fixed title bar, and runs one 8-second beat per style underneath: question bubble, style name, the prompt typed out, then a warning strip. A presenter box on the right is a placeholder for a talking-head shot.

<img src="./assets/layout-9x16.jpg" width="300" alt="9:16 layout: A and B clips stacked, prompt card and warning strip underneath">

**Pipeline.** The rest of [`templates/pipeline`](templates/pipeline) is the tooling behind the video: `encode.sh` (one H.264 spec for every clip), `qa.py` (format, black-frame and jump-cut checks), `color_order_v4.py` (orders styles so neighbours sit on complementary colors), `color_stitch_verify.py` (re-measures every cut on the finished video) and `opener_salience.py` (scores candidate openers in CIELAB). See its [README](templates/pipeline/README.md).

## How the examples were made

Every style is a pair of 8-second clips. A is an upstream reference; B is a second example in the same style, so viewers can see the look carry over to a different subject. {len(OURS)} of the B clips were written and rendered from scratch for this repo by Claude Opus 5.5, from a style prompt plus the A clip as reference, and seven of them retell one short story, how cats moved in with the first farmers, each in its own style. Every clip passed the same checks: 1920×1080, 30 fps, exactly 240 frames, full decode, no black frames, and every flagged jump frame inspected by eye.

## Upstream skills and references

These are the style skills and galleries this library was built on. Their prompts are linked from each style page.

{UPSTREAM_EN}

## Media and licenses

Code, prompts and our own renders (`assets/previews`, `assets/posters` for styles marked *source included*, `templates/`) are MIT. Preview clips for four styles are LemoLab demo films under CC BY 4.0 and are credited on their pages. Clips from prompt-motion.com, X, yasue.org and video-shotcraft are not copied here: their pages link out. The 9:16 sample frame uses a huashu (MIT) A clip and our B clip.

## Acknowledgements

- [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar), [Vincentwei1021/mg-styles-15](https://github.com/Vincentwei1021/mg-styles-15), [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) for the open style recipes.
- [prompt-motion.com](https://prompt-motion.com) and [yasue.org](https://en.yasue.org/article/pushing-opus-5-5-video-generation-limits) for public references.
- [LearnPrompt/awesome-seedance](https://github.com/LearnPrompt/awesome-seedance) for the gallery-plus-Skill format.

## Author

{AUTHOR_EN}
'''


def readme_zh():
    return f'''[English](./README.md) | **[中文](./README_zh.md)**

<img src="./assets/style-wall.webp" width="100%" alt="carl-motion 画风墙：29 种动效画风同时播放">

# carl-motion

**{N} 种动效画风，每种一段能直接复制的提示语。** 纸张拼贴、Synthwave、水墨、木刻、点云、黏土、孔版套印、玻璃拟态等等，每个画风都配 8 秒示例、提示语和最容易翻车的地方，其中 {len(OURS)} 个连渲染示例的完整源码一起给。

装上 Skill，跟你的 Agent 说一句用孔版套印风格做我的主题就行：

{INSTALL}

Claude Code 也可以按插件装：先 `/plugin marketplace add {REPO}`，再 `/plugin install carl-motion@carl-motion`。

## 目录

- [先试一次](#先试一次)
- [{N} 种画风](#{N}-种画风)
- [Skill](#skill)
- [模版和源码](#模版和源码)
- [示例是怎么做出来的](#示例是怎么做出来的)
- [上游 Skill 和参考](#上游-skill-和参考)
- [素材与许可](#素材与许可)
- [致谢](#致谢)
- [作者](#作者)

## 先试一次

第一次用什么都不用装。在下面的画风墙里挑一个顺眼的，点进去，复制提示语，把你的主题换成自己的内容，发给 Claude、ChatGPT 或者任何会写代码的模型，让它出 1920×1080、30 fps、8 秒的 MP4。效果不对就看那一页的容易失败的点，改完再跑一次。

## {N} 种画风

顺序和我们剪的那支盘点视频一致，相邻两个画风的主色大致互补，换组的时候一眼就能看出变了。{N} 个里有 {len(MOVING)} 个能在这里直接动起来，剩下 {N - len(MOVING)} 个只有不能转载的第三方示例，页面里放的是来源链接。

{gallery("zh", "./", "./docs/styles/")}

## Skill

`carl-motion` 把这套画风库交给你的编程 Agent 用。你可以报画风名，也可以只描述感觉，比如扁平、暖色、手作感。Agent 会挑最接近的那一条，把你的主题填进提示语，对着已知的失败点检查一遍；这个画风在仓库里有源码的话，它会直接从那份引擎改起。

| | 画风页 | Skill |
|---|---|---|
| 适合谁 | 所有人，不用安装 | 用 Claude Code、Codex 等编程 Agent 的人 |
| 怎么用 | 复制，换主题，粘贴 | `npx skills add {REPO}`，然后直接提要求 |
| 得到什么 | 一段提示语 | 提示语、渲染方案和对失败点的检查 |

## 模版和源码

**画风引擎。** {len(OURS)} 个画风附带渲染 B 的源码，统一 1920×1080、30 fps、240 帧，每个目录的 README 写了渲染命令和已知限制。

{scene_table("zh")}

**9:16 口播排版。** [`templates/pipeline/script_layout.py`](templates/pipeline/script_layout.py) 把同一画风的两段示例上下叠放，顶上一条常驻标题，底下每 8 秒走一遍同样的节拍：问句气泡、画风名、逐字打出的提示语、注意条。右边的机位框留给真人口播。

<img src="./assets/layout-9x16.jpg" width="300" alt="9:16 排版：A、B 上下叠放，底部是提示语卡和注意条">

**流水线。** [`templates/pipeline`](templates/pipeline) 里还有做那支视频用到的工具。`encode.sh` 把每支片编成同一规格，`qa.py` 查规格、黑帧和跳帧，`color_order_v4.py` 按互补色排画风顺序，`color_stitch_verify.py` 在拼好的成片上复测每个切点，`opener_salience.py` 在 CIELAB 里给开场候选打分。用法见它的 [README](templates/pipeline/README.md)。

## 示例是怎么做出来的

每个画风是一对 8 秒片。A 来自上游参考，B 是同一画风换个题材的第二个例子，让人看得出这个画风能迁移。{len(OURS)} 支 B 是 Claude Opus 5.5 为这个仓库从零写代码渲染的，输入是风格提示语和 A 作参考；其中七支用各自的画风接力讲同一个小故事，猫是怎么住进最早的农人村子的。每支片都过同一套检查：1920×1080、30 fps、正好 240 帧、完整解码、没有黑帧，自动标出的跳帧逐个用眼睛看过。

## 上游 Skill 和参考

这套画风库建立在下面这些开源风格 Skill 和公开画廊之上，每个画风页都链回了对应的上游提示语。

{UPSTREAM_ZH}

## 素材与许可

代码、提示语和我们自己渲染的片段都按 MIT 发布，包括 `templates/`，以及标了含源码的画风在 `assets/` 里的预览。另有四个画风的预览是 LemoLab 的演示片，按 CC BY 4.0 使用并在页面里署名。prompt-motion.com、X、yasue.org 和 video-shotcraft 的片段没有复制进仓库，页面里只放链接。9:16 示例帧里的 A 来自 huashu（MIT），B 是我们渲染的。

## 致谢

- [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)、[Vincentwei1021/mg-styles-15](https://github.com/Vincentwei1021/mg-styles-15)、[alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) 开放了风格配方。
- [prompt-motion.com](https://prompt-motion.com) 和 [yasue.org](https://en.yasue.org/article/pushing-opus-5-5-video-generation-limits) 提供了公开参考。
- [LearnPrompt/awesome-seedance](https://github.com/LearnPrompt/awesome-seedance) 的画廊加 Skill 结构。

## 作者

{AUTHOR_ZH}
'''


def styles_index():
    rows = '\n'.join(f'| {s["order"]:02d} | [{s["name_en"]}]({s["slug"]}.md) | {s["name_zh"]} | {"✓" if s["scene"] else ""} | {"✓" if s["preview"] else ""} |' for s in ZH)
    return f'''# All {N} styles · 全部 {N} 种画风

[Back to README](../../README.md)

| # | Style | 画风 | Source 源码 | Preview 预览 |
|---|---|---|---|---|
{rows}
'''


def skill_reference():
    out = [f'# carl-motion style reference ({N} styles)', '',
           'Generated from data/styles.*.json. Each entry: English and Chinese prompt, key visuals, watch-out line, common failures, palette, references, and the scene folder when the repo ships source.', '']
    for s in ZH:
        e = EN[s['id']]
        out += [f'## {s["order"]:02d} {s["name_en"]} · {s["name_zh"]} (`{s["slug"]}`)', '',
                f'- Use when: the user wants {s["name_en"].lower()} / {s["name_zh"]}.',
                f'- Prompt (EN): {e["full_prompt"]}',
                f'- 提示语（中）: {s["full_prompt"]}',
                f'- Breaks when: {e["fail"]}',
                f'- 容易失败: {s["fail"]}',
                f'- Palette: {", ".join(s["palette"])}',
                f'- Scene source: {s["scene"] or "none, build from the prompt"}',
                f'- References: ' + '; '.join(f'{r["layer"]} {r["by"]} {r["url"] or ""}'.strip() for r in s['refs']), '']
    return '\n'.join(out)


if __name__ == '__main__':
    text_tiles()
    for s in ZH: w(f'docs/styles/{s["slug"]}.md', page(s))
    w('docs/styles/README.md', styles_index())
    w('README.md', readme_en())
    w('README_zh.md', readme_zh())
    w('agents/skills/carl-motion/references/styles.md', skill_reference())
    print('ok', N, 'styles,', len(OURS), 'with source,', len(MOVING), 'with preview')
