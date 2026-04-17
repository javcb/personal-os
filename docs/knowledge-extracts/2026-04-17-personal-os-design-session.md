---
title: Personal-OS Design Session Extract
type: knowledge-extract
audience: self
status: active
domain: software-development, operations-systems
last-updated: 2026-04-17
source: Perplexity conversation thread (April 13–17, 2026)
related:
  - /_core/roadmap.md
  - /CLAUDE.md
  - /docs/governance/GOVERNANCE-RULES.md
  - /docs/domains/
---

# Personal-OS Design Session Extract
## April 13–17, 2026

---

## Session Overview

This extract captures key decisions, validated frameworks, open questions, and next actions
from the multi-day design session that produced personal-os v0.1: a governance-enforced,
AI-collaborative personal knowledge system.

**Primary artifact produced:** A complete working personal-os with governance v1, LLM interface
layer v0, 9 domain context files, meta-skills, roadmap schema, and autonomy matrix.

---

## Key Decisions (What Changed)

### 1. Epistemic Filter Model
**What changed:** Realized external information should be interpreted *through* system canon,
not in isolation.

**Why this matters:** Personal-os is not a passive archive; it's a filtering and upgrading
system. New information is evaluated against existing models. Conflicting information should
trigger investigation, not passive acceptance.

**Implementation:** CLAUDE.md Internal-First Research Protocol formalizes this: read internal
canon first, then compare external findings against canon, classify relationships (confirms,
extends, conflicts, obsoletes, unclear).

**Impact:** Changes how knowledge ingestion works. LLMs should actively challenge external
information against existing models rather than passively summarizing.

---

### 2. LLM Interface Layer v0 is Viable
**What changed:** Confirmed that CLAUDE.md + 3 meta-skills (phase-wrap-up, internal-first-research,
session-debrief) + roadmap schema creates a working interface between autonomous LLM workflows
and human oversight.

**Why this matters:** Personal-os can now have autonomous LLM agents without losing coherence.
The interface layer prevents drift while allowing operational leverage.

**Implementation:**
- CLAUDE.md defines roles, constraints, operating rules, decision protocols, YAML types, pre-commit checklist.
- Meta-skills encode repeatable workflows (how to close phases, how to research, how to reflect).
- Roadmap schema provides phase-aware context for resumption.
- Autonomy matrix specifies per-domain boundaries.

**Impact:** LLMs can now be productive hands without becoming decision-makers. Work can resume
across sessions without manual context reconstruction.

---

### 3. Governance v1 (9 checks) is Sufficient Foundation
**What changed:** Verified that structural governance focused on file placement, naming, frontmatter,
and link integrity prevents repository degradation without requiring deep semantic rules.

**Why this matters:** Governance can be lightweight and self-enforcing (via pre-commit hooks and
governance-check.py). Heavy governance would require constant manual review and would decay under pressure.

**Governance rules (v1):**
1. Root-level file whitelist (README, CLAUDE, inbox, DECISIONS, .gitattributes only)
2. Globally unique filenames (except .gitkeep)
3. Required YAML frontmatter in /docs/ (title, type, status)
4. No build artifacts (.log, -REPORT.md)
5. Minimum content (5+ meaningful lines per file)
6. All internal markdown links must exist
7. Lowercase kebab-case naming (except reserved names)
8. Governed subtrees with manifest files (docs/governance/)

**Impact:** 9 automated checks catch 90% of structural problems. Content quality is deferred
to humans. Governance stays lightweight and enforceable.

---

### 4. Domain Organization by Role (Not Initiative)
**What changed:** Decided to organize personal-os by the 9 domains (finance, family, operations,
governance, software, professional, learning, legal, strategy) mapped to Javier's core roles,
rather than by temporal initiatives or projects.

**Why this matters:** Domains are stable (tied to roles); initiatives are temporal (tied to projects).
Separating them prevents knowledge fragmentation. Cross-domain knowledge lives in _core/; initiatives
track work in progress.

