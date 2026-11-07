---
name: carl-motion
description: 29 motion-graphics styles (paper collage, synthwave, ink wash, woodcut, point cloud, claymation, risograph, glassmorphism, blueprint, pixel game, particles, HUD and more), each with a tested prompt, known failure points and a status; 20 ship the engine that rendered an 8-second example, plus a delivery gate that checks the clip. Use when the user wants an animated clip, explainer or motion graphic in a named visual style, asks which style fits a topic, wants to restyle an animation, or says carl-motion / 动效画风 / 画风盘点 / 用某某画风做动画.
metadata:
  version: "0.2.0"
---

# carl-motion

`<skill>` below means the folder this file is in. Everything you need is inside it: style cards in `references/styles/`, engines in `scenes/`, tools in `scripts/`.

## Which track you are on

- **Open track.** You are Claude Opus 5.5 or stronger. Read anything here, combine engines, write your own renderer. Two things are fixed: the clip ends with `scripts/deliver.py`, and a red verdict means it is not done.
- **Rail track.** Any other model, or you cannot tell. Follow the numbered path below and read only the files it names.

## The rail

0. **Check the machine.** `python3 <skill>/scripts/doctor.py`. If it reports anything missing, tell the user what to install and stop.

1. **Resolve the brief before picking.** Run `python3 <skill>/scripts/resolve_brief.py --request "<the user's words>"`. Add `--media <file>` for each image or video they gave you, and `--media-url` for a link. Read the JSON. It does not render and it does not rewrite engines. `limits.llm_compliance_proven` is false on purpose: the file is a router and a probe, not a claim that you obeyed this skill.
   - `decision: exact` — open that one card and use its engine. `local_preview.decoded: true` means this run measured frames from the redistributable excerpt (color and motion only). `references[].fetched: false` means the catalog URL was not opened. Do not tell the user you watched the original video unless `full_source_video` is true. Do not paste those frames, a logo, or music into the new topic. The engine stays on `engine.stack`.
   - `decision: candidate` or `mixed` — do not start an engine and do not call it an exact match. Name the listed styles, one line each, and ask at most one question.
   - `decision: custom` — do not snap the request onto the 29. Use `style_parameters`. Leave null fields unknown. Then follow 3b.
   - `decision: no_preset` — nothing in the 29 fits, and no reference file was decoded. If `search.reminder` is set, show that string and stop the style step: search is not available, and the reminder is the ask to turn it on so a reference can be found on X. If you already have a search tool, do not ask again; run it once, write `{"results":[{"url","title","source"}]}`, and re-run with `--search-file`. A link in those results is not a video you watched. If `search.refused` is true or `result_count` is 0, keep `steps.house_spec` as a draft and stop where `steps.style_parameters.blocked` is true. Do not invent posts or say you looked on X.
   - Missing material blocks only the step whose `blocked` field is true. Keep the unblocked steps, and mark drafts.
   - Facts stay in `facts`. Do not add measurements you did not make to `inferences`. Do not fabricate a product screen or a number; a number needs a source and a date. Record a path or URL, when you got it, and the size or duration you actually measured.
   - Do not move these engines onto HyperFrames, GSAP, or any other stack, and do not stop after every step waiting for a reply.

2. **Read that card in full** when the decision is exact (`references/styles/NN_slug.md`). Its status decides the next step:
   - *Implemented* or *implemented on an upstream library*: go to 3a.
   - *Upstream only* or *research*: go to 3b.

3a. **Start from the engine.**
   `cp -R <skill>/scenes/<engine> <project>/engine`, then `python3 <skill>/scripts/doctor.py <engine>`. Read `<project>/engine/README.md`; if it has a *Keep / replace* section, follow it. Change the subject only: names, captions, shapes, story beats. Keep the code that makes the look (texture passes, stepping, halftone, brush flow). Preview single frames first where the README offers it (most Python engines take `ONLY=60,150`). Then `<project>/engine/render.sh <project>/work`.

3b. **Build a new engine.** Read `references/scene-contract.md` and write `<project>/engine/render.sh` plus the scene code by those rules, using the card's prompt and pipeline. Render one still at 4 s first and show it to the user. Animate only after they say it reads as the style.

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
