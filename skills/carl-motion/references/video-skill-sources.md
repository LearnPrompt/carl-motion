# 八个视频 Skill：来源与选用

核对日期：2026-11-07。清单来自 [Snail 的原帖](https://x.com/Cryptoxorz/status/2110044544494600619)，按原顺序列出。它是八个视频制作 Skill 的合集，其中第八项使用历史影像，并非代码动画画风。

以下能力来自作者说明；本次只核读原帖、仓库及 README，未安装或渲染这些上游项目。原帖中的画风、镜头数量属于当时版本，不作为当前数量承诺。

| # | 原帖名称与当前入口 | 适合的任务 | Carl Motion 当前关系 |
|---|---|---|---|
| 1 | [xilo-opus-video](https://github.com/Kianzzz/xilo-opus-video) | 想法、文章或参考片 → 多方案预览 → 选定方案后制作 | 新增参考入口；未集成其流程 |
| 2 | [lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) | 按画风选择代码影片方案与样片 | 已有风格来源，按各风格卡核对 |
| 3 | [mg-styles-15](https://github.com/Vincentwei1021/mg-styles-15) | MG 动态设计、短片风格与代码参考 | 已有风格来源，按各风格卡核对 |
| 4 | [dashi-animationstyle](https://github.com/chuspeeism/dashi-animationstyle) | 中文口播 → 分镜、静帧、带字幕和声音的讲解动画 | 新增参考入口；未集成口播与字幕管线 |
| 5 | [huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | 艺术画风与解说动画方法 | 已有部分绘画引擎来源；不代表整个上游已集成 |
| 6 | wtt-code-animation-studio → [wtt-code-video-studio](https://github.com/WaterDJiang/Wattter_openSkills/tree/main/wattter_skills/wtt-code-video-studio) | 想法、文章或剧本 → 分镜、代码动画、配音和 MP4 | 新增参考入口；上游当前目录已更名，未复制代码或素材 |
| 7 | [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | 网页、前端产品的宣传片与 2.5D 运镜 | 已有产品界面等参考，不是内置完整产品宣传片工作流 |
| 8 | archival-doc（Snail 自制） | 公有领域／CC 授权的真实历史影像整理与纪录片剪辑 | 原帖未提供仓库地址；保留名称，不猜安装入口、不标记可用 |

## 如何选用

- 已指定画风、要制作 Carl Motion 的短动画：继续按本 Skill 的风格卡与引擎执行。
- 还在比较表现形式：可参考 xilo 的方案预览方法；用户已选定形式时无需重新选。
- 已有口播、需要声音和字幕同步：先核读 dashi 的当前说明，区分它的上游能力与 Carl Motion 现有的无音轨短片规格。
- 从长文章或剧本制作叙事视频：可研究 WTT 的编排与校时方法；其当前许可见下文，不能直接当作本仓库的 MIT 代码。
- 做产品介绍：参考 video-shotcraft 的镜头方法，以真实界面和功能作为输入。
- 做历史纪录片：archival-doc 仅为来源线索；没有可检查的公开实现，不能声称已接入。

这些入口不自动安装依赖，不改变已有 29 张风格卡、20 个画风源码及交付门禁。新增渲染能力须另有实际源码、样片和验证记录；资料收录不增加已实现数量。

## 当前地址与使用范围

WTT 的仓库当前仅列出 `wtt-code-video-studio` 目录，本文保留原帖旧名以便追溯。[上游 README](https://github.com/WaterDJiang/Wattter_openSkills/blob/3a9c4a88c8d8d3c12ace7df5604097ab15b8ee7a/README.md) 声明默认 CC BY-NC-SA 4.0，个别目录另有许可。本文只提供链接与用途摘要，不引入其代码、提示语或媒体。

dashi 的 [README](https://github.com/chuspeeism/dashi-animationstyle/blob/aa620f3b859aa5d191b783b2eb0fb59263731c76/README.md) 声明代码和文档 MIT，但作者示例口播仅供试用该 Skill，不用于其他作品。其他项目的素材、人物形象、字体和音频也应按具体文件的说明核对；仓库顶层许可不自动覆盖全部第三方内容。

本次核对的仓库版本：

| 仓库 | 核对提交 |
|---|---|
| Kianzzz/xilo-opus-video | `f2cd828e2692e7186186408ee01a936707c2c38d` |
| lemomo-ai/lemo-opuscar | `bc0992ae25f63c1780dd9cfe39a020e2deda79ec` |
| Vincentwei1021/mg-styles-15 | `49052d80bfaf9fa8412cc9710530e5e95a3b8d8c` |
| chuspeeism/dashi-animationstyle | `aa620f3b859aa5d191b783b2eb0fb59263731c76` |
| alchaincyf/huashu-art-motion | `8a0d7d72ca65fcce6f8ba82c4a6c8dfe35b8422c` |
| WaterDJiang/Wattter_openSkills | `3a9c4a88c8d8d3c12ace7df5604097ab15b8ee7a` |
| Vincentwei1021/video-shotcraft | `1266a3ec4831289c4d893d42dd5102723658039a` |

## 后续补充帖，单独保留

[雪踏乌云的后续帖](https://x.com/Pluvio9yte/status/2114717699549126739) 提到 ClaudeAnimationBase、mg-styles-15、video-shotcraft。这是另一份三项推荐，不能将 ClaudeAnimationBase 填入原八项清单，也不能把作者的效果评价视为 Carl Motion 的实测。本次没有集成 ClaudeAnimationBase。
