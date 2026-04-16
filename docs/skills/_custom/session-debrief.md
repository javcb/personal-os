---
title: Session Debrief
type: meta-skill
audience: ai
status: active
domain: [meta, learning]
related:
  - /CLAUDE.md
  - /docs/skills/_custom/internal-first-research.md
  - /docs/skills/_custom/phase-wrap-up.md
---

# Session Debrief

A meta-skill for extracting durable takeaways and repo-update proposals at the end of meaningful LLM sessions, so the system grows stronger over time.

## Purpose

Use this skill at the end of any session where something changed: understanding, architecture, decisions, pipelines, skills, or future plans.

**The core principle:**

Extract only durable takeaways and structured repo-update proposals.

This allows future-you or any LLM to update the system and restart later without reconstructing context from memory.

The debrief is the primary mechanism by which this system accumulates knowledge, stays consistent, and becomes self-sustaining.

---

## When to Use This Skill

Apply this skill at the end of a session where any of these are true:

1. **We finished a multi-step exploration or design session** — Design, architecture, or strategy work that took more than one prompt.
2. **We made (or seriously considered) structural decisions** — Governance, process, or system design that affects future work.
3. **We discovered new models, processes, or patterns worth reusing** — Mental frameworks, workflows, or operating patterns that could be durable.
4. **We identified gaps, risks, or blind spots** — BL (Blind Spot, future risk) or KU (Known Unknown) items that should be tracked or escalated.
5. **We are about to pause or end the session** — Even exploratory work sometimes yields useful takeaways for the next session.
6. **We did meaningful work that benefits from being recorded** — Anything beyond trivial fact-checking or quick lookup.

**Do not use this skill for:**
- Single-turn fact lookups ("What time is the meeting?")
- Purely exploratory queries with no concrete output
- Questions where nothing changed or was decided

For those, answer directly. For everything else, run a debrief.

---

## Required Outputs

Every session debrief must produce:

### Durable Takeaways

A structured list where each item follows this exact format:

```
- [TYPE: model/skill/process/pipeline/canon-candidate/governance-candidate/decision/inbox]
  - Summary: <one-sentence description of the takeaway>
  - Why durable: <why this matters beyond today; why it should be preserved>
  - Suggested destination: <file path or category, e.g., docs/domains/..., _core/models.md, DECISIONS.md, inbox.md>
  - Relation to canon: [confirm/extend/conflict/obsolete/unclear]
```

Each takeaway must have all four fields. No exceptions.

### No-Takeaway Sessions

If the session produced no durable takeaways (e.g., purely exploratory or debugging), explicitly state:

```
No durable takeaways from this session.
Reason: [brief explanation, e.g., "exploratory only", "debugging unresolved issue", "answered one-off question"]
```

### Notes (Optional)

A brief free-form section if there are contextual comments that help future-you or an LLM interpret the takeaways (e.g., "This decision depends on X being resolved first" or "Revisit in Phase N when Y is clearer").

---

## Step-by-Step Protocol

Follow these steps in order:

### Step 1: Scan the Session for Durable Changes

Review the conversation and identify ideas that:

- **Change how Javier should think or act in the future** — New mental models, frameworks, or principles.
- **Define a reusable model, skill, or process** — Something that could be used again.
- **Affect architecture or governance** — Structural decisions, rule changes, or process refinements.
- **Belong on the roadmap or in future phases** — Discoveries that shape priorities or next steps.
- **Resolve or clarify prior unknowns** — Answers to known unknowns (KK) or blind spots (BL).

### Step 2: Filter Out Ephemeral Details

Exclude:
- One-off examples or illustrations.
- Transient debugging details or exploration notes.
- Context that won't matter in the next session.
- Repetition or reworking of earlier versions (unless the final version is significantly different).

**Default bias:** Fewer, higher-quality takeaways are better than many marginal ones.

### Step 3: Classify Each Takeaway

For each candidate, assign a TYPE from:

| Type | Belongs in |
|---|---|
| **model** | _core/models.md (later atomic files in docs/domains/) |
| **skill** | docs/skills/ |
| **process** | docs/workflows/ or docs/processes/ |
| **pipeline** | docs/pipelines/ |
| **canon-candidate** | docs/domains/, docs/architecture/, or domain-specific reference |
| **governance-candidate** | docs/governance/, GOVERNANCE-RULES.md, or GOVERNANCE-CHANGE-LOG.md |
| **decision** | DECISIONS.md |
| **inbox** | inbox.md (for rough, underspecified, or "think about later" items) |

Choose the type that best reflects where the takeaway ultimately belongs.

### Step 4: Assess Durability and Relation to Canon

For each takeaway, briefly justify why it's durable:
- Does it apply to multiple scenarios or decisions?
- Is it a principle or pattern, not a one-off observation?
- Would future-you benefit from seeing it again?

