---
title: Mental Models
type: context
audience: self
status: draft
last-updated: 2026-04-17
related:
  - /_core/self-model.md
  - /_core/quadrants.md
---

# Mental Models

## Purpose

A library of the mental models I actually use when making decisions.
Not aspirational. Only models I have tested and rely on.
When this grows past ~15 models, split into atomic files in `models/`.

---

## Finance & Economics

### Cash Flow Hierarchy
Sequence matters more than amounts. Operating reserves → debt reduction →
tax-advantaged investment → taxable investment → discretionary.
Do not skip layers under pressure.

### Reversibility Over Speed
Before any financial decision, ask: is this reversible? Irreversible decisions
require more evidence and slower execution. Reversible decisions can move fast.

### Compound Asymmetry
Small consistent advantages compound dramatically over time.
This applies to: savings rate, knowledge accumulation, habit quality.
Optimizing the rate matters less than starting early and staying consistent.

---

## Decision-Making

### Critique-Before-Commit
Generate ideas fast; act slow. The bottleneck that saves wasted effort
is the critique layer between ideation and action.
Steps: Inform → Compare → Critique → Connect → Commit or Pause.

### Known-Unknown Matrix (Johari / Quadrants)
Four epistemic states: KK (expertise), KU (acknowledged gaps),
UK (unarticulated intuition), BL (blind spots / danger zone).
Primary mission: shrink BL→KU→KK cycle time.

### Cargo Cult vs. First Principles
Copying the artifact (prompt, template, framework) without understanding
the system that produced it creates fragile results.
Always ask: what is the underlying logic, not just what is the format?

---

## Systems & Operations

### Systems Beat Goals
A well-designed repeatable process outperforms willpower, motivation,
and individual talent over time. Design the system; the outcomes follow.

### Governance as Immune System
Rules enforced automatically prevent entropy; rules enforced manually
degrade under pressure. Governance must be self-enforcing to be real.

### Monorepo for Single Operators
Single person + single LLM doing cross-domain work needs everything
visible in one pass. Splitting creates coordination overhead with no benefit.

---

## Learning & Knowledge

### Frictionless Capture First
If capture requires organization at capture time, it won't happen.
Capture everything to inbox; organize on a cadence (weekly).

### Blind Spot Tagging
Unknown unknowns are the most dangerous because they're invisible.
Tag BL aggressively; accumulation over time maps cognitive blind spots.

### Extraction Over Summary
Knowledge ingestion goal is not to summarize a source but to extract
what changed your mental models. Summaries are archives; extractions
are upgrades.

---

## LLM Interface & Systems Design

### Epistemic Filter
External information should be interpreted *through* this system's existing models,
decisions, and canon — not in isolation. When encountering new ideas, check what
the system already knows first. Accept information that extends canon; flag and investigate
information that conflicts with canon.

### Governed Subtrees Pattern
Some directories function as self-contained systems with their own documentation, rules,
and change logs (manifest files). This pattern allows specialized governance in specific
areas without forcing boilerplate on every folder. Declare subtree requirements explicitly;
enforce them automatically.

### Autonomy Matrix for Human-AI Division
For each domain, specify what LLMs can do autonomously (Analysis, Drafting, Execution)
vs. what requires human review/decision (Final Decision). This prevents scope creep
and makes boundaries explicit. Conservative by default; upgrade to higher autonomy
only after validation through actual use.

### Meta-Skills as Operating System
Repeatable workflows encode better as portable meta-skills (how to approach work)
rather than procedural docs (what tool to use). Meta-skills survive tool changes;
procedures become stale. Meta-skills are the OS layer; domain-specific pipelines
are applications.

### Extraction Over Summary in Knowledge Ingestion
Knowledge ingestion goal is not to produce a passive summary (archive) but to identify
what changed your mental models (upgrade). Ask: what was I wrong about? What now
makes more sense? What new framework do I now trust? Summaries are dead; extractions live.

### Roadmap Governance Rule
Roadmap is human-curated. LLMs may propose updates via session-debrief structured
format, but Javier reviews and edits directly. No automation of roadmap generation
from debrief output. Prioritization decisions involve tradeoffs and context that
require human judgment.

---

## [JAVIER TO FILL: Parenting / Family Models]

Add 1–2 frameworks you actually use when making parenting or family decisions.

---

## [JAVIER TO FILL: Professional / Advisory Models]

Add 1–2 frameworks you rely on in client work or advisory relationships.
