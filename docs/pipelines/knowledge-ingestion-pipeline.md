---
title: Knowledge Ingestion Pipeline
type: pipeline
audience: self, ai
status: active
last-updated: 2026-04-17
domain: learning-research
related:
  - /_core/quadrants.md
  - /_core/models.md
  - /docs/knowledge-extracts/
  - /docs/templates/knowledge-extract.md
---

# Knowledge Ingestion Pipeline

Protocol for processing external material (courses, articles, books, research, conversations)
into durable knowledge warehouse. Distinguishes extraction (what changed your thinking)
from summary (passive archive).

---

## Purpose

External material is only valuable if it changes mental models, answers known unknowns,
or surfaces blind spots. This pipeline ensures material is processed to identify what changed
thinking, not just summarized. Output: knowledge extract tagged for human review before
promotion to canon.

The core distinction: summaries are archives (passive). Extractions are upgrades (active).
Ask: "What was I wrong about? What now makes more sense? What new framework do I trust?"

---

## Trigger

- Completed reading or engagement with external material (article, book, course, research, podcast)
- Completion of conversation or session that surfaced new learning
- Attending conference, taking course, or completing significant learning activity
- Encountering unexpected insight or framework from external source
- Material directly addresses known unknown from _core/quadrants.md

**Not needed for:**
- Passive consumption without engagement
- Material that confirms existing KK without adding nuance
- Quick reference lookups that don't change thinking

---

## Steps

### Step 1: Intake Assessment
**Who:** LLM  
**Time:** 2–3 minutes

Classify the material before processing:

**Material type:** Article, book, course, conversation, research paper, podcast, video, other?  
**Domain:** Which personal-os domain is this primarily about? (finance, family, operations, software, learning, legal, strategy, professional, governance)  
**Source credibility:** Is this authoritative in the domain? Is it opinion, research, personal experience, anecdote?  
**Engagement depth:** Did you consume the full material or extract/sample?  
**Time investment:** How much effort was this?

Output: 1–2 sentence classification of material.

### Step 2: Load Context
**Who:** LLM  
**Time:** 3–5 minutes

Before extracting, load this system's existing knowledge:

- `_core/self-model.md` — Javier's context, priorities, constraints
- `_core/quadrants.md` — Known Knowns, Known Unknowns, Blind Spots
- `_core/models.md` — Mental models already adopted
- Relevant `docs/domains/*.md` — Domain-specific frameworks
- Related `docs/knowledge-extracts/` — Prior extractions on similar topics

**Why?** To compare new material against existing canon. New material either:
- Confirms KK (validates existing model)
- Extends KK (adds nuance without contradicting)
- Answers KU (addresses known gap)
- Surfaces new BL (reveals blind spot)
- Contradicts KK (requires investigation)

Identifying which category changes how material is processed.

### Step 3: Extract What Changed Thinking
**Who:** LLM  
**Time:** 10–20 minutes depending on material

Extract what the material taught you. Focus on changes, not summary.

**New Known Knowns (KK):**
- What did this material confirm or establish as reliable?
- What mental model was validated?
- What moved from "uncertain" to "confident"?

**New Known Unknowns (KU):**
- What questions did this material raise?
- What do we now know we need to understand better?
- What follow-up learning is required?

**New Blind Spots (BL):**
- What surprised you or contradicted prior assumption?
- What gap or blind spot did this surface?
- What did you not see coming?

**Mental Model Changes:**
- What framework or concept is now clearer?
- What model did this upgrade?
- What assumptions were challenged?

**Relation to Existing Canon:**
- Does this confirm/extend/conflict/obsolete any existing KK or KU?
- If conflict: what is the contradiction? Why might material be wrong, or why might canon be wrong?

**Do NOT:** Summarize the entire material. Extract only what changed your thinking.

Output: Bulleted list of KK/KU/BL/model changes with brief justification.

### Step 4: Format as Knowledge Extract
**Who:** LLM  
**Time:** 5–10 minutes

Write formatted knowledge extract file to: `docs/knowledge-extracts/YYYY-MM-DD-[slug].md`

**Sections (use template from docs/templates/knowledge-extract.md):**

1. **Overview** — What is this material? Why engage with it? (2–3 sentences)

2. **Key Decisions or Arguments** — If material advocates for specific choices, what are they?

3. **New Known Knowns (KK)** — Bulleted list of what material confirmed or established

4. **New Known Unknowns (KU)** — Questions surfaced or gaps identified

5. **Blind Spots (BL)** — Surprises or contradictions with prior thinking

6. **Mental Model Changes** — Frameworks upgraded or new frameworks introduced

