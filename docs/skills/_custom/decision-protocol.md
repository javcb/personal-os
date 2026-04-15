---
title: Decision Protocol
type: meta-skill
domain: cognition
audience: self
status: active
quadrant: KK
change-velocity: low
last-updated: 2026-04-15
related:
  - _core/models.md
  - docs/skills/_custom/session-debrief.md
  - CLAUDE.md
standalone: true
---

# Decision Protocol

## Purpose
A 5-stage protocol to move from uncertainty to committed action 
without locking in too early or drifting indefinitely.
Run this before any architectural, financial, or irreversible decision.

## When to Run
- Before any structural change to this repo
- Before adopting a new tool, framework, or process
- Before any decision that is hard to reverse
- Whenever momentum is pushing toward a choice faster than thinking is

## The 5 Stages

**1. Inform**
What do I actually know vs. what am I assuming?
What would I need to know to evaluate this properly?
→ Failure mode if skipped: fighting the wrong problem at full speed.

**2. Compare**
What are the legitimate alternatives — not strawmen?
What criteria matter, and how does each option score?
→ Failure mode if skipped: defaulting to the familiar path.

**3. Critique**
What is the strongest argument against the leading option?
Give the counterargument its full weight — not a weakened version.
→ Failure mode if skipped: building the wrong thing with confidence.

**4. Connect**
What else does this decision touch?
What breaks upstream or downstream if this choice is wrong?
→ Failure mode if skipped: local coherence, global inconsistency.

**5. Commit or Pause**
Is there one question whose answer would change everything?
→ If yes: pause. Surface the question. Get the answer first.
→ If no: commit. Log the decision in DECISIONS.md. Move.

## The Rule
A decision that cannot survive Stage 3 is not ready to commit.
A decision that survives all five stages can be committed with confidence —
not certainty, but confidence.

## Output
Every committed decision gets one line in DECISIONS.md:
[DATE]: [decision] — [reason in one sentence]

That line is the proof the protocol ran.

After writing, run governance-check.py and confirm it passes.
