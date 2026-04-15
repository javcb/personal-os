---
title: session-debrief
type: meta-skill
status: active
last-updated: 2026-04-15
---

# Session Debrief

Extract durable learning at the end of any work session (with AI, with a team, or solo).

## Trigger Question

Ask at session end:  
**What did this session reveal that will still matter in 3+ future sessions?**

## Output Format

One takeaway per line, in this format:

```
[TYPE] takeaway — why it's durable
```

### Required Fields

- **`[TYPE]`** — must be one of: `principle` | `process` | `heuristic` | `constraint` | `anti-pattern` | `trap`
- **`takeaway`** — one sentence, concrete, reusable, not task-specific
- **`why it's durable`** — explicit claim about staying valid (minimum bar: "applies to at least 3 future tasks of this kind")

## Examples

### With takeaways

```
[principle] Governance at the structural level prevents compound errors — catches violations before they cascade into downstream work.
[anti-pattern] Choosing the first acceptable option blocks discovery of better options — always evaluate at least two alternatives.
[constraint] Python scripts in git hooks must use explicit path detection — shell PATH inheritance is unreliable on GitHub Desktop.
[process] Pre-commit hooks should warn, not silently fail — failing silently creates false confidence in protection.
[trap] Emoji in Python print() can cause encoding errors on Windows — use ASCII equivalents or wrap in UTF-8 encoding fix.
```

### Without takeaways (valid result)

```
No durable takeaways from this session.
```

This is a complete, acceptable result.

## Rules

**Prefer quality over quantity.** One solid takeaway beats five mediocre ones.

**Filter task-specific trivia.** "We fixed line 47" is not durable. "We fixed a bug by reading error messages more carefully" is.

**Zero takeaways is valid.** If a session taught nothing generalizable, recording "No durable takeaways" is the honest and correct output.

**Be honest about durability.** A takeaway that only applies to one specific project is not durable yet—unless you can explain why the next similar project will face the same constraint.

## Session Metadata (optional)

If you want to query your learnings later, add optional context:

```
## 2026-04-15 (repo setup, Claude Code)

[principle] ...
```

Date helps you spot patterns (e.g., "all April decisions revolved around governance"). Tool context helps you remember whether a learning is tool-specific or universal.

## Where to Store

- **Quick captures:** Add entries to `inbox.md` under the session date.
- **Formal log:** Create a `_core/learnings.md` if you build a searchable archive.
- **Linked:** Link back to `DECISIONS.md` if a takeaway influenced a decision.
