---
title: Phase Wrap-Up
type: meta-skill
status: active
---

# Phase Wrap-Up

A meta-skill for closing a work phase, documenting the stopping point, and leaving a clean re-entry point for the next session.

## Purpose

Use this skill whenever:
- A phase is ending
- Work is being paused (mid-task or end-of-session)
- A productive digression needs to be closed out
- Governance or another subproject reaches a "good enough for now" stopping point
- You're about to switch to a new major area of work
- You need to preserve breadcrumbs before losing the thread

The goal is **not** to finish everything. The goal is to leave the current area in a legible, resumable state so future-you or any LLM can restart without reconstructing context from memory.

## Core Principle

A good wrap-up creates a **resumable state**:
- Future-you knows exactly where work stopped
- Next action is named, not vague
- Remaining work is visible and triaged
- Intentional deferrals are documented (not forgotten)
- Files are in a consistent state for the next person to pick up

## Trigger Conditions

Run this skill when any of these are true:

1. **Switching streams** — "We are about to switch to a different workstream or project."
2. **Stable checkpoint** — "This area is stable enough for now; it no longer needs active attention."
3. **Diminishing returns** — "I'm getting diminishing returns on effort; continuation is deferred."
4. **Follow-on work discovered** — "I've uncovered follow-on work that belongs in a later phase, not now."
5. **Context fragility** — "I need to preserve breadcrumbs before I lose the thread or context resets."
6. **End of session** — "This is the end of my session; I need to leave clear notes for the next one."

## Required Outputs

Every phase wrap-up must produce:

1. **What was completed** — summary of deliverables, decisions, or progress made
2. **Current stopping point** — exact state: what's done, what's in progress, what's waiting
3. **What remains to do** — unfinished work that is still in scope
4. **What is intentionally deferred** — work that is valid but out-of-scope for this phase
5. **What files were updated** — list of files created, modified, or affected
6. **What the next recommended action is** — specific, named next step (not vague)
7. **Exact re-entry prompt or instruction** — what to paste at the start of the next session

## Canonical Wrap-Up Checklist

Run through these steps in order:

1. **Name the phase.** What is this work slice called? (e.g., "Governance v1 finalization", "LLM interface design")
2. **Summarize completion.** What was delivered or decided in this phase?
3. **State the stopping point.** Why is now a valid place to pause? (e.g., "all 9 checks passing", "architecture approved", "backlog documented")
4. **List remaining work.** What is not done yet? Be specific: list files, decisions, or tasks.
5. **Separate phases.** Explicitly mark what is "remaining in scope" vs. "deferred for later phase."
6. **Record breadcrumbs.** Update the right files (see "File-Target Guidance" below) with stopping point and next action.
7. **Identify the next re-entry action.** What is the first thing to do when work resumes?
8. **Run governance check** (if applicable). If this repo has governance, run checks before closing. Fix any violations.
9. **Produce a handoff.** Write a 2–3 sentence summary that future-you or another LLM can read in 10 seconds.

## File-Target Guidance

Record wrap-up information in the right places:

| Type of Information | Where to Record |
|---|---|
| Structural or architectural decisions made | DECISIONS.md (one line per decision) |
| Governance-related remaining work | docs/governance/GOVERNANCE-CHANGE-LOG.md or backlog section |
| Raw, unresolved ideas not yet triaged | inbox.md (append-only, with [tag] label) |
| Next-phase execution or roadmap notes | _core/roadmap.md (or create if not live yet) |
| Durable process insights or skill refinements | Update relevant skill file or mental-model file |
| Session notes or context breadcrumbs | _core/how-to-resume.md or session-specific note |
| Work that is genuinely deferred (not forgotten) | Explicitly section in DECISIONS.md or relevant doc |

## Output Template

Copy and paste this template at the end of your work session or phase transition:

```
## Phase Being Closed
[Name of the workstream or phase]

## What We Completed
- [Deliverable or decision 1]
- [Deliverable or decision 2]
- [etc.]

## Why We're Stopping Here
[Explain the stopping point. Be concrete: "all checks passing", "architecture reviewed", "foundation stable".]

## Remaining Work
### Still in Scope (Next Phase)
- [Task or file 1]
- [Task or file 2]

### Intentionally Deferred
- [Task that is valid but out-of-scope]
- [Task that depends on earlier decision]

## Files Updated
- [File 1]: [brief note on what changed]
- [File 2]: [brief note]

## Re-entry Point
[What was the last action? What is the immediate next step?
Example: "All governance checks pass. Ready to commit. Next: create LLM interface pipeline."]

## Suggested Next Prompt
[Paste this prompt at the start of the next session to resume cleanly.]
Example:
"""
You are working in my personal-os repo.
Your task is [name the next work area].
Background: [1–2 sentences on what was completed before].
Next step: [exact action to take first].
"""
```

## Good vs. Bad Wrap-Up

### Bad Wrap-Up (❌ avoid)
- "I did governance stuff. Pick it up later."
- "Several things remain. Figure it out."
- "Files were updated. Check git diff."

**Why it fails:** Vague, no re-entry point, forces future-you to reconstruct context.

### Good Wrap-Up (✅ follow this pattern)
- "Governance v1 is frozen with 9 checks enforced. Backlog is documented in GOVERNANCE-RULES.md Section 6. All checks pass. Next: commit changes, then move to LLM interface design. Paste this prompt in the next session: `You are working in my personal-os repo. Your task is to design the LLM interface pipeline...`"

**Why it works:** Specific, self-contained, re-entry is explicit.

## Relationship to Other Meta-Skills

This skill is distinct from but complements:

- **session-debrief** — Captures reflection and learning from a session. Phase-wrap-up is about operational continuity, not reflection.
- **pre-action-critique** — Evaluates a decision before taking action. Phase-wrap-up documents after action is complete.
- **governance** — Enforces structural rules. Phase-wrap-up documents how work was organized and what comes next.

Use phase-wrap-up at **phase boundaries and major transitions**. Use session-debrief for reflection. Use pre-action-critique before major decisions.

## Final Quality Requirement

This skill is complete when:
- Any capable LLM can follow it with the instructions as written
- No additional context is needed beyond the template and checklist
- Re-entry instructions are specific and testable
- Remaining work is triaged (not just listed)
- Deferred work is explicit, not forgotten
- The next action is named, not assumed
