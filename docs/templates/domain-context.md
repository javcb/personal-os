---
title: Domain Context Template
type: template
audience: self
status: active
last-updated: 2026-04-17
related:
  - /docs/governance/autonomy-matrix.md
  - /_core/self-model.md
---

# Domain Context Template

Use this template to create a new domain file in `docs/domains/[domain-name].md`.

Replace `[domain-name]` with the lowercase kebab-case name of the domain (e.g., `finance-economics.md`, `family-parenting.md`).

---

## Purpose & Scope

**Why this domain matters:**
[Describe the domain's role in your life/work. Connect to the corresponding role in _core/self-model.md. Example: "Finance & Economics is where I manage personal wealth, tax planning, investment decisions, and financial strategy as a CPA."]

**What is in scope:**
- [Aspect 1]
- [Aspect 2]
- [Aspect 3]

**What is explicitly out of scope:**
- [Excluded aspect 1]
- [Excluded aspect 2]

---

## Key Models & Frameworks

**Mental models you apply in this domain:**
- [Reference models from _core/models.md, or describe them inline]
- [Example: For finance, mental models might include "cash flow hierarchy," "tax-efficient sequencing," "risk tolerance vs. actual behavior"]

**Key concepts:**
- [Concept 1]: [brief explanation]
- [Concept 2]: [brief explanation]

---

## Operating Rules & Decision Protocols

**Rules that govern work in this domain:**
- [Rule 1: what triggers decisions; what the decision process is]
- [Rule 2]
- [Rule 3]

**Decision protocol (if applicable):**
If [situation], then [check these sources], then [apply this framework], then [decide / propose].

**Example:**
"If a new tax opportunity arises, check current year's filing status, run through the 5-Stage Decision Protocol, consult _core/models.md for any relevant financial frameworks, then either decide (if within normal guardrails) or propose."

---

## Autonomy Boundaries

**Reference from autonomy-matrix.md:**

| Action Type | Autonomy | Notes |
|---|---|---|
| Analysis | [Copy from matrix] | [Why this boundary exists] |
| Drafting/Proposals | [Copy from matrix] | [Why this boundary exists] |
| Execution | [Copy from matrix] | [Why this boundary exists] |
| Final Decision | [Copy from matrix] | [Why this boundary exists] |

**What this means in practice:**
[Concrete example of what LLMs can do autonomously and what must be proposed]

---

## Pipelines & Knowledge Ingestion

**Pipelines that feed this domain:**
- [Pipeline name]: [what it ingests; where it stores output]
- Example: "Knowledge Ingestion Pipeline → feeds finance articles, research papers to docs/knowledge-extracts/finance-economics/"

**Knowledge sources:**
- [External source 1]: [how to keep it fresh]
- [External source 2]

**Integration triggers:**
- When [event], update this domain's knowledge base with [action].
- Example: "When tax law changes, run knowledge-ingestion pipeline and propose updates to this file."

---

## Related Skills & Workflows

**Meta-skills that apply here:**
- [Link to docs/skills/_custom/[skill-name].md]
- Example: "internal-first-research.md — Use this skill when encountering new information in this domain"

**Domain-specific workflows:**
- [Link to docs/workflows/[workflow-name].md]
- Example: "docs/workflows/annual-tax-planning.md"

**Pipelines:**
- [Link to docs/pipelines/[pipeline-name].md]

---

## Where to Look

**High-velocity reference for this domain:**

| What | Where |
|---|---|
| [Key concept/decision] | [File path] |
| [Key source/rule] | [File path] |
| [Key contact/resource] | [File path or note] |
| [Most recent context] | [File path] |

**Example for Finance:**

| What | Where |
|---|---|
| Tax rules and thresholds | docs/knowledge-extracts/finance-economics/[latest-tax-summary].md |
| Investment framework | _core/models.md (investment decision framework) |
| Current financial state | _core/self-model.md (Financial Context section) |
| 2026 goals | _core/roadmap.md (Strategy & Planning phase) |

---

## Quick Reference (Optional)

**Checklist for decisions in this domain:**
- [ ] Have I read the latest context file in this domain?
- [ ] Does this decision touch other domains? (Check related)
- [ ] Am I within autonomy boundaries? (Check autonomy-matrix.md)
- [ ] Should I consult _core/models.md? (If so, do that first)
- [ ] Is this a proposal or a decision I can make autonomously?

---

*Domain-context files are living documents. Review quarterly or after role changes.*