7. **Relation to Existing Canon** — Does this confirm/extend/conflict/obsolete existing KK or KU?

8. **Practical Application** — [LEAVE BLANK FOR HUMAN TO WRITE]
   - How should this change behavior or decisions?
   - What actions does this enable or suggest?
   - How does this integrate into current projects?
   *LLM must leave this section blank. Human writes this after review.*

9. **Next Actions** — What follow-up learning or validation is needed?

**Do NOT:** Auto-populate the "Practical Application" section. That requires human judgment about integration into Javier's life and work.

Output: Complete knowledge extract file formatted and ready for staging.

### Step 5: Stage for Review
**Who:** LLM  
**Time:** 1 minute

**Do NOT auto-commit.**

Instead:

1. Write knowledge extract to docs/knowledge-extracts/YYYY-MM-DD-[slug].md
2. Append entry to inbox.md with tag `[knowledge-extract:YYYY-MM-DD]`
3. Provide summary of what was extracted and where file was written
4. Wait for human to review before promoting extract to canon

**Human review checks:**
- Are the KK/KU/BL extractions accurate?
- Are there contradictions with existing canon that need investigation?
- Is the "Practical Application" section appropriately blank?
- Should this extract be promoted to quadrants.md or models.md?

---

## Output

**Primary output:** Formatted knowledge extract file
- Location: `docs/knowledge-extracts/YYYY-MM-DD-[slug].md`
- Format: Markdown with YAML frontmatter
- Sections: Overview, Key Decisions, KK, KU, BL, Model Changes, Relation to Canon, [BLANK] Practical Application, Next Actions
- Status: Staged for human review (not yet promoted to canon)

**Secondary output:** Inbox entry
- Tag: `[knowledge-extract:YYYY-MM-DD]`
- Summary: What was extracted, where to find it, any conflicts with existing canon
- Flags: Any contradictions, BL items, or questions requiring human decision

**Artifacts:**
- Complete extract ready for review in docs/knowledge-extracts/
- Inbox entry flagging material for Javier's review cycle
- Practical Application section left blank for human to populate

---

## Autonomy Rules

**LLM can do autonomously:**
- Classify material type, domain, source credibility
- Load and read context files (_core/, domains/, prior extracts)
- Identify KK/KU/BL from material
- Identify mental model changes
- Compare against existing canon
- Format extract with all sections
- Write to knowledge-extracts/ directory

**LLM cannot do (human or requires review):**
- Write the "Practical Application" section
  - LLM must leave it blank
  - Javier fills this after reviewing extract
  - This ensures practical integration reflects his judgment, not LLM inference
- Promote extract to canon (KK in quadrants.md, models in models.md, etc.)
  - LLM stages for review; human promotes
  - Prevents material from becoming canon without validation
- Resolve contradictions with existing canon
  - If material conflicts with existing KK, flag for human decision
  - Human determines if canon should update or material is wrong

**When material contradicts canon:**
1. Flag clearly in extract: "CONFLICTS WITH: [existing KK]"
2. Explain the contradiction
3. Wait for human review to resolve
4. Do NOT silently choose which authority to trust

**When confidence is low:**
- If material quality seems questionable or material is anecdotal
- Tag clearly in frontmatter and extraction
- Flag for review; let human decide weight

---

## Quality Checklist

Before staging extract for review:

- [ ] Intake assessment is clear (material type, domain, source credibility)
- [ ] Context files were loaded before extraction
- [ ] KK/KU/BL extractions are specific (not vague)
- [ ] Extractions identify what *changed* thinking, not what was summarized
- [ ] Mental model changes identified if applicable
- [ ] Relation to existing canon is explicit (confirm/extend/conflict/obsolete)
- [ ] "Practical Application" section is **left blank** (do NOT fill)
- [ ] All other sections are complete
- [ ] Frontmatter is present and valid (title, type, domain, source, material-type, related)
- [ ] File is formatted consistently with prior extracts
- [ ] No contradictions with existing canon are silently accepted
- [ ] File is readable and well-organized

---

## Related Files

- Context files: `/_core/self-model.md`, `/_core/quadrants.md`, `/_core/models.md`
- Extract template: `/docs/templates/knowledge-extract.md`
- Prior extracts: `/docs/knowledge-extracts/`
- Domain files: `/docs/domains/*.md`
- Inbox for staging: `/inbox.md`

---

## Notes for Future Iteration

- After 10+ ingested materials, review patterns in what surfaces as KU/BL
- Consider tracking source types most valuable to learning goals
- May evolve to include "Prior Exposure" field (have we seen similar material before?)
- Could create domain-specific extraction templates with tighter guidance

---

*Last updated: 2026-04-17*
