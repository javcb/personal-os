---
title: Knowledge Ingestion Pipeline
type: pipeline
domain: learning
audience: self
status: active
quadrant: KK
change-velocity: medium
review-by: 2026-10-15
last-updated: 2026-04-15
related:
  - _core/self-model.md
  - _core/quadrants.md
  - docs/templates/knowledge-extract.md
standalone: false
---
-

# Knowledge Ingestion Pipeline

## Purpose
Convert external material into durable, structured, context-aware knowledge.

## Triggers
- Course video
- Lecture
- Book
- Article
- Notes packet
- Homework set
- Research material

## Context Load
Load:
- _core/self-model.md
- relevant docs/domains/[domain].md
- existing knowledge extracts in the same area
- _core/models.md when mental model overlap is likely

## Steps
1. Decide whether the material is worth ingesting now.
2. Extract durable content using the knowledge-extract template.
3. Identify any BL→KU→KK movement and log it appropriately.
4. Suggest practical applications based on existing context.
5. Require human review before any application is adopted.
6. Update the warehouse only with durable outputs.

## Output Locations
- docs/knowledge-extracts/[domain]/[material-slug].md
- _core/quadrants.md
- _core/models.md
- docs/domains/[domain].md (only if canon should change)

## Rules
- Do not summarize for completeness; summarize for future usefulness.
- Practical Application is advisory only.
- Unknowns surfaced should be captured even if no action is taken.
- Canon updates must be slower than extraction.

## Failure Modes
- Treating all source material as equally important
- Skipping critique because the source feels authoritative
- Confusing summary with durable knowledge
- Promoting too much into canon
- Letting applications bypass human judgment
