---
title: Strategy & Planning
type: domain-context
audience: self
status: active
domain: strategy-planning
last-updated: 2026-04-17
related:
  - /docs/domains/operations-systems.md
  - /docs/domains/governance-policy.md
  - /docs/domains/learning-research.md
  - /docs/domains/family-parenting.md
  - /docs/domains/finance-economics.md
  - /_core/roadmap.md
  - /_core/self-model.md
---

# Strategy & Planning

Domain for long-term planning, vision, strategy, and prioritization across all other domains.

---

## Purpose & Scope

**Why this domain matters:**

Strategy and planning are cross-domain activities that determine what gets worked on, when, and why. This domain covers long-term vision (what does success look like in 1–10 years?), medium-term planning (3–12 months), and prioritization (what are we working on right now?). Good strategy clarifies trade-offs and prevents drift; bad strategy creates busy-ness without direction.

**What is in scope:**
- Long-term vision and life goals
- Strategic planning across domains (family, finances, career, personal-os)
- Prioritization and trade-off decisions
- Roadmap design and phase planning
- Quarterly planning and reviews
- Initiative tracking and closure
- Resource allocation decisions
- Life phase management

**What is explicitly out of scope:**
- Operational execution (see operations-systems)
- Detailed domain decisions (see individual domains)
- Personal relationships (see family-parenting)
- External market strategy (see professional-advisory)

---

## Key Models & Frameworks

**Mental models you apply in this domain:**

- **Vision informs strategy informs tactics**: Without a clear vision (what does success look like?), strategy becomes random activity. With vision, strategy guides which tactics matter. Tactics without strategy is busy-ness.
- **Time horizons matter**: Decisions have different time horizons. Short-term decisions (this week) should align with medium-term planning (this year) which should align with long-term vision (this decade). Misalignment creates conflict.
- **Trade-offs are real**: You cannot optimize everything simultaneously. Strategy is explicit about what you're optimizing for (financial security, family time, intellectual growth) and what you're trading off (fast advancement, maximized income, cutting-edge knowledge).
- **Seasons exist in life**: Different seasons have different constraints and opportunities. Parenting young children is different from parenting teenagers; building a startup is different from scaling it. Strategy varies by season.
- **Reversibility guides timing**: Strategic decisions that are hard to reverse (major commitments, moving, career pivots) need more deliberation than reversible ones. Plan reversible decisions faster; pause on irreversible ones.

**Key concepts:**
- **Optionality and flexibility**: Strategy should preserve optionality where possible. Avoid lock-in that forecloses future choices.
- **Milestones and progress**: Long-term vision gets broken into milestones. Milestones help you know you're making progress and help you course-correct if you're drifting.
- **Resilience over optimization**: A plan that adapts to changes is better than an optimized plan that breaks under stress. Strategy should be robust, not fragile.

---

## Operating Rules & Decision Protocols

**Rules that govern work in this domain:**

1. **Vision and strategy are documented** — Long-term vision, current strategy, and top priorities are documented in _core/roadmap.md (or equivalent). Not written down = not real.

2. **Roadmap is human-curated** — LLMs may propose roadmap updates via session-debrief, but Javier reviews and edits. Automated roadmap generation is not allowed (GOVERNANCE-RULES.md Section 7).

3. **Priorities are explicit and few** — Having 10 priorities means having zero priorities. Current roadmap lists top 3 priorities (next phase). Focus beats breadth.

4. **Strategy is revisited quarterly** — Quarterly reviews check whether strategy is working, whether priorities are still right, and whether life circumstances have changed. Adjust as needed.

5. **Trade-offs are acknowledged** — Strategy is not about doing everything; it's about choosing. Acknowledge what you're trading off (speed for stability, advancement for family time, etc.).

**Decision protocol (if applicable):**

