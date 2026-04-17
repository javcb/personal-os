---
title: Roadmap
type: context
status: active
last-updated: 2026-04-15
current-phase-name: LLM Interface Layer v0 Implementation & Validation
---

# Roadmap

Live, resumable checklist. Single source of truth for phase-aware project progress.

> **Returning after time away?** Read this roadmap first to see current phase, next priorities, blockers, and re-entry breadcrumbs.

---

## Current Phase

**Phase Name:** LLM Interface Layer v0 Implementation & Validation  
**Status:** in-progress  
**Started:** 2026-04-10  
**Target Completion:** 2026-04-20  
**Rationale:** Complete the LLM operating layer (CLAUDE.md + 3 meta-skills + roadmap schema) so LLMs can operate autonomously while respecting governance. This unblocks real-world testing and enables feedback loops.

### Completed in This Phase
- [x] **Governance v1 Foundation** — 9 enforcement checks, governed subtrees pattern, repository immune to structural degradation
- [x] **CLAUDE.md** — AI constitution with governance rules, file placement tree, internal-first-research protocol, how to end sessions
- [x] **phase-wrap-up meta-skill** — formalize phase transitions, document stopping points, leave resumable re-entry
- [x] **internal-first-research meta-skill** — operationalize research protocol (repo first, then external)
- [x] **session-debrief meta-skill** — extract durable takeaways, structured repo-update proposals
- [x] **_core/roadmap.md schema design** — current phase, next phase queue, blockers, re-entry breadcrumbs, deferrals
- [x] **_core/roadmap.md created** — populated with current state and next priorities
- [x] **CLAUDE.md examples** — added "Example: Session Debrief + Roadmap Update" showing integration

### In Progress
- [ ] Run a real session using all meta-skills + roadmap together to validate integration and identify gaps

### Known Blockers or Dependencies
- None. All governance blocks resolved. Ready to validate in practice.

---

## Next Phase (Prioritized Queue)

**Phase Name:** Domain Expansion & Knowledge Ingestion  
**Estimated Start:** 2026-04-21  
**Rationale:** With the LLM interface layer stable, expand into specific domains (finance, operations, product, etc.) and build knowledge ingestion pipelines. This makes personal-os domain-aware and prevents context loss.

### Priority 1 (First)
- [ ] Define primary domains (finance, operations, product, strategy, etc.)
- [ ] Create domain-specific canon in docs/domains/
- [ ] Build knowledge-ingestion pipeline (external sources → docs/knowledge-extracts/)
- [ ] Create first domain model and add to _core/models.md

### Priority 2 (Then)
- [ ] Test knowledge-ingestion pipeline with real external sources
- [ ] Refine domain boundaries based on actual Javier use cases
- [ ] Build feedback loop: session-debrief proposes new knowledge → pipeline ingests
- [ ] Document domain-specific workflows in docs/workflows/

### Priority 3 (After that)
- [ ] Add domain enforcement to governance (prevent orphan docs)
- [ ] Create domain-specific meta-skills
- [ ] Build first real-world project using LLM interface + domains

---

## Explicitly Deferred (Not Doing Now)

### Deferred to "LLM Interface v1"
- **pre-action-critique meta-skill** — Valuable for major decisions, but deferred until current patterns stabilize. Will add after 5–10 real sessions.
- **Roadmap as governed subtree** — Would add ROADMAP-README.md with versioning rules; better to wait and validate pattern first.
- **Multi-track roadmaps** — Tempting for parallel domains; premature for v0. Single roadmap is sufficient.

### Deferred / Under Discussion
- **Automated roadmap generation from debrief** — Keep roadmap human-curated so Javier retains control.
- **Roadmap UI/dashboard** — Text file is sufficient for v0; web interface later if needed.
- **Authorship tracking in debrief** — Not required for v0; can add metadata later.
- **Content-level governance rules** — Parked in governance backlog (Phase 0 decision).

### Open Questions / Decisions Awaiting
- **Domain vs. Initiative organization:** → RESOLVED 2026-04-17. Organize by domain. See DECISIONS.md. Domain files in docs/domains/ are primary context layer; initiatives tracked in _core/initiatives.md; _core/ holds cross-domain knowledge.
- **Feedback loop automation:** How much of session-debrief → roadmap → repo update should be automated vs. human-reviewed? → Validate through real sessions first.

---

## Re-entry Breadcrumbs

**Last Session Left Off At:**  
Completed LLM interface layer v0 design and implementation. All meta-skills created and in place. CLAUDE.md comprehensive and validated. _core/roadmap.md created with new schema and populated. Ready to use in practice.

**Immediately Resume With:**  
Run a real, full session using CLAUDE.md, internal-first-research, session-debrief, and this roadmap. Test the complete loop: work → debrief → roadmap update proposal → human review. Identify integration gaps and refine patterns.

**Context Snapshot:**  
Personal-os now has a complete LLM operating layer. CLAUDE.md defines governance and operating rules. Three meta-skills (phase-wrap-up, internal-first-research, session-debrief) encode repeatable patterns. _core/roadmap.md provides phase-aware structure for resumability. Governance layer (9 checks, governed subtrees) is frozen at v1. Foundation is stable. Next phase is domain expansion and knowledge ingestion.

---

## Metadata for LLMs

**How to Update This Roadmap:**
- phase-wrap-up outputs feed directly: "Completed" items → move to "Completed in This Phase"; "Remaining Work" → add to "In Progress" or next phase; "Re-entry Point" → update "Re-entry Breadcrumbs".
- session-debrief proposals that affect priorities → let Javier decide → then update roadmap.
- **Never edit roadmap directly. Always propose changes via session-debrief.**

**When to Consult Roadmap:**
- At session start: read current phase, next priorities, blockers, and re-entry breadcrumbs.
- During work: if a discovery changes priorities, note it for session-debrief.
- At session end: phase-wrap-up proposes updates; Javier reviews and edits asynchronously.

---

## Historical Phases (Reference)

**Phase 0: Foundation** — Completed 2026-04-15  
Repo structure, governance (9 checks), core context vault, CLAUDE.md, meta-skills foundation.

**Phase 1: Content Population** — Deferred to after Domain Expansion  
Will populate _core/ files (human chisel work), domain structure, inbox workflow once domain boundaries are clear.

**Phase 2: Knowledge Extraction & Integration** — Follows Domain Expansion  
Ingest external sources, build pipelines, populate knowledge-extracts.

**Phase 3: Automation & Scaling** — Future  
Backup automation, search/discovery, CI/CD enhancements.

**Phase 4: Sustainability & Evolution** — Future  
Documentation, metrics, refinement cycles.

---

*Last updated: 2026-04-15*
