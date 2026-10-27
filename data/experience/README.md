# Field notes · 实测记录

One JSON line per use of a style, in `<slug>.jsonl`: `{"date", "topic", "verdict", "note"}`.
They show up in the *Field notes* section of that style's card the next time `scripts/generate.py` runs.

Add them with `python3 scripts/import_experience.py <carl-motion-log.md>` (the log the skill writes in a user's project), or from a GitHub issue that used the field-note template.

每次用某个画风踩到的坑和修法，一行一条，生成卡片时会进到那张卡的实测记录段。