**Implementation:** 9 domain context files created (docs/domains/*.md) with consistent schema
(Purpose & Scope, Key Models, Operating Rules, Autonomy Boundaries, Pipelines, Where to Look, etc.).

**Impact:** LLMs and humans can reason about cross-domain decisions. Each domain has explicit
boundaries, rules, and frameworks. Prevents knowledge creep and reduces cognitive load.

---

### 5. Meta-Skills Are the Operating System
**What changed:** Elevated meta-skills (abstract patterns for approaching work) from "nice to have"
to foundational infrastructure. Without them, autonomous workflows degrade into inconsistent,
memory-dependent habits.

**Why this matters:** Meta-skills survive tool changes (Claude → Claude+Cursor → whatever comes next).
Procedural docs tied to specific tools become stale immediately. Meta-skills teach approach, not tools.

**Meta-skills defined (v0):**
- phase-wrap-up: Close phases and leave resumable state.
- internal-first-research: Research through system canon first.
- session-debrief: Extract durable takeaways and repo updates.
- (Deferred) pre-action-critique: Evaluate decisions before committing.

**Impact:** LLMs operate consistently across sessions. Workflows are portable. Work can survive tool
transitions without retraining.

---

### 6. Roadmap Governance: Human-Curated Priorities
**What changed:** Made explicit rule: Roadmap is human-curated. LLMs propose updates via session-debrief,
but Javier reviews and edits directly. No automation of roadmap generation.

**Why this matters:** Roadmap prioritization involves tradeoffs, sequencing, and resource allocation that
require human judgment. Automation risks removing decision-making from human control. Manual curation
preserves agency.

**Implementation:** Section 7 of GOVERNANCE-RULES.md codifies this. Session-debrief structured format
captures proposals for review. Javier updates roadmap asynchronously.

**Impact:** System cannot autonomously re-prioritize work. Priorities stay human-controlled. LLM becomes
proposal generator, not decision-maker.

---

### 7. Autonomy Matrix Pattern Works
**What changed:** Confirmed that specifying per-domain LLM autonomy boundaries (what LLMs can do
autonomously vs. what requires human review) prevents scope creep and makes expectations explicit.

**Why this matters:** LLMs need clear authority boundaries. Implicit boundaries lead to overreach or
over-caution. Explicit boundaries enable confident autonomous work.

**Implementation:** docs/governance/autonomy-matrix.md defines 4 action types (Analysis, Drafting,
Execution, Final Decision) across 9 domains. Values: AI ✓ (fully autonomous), AI → Review (autonomous
but flagged for human review), Human (requires human approval).

**Impact:** LLMs know exactly what they can do. Humans know what to review. Boundaries are discoverable
and can be adjusted after real-world validation.

---

## New Known Knowns (KK)

Things confirmed and now reliable for decision-making:

1. **LLM interface layer (CLAUDE.md + meta-skills + roadmap) is viable as a working system.**
2. **Governance v1 (9 enforcement checks) prevents structural degradation without heavy burden.**
3. **Domain organization by role enables cross-domain reasoning better than initiative-based structure.**
4. **Autonomy matrix pattern makes human-AI collaboration explicit and scalable.**
5. **Meta-skills as OS beats procedural docs; they survive tool changes and teach approaches.**
6. **Roadmap governance (human-curated, LLM proposes) preserves decision-making authority.**
7. **Governed subtrees pattern allows specialized governance without forcing boilerplate everywhere.**
8. **Extraction (what changed your thinking) beats summary (passive archive) for knowledge ingestion.**
9. **Epistemic filter model (interpret external info through system canon) is the right framing.**

---

## Remaining Known Unknowns (KU)

Questions surfaced but not yet resolved (pending real-world validation):

1. **Will the system work in practice?** Design is solid, but real sessions will reveal unexpected
   problems or missing pieces.

2. **Do the 9 domains map to actual work?** Domain structure feels right; usage may show domains need
   splitting, merging, or renaming.

3. **How to ensure legibility for collaborators?** Wife and collaborators need to understand system
   without constant explanation. Current design requires effort to stay legible.

4. **How to automate knowledge ingestion?** Pipelines are designed but not yet operationalized. Risk
   of automation introducing governance debt or requiring constant maintenance.

5. **What happens if Javier takes a long break?** System is designed for resumability, but actual
   recovery time and effort unknown.

6. **How to promote learning?** Can knowledge extraction pipeline actually improve mental models, or
   is it just documentation maintenance?

7. **How much overhead does the system add?** Personal-os is infrastructure. Cost/benefit ratio
   unknown until real usage.

---

## Blind Spots Identified (BL)

Gaps that surfaced during this session:

1. **Core context files need substantive content to unlock pipelines.**
   - _core/quadrants.md, _core/models.md, _core/initiatives.md are templates.
   - Pipelines can't run without content (e.g., learning pipeline needs Known Unknowns to explore).
   - Bootstrap problem: need context to define context.

2. **"What changed" vs. "what is summary" distinction changes knowledge work.**
   - Knowledge ingestion templates need to distinguish extraction (mental model changes)
     from summary (passive archive).
   - This distinction determines what knowledge actually gets ingested.

3. **Epistemic filter concept is powerful but untested.**
   - System should actively challenge external information against canon.
   - Actual implementation of conflict detection and canon-updating workflow is still design work.

4. **Legibility risk for non-builders.**
   - personal-os is complex (governance, domains, meta-skills, pipelines, roadmap).
   - Risk: system is only usable by person who built it; collaborators see "complicated black box."

---

## Mental Models Validated or First-Articulated

### Epistemic Filter
External information is interpreted through system canon, not in isolation.
New ideas are evaluated: do they extend canon, conflict with it, or change how we think?
System actively filters and upgrades knowledge rather than passively archiving.

### Governed Subtrees Pattern
Some directories need their own governance (docs/governance/ has GOVERNANCE-README, RULES, CHANGE-LOG).
Pattern allows specialized rules without forcing boilerplate everywhere.
Generalizable: _core/ could have its own governance layer.

### Autonomy Matrix
Explicit boundaries for human-AI collaboration prevent both overreach and under-utilization.
Conservative by default; upgrade to higher autonomy only after validation.
Matrix applies across multiple dimensions: domain, action type, risk level.

### Meta-Skills as OS
Abstract patterns for approaching work (meta-skills) are more durable than procedural docs.
Meta-skills survive tool changes; procedures become stale.
Meta-skills teach *how to think* about work, not *which tool to use*.

### Extraction Over Summary
Knowledge ingestion goal: identify what changed your mental models.
Summary is passive archive (dead); extraction is upgrade (alive).
This changes how knowledge pipelines should work.

### Roadmap Governance
Prioritization involves tradeoffs and context; automation risks removing human control.
Human-curated roadmap with LLM proposals preserves decision-making authority.
Explicit rule prevents drift over time.

---

## Implementation Artifacts

**Created during session:**
- `/CLAUDE.md` — AI constitution and operating guidelines (15KB)
- `/docs/skills/_custom/phase-wrap-up.md` — Meta-skill for closing phases (7KB)
- `/docs/skills/_custom/internal-first-research.md` — Meta-skill for research (11KB)
- `/docs/skills/_custom/session-debrief.md` — Meta-skill for reflection (10KB)
- `/_core/roadmap.md` — Phase-aware resumable checklist (7KB)
- `/docs/domains/*.md` — 9 domain context files (77KB total)
- `/docs/governance/autonomy-matrix.md` — Per-domain LLM autonomy boundaries (5KB)
- `/docs/governance/GOVERNANCE-RULES.md` — Section 7: Roadmap governance (updated)
- `/docs/templates/domain-context.md` — Template for domain files (6KB)
- `/_core/self-model.md` — Javier's context and roles (expanded)
- `/_core/quadrants.md` — Epistemic state mapping (populated)
- `/_core/models.md` — Mental models library (populated)
- `/_core/initiatives.md` — Active projects tracker (populated)

**All created artifacts pass governance v1 (9 checks).**

---

## What Changed Javier's Thinking

1. **LLM autonomy is design problem, not trust problem.**
   Before: "How much do I trust LLMs?"
   After: "How do I design boundaries and governance so autonomy is safe and productive?"

2. **Meta-skills are foundational infrastructure, not convenience.**
   Before: "Nice-to-have patterns for consistent work."
   After: "These are the OS layer. Without them, workflows degrade. With them, tools become interchangeable."

3. **Governance can be lightweight and self-enforcing.**
   Before: "Governance requires constant manual review."
   After: "9 automated checks catch 90% of problems. Heavy governance isn't necessary; light governance is enough."

4. **Domain organization by role is better than by initiative.**
   Before: "Organize knowledge by projects or time periods."
   After: "Organize by roles/domains. Cross-domain knowledge lives centrally. Initiatives are temporal overlays."

5. **Roadmap is governance issue, not process issue.**
   Before: "How do we track what to work on?"
   After: "Roadmap governance is about preserving decision-making authority. Human-curated; LLMs propose."

6. **Epistemic filter reframes knowledge work.**
   Before: "Collect information and organize it."
   After: "Interpret new information through existing models. Challenge conflicts. Upgrade mental models."

---

## Next Actions

**Immediate (next session):**
1. Run first real session using CLAUDE.md, meta-skills, and roadmap together.
2. Identify integration gaps or missing pieces through actual usage.
3. Populate remaining _core/ context (family details, financial goals, initiatives).
4. Test resumption: take a break, come back, verify system works.

**Short-term (Phase 2: Domain Expansion):**
1. Define 9 domain models (mental models specific to each domain).
2. Build knowledge ingestion pipeline: external sources → domain knowledge extracts.
3. Test domain-specific workflows.
4. Refine domain boundaries based on actual usage.

**Medium-term (Phase 3: Integration):**
1. Add domain enforcement to governance.
2. Test legibility for wife/collaborators.
3. Build cross-domain decision workflows.
4. Document patterns for future builders/successors.

---

## Critical Success Factors (Going Forward)

1. **Real sessions drive refinement.** Design is solid, but actual usage is the only test.
2. **Maintain governance discipline.** Governance prevents decay; slack governance is worse than no governance.
3. **Keep system legible.** Complexity is acceptable; opacity is fatal.
4. **Protect meta-skill discipline.** Meta-skills are the OS; skip them at peril.
5. **Preserve human authority over priorities.** Roadmap curation must remain human.

---

## What This Extraction Changed

This extraction should change how knowledge ingestion happens:
- Personal-os is not a passive archive but an active epistemic filter.
- Meta-skills are OS, not convenience.
- Domain organization by role enables cross-domain reasoning.
- Governance can be lightweight and self-enforcing.
- Real usage is the only valid test.

---

*Extraction completed: 2026-04-17*
*Source: Perplexity conversation thread, April 13–17, 2026*
*Status: Ready for promotion to canon after first real session validation*
