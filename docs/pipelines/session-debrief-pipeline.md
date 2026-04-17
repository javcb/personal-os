---
title: Session Debrief Pipeline
type: pipeline
audience: self, ai
status: active
last-updated: 2026-04-17
related:
  - /docs/skills/_custom/session-debrief.md
  - /DECISIONS.md
  - /_core/quadrants.md
  - /_core/initiatives.md
---

# Session Debrief Pipeline

Protocol for end-of-session capture, extracting durable takeaways and updating
repo state to ensure resumability and knowledge accumulation.

Run this pipeline at the end of every working session.

---

## Purpose

Every session produces decisions, learnings, and insights that matter for future work.
This pipeline ensures those are captured (not lost), classified (durable vs. temporary),
and indexed (findable later). Without this, work becomes fragmented across sessions
and context evaporates.

The pipeline feeds into DECISIONS.md, quadrants.md, and initiatives.md, creating
a comprehensive record of what the system learned and what changed.

---

## Trigger

- End of any working session (even short ones)
- After completing a task or project phase
- When a decision was made during the session
- When unexpected learnings or insights emerged
- When blockers, risks, or blind spots were surfaced

**This is non-negotiable.** Every session, no matter how short, runs debrief.
Skipping debrief is how knowledge evaporates.

---

## Steps

### Step 1: Summarize What Was Done
**Who:** LLM or Human  
**Time:** 2–5 minutes

Quick summary of session work:
- What was the intended goal?
- What was actually accomplished?
- What blockers or surprises emerged?
- What remains unfinished?

This establishes context for later work and helps identify what changed.

Example:
```
Goal: Create 9 domain context files
Accomplished: All 9 files created and pass governance checks
Surprises: Discovered that domain context files need substantive content
          from self-model to be useful (bootstrap problem)
Unfinished: Need to populate _core/ files before pipelines can run effectively
```

### Step 2: Extract Decisions Made
**Who:** LLM  
**Time:** 3–5 minutes

What decisions were made in this session?

- **Structural decisions:** Changes to repo organization, governance, or architecture
- **Process decisions:** How to approach a problem, which pipeline to use
- **Domain decisions:** Financial, family, professional, operational choices made
- **Deferred decisions:** What was explicitly decided NOT to do now (with rationale)

For each decision:
- State the decision clearly: "We decided to [X] instead of [Y]"
- Record the reason (why this was chosen)
- Note if it's reversible (easy to undo) or irreversible (hard to change)

Format for later DECISIONS.md entry:
```
[YYYY-MM-DD]: Decided to [decision]. Reason: [why]. Reversibility: [reversible/irreversible]
```

### Step 3: Extract New Knowledge (KK/KU/BL)
**Who:** LLM  
**Time:** 5–10 minutes

What did the session teach us?

**New KK (Known Knowns):**
- What was confirmed or became clear?
- What moved from "we thought this might be true" to "we know this"?
- What mental model was validated?

Tag format: `[quadrant:KK] [session:YYYY-MM-DD]`

Example:
```
[quadrant:KK] [session:2026-04-17] Domain context files must include
substantive content from _core/ or they are useless templates.
```

**New KU (Known Unknowns):**
- What questions surfaced during this session?
- What do we know we need to understand better?
- What are we explicitly exploring now?

Tag format: `[quadrant:KU] [session:YYYY-MM-DD]`

Example:
```
[quadrant:KU] [session:2026-04-17] Will the system actually work with
real sessions, or will usage reveal critical design flaws?
```

**New BL (Blind Spots):**
- What didn't we see coming?
- What surprised us or revealed a gap in thinking?
- What unknown unknowns became known?

Tag format: `[quadrant:BL] [session:YYYY-MM-DD]`

Example:
```
[quadrant:BL] [session:2026-04-17] "What changed" vs. "what is summary"
distinction for knowledge extraction. Summaries are passive; extractions
that identify mental model changes are what matter.
```

### Step 4: Update _core/quadrants.md
**Who:** LLM (with human review)  
**Time:** 3–5 minutes

Add new KK/KU/BL entries to quadrants.md under the relevant sections:

1. **Known Knowns (KK):** Add new items to appropriate subsection (Finance, Systems, etc.)
2. **Known Unknowns (KU):** Add new questions to the list
3. **Unknown Unknowns (BL):** Add tagged entries with [quadrant:BL] [session:date]
4. **Promotion Log:** If any KU or BL moved to KK, add entry to promotion table

Example edit:
```
## Known Unknowns (KU)
- [session:2026-04-17] Will the system work in practice with real sessions?
- [session:2026-04-17] Do the 9 domains need refinement after actual usage?
```

### Step 5: Update _core/initiatives.md
**Who:** LLM (with human review)  
**Time:** 2–3 minutes

Update initiative tracker:

