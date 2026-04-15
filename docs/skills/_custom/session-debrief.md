---
title: Session Debrief
type: meta-skill
domain: cognition
audience: self
status: active
quadrant: KK
change-velocity: low
last-updated: 2026-04-15
related:
  - _core/models.md
  - docs/skills/_custom/decision-protocol.md
standalone: true
---

# Session Debrief

## Purpose
At the end of any working session — with an AI tool, a collaborator, 
or alone — extract only the takeaways worth keeping permanently. 
Prevent insight from evaporating between sessions.

## When to Run
- End of any LLM session that produced a decision, framework, or 
  new understanding
- End of any deep work session where thinking evolved
- After any after-action review

## The Trigger Question
"What came out of this session that I would want to know in six months?"

## Format for Each Takeaway
- [TYPE]: model | skill | meta-skill | process | canon-candidate
- One sentence summary of the insight
- Why it's durable — not just useful today, but true across contexts

## The Rule
Zero takeaways is a valid and honest answer.
Do not manufacture takeaways to justify the session.
If nothing durable emerged, that is useful signal too.

## Where Takeaways Go
- Append raw to inbox.md with [session:date] tag
- Weekly review promotes to permanent home
- Never create a new file directly from a session debrief

## What Does Not Qualify
- Tactical steps completed (those belong in DECISIONS.md)
- Tool-specific tricks that will be obsolete
- Anything you already knew before the session started

After writing, run governance-check.py and confirm it passes.
