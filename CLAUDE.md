---
title: CLAUDE.md — AI Constitution
type: context
status: active
last-updated: 2026-04-15
---

# CLAUDE.md — Personal OS AI Constitution

Read this entire file before taking any action in this repo.
No exceptions. No shortcuts.

---

## 1. File Placement Decision Tree

Before creating any file, run through this in order:

1. Does this file already exist?
   → Run: find . -name "filename.md"
   → If yes: update it. Never create a duplicate.

2. Is this a raw idea, capture, or unprocessed thought?
   → Append to inbox.md. Stop here.

3. What type is this content?

| Content type | Goes in |
|---|---|
| Personal context, roles, priorities | _core/self-model.md |
| Mental models, cognitive frameworks | _core/models.md |
| Active work, projects | _core/initiatives.md |
| KK/KU/BL/UK entries | _core/quadrants.md |
| Emergency/legacy info | _core/emergency.md |
| Living checklist | _core/roadmap.md |
| Domain knowledge (one of 9 domains) | docs/domains/ |
| Step-by-step process | docs/skills/ or docs/workflows/ |
| Meta-skill (skill about using skills) | docs/skills/_custom/ |
| Pipeline definition | docs/pipelines/ |
| Knowledge extract from external source | docs/knowledge-extracts/[domain]/ |
| Reference pointer (where to look, not what) | docs/domains/ with type: reference-pointer |
| Templates | docs/templates/ |

4. Still uncertain?
   → inbox.md. Never a new file.

---

## 2. YAML Type Registry

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

## 3. The 5-Stage Decision Protocol

Before committing to any structural decision, run these stages:

1. **Inform** — What do I need to know before evaluating this?
2. **Compare** — What are the legitimate alternatives?
3. **Critique** — What is the strongest argument against the leading option?
4. **Connect** — What else in this repo does this decision touch?
5. **Commit or Pause** — Is there one question that would change everything?

If yes to Stage 5: pause and surface the question.
If no: commit and log it in DECISIONS.md.

---

## 4. End-of-Session Checklist

Run this before every commit, without exception:

- [ ] Run: `python3 scripts/governance-check.py`
- [ ] Fix all violations before committing
- [ ] Append one line to DECISIONS.md for every structural decision made
- [ ] Confirm no new files were created at root level
- [ ] Confirm no duplicate filenames were introduced
- [ ] Commit with a clear message

---

## 5. The inbox.md Rule

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

## 6. What You Must Never Do

- Create .md files at root (except README.md, CLAUDE.md, inbox.md, DECISIONS.md)
- Create a file without checking if it already exists first
- Skip the end-of-session checklist
- Auto-populate _core/ files — those are chisel work, human-written only
- Delete any file — deprecate using status: deprecated and updated-by: field
- Make a structural decision without logging it in DECISIONS.md

After writing, confirm the file exists at root level and 
run governance-check.py to verify it passes.
