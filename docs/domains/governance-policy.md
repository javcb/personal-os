---
title: Governance & Policy
type: domain-context
audience: self
status: active
domain: governance-policy
last-updated: 2026-04-17
related:
  - /docs/domains/operations-systems.md
  - /docs/domains/legal-regulatory.md
  - /docs/domains/strategy-planning.md
  - /docs/governance/GOVERNANCE-RULES.md
---

# Governance & Policy

Domain for personal, organizational, and institutional governance, policy development, and oversight responsibilities.

---

## Purpose & Scope

**Why this domain matters:**

As a nonprofit governance contributor with board and policy experience, governance and policy are core professional responsibilities. This domain covers personal governance (rules for self), family governance (decisions about how the household operates), and organizational governance (nonprofit board, policy oversight, institutional decision-making). Good governance clarifies authority, prevents drift, and creates accountability. Bad governance creates paralysis or unchecked risk.

**What is in scope:**
- Personal governance rules and decision protocols
- Family governance (household rules, decision-making authority)
- Nonprofit board responsibilities and policies
- Organizational governance frameworks and best practices
- Policy development and documentation
- Institutional risk and compliance oversight
- Accountability structures and feedback mechanisms
- Ethical and values-based governance

**What is explicitly out of scope:**
- Professional advisory work (see professional-advisory)
- Regulatory compliance details (see legal-regulatory)
- Technical system implementation (see operations-systems, software-development)
- Strategic planning (see strategy-planning)

---

## Key Models & Frameworks

**Mental models you apply in this domain:**

- **Governance as enabler, not constraint**: Governance should clarify decision authority and reduce drift, not create bureaucracy. A good governance rule enables faster, more confident decisions; a bad rule creates paralysis.
- **Distributed authority with alignment**: Not all decisions need central approval. Governance distributes authority (LLMs can do X autonomously) while maintaining alignment with values and priorities.
- **Accountability through transparency**: Governance is only effective if decisions and rules are documented and visible. Hidden governance rules breed distrust and error.
- **Evolution, not perfection**: Governance v1 is incomplete and will evolve. Better to have imperfect governance that works in practice than perfect governance that's too heavy to follow.
- **Values-first policy**: Policy should flow from core values and principles, not from abstract best practice. Policies that conflict with actual values will be ignored or circumvented.

**Key concepts:**
- **Sovereignty and consent**: In any governing body (family, organization, personal), people need to understand the rules, have input into them, and consent to follow them. Rule-by-fiat fails.
- **Explicit deferral**: Good governance explicitly says what is NOT being governed (yet), so people know the boundaries. "Not yet governed" is clearer than silent gaps.
- **Enforcement consistency**: Rules are only credible if enforced consistently. Inconsistent enforcement destroys trust in governance faster than having no rules.

---

## Operating Rules & Decision Protocols

**Rules that govern work in this domain:**

1. **All governance rules must be documented and indexed** — Personal-os governance is documented in docs/governance/; nonprofit policies in organizational systems. Undocumented rules are not governance, they're confusion.

2. **Governance changes follow protocol** — Any new governance rule must be: documented in GOVERNANCE-RULES.md, implemented in enforcement code (if active), logged in GOVERNANCE-CHANGE-LOG.md, and justified in DECISIONS.md. Deliberate process, not ad-hoc rules.

3. **Governance is conservative and bounded** — Governance is slow to change and applies only to what it explicitly covers. Deferral is explicit. Creeping governance is a warning sign.

4. **Accountability requires visibility** — Governance rules are visible; decisions using those rules are documented. Hidden or informal governance creates injustice and resentment.

5. **Governance serves people, not process** — If a governance rule makes the system harder to use in real life, the rule is wrong, not the usage. Governance is judged by whether it enables better, more confident decisions.

**Decision protocol (if applicable):**

