---
title: Autonomy Matrix
type: reference
audience: ai
status: active
domain: governance
last-updated: 2026-04-17
related:
  - /_core/self-model.md
  - /docs/governance/GOVERNANCE-RULES.md
---

# Autonomy Matrix

Per-domain guide for what LLMs can do autonomously vs. what requires Javier's review.

---

## Purpose

This matrix defines the boundary between autonomous LLM action and human-required decisions in each of the nine domains. It is the authoritative guide for LLM scope within personal-os.

Before acting in any domain, check your action type against this matrix. If the cell is marked **Human**, stop and propose instead. If marked **AI → Review**, proceed but surface the work for human review before it is deployed or applied to the repo.

---

## How to Use (For LLMs)

1. Identify your intended action type: Analysis, Drafting/Proposals, Execution, or Final Decision.
2. Find the row corresponding to the domain you're working in.
3. Look up the cell at the intersection of your action type and the domain.
4. **AI ✓** — You may act autonomously. No approval needed.
5. **AI → Review** — You may act autonomously, but flag the work for human review before use.
6. **Human** — Stop. Propose the action instead; wait for human decision.

When in doubt, treat as **AI → Review** (safer than assuming autonomous permission).

---

## Autonomy Matrix

| Domain | Analysis | Drafting/Proposals | Execution | Final Decision |
|---|---|---|---|---|
| **finance-economics** | AI → Review | AI → Review | Human | Human |
| **family-parenting** | AI → Review | AI → Review | Human | Human |
| **operations-systems** | AI ✓ | AI → Review | AI → Review | Human |
| **governance-policy** | AI ✓ | AI → Review | Human | Human |
| **software-development** | AI ✓ | AI ✓ | AI → Review | Human |
| **professional-advisory** | AI → Review | AI → Review | Human | Human |
| **learning-research** | AI ✓ | AI ✓ | AI ✓ | Human |
| **legal-regulatory** | AI → Review | AI → Review | Human | Human |
| **strategy-planning** | AI ✓ | AI → Review | AI → Review | Human |

---

## Rationale by Domain

**Finance & Economics** — High stakes. Financial decisions carry direct consequences. Analysis is safe (LLM can process data); drafts are useful (LLM can propose structures); but execution and final decision remain with Javier (CPA-licensed, understands full tax and investment context).

**Family & Parenting** — Deeply personal. Parenting decisions are values-driven and context-dependent. Analysis of parenting concepts is okay; proposals for approaches are useful; but Javier must decide what applies to his family.

**Operations & Systems** — Lower stakes. System design and operational procedures can be analyzed and drafted by LLM; execution (creating docs, processes) can be reviewed; final decisions on adoption rest with Javier.

**Governance & Policy** — Moderate stakes. LLM can analyze governance concepts; can draft rules and checks; but execution (committing governance changes) and final decisions require human review.

**Software & Development** — Technical domain. LLM has high autonomy for analysis and drafting code; execution (implementing features) can be reviewed; Javier makes final architectural decisions.

**Professional Advisory** — High stakes. This is Javier's professional work (finance advising, consulting). Analysis and drafting require human review (Javier's expertise is needed); execution and decisions are Javier's.

**Learning & Research** — Lowest stakes. Research and learning are LLM-friendly. Analysis is autonomous; drafting (notes, summaries) is autonomous; execution (creating docs) is autonomous; Javier makes final decisions about what to integrate.

**Legal & Regulatory** — Highest stakes. Compliance and legal decisions carry legal risk. Analysis requires review; drafting requires review; execution is Javier's only; decisions are Javier's.

**Strategy & Planning** — Moderate stakes. LLM can analyze strategic options; can draft strategic proposals; execution and review are collaborative; final decisions are Javier's.

---

## Override Rule

**When in doubt, treat as AI → Review.** Never assume full autonomy in a domain not listed here.

This matrix is conservative by design. It assumes LLMs err on the side of caution in high-stakes domains. As confidence in specific workflows builds, Javier may revise individual cells to expand AI autonomy (e.g., "learning-research" drafting is fully autonomous; others might follow). Changes to this matrix are governance decisions and must be logged in GOVERNANCE-CHANGE-LOG.md.

---

## When to Revisit This Matrix

- After 10 real sessions, review whether autonomy boundaries match actual comfort level.
- If an action marked **AI → Review** is consistently approved without modification, consider upgrading to **AI ✓**.
- If an action marked **AI ✓** frequently triggers re-work or concern, downgrade to **AI → Review**.
- When new domains are added to personal-os, define initial matrix values in the domain-context file.

---