If making a strategic decision or planning a phase:
1. Clarify vision: What does success look like in 1–10 years? What are non-negotiables?
2. Assess current state: Where are we now relative to vision? What are the gaps?
3. Identify strategic options: What are 2–3 ways to move from current state to vision? What are the trade-offs?
4. Choose strategy: Based on vision and constraints, which path makes sense?
5. Plan the phase: What's the next 3–12 months? What are success criteria?
6. Set priorities: What are the top 3 things we're working on? What's explicitly deferred?
7. Document: Update roadmap, DECISIONS.md, and communicate priorities.
8. Execute and monitor: Monthly check-ins on progress; quarterly reviews on whether strategy is still right.

---

## Autonomy Boundaries

**Reference from autonomy-matrix.md:**

| Action Type | Autonomy | Notes |
|---|---|---|
| Analysis | AI ✓ | LLM can analyze strategic options and planning questions fully autonomously |
| Drafting/Proposals | AI → Review | LLM can draft strategic options and roadmap proposals; Javier reviews and decides |
| Execution | AI → Review | LLM can execute against approved strategy (e.g., break down roadmap into tasks); reviewed before deployment |
| Final Decision | Human | Strategic direction and prioritization are Javier's final decisions |

**What this means in practice:**

LLMs can analyze strategy questions and propose options. LLMs can draft roadmap proposals and strategic plans. But final decisions on direction, vision, and priorities remain with Javier. LLM is strategic analyst; Javier is strategic decider. Roadmap updates flow through session-debrief and require Javier approval (GOVERNANCE-RULES.md Section 7).

---

## Pipelines & Knowledge Ingestion

**Pipelines that feed this domain:**

- **Strategic Planning Pipeline** → Tracks long-term vision, medium-term plans, and quarterly reviews; documents in _core/roadmap.md and _core/initiatives.md
- **Initiative Tracking Pipeline** → Manages active projects and strategic initiatives; tracks status and closure
- **Quarterly Review Pipeline** → Reviews progress toward strategy; assesses whether direction is still right; proposes adjustments

**Knowledge sources:**

- Session debriefs and learnings from execution
- Domain-specific context (from all domains)
- Self-model and personal values (CLAUDE.md, _core/self-model.md)
- Life circumstances and external changes
- Mentor and peer feedback

**Integration triggers:**

- Quarterly: Run quarterly review; assess progress; propose roadmap adjustments via session-debrief.
- When major life change occurs: Revisit strategy; assess impact on priorities and timelines.
- When domain priorities shift: Update roadmap to reflect new cross-domain alignment.
- When an initiative closes: Document learnings; assess impact on overall strategy.

---

## Related Skills & Workflows

**Meta-skills that apply here:**

- `internal-first-research.md` — Use when analyzing strategic questions; research through internal canon first.
- `session-debrief.md` — Strategic learnings and priority shifts should surface as durable takeaways.
- `phase-wrap-up.md` — Use when closing a phase or major initiative to document what was completed and plan re-entry.

**Domain-specific workflows:**

- /docs/workflows/quarterly-planning-protocol.md (when created)
- /docs/workflows/long-term-vision-clarification.md (when created)
- /docs/workflows/roadmap-update-protocol.md (when created)

**Pipelines:**

- /docs/pipelines/knowledge-ingestion.md — For strategic and planning content

---

## Where to Look

**High-velocity reference for this domain:**

| What | Where |
|---|---|
| Current phase and priorities | _core/roadmap.md (current phase section) |
| Next phases and roadmap | _core/roadmap.md (next phase queue section) |
| Long-term vision and goals | _core/self-model.md (current priorities section) |
| Strategic decisions and rationale | DECISIONS.md (entries with [strategy]) |
| Active initiatives and projects | _core/initiatives.md (when created) |
| Deferred initiatives and decisions | _core/roadmap.md (explicitly deferred section) |

---

## Quick Reference (Optional)

**Checklist for strategic decisions in this domain:**

- [ ] Does this align with long-term vision?
- [ ] What are the strategic trade-offs? (What are we optimizing for? What are we trading off?)
- [ ] Is this reversible or hard to undo?
- [ ] How does this affect other domains?
- [ ] Have I documented the decision and rationale?
- [ ] How will I know if this strategy is working?
- [ ] When will I revisit this decision?
- [ ] Have I communicated priorities clearly?

---

*Domain-context files are living documents. Review quarterly or after major strategic changes.*
