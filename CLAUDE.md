---
title: personal-os AI Constitution
type: reference-pointer
audience: ai
status: active
---

# CLAUDE.md — AI Operating Guidelines for personal-os

Read this entire file before taking any action in this repo.

---

## What Is personal-os?

**personal-os** is Javier's personal operating system and second brain.

It is an **epistemic filter**: external information should be interpreted *through* this system's existing models, decisions, and canon — not in isolation. When you encounter new ideas, data, or questions, the first step is always to check what this repo already knows, has decided, or has explicitly deferred.

The architecture (governance + meta-skills + pipelines) is designed to make the system **self-sustaining and consistent over time**. Governance enforces structural hygiene. Meta-skills encode repeatable operating patterns. Pipelines automate knowledge ingestion. Together, they allow the system to grow stronger without degrading.

Your role as an AI working in this repo: Be the system's operational hands. Think *through* its models. Propose changes transparently. Preserve its integrity.

---

## Files to Read Before Doing Anything

Before making any structural changes, proposing major decisions, or adding durable content, load these files:

1. **README.md** — overall manifest of what this repo contains.
2. **CLAUDE.md** — this file. You are reading it now.
3. **DECISIONS.md** — structural decisions and history. Shows what was decided and why.
4. **docs/governance/GOVERNANCE-RULES.md** — current governance rules. You must obey these unconditionally.
5. **_core/roadmap.md** (if it exists) — current phase and prioritized next actions.

After reading these, load any relevant domain files, skill files, or pipeline definitions that relate to your task.

**Why?** These files establish the system's current state, constraints, and priorities. Skipping them risks proposing work that conflicts with existing decisions or duplicates effort already deferred.

---

## Internal-First Research Protocol

For any non-trivial question, decision, analysis, or learning task, follow this protocol:

### Step 1: Identify the Question Type
Classify the question: decision? architecture? learning? refactor? process design? domain expansion?

### Step 2: Locate and Read Relevant Internal Files First
Before consulting external sources, search this repo for:

- **_core/self-model.md** — Javier's context, roles, and priorities.
- **_core/quadrants.md** — Known unknowns (KK), unknown unknowns (UK), known unknowables, etc.
- **_core/models.md** — Mental models and cognitive frameworks already adopted.
- **docs/domains/\*.md** — Domain-specific canon in the relevant area.
- **docs/pipelines/\*.md** — Process definitions and automated workflows.
- **docs/skills/\*.md** — Operating skills and meta-skills (how to approach work).
- **docs/governance/\*.md** — Structural rules and design decisions.
- **DECISIONS.md** — Structural choices and their rationale.

### Step 3: Compare Against Internal Canon
After reading internal sources, if you consult external sources (web, LLM background knowledge), classify your findings:

- **confirms canon** — new finding aligns with existing decision or model.
- **extends canon** — new finding adds nuance or depth without contradicting.
- **conflicts with canon** — new finding contradicts something repo already decided.
- **obsoletes canon** — new finding makes an existing decision outdated.
- **unclear / needs human judgment** — finding is relevant but doesn't fit above categories.

### Step 4: Propose, Don't Silently Change
When canon needs updating based on new research:

Do **not** arbitrarily edit existing files.

Instead, propose the change using the **session-debrief format** (see "How to End a Session" below). This creates a record of why the change was made and allows human review before committing.

**Note:** This protocol corresponds to the `internal-first-research` meta-skill. Use it for any non-obvious question.

---

## Where to Put Things

Before creating a file, follow this decision tree:

### 1. Unsure Where It Goes?
→ **Append to inbox.md** with a tag: `[model]`, `[quadrant:BL]`, `[initiative:name]`, `[session:date]`, or other label.  
**Stop here.** Never invent a new file to hold an unprocessed thought.

