---
title: Software & Development
type: domain-context
audience: self
status: active
domain: software-development
last-updated: 2026-04-17
related:
  - /docs/domains/operations-systems.md
  - /docs/domains/learning-research.md
  - /docs/domains/strategy-planning.md
  - /_core/models.md
---

# Software & Development

Domain for software development, coding projects, AI tool integration, and technical learning.

---

## Purpose & Scope

**Why this domain matters:**

As a developer and AI tool user, software development is both a professional activity and a tool for system-building. This domain covers personal coding projects, LLM-assisted development, tool evaluation, and continuous learning in software architecture and AI. The personal-os itself is a software project in this domain.

**What is in scope:**
- Coding and software architecture decisions
- Tool evaluation and integration (programming languages, frameworks, AI tools)
- Technical learning and skill development
- LLM-assisted development patterns and best practices
- Code quality, testing, and documentation standards
- Open-source and reusable code libraries
- Automation and scripting
- DevOps, CI/CD, and deployment

**What is explicitly out of scope:**
- Professional software development for clients/employers (see professional-advisory)
- Research and writing about software (see learning-research)
- Business decisions about software products (see strategy-planning)
- Governance of development processes (see governance-policy)

---

## Key Models & Frameworks

**Mental models you apply in this domain:**

- **Code as documentation**: Good code is readable and self-documenting. Comments explain "why", not "what". If code is hard to understand, refactor it.
- **Technical debt compounds**: Small shortcuts accumulate into unmaintainable systems. Resist the urge to "ship dirty and fix later." Maintain code quality as you build.
- **Testing is design**: Writing tests forces you to think about inputs, outputs, and edge cases. Tests are not overhead; they're clarity on what the code should do.
- **Simplicity over cleverness**: The most complex solution is rarely the best one. Prefer readable, boring solutions over clever ones. Optimize for maintenance, not for showing off.
- **Reversibility in architecture**: Make architectural decisions reversible where possible. Lock-in to a particular pattern or technology is a cost. Build ramps and abstraction layers.

**Key concepts:**
- **AI as tool, not replacement**: LLMs are powerful for scaffolding, refactoring, and knowledge synthesis. But architectural decisions, code review, and quality gates require human judgment.
- **Learning through building**: The best way to learn software concepts is to build something real. Theory is useful, but application is where understanding happens.
- **Open formats and portability**: Default to technologies that are open, portable, and not tied to a single vendor. Git, Markdown, and standard libraries over proprietary tools.

---

## Operating Rules & Decision Protocols

**Rules that govern work in this domain:**

1. **All code changes must pass governance checks** — personal-os code (scripts/governance-check.py, .git/hooks/) must pass the governance test suite. Broken code blocks commits.

2. **Code review before deployment** — Any code that affects other systems (governance scripts, pipelines, automation) requires review before deployment. Personal scripts can be more informal.

3. **Documentation is not optional** — Code that does important work must be documented. At minimum: what does this do? How is it used? What are edge cases?

4. **Testing reduces surprises** — Code that processes important data or affects the system should have tests. Tests are cheaper than production failures.

5. **AI-assisted code is reviewed code** — If LLMs write or help write the code, Javier (or another human) reads and approves it. Generated code is not auto-trusted.

**Decision protocol (if applicable):**

If making an architectural decision or choosing technology:
1. Clarify the problem: what are we solving? What constraints matter? (Performance, portability, maintainability, learning value?)
2. Identify legitimate alternatives: what are 2-3 good options?
3. Evaluate against constraints: which option best satisfies the priorities?
4. Plan the migration path: if we change our mind later, how hard is it to switch?
5. Document the decision with rationale in DECISIONS.md or in code comments.
6. Plan for review: when will we revisit this decision and reconsider?

---

## Autonomy Boundaries

**Reference from autonomy-matrix.md:**

| Action Type | Autonomy | Notes |
|---|---|---|
| Analysis | AI ✓ | LLM can freely analyze code, architecture, and technical questions |
| Drafting/Proposals | AI ✓ | LLM can write code, scaffold projects, draft documentation |
| Execution | AI → Review | LLM can implement features (with governance checks); changes reviewed before deployment |
| Final Decision | Human | Architectural decisions and code review are Javier's |

**What this means in practice:**

LLMs have high autonomy in this domain. They can analyze technical questions, write and refactor code, scaffold projects. LLMs can implement features autonomously as long as governance checks pass. But architectural decisions (choosing technologies, designing systems) and final code review remain with Javier. LLM output should be treated as a draft or proposal, not as final code.

---

## Pipelines & Knowledge Ingestion

**Pipelines that feed this domain:**

- **Software Learning Pipeline** → Ingests coding tutorials, architecture patterns, AI development best practices; stores in docs/knowledge-extracts/software-development/
- **Tool Evaluation Pipeline** → Researches and evaluates new tools, frameworks, LLM services; documents findings and decisions
- **Code Library Pipeline** → Curates reusable code snippets, utilities, and boilerplate for common tasks

**Knowledge sources:**

- Software engineering literature and design patterns
- Open-source projects and community practices
- LLM documentation and AI development best practices
- Session learnings about what works and what doesn't

**Integration triggers:**

- When learning a new technology or pattern: Document in docs/knowledge-extracts/software-development/
- When a coding decision is made: Add entry to DECISIONS.md or code comments
- Quarterly: Review personal-os architecture and code quality; propose improvements

---

## Related Skills & Workflows

**Meta-skills that apply here:**

- `internal-first-research.md` — Use when researching technical questions; check docs/domains/software-development.md canon first, then external sources.
- `session-debrief.md` — Any architectural insight or learning should surface as durable takeaway.

**Domain-specific workflows:**

- /docs/workflows/code-review-checklist.md (when created)
- /docs/workflows/ai-assisted-development.md (when created)

**Pipelines:**

- /docs/pipelines/knowledge-ingestion.md — For ingesting software learning content

---

## Where to Look

**High-velocity reference for this domain:**

| What | Where |
|---|---|
| personal-os governance code | scripts/governance-check.py, .git/hooks/ |
| Code and architecture decisions | DECISIONS.md (entries with [architecture]) |
| Architectural patterns and models | _core/models.md (software section, when created) |
| Software learning and research | docs/knowledge-extracts/software-development/ (when created) |
| Tool evaluations and decisions | docs/knowledge-extracts/software-development/tools/ (when created) |
| Reusable code libraries and utilities | scripts/ (for personal-os utilities) |

---

## Quick Reference (Optional)

**Checklist for code and architectural decisions in this domain:**

- [ ] Does this code pass governance checks?
- [ ] Have I tested this code, or planned to test it?
- [ ] Is this code documented (what does it do, how is it used)?
- [ ] Is this an architectural decision that should be in DECISIONS.md?
- [ ] Have I considered reversibility? (Can we change our mind later?)
- [ ] Is this code human-readable and maintainable?
- [ ] Have I considered edge cases and failure modes?

---

*Domain-context files are living documents. Review quarterly or after major architectural changes.*