**For completed initiatives:**
- Move to Archive section with completion date
- Note what was accomplished
- Reference related DECISIONS.md entries

**For in-progress initiatives:**
- Update status (% complete, blockers, next steps)
- Update timeline if changed
- Note any learning that affects approach

**For new initiatives surfaced:**
- Add to appropriate domain section
- Set initial status and timeline
- Link to related decisions or learning

Example:
```
## Software & Development

### personal-os (In Progress)
- **Status:** Domain expansion in progress. 9 domain files created.
  Core _core/ files need population before pipelines can run.
- **Next:** Populate _core/quadrants, models, initiatives with substantive content
- **Horizon:** Ongoing infrastructure; next phase after real session validation
```

### Step 6: Format Takeaways for Review
**Who:** LLM  
**Time:** 5 minutes

Create structured debrief output with all findings:

```
## Session Debrief — YYYY-MM-DD

**What Was Done:** [summary]
**Decisions Made:** [list with rationale]
**New KK:** [bullet points]
**New KU:** [bullet points]
**New BL:** [bullet points]
**Updated Files:** [list of what was changed in quadrants/initiatives]
**Files Ready to Commit:** [list of modified files]
**Blockers Remaining:** [if any]
**Next Action for Next Session:** [specific next step]
```

### Step 7: Stage for Commit (or Hold for Review)
**Who:** LLM  
**Time:** 1 minute

**If human review is needed:**
- Save debrief output to inbox.md tagged [session-debrief:YYYY-MM-DD]
- Flag any decisions or KK/KU/BL that need human confirmation
- Wait for human to review before committing

**If routine debrief with no controversial items:**
- Add modified quadrants.md and initiatives.md to staging
- Create commit with message format:
  ```
  session-debrief: YYYY-MM-DD [one-line summary]
  
  Updated:
  - _core/quadrants.md: [summary of KK/KU/BL added]
  - _core/initiatives.md: [summary of status updates]
  
  Decisions logged: [reference to DECISIONS.md entries if made]
  ```
- Run governance check before committing
- Commit changes

---

## Output

**Primary output:** Updated _core/ files
- `_core/quadrants.md` — New KK/KU/BL entries added and tagged
- `_core/initiatives.md` — Initiative status updated
- `DECISIONS.md` — Major decisions logged with rationale (if applicable)

**Secondary output:** Structured debrief summary
- Captures what was done, what was learned, what changed
- Surfaces any blockers or concerns for next session
- Provides resumption breadcrumbs for future work

**Artifacts for review:**
- Debrief output in inbox.md (tagged) if human decision needed
- List of files ready for commit
- Any flagged conflicts or surprises requiring attention

---

## Autonomy Rules

**LLM can do autonomously:**
- Summarize session work
- Extract decisions made
- Identify new KK/KU/BL from session
- Format debrief output
- Update quadrants.md and initiatives.md with session-tagged entries
- Stage files for review
- Run governance check

**LLM cannot do (human must do):**
- Make final decision about what gets logged in DECISIONS.md
  - LLM can recommend; human approves
- Resolve any conflicts between new learning and existing KK
  - If session learning conflicts with prior decisions, human decides
- Determine if decision is "major" (requires DECISIONS.md entry)
  - LLM flags candidates; human decides threshold
- Commit changes without governance check passing
- Override or delete prior KK/KU/BL entries

**When in doubt:**
- Err toward capturing more, not less (over-capture is better than forgetting)
- Flag anything that's unclear for human review
- Tag everything with [session:date] so it's traceable
- Keep new entries as direct quotes when possible (less interpretation)

---

## Quality Checklist

Before marking debrief complete:

- [ ] Session work is summarized (goal, accomplishment, surprises, blockers)
- [ ] All decisions made are explicit with rationale
- [ ] New KK/KU/BL are specific and tagged with [session:date]
- [ ] quadrants.md has been updated with new entries
- [ ] initiatives.md has been updated with status changes
- [ ] Any major decisions have been flagged for DECISIONS.md
- [ ] Governance check passes on modified files
- [ ] Next action for future session is stated
- [ ] Any conflicts or concerns are flagged for human attention

---

## Related Files

- Meta-skill version: `/docs/skills/_custom/session-debrief.md`
- Decision logging: `/DECISIONS.md`
- Epistemic state: `/_core/quadrants.md`
- Work tracking: `/_core/initiatives.md`
- Inbox for review: `/inbox.md`

---

## Notes for Future Iteration

- After 10+ debriefs, review patterns in what gets surfaced (most common KU types, etc.)
- Consider automated extraction of related prior decisions when logging new ones
- May evolve to include session metrics (time spent, files created, decisions made count)
- Could create debrief templates for different session types (learning, decision-making, building)

---

*Last updated: 2026-04-17*