If proposing a new governance rule or policy:
1. Identify the problem: what decision drift or risk is this rule trying to prevent?
2. Define the rule narrowly: what is in scope? What is explicitly deferred?
3. Design enforcement: how will this rule be checked? Automated, convention-only, or manual?
4. Document with rationale: why does this rule matter? What values does it protect?
5. Plan for evolution: when and how will this rule be revisited and updated?
6. Log as governance decision: GOVERNANCE-RULES.md, GOVERNANCE-CHANGE-LOG.md, DECISIONS.md.
7. Communicate: make sure anyone affected by the rule understands it.

---

## Autonomy Boundaries

**Reference from autonomy-matrix.md:**

| Action Type | Autonomy | Notes |
|---|---|---|
| Analysis | AI ✓ | LLM can fully analyze governance questions and policy frameworks |
| Drafting/Proposals | AI → Review | LLM can draft governance rules and policy documents; Javier reviews before adoption |
| Execution | Human | Committing governance changes and enforcing policies are Javier's |
| Final Decision | Human | Governance and policy decisions are Javier's final call |

**What this means in practice:**

LLMs can analyze governance questions and propose rule improvements. LLMs can draft policy documents and governance frameworks. But execution (committing changes to governance files) and final decisions on what rules to enforce remain with Javier. Governance is foundational enough to require human judgment.

---

## Pipelines & Knowledge Ingestion

**Pipelines that feed this domain:**

- **Governance Evolution Pipeline** → Monitors governance changes needed, proposals, lessons learned; documents in docs/governance/
- **Policy Research & Best Practices Pipeline** → Ingests governance frameworks, nonprofit best practices, policy templates; stores in docs/knowledge-extracts/governance-policy/
- **Organizational Oversight Pipeline** → Tracks nonprofit board responsibilities, meeting notes, policy decisions; documents in _core/initiatives.md (nonprofit section)

**Knowledge sources:**

- Nonprofit governance best practices (BoardSource, governance literature)
- Organizational policy templates and frameworks
- Lessons from running personal-os governance
- Session-debrief learnings about what works

**Integration triggers:**

- Quarterly governance review: Check if current rules are being followed, if enforcement is consistent, if rules need refinement.
- When governance problem surfaces (e.g., rule is too heavy, leads to drift): Analyze and propose rule change.
- When nonprofit board needs policy update: Research relevant frameworks; propose policy.

---

## Related Skills & Workflows

**Meta-skills that apply here:**

- `internal-first-research.md` — Use when researching governance questions; check personal-os governance docs and nonprofit policies first.
- `session-debrief.md` — Any governance insight or policy learning should surface as durable takeaway.

**Domain-specific workflows:**

- /docs/workflows/governance-change-protocol.md (when created)
- /docs/workflows/nonprofit-policy-development.md (when created)

**Pipelines:**

- /docs/pipelines/knowledge-ingestion.md — For governance and policy research content

---

## Where to Look

**High-velocity reference for this domain:**

| What | Where |
|---|---|
| Active governance rules and rationale | docs/governance/GOVERNANCE-RULES.md |
| Governance change history | docs/governance/GOVERNANCE-CHANGE-LOG.md |
| Governance enforcement code | scripts/governance-check.py |
| Governance decisions and precedents | DECISIONS.md (entries with [governance]) |
| Nonprofit board policies and procedures | _core/initiatives.md (nonprofit section) |
| Governance research and frameworks | docs/knowledge-extracts/governance-policy/ (when created) |

---

## Quick Reference (Optional)

**Checklist for governance decisions in this domain:**

- [ ] Is this rule solving a real problem, or solving for theoretical concerns?
- [ ] How will this rule be enforced? (Automated, convention, manual?)
- [ ] What is explicitly deferred or out of scope?
- [ ] Have I documented the rule with rationale?
- [ ] Is this rule light enough to follow in real life?
- [ ] How will I know if this rule is working?
- [ ] When will I revisit and reconsider this rule?

---

*Domain-context files are living documents. Review quarterly or after major governance changes.*