Compare it against existing canon (relevant files in the repo):
- **confirm** — aligns with existing decisions or beliefs.
- **extend** — adds nuance or depth without contradicting.
- **conflict** — contradicts something the repo already decided.
- **obsolete** — makes an existing decision outdated or invalid.
- **unclear** — relevant but doesn't fit clean categories.

If a takeaway conflicts or obsoletes existing canon, **highlight that explicitly**. Don't smooth it over.

### Step 5: Propose Concrete Destinations

For each takeaway, suggest a specific file path or location:

**Examples:**
- docs/domains/finance.md (if it's domain-specific knowledge)
- _core/models.md (if it's a mental model)
- docs/governance/GOVERNANCE-RULES.md (if it's a rule proposal)
- DECISIONS.md (if it's an architectural choice)
- _core/roadmap.md (if it affects next-phase priorities)
- inbox.md (if it's still rough and needs later processing)

These are **proposals only**. Actual updates must go through governance and human review.

### Step 6: Produce the Structured Output

Render the debrief using the Durable Takeaways format defined in "Required Outputs" above.

Use the exact format:
```
- [TYPE: ...]: ...
  - Summary: ...
  - Why durable: ...
  - Suggested destination: ...
  - Relation to canon: ...
```

If there are no durable takeaways, explicitly state "No durable takeaways from this session" with a reason.

---

## Relationship to Other Meta-Skills

Session-debrief is usually:

- **Used near the end of a session** — After meaningful work is done, before wrapping up.
- **Followed by phase-wrap-up** (if applicable) — If a workstream or phase is being paused, run phase-wrap-up to document stopping point and re-entry.
- **Informed by internal-first-research and pre-action-critique** — These skills ran earlier; debrief captures the takeaways from that work.

**Debrief vs. Phase-Wrap-Up:**
- **Session-debrief** — Captures learning and repo updates. Focused on what we learned and what should change.
- **Phase-wrap-up** — Captures stopping point, remaining work, and re-entry instructions. Focused on continuity and breadcrumbs.

Both are important. A session can have a debrief but no phase-wrap-up (if work continues in the next session). A phase can have both debrief (what we learned) and wrap-up (where we stopped).

---

## Good vs Bad Usage

### Bad Debrief (❌ avoid)

```
## Session Debrief

We did a lot today. Good work. Should pick this up later when we have time.
```

**Why it fails:**
- Vague; no specific takeaways.
- No types, destinations, or relation to canon.
- Doesn't help future sessions.
- Doesn't grow the system.

### Good Debrief (✅ follow this pattern)

```
## Session Debrief

- [TYPE: governance-candidate]
  - Summary: Broken links should block commits (not just warn).
  - Why durable: Link rot degrades docs over time. Early detection prevents accumulation.
  - Suggested destination: docs/governance/GOVERNANCE-RULES.md Section 5.
  - Relation to canon: extends canon (current rule warns; propose change to fail).

- [TYPE: decision]
  - Summary: Governance v1 scope finalized: 8 active checks, content-level rules deferred.
  - Why durable: Establishes boundary for Phase 2 work; prevents mid-stream governance churn.
  - Suggested destination: DECISIONS.md.
  - Relation to canon: confirm (consistent with design principles).

- [TYPE: process]
  - Summary: Phase-wrap-up skill formalizes "pause, document, re-entry" workflow.
  - Why durable: Prevents context loss across sessions; improves resumability.
  - Suggested destination: docs/skills/_custom/phase-wrap-up.md.
  - Relation to canon: new (no prior process existed).
```

**Why it works:**
- Each takeaway is specific and actionable.
- Types and destinations are clear.
- Relation to canon is explicit.
- Future-you can read this and understand what to encode and where.

---

## Quality Checklist

This debrief is complete when:

- [ ] I considered whether there are durable takeaways (and explicitly said "none" if not).
- [ ] Each takeaway has all four fields: Summary, Why durable, Suggested destination, Relation to canon.
- [ ] Each takeaway has a TYPE from the defined list.
- [ ] Conflicts, obsoletes, and unclear items are explicitly called out (not hidden).
- [ ] Destinations are concrete file paths, not vague categories.
- [ ] Durability is justified (why this matters beyond today).
- [ ] The output is concise enough to be readable in a future session without scrolling excessively.

---

## How to Know When to Stop

Session-debrief is complete when:

- You have extracted all takeaways that are genuinely durable (not exploratory flotsam).
- Each takeaway could be understood and implemented by a future LLM without the full session context.
- The list is short enough to be actionable (3–7 items is typical; more is usually a sign you need to be more selective).

When in doubt, err on the side of fewer, clearer takeaways.

---

*Last updated: 2026-04-15*
