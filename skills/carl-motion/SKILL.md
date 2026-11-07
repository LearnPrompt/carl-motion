---
name: carl-motion
description: 29 motion-graphics styles (paper collage, synthwave, ink wash, woodcut, point cloud, claymation, risograph, glassmorphism, blueprint, pixel game, particles, HUD and more), each with a tested prompt, known failure points and a status; 20 ship the engine that rendered an 8-second example, plus a delivery gate that checks the clip. Use when the user wants an animated clip, explainer or motion graphic in a named visual style, asks which style fits a topic, wants to restyle an animation, or says carl-motion / 动效画风 / 画风盘点 / 用某某画风做动画.
metadata:
  version: "0.2.0"
---

# carl-motion

`<skill>` below means the folder this file is in. Everything you need is inside it: style cards in `references/styles/`, engines in `scenes/`, tools in `scripts/`.

## Which track you are on

- **Open track.** You are Claude Opus 5.5 or stronger. You may read anything here and combine engines. Before copying an engine or writing a renderer, run step 1 and obey `steps` and `claims`. The clip still ends with `scripts/deliver.py`, and a red verdict means it is not done.
- **Rail track.** Any other model, or you cannot tell. Follow the numbered path below and read only the files it names. Do not skip step 1.

## The rail

0. **Check the machine.** `python3 <skill>/scripts/doctor.py`. If it reports anything missing, tell the user what to install and stop.

1. **Resolve the brief before picking or rendering.** Run `python3 <skill>/scripts/resolve_brief.py --request "<the user's words>"`. Add `--media <file>` for each local image or video, and `--media-url` for a link. Do not copy an engine, write a renderer, or run `render.sh` / `deliver.py` until you have obeyed this JSON. `limits.llm_compliance_proven` is false: the file is a router and a probe, not proof that a model obeyed this skill.
   - `claims.video_guided_generation` and `claims.engine_consumes_reference_video` are false. An exact match is drawn by the engine's own code. Decoding a preview measures that repo excerpt (color and frame difference). It is not an input to `render.sh`, and it is not the original URL. Do not say the clip was video-guided or that you referenced a video to generate it.
   - If `claims.may_claim_referenced_video` is false, do not say you referenced a video. If `claims.may_claim_watched_link` is false, do not say you watched a link. Search hits and catalog URLs with `decoded: false` stay unread.
   - A readable reference is a local file. Ask for one and re-run with `--media`. A URL becomes readable only after it is saved locally and that file decodes.
   - A draft without a reference stays blocked. Continue only after the user explicitly approves that draft, then re-run with `--approve-unreferenced-draft`. The label becomes 用户已批准的无参考草稿. Still do not claim a video was used. Style numbers that were not measured stay empty.
   - `decision: exact` — open that one card and, when `steps.render.blocked` is false, use its engine on `engine.stack`. Do not paste preview frames, a logo, or music into the new topic.
   - `decision: candidate` or `mixed` — do not start an engine and do not call it an exact match. Name the listed styles, one line each, and ask at most one question.
   - `decision: custom` — do not snap the request onto the 29. Use `style_parameters`. Leave null fields unknown. Then follow 3b.
   - `decision: no_preset` — nothing in the 29 fits, and no reference file was decoded. If `search.reminder` is set, show that string and stop the style step. If you already have a search tool, do not ask again; run it once, write `{"results":[{"url","title","source"}]}`, and re-run with `--search-file`. If `search.refused` is true or `result_count` is 0, keep the house spec as a draft and stop. Do not invent posts or say you looked on X.
   - Missing material blocks only the step whose `blocked` field is true. Keep the unblocked steps, and mark drafts.
   - Facts stay in `facts`. Do not add measurements you did not make to `inferences`. Do not fabricate a product screen or a number; a number needs a source and a date. Record a path or URL, when you got it, and the size or duration you actually measured.
   - Do not move these engines onto HyperFrames, GSAP, or any other stack, and do not stop after every step waiting for a reply.

2. **Read that card in full** when the decision is exact (`references/styles/NN_slug.md`). Its status decides the next step:
   - *Implemented* or *implemented on an upstream library*: go to 3a.
   - *Upstream only* or *research*: go to 3b.

3a. **Start from the engine** only when `decision` is `exact`, an engine is listed, and `steps.render.blocked` is false.
   `cp -R <skill>/scenes/<engine> <project>/engine`, then `python3 <skill>/scripts/doctor.py <engine>`. Read `<project>/engine/README.md`; if it has a *Keep / replace* section, follow it. Change the subject only: names, captions, shapes, story beats. Keep the code that makes the look (texture passes, stepping, halftone, brush flow). Do not pass a reference video, a preview, or a URL into the renderer. Preview single frames first where the README offers it (most Python engines take `ONLY=60,150`). Then `<project>/engine/render.sh <project>/work`.

3b. **Build a new engine** when `decision` is `custom`, or when `decision` is `no_preset` and `approved_unreferenced_draft` is true. Otherwise stop. Read `references/scene-contract.md` and write `<project>/engine/render.sh` plus the scene code by those rules. Render one still at 4 s first and show it to the user. Animate only after they say it reads as the style. An approved draft is still not a reference-video recreation.

4. **Design against the pitfalls.** Before the full render, list each line of the card's *Pitfalls* and say where the code handles it.

5. **Deliver.** `python3 <skill>/scripts/deliver.py --frames <project>/work/frames --out <project>/<slug>.mp4 --palette "<the card's palette>"` (add `--crf` if the card says so).
   Exit code 0 is green, 1 is yellow (the clip is still written), 2 is red. `info:` lines, such as palette distance, never change the verdict; the card palette is sampled from the example clips, so a different topic will drift.
   - Red: nothing was delivered. Apply the printed fix, re-render, run it again.
   - Yellow: the clip is written. Say for each flagged item whether it is intended (a designed cut, a beat change) or a problem.
   - Green or yellow: show the user `<slug>.mp4.qa/contact.jpg`.

6. **Log it.** Append one line to `<project>/carl-motion-log.md`:
   `- YYYY-MM-DD · <slug> · <topic> · <verdict> · <what broke> · <how you fixed it>`

## Output

Give the filled prompt as one copy-pasteable block, the style and its status, and the pitfalls you designed against. When you rendered, add the MP4 path, the verdict, and the contact sheet. List anything that did not pass.

## Open track extras

- `references/workflow.md`: the A/B method, ordering many styles by complementary colour, the 9:16 explainer layout.
- `pipeline/`: the tools behind a multi-style video (`color_order_v4.py`, `color_stitch_verify.py`, `script_layout.py`). They work on a delivery folder; see `pipeline/README.md`.

## Language

Answer in the user's language. Every card carries the prompt in English and Chinese.
