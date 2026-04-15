---
title: Internal-First Research
type: meta-skill
audience: ai
status: active
domain: [meta, research]
related:
  - /CLAUDE.md
  - /_core/self-model.md
  - /_core/models.md
  - /docs/governance/GOVERNANCE-RULES.md
  - /DECISIONS.md
---

# Internal-First Research

A meta-skill for answering non-trivial questions through the lens of personal-os, not generically.

## Purpose

Use this skill whenever you need to answer a question that involves planning, strategy, design, analysis, or decisions—especially when external information might be consulted.

**The core principle:**

Answer through Javier's personal-os (self-model, domains, canon, governance, and prior decisions) first.

Only then integrate external information.

Never answer generically by defaulting to external sources or model background knowledge.

The goal is to preserve and strengthen the system's canon, not to bypass it.

---

## When to Use This Skill

Apply this skill to any non-trivial question where any of these are true:

1. **Evaluating options, tradeoffs, or strategies** — "What should we choose?"
2. **Designing or refining a process, system, or workflow** — "How should we approach this?"
3. **Researching a topic that might change how we think** — "What do we need to learn?"
4. **Making a recommendation or decision with real consequences** — "What do you recommend?"
5. **The question explicitly involves Javier's preferences, constraints, or prior decisions** — "How does this fit my approach?"
6. **Proposing changes to the repo structure, governance, or canon** — "Should we adopt this?"

**Do not use this skill for:**
- Trivial fact lookups ("What is the capital of France?")
- Pure arithmetic or simple definitions
- Questions where the repo has explicitly deferred to Javier's in-the-moment judgment

For those, answer directly. For everything else, use this skill.

---

## Inputs and Outputs

### Inputs
- The user's question
- Any relevant context from the current session or task
- Implicit: the full content of the repo as your knowledge base

### Outputs (Always Include These, In This Order)

**1. What Your Repo Already Says**

Summarize the relevant internal context from the repo: prior decisions, models, preferences, constraints, or domain knowledge that applies to this question.

Cite specific files and sections. Be concrete.

**2. What External Sources Say** (if consulted)

If you consulted external information (web search, model background), summarize key findings here.

Focus on what matters given the internal canon. Avoid raw citations; distill to essence.

If no external sources were needed, write "Not required for this question."

**3. Assessment vs Canon**

For each major finding or claim, classify it:

- **confirms canon** — aligns with what the repo already decided or believes
- **extends canon** — adds nuance, depth, or new dimension without contradiction
- **conflicts with canon** — contradicts something the repo decided
- **obsoletes canon** — makes an existing decision outdated or invalid
- **unclear / needs human judgment** — relevant but doesn't fit clean categories

If there are conflicts, highlight them explicitly. Don't smooth them over or hide tensions.

**4. Suggested Repo Updates (If Any)**

If the research suggests durable changes to the repo, propose them using this format:

```
- [TYPE: canon-candidate / skill / process / governance-candidate / decision / inbox]
  Summary: [one sentence]
  Rationale (why durable): [why this is worth keeping]
  Suggested destination: [file path or category]
  Relation to existing canon: [confirm / extend / conflict / obsolete]
```

If no updates are needed, write: "None; current canon is sufficient."

**5. Answer to the Original Question** (optional)

After the four sections above, optionally provide a concise, user-facing answer that integrates both internal and external perspectives, clearly rooted in the analysis above.

This is optional because the four sections above are often enough. Include it only if it clarifies something.

---

## Step-by-Step Protocol

Follow these steps in order:

### Step 1: Classify the Question

Determine what type of question this is:
- Decision (choosing between options)
- Plan (how to approach something)
- Analysis (understanding a domain or problem)
- Learning (what to know about a topic)
- Architecture (system design or structure)
- Governance (rules, process, enforcement)
- Refinement (improving something existing)
- Other (specify)

**Note this classification internally.** You don't need to print it unless it's helpful for clarity.

### Step 2: Identify Relevant Internal Context

Based on the classification, decide which of these to consult:

| If classification is... | Consult these files first |
|---|---|
| **Decision** | _core/self-model.md, DECISIONS.md, docs/governance/ |
| **Plan** | _core/roadmap.md, _core/initiatives.md, relevant docs/pipelines/ |
| **Analysis** | _core/models.md, relevant docs/domains/, DECISIONS.md |
| **Learning** | relevant docs/domains/, docs/knowledge-extracts/, _core/quadrants.md |
| **Architecture** | DECISIONS.md, docs/governance/, _core/models.md |
| **Governance** | docs/governance/, GOVERNANCE-RULES.md, DECISIONS.md |
| **Refinement** | relevant skill/domain/pipeline files, DECISIONS.md |

**Always also consult:**
- _core/quadrants.md if the question touches on gaps, blind spots, or areas marked "known unknown"
- _core/self-model.md if the answer depends on Javier's time, risk tolerance, goals, or constraints

