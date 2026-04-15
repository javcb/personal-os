---
title: How to Resume Work on personal-os
type: context
status: active
audience: self
quadrant: KK
change-velocity: medium
last-updated: 2026-04-15
standalone: true
related:
  - _core/roadmap.md
  - _core/context/prompt-index.md
---

# How to Resume Work on personal-os

## 1. Where to Start

- Open `_core/roadmap.md` — this is the living checklist.
- Look for the first unchecked item in the current phase.
- If nothing is obvious, run the Session Debrief meta-skill on 
  your last few commits and update the roadmap.

## 2. Daily Session Pattern

1. Read `_core/roadmap.md` and pick ONE task.
2. Find the matching prompt in `_core/context/prompt-index.md`.
3. Run that prompt with Claude Code or Cursor.
4. Run the Session Debrief meta-skill.
5. Update `_core/roadmap.md` and the "Next Action" note below.

## 3. Next Action (update at end of every session)

- As of 2026-04-15: Diagnose and fix GitHub Desktop pre-commit hook environment (Python PATH not inherited in GitHub Desktop context)

## 4. Rules for Future Javier

- Do not edit `global-docs` when working on Personal OS. 
  Treat it as read-only.
- Do not start new files at root. If in doubt, append to `inbox.md`.
- Do not run large refactors without:
  - governance passing
  - a DECISIONS.md entry
- If you feel lost:
  1. Read this file.
  2. Read `_core/roadmap.md`.
  3. Run the Session Debrief meta-skill on the last session.
  4. Write a fresh "Next Action" above.
