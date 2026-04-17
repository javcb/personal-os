---
title: Operations & Systems
type: domain-context
audience: self
status: active
domain: operations-systems
last-updated: 2026-04-17
related:
  - /docs/domains/family-parenting.md
  - /docs/domains/governance-policy.md
  - /docs/domains/software-development.md
  - /docs/domains/strategy-planning.md
  - /_core/roadmap.md
---

# Operations & Systems

Domain for designing and maintaining personal, household, and work systems, processes, and automation.

---

## Purpose & Scope

**Why this domain matters:**

As an operator and builder, systems thinking is foundational. This domain covers the personal-os itself, household operations, workflows, automation, and any repeatable process that affects daily life or work. Good systems reduce friction and cognitive load; bad systems compound problems. This is where "how do we do things" gets designed and maintained.

**What is in scope:**
- personal-os architecture, governance, and evolution
- Household operations (budgeting systems, chore systems, calendaring, meal planning)
- Workflow automation and tooling
- Documentation and knowledge management
- Decision-making processes and protocols
- Information systems and backup/recovery
- Time management and scheduling
- Task and project organization

**What is explicitly out of scope:**
- Family relationship dynamics (see family-parenting)
- Professional systems you don't own (your employer's systems; see professional-advisory)
- Technical implementation details (see software-development)
- Strategic planning at the enterprise level (see strategy-planning)

---

## Key Models & Frameworks

**Mental models you apply in this domain:**

- **Systems thinking**: Every system has inputs, processes, outputs, and feedback loops. Optimize the system, not just individual components. Understand trade-offs and unintended consequences.
- **Friction and consistency**: Friction in a system compounds; small frictions become avoidance become system failure. Design systems that are easy to use consistently, not systems that are "perfect in theory but impossible in practice."
- **Reversibility and optionality**: Good systems preserve optionality and reversibility. Lock-in to tools, formats, or processes is a cost. Default to open, portable formats; avoid vendor lock-in.
- **Automation as clarity**: Automate not for speed, but for consistency and clarity. If something is important enough to automate, it's important enough to document. Automation = documented process.
- **Seasonal systems**: Systems need different modes in different seasons. Parenting load varies by school year; work varies by season; energy varies. Systems should accommodate seasonal variation, not fight it.

**Key concepts:**
- **Governance as immune system**: Rules exist to prevent degradation. Governance is not bureaucracy; it's system health.
- **Resilience over optimization**: A system that degrades gracefully under stress is better than one that is optimized for ideal conditions but fragile.
- **Documentation as design**: If you can't document a process, you don't understand it well enough. Documentation is clarity.

---

## Operating Rules & Decision Protocols

**Rules that govern work in this domain:**

1. **All systems must pass governance checks** — personal-os has formal governance. Any new system or process added to the repo must comply with structure rules (naming, frontmatter, organization, links).

2. **Prefer portable formats and open tools** — Default to Markdown + Git, free or self-hosted tools, and formats that don't require subscriptions or vendor lock-in. "What if the tool disappears?" is a design question.

3. **Document before automating** — Don't automate a process you haven't documented. Documentation is the specification. Automation is the implementation.

4. **Validate systems in practice, not theory** — Live in the system for a season before optimizing it. Theoretical systems often don't survive contact with real life. Adjust based on actual usage.

5. **Systems changes are governance decisions** — Adding new directories, changing naming conventions, or restructuring processes requires a DECISIONS.md entry. System architecture is durable and affects everyone using the system.

**Decision protocol (if applicable):**

If redesigning a system or adding a new operational process:
1. Map the current system: inputs, process, outputs, friction points.
2. Define what "better" means: reduced friction? Faster? More consistent? Easier to maintain?
3. Prototype the new system on a small scale or in a limited time window.
4. Document the new process before deploying it widely.
5. Validate with actual usage; iterate based on real feedback, not theoretical concerns.
6. Document the decision and rationale in DECISIONS.md or GOVERNANCE-CHANGE-LOG.md.
7. Plan for periodic review: systems that work at scale S1 may not at scale S2.

---

## Autonomy Boundaries

**Reference from autonomy-matrix.md:**

| Action Type | Autonomy | Notes |
|---|---|---|
| Analysis | AI ✓ | LLM can fully analyze system design, process flows, and operational bottlenecks |
| Drafting/Proposals | AI → Review | LLM can draft process docs and system proposals; Javier reviews for feasibility and alignment |
| Execution | AI → Review | LLM can implement system changes (create docs, refactor); changes reviewed before deployment |
| Final Decision | Human | Structural decisions and system architecture choices are Javier's |

**What this means in practice:**

LLMs can freely analyze this domain and propose systems improvements. LLMs can draft operational docs and system designs. LLM can execute changes under governance (creating new files, refactoring structure) and flag them for review. But final decisions on system direction and architectural choices remain with Javier.

---

## Pipelines & Knowledge Ingestion

**Pipelines that feed this domain:**

- **System Design & Improvement Pipeline** → Captures system design patterns, operational learnings, process templates; stores in docs/pipelines/
- **Governance & Architecture Pipeline** → Tracks governance rules, architectural decisions, system changes; documents in docs/governance/ and DECISIONS.md
- **Tool & Automation Research Pipeline** → Evaluates tools and automation opportunities; ingests to docs/knowledge-extracts/operations-systems/

**Knowledge sources:**

- Systems thinking literature (theory)
- Personal operational experience (practice)
- Other well-designed systems in open-source and other domains (inspiration)
- Session-debrief learnings about what works and what doesn't (validation)

**Integration triggers:**

- When a process becomes painful or error-prone: Analyze via internal-first-research; propose system redesign.
- Quarterly: Review personal-os governance and architecture; propose refinements.
- When learning from external systems: Document in docs/knowledge-extracts/operations-systems/

---

## Related Skills & Workflows

**Meta-skills that apply here:**

- `internal-first-research.md` — Use when analyzing operational problems or learning from other systems.
- `session-debrief.md` — Any system improvement or operational learning should surface as durable takeaway.
- `phase-wrap-up.md` — Use when closing a project or redesign cycle to document what worked.

**Domain-specific workflows:**

- /docs/workflows/system-design-protocol.md (when created)
- /docs/workflows/governance-change-process.md (when created)

**Pipelines:**

- /docs/pipelines/knowledge-ingestion.md — For ingesting content about systems and operations

---

## Where to Look

**High-velocity reference for this domain:**

| What | Where |
|---|---|
| Current system architecture and design | README.md, _core/roadmap.md |
| Governance rules and enforcement | docs/governance/GOVERNANCE-RULES.md |
| Structural decisions and rationale | DECISIONS.md |
| personal-os implementation and scripts | scripts/governance-check.py, .git/hooks/ |
| System design patterns and templates | docs/templates/, docs/pipelines/ (when created) |
| Operational workflows and procedures | docs/workflows/ (when created) |

---

## Quick Reference (Optional)

**Checklist for systems decisions in this domain:**

- [ ] Is this a documentation/governance decision? (If yes: DECISIONS.md entry required)
- [ ] Does this system pass governance checks?
- [ ] Have I documented the process before automating it?
- [ ] Have I tested this in practice, not just theory?
- [ ] Is this reversible or difficult to unwind? (If irreversible: extra deliberation required)
- [ ] Does this introduce vendor lock-in or non-portable formats? (If yes: reconsider)
- [ ] How will I monitor this system for degradation or unintended consequences?

---

*Domain-context files are living documents. Review quarterly or after major operational changes.*