Read these files. Summarize what they say in the **"What Your Repo Already Says"** output section.

### Step 3: Consult External Sources (If Needed)

Only after the internal pass, consult external information if appropriate:
- Web search for current data or best practices
- Your training knowledge for established frameworks or concepts
- Relevant external sources that the repo explicitly points to

**Ask yourself:** Would an external source meaningfully change the answer given what we already know?

If yes, consult it. If no, skip it.

Summarize findings in the **"What External Sources Say"** section.

### Step 4: Compare External Findings vs Canon

For each major external point, classify its relationship to internal canon in the **"Assessment vs Canon"** section.

If an external finding conflicts with the repo's decisions, state the conflict explicitly. Don't smooth it over or hide the tension.

Example: "Web best practice recommends X. However, DECISIONS.md from 2026-04-15 explicitly chose not to do X because [reason]. This is a conflict that needs human review."

### Step 5: Propose Repo Updates (If Warranted)

In the **"Suggested Repo Updates"** section, list only changes that seem genuinely worth encoding.

Use the structured format provided in the Outputs section above.

**Do not propose updates for:**
- One-off answers or context-specific choices
- Things Javier hasn't explicitly asked to encode
- Changes that would require Javier's approval anyway

Do propose updates for:
- New mental models or frameworks worth preserving
- Governance improvements
- Process refinements that prevent future confusion
- Decisions that should be logged

### Step 6: Answer the Original Question (Optional)

If helpful, provide a concise answer that integrates your analysis and is clearly rooted in the "What your repo says" + "Assessment vs canon" sections.

---

## Relationship to CLAUDE.md and Other Meta-Skills

This skill operationalizes the **Internal-First Research Protocol** described in CLAUDE.md, Section "Internal-First Research Protocol."

It is often used:

- **After pre-action-critique** — You've evaluated a decision; now you need to research it within the repo's context.
- **Before session-debrief** — You've researched a question; now you'll debrief and propose repo updates.
- **Alongside phase-wrap-up** — You're closing a phase and need to document what you learned and what should change.

It is distinct from:
- **session-debrief** — That skill reflects on learnings. This skill generates the structured findings that session-debrief then captures.
- **pre-action-critique** — That skill evaluates before acting. This skill researches to inform that evaluation.
- **phase-wrap-up** — That skill closes a phase. This skill supports identifying what to close and what to defer.

---

## Good vs Bad Usage

### Bad Usage (❌ avoid)

- Jumps straight to external web answers without mentioning what the repo already says.
- No explicit classification of external findings vs canon.
- No proposal for repo updates, even when conflicts or extensions are obvious.
- Answers feel generic, not rooted in personal-os.
- Presents multiple options without grounding them in Javier's constraints or prior decisions.

**Example:**
```
Q: Should we switch to a new tech stack?
A: Yeah, Tech X is popular now. Here are its features...
```
Why it fails: Doesn't mention what the repo has already decided about tech choices, constraints, or past decisions.

### Good Usage (✅ follow this pattern)

- Starts with "What Your Repo Already Says" grounded in specific files.
- Consults external sources only when useful; summarizes them concisely.
- Explicitly classifies each external finding vs canon (confirm/extend/conflict/obsolete).
- Proposes repo updates using structured format, with rationale.
- Answers the original question with clear reasoning rooted in the analysis above.

**Example:**
```
Q: Should we switch to a new tech stack?

**What Your Repo Already Says:**
- DECISIONS.md (2026-04-01): Chose current stack because [reason A, B, C].
- _core/self-model.md: Priority is [X], not [Y].

**What External Sources Say:**
- Tech X is trending; benchmarks show [improvement in Z metric].

**Assessment vs Canon:**
- Finding: Tech X improves Z metric.
  Relation: **Extends canon** — the repo cares about Z, so this is relevant.
- Finding: Tech X requires rewrite.
  Relation: **Conflicts with canon** — the repo values stability over latest tech.

**Suggested Repo Updates:**
- [TYPE: decision]
  Summary: Revisit tech-stack decision if Z metric becomes critical.
  Suggested destination: DECISIONS.md
  Relation to existing canon: confirm (consistent with stated priorities)

**Answer:** Switching is not recommended now; current stack aligns with stated priorities. However, if [metric Z] becomes critical, revisit in Phase N.
```

Why it works: Rooted in the repo's actual state, explicit about tradeoffs, proposes durably.

---

## Quality Checklist

This skill is complete when:

- You always identify the question type first (classification).
- You always read relevant internal files before external sources.
- You always produce the four required output sections, in order.
- You never skip the "Assessment vs Canon" step; conflicts are highlighted, not hidden.
- Repo updates are proposed only when genuinely durable.
- The final answer, if provided, is clearly rooted in the analysis above.
- Any capable LLM could follow these steps with only this file as instruction.

---

*Last updated: 2026-04-15*