### 2. Durable Principle or Concept?
→ **docs/domains/** or **docs/architecture/** (domain canon).  
Use frontmatter: `type: reference`, `type: explanation`, or `type: mental-model`.

### 3. How-To or Procedure?
→ **docs/workflows/** or **docs/skills/**.  
Use frontmatter: `type: how-to`, `type: sop`, or `type: tutorial`.

### 4. Meta-Skill or Operating Pattern?
→ **docs/skills/_custom/**.  
Use frontmatter: `type: meta-skill`.

### 5. Structural Rule or Governance Change?
→ **docs/governance/** and **GOVERNANCE-CHANGE-LOG.md**.  
Update `GOVERNANCE-RULES.md` with the rule and `scripts/governance-check.py` with enforcement (if active).

### 6. Architecture Decision?
→ **DECISIONS.md** (one-line entry per decision).  
Format: `[YYYY-MM-DD]: [Decision made]. Reason: [why].`

### 7. Ingested External Content?
→ **docs/knowledge-extracts/[domain]/** with appropriate template.  
Use frontmatter: `type: knowledge-extract`.

### 8. Personal Context or Active Work?
→ **_core/** (context vault). Examples:
  - **_core/self-model.md** — roles, strengths, priorities.
  - **_core/initiatives.md** — active projects.
  - **_core/models.md** — mental models and frameworks.
  - **_core/roadmap.md** — next-phase execution.

**Key principle:** Propose changes (snippets, diffs, or suggestions), don't arbitrarily invent new locations outside this tree.

---

## Governance Is Non-Negotiable

The repo enforces structural rules via:
- **scripts/governance-check.py** — automated checks on every commit.
- **.git/hooks/pre-commit** and **.git/hooks/pre-push** — enforcement gates.

### What You Cannot Do

LLMs working here must **not**:

- Create root-level `.md` files except: `README.md`, `CLAUDE.md`, `inbox.md`, `DECISIONS.md`, `.gitattributes`.
- Create duplicate filenames anywhere in the repo (except `.gitkeep`).
- Violate governed subtree manifest rules (docs/governance/ must have GOVERNANCE-README.md, GOVERNANCE-RULES.md, GOVERNANCE-CHANGE-LOG.md).
- Add `.md` files to `docs/` without YAML frontmatter (title, type, status required).
- Commit build artifacts (`.log`, `-REPORT.md` files).
- Introduce broken internal markdown links.
- Name files using CamelCase or snake_case (use lowercase kebab-case instead, except reserved names).

### If Governance Fails

The response is always: **Fix the structure to comply with the rules.**

Never propose weakening governance. Governance is the system's immune system.

If a rule feels wrong, propose a change to `GOVERNANCE-RULES.md` (and document it in `GOVERNANCE-CHANGE-LOG.md`). But follow the current rules while they stand.

---

## Meta-Skills and Pipelines

The system's behavior emerges from two layers:

### Meta-Skills (Operating System)
These are portable, tool-agnostic patterns for how to approach work:

- **pre-action-critique** — Evaluate a decision before committing.
- **internal-first-research** — Research using this repo's canon first.
- **session-debrief** — Reflect and capture learnings after a session.
- **phase-wrap-up** — Close a work phase and leave a resumable state.

Use these skills in every session. They are documented in **docs/skills/_custom/**.

### Pipelines and Domain Skills (Applications)
These compose meta-skills to solve specific problems:

- Knowledge ingestion pipelines (external → canon).
- Decision-making workflows.
- Content generation pipelines.
- Domain-specific processes.

When doing meaningful work:

1. Load the relevant meta-skill file.
2. Follow its steps explicitly.
3. Produce the required outputs (debrief items, wrap-up summaries, etc.).
4. Use those outputs to drive repo updates.

---

## How to End a Session

Whenever a session has done meaningful work, perform both a **session-debrief** and (if applicable) a **phase-wrap-up**.

### Session-Debrief (Always)

At the end of every session, output:

```
## Session Debrief — [Date]

[TYPE: model]: [summary]
  Why durable: [reason]
  Suggested destination: [file path]
  Relation to canon: [confirm/extend/conflict/obsolete/unclear]

[TYPE: skill]: [summary]
  Why durable: [reason]
  Suggested destination: [file path]
  Relation to canon: [confirm/extend/conflict/obsolete/unclear]

[TYPE: decision]: [summary]
  Why durable: [reason]
  Suggested destination: [DECISIONS.md]
  Relation to canon: [confirm/extend/conflict/obsolete/unclear]

[TYPE: governance-candidate]: [summary]
  Why durable: [reason]
  Suggested destination: [docs/governance/ or GOVERNANCE-RULES.md]
  Relation to canon: [confirm/extend/conflict/obsolete/unclear]

[TYPE: pipeline]: [summary]
  Why durable: [reason]
  Suggested destination: [docs/pipelines/]
  Relation to canon: [confirm/extend/conflict/obsolete/unclear]

[TYPE: inbox]: [summary]
  Tags: [tag1, tag2]
  Suggested destination: [inbox.md]
```

Each item captures something worth keeping. The suggested destination guides where it belongs next (during weekly review or next session).

### Phase-Wrap-Up (When Closing a Phase)

If you are pausing or closing a major work area or phase, also run the **phase-wrap-up** skill (see **docs/skills/_custom/phase-wrap-up.md**). Output:

```
## Phase Wrap-Up

Phase Being Closed: [name]
What We Completed: [list]
Why We're Stopping Here: [reason]
Remaining Work: [triaged list]
Files Updated: [list]
Re-entry Point: [exact next action]
Suggested Next Prompt: [template for resumption]
```

### Why This Matters

These outputs are the **primary mechanism** by which the system:
- Captures insights before they evaporate.
- Stays resumable across sessions.
- Accumulates knowledge without degrading.
- Allows human review and prioritization.

**Do not skip these.** They are the connective tissue.

### Example: Session Debrief + Roadmap Update

This example shows how a session-debrief proposal flows into _core/roadmap.md updates.

**Session-Debrief Output (from a hypothetical session):**

```
## Session Debrief — 2026-04-20

- [TYPE: decision]
  - Summary: Decided to defer pre-action-critique meta-skill to v1; current 3 meta-skills (phase-wrap-up, internal-first-research, session-debrief) are sufficient foundation.
  - Why durable: Establishes boundary for v0 scope; prevents scope creep; allows validation without overcomplicating.
  - Suggested destination: DECISIONS.md
  - Relation to canon: confirm (aligns with deferred items in _core/roadmap.md and governance backlog).

- [TYPE: process]
  - Summary: Discovered that roadmap updates should always flow through session-debrief, never direct LLM edits.
  - Why durable: Prevents accidental inconsistency; ensures Javier reviews all priorities; maintains human control.
  - Suggested destination: docs/skills/_custom/roadmap-integration.md or CLAUDE.md "Example" section.
  - Relation to canon: extends canon (clarifies LLM interface pattern).
```

**How Javier would update _core/roadmap.md based on this debrief:**

1. The first debrief item (decision) → Already captured in _core/roadmap.md "Explicitly Deferred" section; nothing to update.
2. The second debrief item (process) → Documentation note for future; no roadmap change needed; could update CLAUDE.md examples (which we did).

If the debrief had proposed moving a task from "In Progress" to "Completed," Javier would update _core/roadmap.md accordingly.

---

## YAML Type Registry

Every .md file in docs/ requires frontmatter with at minimum:
title, type, status.

Valid values for `type`:

| Value | Use for |
|---|---|
| tutorial | Learning-oriented, step by step |
| how-to | Task-oriented, goal-driven |
| reference | Look-up content, not narrative |
| explanation | Concept-oriented, understanding-focused |
| mental-model | Reusable cognitive framework |
| sop | Standard operating procedure |
| reference-pointer | Points to external authoritative source |
| context | Background/situational awareness |
| meta-skill | A skill about how to use skills |
| pipeline | Trigger → output workflow definition |
| knowledge-extract | Ingested content from external material |

---

## The 5-Stage Decision Protocol

Before committing to any structural decision, run these stages:

1. **Inform** — What do I need to know before evaluating this?
2. **Compare** — What are the legitimate alternatives?
3. **Critique** — What is the strongest argument against the leading option?
4. **Connect** — What else in this repo does this decision touch?
5. **Commit or Pause** — Is there one question that would change everything?

If yes to Stage 5: pause and surface the question.
If no: commit and log it in DECISIONS.md.

---

## Pre-Commit Checklist

Run this before staging any commit:

- [ ] Run: `python3 scripts/governance-check.py` — all checks must pass.
- [ ] Fix all governance violations before committing.
- [ ] Run a session-debrief to capture learnings and durable insights.
- [ ] If closing a work phase, run a phase-wrap-up.
- [ ] Append one line to DECISIONS.md for every structural decision made.
- [ ] Confirm no new files were created at root level (except allowed files).
- [ ] Confirm no duplicate filenames were introduced.
- [ ] Commit with a clear, descriptive message.

---

## The inbox.md Rule

**When in doubt: inbox.md. Always.**

inbox.md is append-only. Never organize at capture time.
Never create a new file to hold an unprocessed thought.
Weekly review decides permanent home.

Valid inbox tags:
- [model] — reusable mental framework
- [quadrant:BL] — unknown unknown surfaced
- [initiative:name] — project-specific note
- [session:date] — from an LLM conversation

---

## What You Must Never Do

- **Create .md files at root** (except README.md, CLAUDE.md, inbox.md, DECISIONS.md, .gitattributes).
- **Create a file without checking if it already exists first.** Run `find . -name "filename.md"` to check.
- **Skip session-debrief and phase-wrap-up.** These are non-negotiable for meaningful work.
- **Skip the governance check.** Always run `python3 scripts/governance-check.py` before proposing any commit.
- **Auto-populate _core/ files.** Those are chisel work, human-written only. Propose changes; don't edit directly.
- **Delete any file.** Deprecate using `status: deprecated` and `updated-by: [new file]` fields instead.
- **Make a structural decision without logging it in DECISIONS.md.**
- **Propose governance changes without updating GOVERNANCE-CHANGE-LOG.md.**

---

## Tone, Style, and Expectations

Write content for this repo as if it will outlive any single session:

- Be **explicit**. Prefer clarity over brevity.
- Be **durable**. Prefer structured, reusable patterns over ad-hoc solutions.
- Be **humble about change**. Propose updates via session-debrief; don't silently edit canon.
- Be **obedient to governance**. The rules exist for a reason.
- Be **kind to future-you and future-LLMs**. Leave breadcrumbs, document stopping points, index everything.

---

*Last updated: 2026-04-15*
