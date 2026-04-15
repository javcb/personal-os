---
title: roadmap
type: context
status: active
last-updated: 2026-04-15
---

# Personal OS Roadmap

Live checklist. Single source of truth for project progress.

> **Returning after time away?** Read `_core/how-to-resume.md` first. It points to the prompt index and tells you today's next action.

---

## Phase 0: Foundation (ACTIVE → COMPLETE)

### Repo Structure & Governance
- [x] personal-os repo created on GitHub
- [x] Directory structure: _core/, docs/, scripts/, .github/
- [x] .gitkeep files for all empty directories
- [x] scripts/governance-check.py implemented (6-point check)
- [x] scripts/sync-check.py implemented (duplicate detection)
- [x] scripts/backup.py implemented (timestamped backups)
- [x] .git/hooks/pre-commit wired to governance-check.py
- [x] Pre-commit hook verified working (rejection tested)
- [x] mkdocs.yml configured with Material theme
- [x] .github/workflows/deploy-docs.yml configured

### Core Context Vault
- [x] _core/self-model.md (stub with frontmatter)
- [x] _core/quadrants.md (stub with frontmatter)
- [x] _core/models.md (stub with frontmatter)
- [x] _core/initiatives.md (stub with frontmatter)
- [x] _core/emergency.md (3-line minimum, frontmatter)
- [x] _core/roadmap.md (this file)

### Metadata & Governance
- [x] README.md (project overview)
- [x] CLAUDE.md (AI constitution with file placement tree)
- [x] inbox.md (dated capture zone)
- [x] DECISIONS.md (decision log with 5+ entries)
- [x] .gitattributes added to root whitelist
- [x] governance-check.py whitelist updated

### Meta-Skills
- [x] docs/skills/_custom/session-debrief.md created
- [x] docs/skills/_custom/decision-protocol.md created
- [x] docs/meta-skills/ duplicates removed and logged

### Verification
- [x] All governance checks passing (exit code 0)
- [x] Pre-commit hook blocks violations
- [x] DECISIONS.md logged all structural decisions
- [x] CLAUDE.md serves as AI guardrails

---

## Phase 1: Content Population

### Populate _core/ (Human Chisel Work)
- [ ] _core/self-model.md: roles, priorities, goals, constraints
- [ ] _core/quadrants.md: KK/KU/BL/UK knowledge matrix
- [ ] _core/models.md: mental models, cognitive frameworks
- [ ] _core/initiatives.md: active projects and milestones
- [ ] _core/emergency.md: critical procedures, escalation paths
- [ ] _core/roadmap.md: quarterly OKRs and milestones (link from here)

### Domain Structure
- [ ] docs/domains/ organized by 9 domains (define them)
- [ ] Stub README.md in each domain directory

### Inbox Workflow
- [ ] Inbox review process defined (weekly cadence)
- [ ] First 50 captures moved from inbox.md to permanent homes

---

## Phase 2: Knowledge Extraction & Integration

### Ingest External Sources
- [ ] docs/knowledge-extracts/ populated from reading/research
- [ ] Reference pointers documented (links to authoritative sources)
- [ ] docs/domains/ enriched with domain knowledge

### Pipelines & Workflows
- [ ] docs/pipelines/ defined for key workflows
- [ ] Trigger → output relationships documented
- [ ] docs/skills/ populated with how-to guides

### Templates
- [ ] docs/templates/ seeded with reusable formats
- [ ] Session templates, decision templates, etc.

---

## Phase 3: Automation & Scaling

### Backup & Versioning
- [ ] Backup script automated (cron or scheduler)
- [ ] Version history in ~/backups/personal-os/ verified

### Search & Discovery
- [ ] MkDocs site builds and deploys (GitHub Pages)
- [ ] Full-text search across all domains
- [ ] Cross-domain reference indices

### CI/CD
- [ ] GitHub Actions deploy-docs.yml tested
- [ ] Governance checks run on every PR
- [ ] sync-check.py detects duplicates in CI

---

## Phase 4: Sustainability & Evolution

### Documentation
- [ ] Contributing guide for future updates
- [ ] Maintenance checklist (quarterly review)
- [ ] Archival strategy for deprecated content

### Metrics & Health
- [ ] Inbox queue health (size, age)
- [ ] Decision log review (quarterly)
- [ ] Domain coverage assessment

### Refinement
- [ ] CLAUDE.md refined based on real usage
- [ ] Meta-skill library expanded
- [ ] Governance rules adjusted as needed

---

## Blocked / To-Revisit

- (none currently)

---

## Last Updated

2026-04-15 — Phase 0 complete. Phase 1 beginning.
