---
title: Quadrants
type: context
audience: self
status: draft
last-updated: 2026-04-17
related:
  - /_core/self-model.md
  - /_core/models.md
---

# Quadrants

## Purpose

This file maps Javier's epistemic state across domains.
Goal: shrink the lag time between something existing in the blind spot (BL)
and knowing it's there. Tag aggressively; promote through use.

Cycle: BL → KU → KK

## Known Knowns (KK)

Things I know and can rely on in decision-making.

### Finance & Economics
- Cash flow hierarchy: operating reserves first, then debt reduction,
  then investment, then discretionary.
- Tax-advantaged sequencing: maximize 401k/IRA before taxable accounts.
- Compound interest favors time over rate; starting early beats optimizing later.
- CPA-level fluency in tax law, financial statements, and reporting standards.

### Operations & Systems
- Systems beat goals: a repeatable process outperforms willpower every time.
- Governance prevents entropy; rules must be enforced automatically or they degrade.
- Monorepo beats polyrepo for single-person knowledge systems.

### Learning & Research
- Spaced repetition and active recall outperform passive re-reading.
- Unknown unknowns are the most dangerous; tag BL aggressively.
- Frictionless capture is prerequisite to anything else.

### LLM Interface & Systems Design
- LLM interface layer (CLAUDE.md + meta-skills + roadmap) successfully designed and validated.
- Autonomy matrix pattern works: explicit per-domain boundaries prevent scope creep.
- Governance v1 (9 checks, governed subtrees) prevents structural degradation.
- Meta-skills encode repeatable workflows better than procedural docs.
- Roadmap governance: LLMs propose via session-debrief, humans decide. No automation of priorities.
- Domain organization by role (not initiative) is correct for cross-domain knowledge systems.

### Family & Parenting
- Family stability and financial resilience are the non-negotiables everything
  else is sequenced around.
- [JAVIER TO FILL: 1–2 parenting frameworks you rely on]

## Known Unknowns (KU)

Things I know I don't know and am actively trying to understand.

- [session:2026-04-17] Will the personal-os system actually work in practice with real sessions,
  or will usage reveal critical design flaws?
- [session:2026-04-17] Do the 9 domains capture the actual work, or will real usage
  reveal domains that need splitting, merging, or renaming?
- [session:2026-04-17] How to ensure system legibility for wife and collaborators
  without creating extra documentation overhead?
- [session:2026-04-17] How to automate knowledge ingestion pipelines without
  introducing governance debt or requiring constant maintenance?
- [session:2026-04-17] What happens to system coherence if Javier takes a long break?
  How quickly can work resume?
- [JAVIER TO FILL: e.g., "How do I structure my advisory practice for scalability
  without adding unsustainable overhead?"]
- [JAVIER TO FILL: e.g., "What is the right college savings strategy given
  current timeline and income constraints?"]
- [JAVIER TO FILL: e.g., "How do economic policy cycles affect my clients'
  industries and what should I be tracking?"]
- [JAVIER TO FILL: e.g., "What are the best frameworks for teaching financial
  literacy to kids at different developmental stages?"]
- How to design compounding personal knowledge systems that get smarter from
  use rather than requiring constant manual maintenance.
- What governance patterns from nonprofit board work are most transferable
  to personal decision-making.

## Unknown Unknowns (BL)

Blind spots surfaced through sessions, readings, or surprises.
Tag new entries: `[quadrant:BL] [session:YYYY-MM-DD]`

- [quadrant:BL] [session:2026-04-13] The AI entropy problem: every stateless LLM
  session degrades repo quality unless governance actively prevents it. This was
  a complete blind spot until this design session.
- [quadrant:BL] [session:2026-04-13] Budget/legacy risk: a single SaaS dependency
  could erase years of knowledge work. Hadn't named this risk until forced to ask
  "what will I regret not doing now?"
- [quadrant:BL] [session:2026-04-15] Meta-skills are the OS, not a convenience.
  Without them, autonomous workflows degrade into inconsistent, memory-dependent habits.
- [quadrant:BL] [session:2026-04-17] Core context files (_core/quadrants, models, initiatives)
  need substantive content to unlock pipelines. Template files that are only stubs
  create a bootstrap problem: pipelines need context to run, but context requires
  knowing what to fill in.
- [quadrant:BL] [session:2026-04-17] "What changed" vs "what is the summary" distinction
  for knowledge extraction. Summaries are passive archives; extractions that identify
  what changed your thinking are what upgrades mental models. This distinction changes
  how knowledge ingestion pipelines should work.
- [quadrant:BL] [session:2026-04-17] Epistemic filter concept: external information
  interpreted through system canon, not in isolation. Personal-os should actively
  reject information that doesn't fit existing models or explicitly update models
  when new information conflicts. This is different from passive curation.

## Known Unknowables

Things I accept I cannot know or have decided not to pursue.

- Exact future tax law changes (monitor, don't predict).
- Market timing (irrelevant to long-term strategy; ignore).
- [JAVIER TO FILL: anything else explicitly out of scope or unknowable]

## Promotion Log

When a KU becomes a KK, log it here.

| Date | Item | From | To | How |
|---|---|---|---|---|
| 2026-04-15 | AI entropy / governance | BL | KK | Design session: built governance-check.py |
| 2026-04-15 | Meta-skills as OS layer | BL | KK | Design session: encoded as SKILL files |
| 2026-04-17 | LLM interface layer design | KU | KK | Design session: CLAUDE.md + 3 meta-skills + roadmap validated |
| 2026-04-17 | Autonomy matrix pattern | KU | KK | Design session: implemented in docs/governance/autonomy-matrix.md |
| 2026-04-17 | Domain organization by role | KU | KK | Design session: 9 domains created in docs/domains/ |
| 2026-04-17 | Governance v1 is sufficient | KU | KK | Design session: 9 enforcement checks verified via governance-check.py |
| 2026-04-17 | Roadmap governance rule | KU | KK | Design session: codified in GOVERNANCE-RULES.md Section 7 |
