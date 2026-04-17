---
title: Internal-First Research Pipeline
type: pipeline
audience: self, ai
status: active
last-updated: 2026-04-17
related:
  - /CLAUDE.md
  - /docs/skills/_custom/internal-first-research.md
  - /_core/quadrants.md
  - /_core/models.md
  - /docs/domains/
---

# Internal-First Research Pipeline

Protocol for answering questions by loading internal canon first, attempting to
answer from existing knowledge, then only reaching outward when gaps are explicit.

This pipeline implements the "epistemic filter" concept: external information is
interpreted *through* existing models, not in isolation.

---

## Purpose

Not all questions need external research. Many can be answered from _core/ context
(self-model, quadrants, models) and existing domain files. This pipeline ensures
we check internal canon first, making explicit what we don't know, before investing
time in external research.

Output: Confidence-rated answer with gap list, enabling better decisions about whether
external research is worth the time.

---

## Trigger

- LLM is asked a question that might benefit from external research
- Session-debrief surfaces a question worth exploring
- Javier encounters a decision that requires understanding a new topic
- New idea or concept is encountered and needs to be evaluated against existing models

---

## Steps

### Step 1: Classify the Question
**Who:** LLM or Human  
**Time:** 1–2 minutes

What type of question is this?

- **Decision question:** "Should I do X?" — needs decision framework + constraints
- **Domain question:** "How does Y work in [domain]?" — needs domain canon + mental models
- **Learning question:** "What is Z?" — needs research in _core/quadrants.md KU section
- **System question:** "How should we handle X?" — needs governance rules + decision protocol
- **Conflict question:** "New info conflicts with existing model. What's right?" — needs careful evaluation

Classification determines which context to load first.

### Step 2: Load Internal Canon
**Who:** LLM  
**Time:** 2–5 minutes

Load these files based on question type:

**All questions:**
- `_core/self-model.md` — Javier's roles, constraints, priorities (context for decision)
- `CLAUDE.md` — Operating rules and decision protocols (frames how to think)
- `DECISIONS.md` — Prior decisions and precedents (what was decided and why)

**Domain questions:**
- Relevant `docs/domains/*.md` — Domain-specific rules and frameworks
- `_core/models.md` — Mental models in that domain
- `docs/governance/autonomy-matrix.md` — What LLMs can vs. can't do in that domain

**Learning questions:**
- `_core/quadrants.md` — Known Knowns (KK) and Known Unknowns (KU) in relevant area
- Related `docs/knowledge-extracts/` — Prior extractions on topic
- `docs/domains/learning-research.md` — Learning protocols and frameworks

**Decision questions:**
- `_core/self-model.md` — Constraints and conflict resolution rules
- `docs/governance/autonomy-matrix.md` — What Javier decides vs. what LLMs handle
- `_core/models.md` section: "Critique-Before-Commit" — decision protocol
- `DECISIONS.md` — Similar prior decisions

**Conflict questions:**
- `_core/quadrants.md` — Existing KK that is being challenged
- Related `docs/domains/*.md` — Domain-specific context for the conflict
- `_core/models.md` — Related mental models that might clarify the conflict

### Step 3: Attempt Answer from Canon
**Who:** LLM  
**Time:** 5–15 minutes depending on question complexity

Using loaded context, answer the question fully.

- State what the canon says about this question
- Identify which mental models or domain rules apply
- Note any constraints from self-model or autonomy matrix
- Explain the reasoning from existing frameworks

Output: Complete answer based solely on internal canon.

### Step 4: Assess Confidence and Flag Gaps
**Who:** LLM  
**Time:** 2–5 minutes

Rate the answer:

**Confidence Level:**
- **High:** Canon provides clear answer with explicit framework; high confidence in applicability
- **Medium:** Canon provides partial answer; some gaps or uncertainties remain
- **Low:** Canon provides minimal guidance; significant gaps remain
- **Conflicted:** Canon contradicts itself or new question conflicts with existing KK

**Gap Identification:**
- What information would make this answer more confident?
- What assumptions are we making that we haven't verified?
- What KU (Known Unknowns) from quadrants.md are directly relevant?
- What domain rules or mental models are we uncertain about?

Example gap list:
```
- Need: Specific data on [topic] to complete financial analysis
- Assumption: [X is true], but this is assumed not verified
- KU connection: Related to KU #3 in quadrants.md
- Confidence blocker: Don't know how much this applies to Javier's situation
```

### Step 5: Recommend (Defer/Research/Accept)
**Who:** LLM (recommendation), Human (decision)  
**Time:** 1 minute

Based on confidence + gaps, recommend:

**Accept answer as-is:**
- High confidence and low gaps
- Question answered adequately for current decision
- External research would add marginal value

**Research externally:**
- Low/medium confidence and significant gaps
- External research would materially improve answer
- Time investment is justified by decision importance
- Specific research questions are clear (from gap list)

**Defer:**
- Question is interesting but not urgent
- Defer to next learning review cycle
- Note in _core/quadrants.md (KU section) for future exploration

---

## Output

**Primary output:** Formatted answer with these sections:

1. **Answer:** Inline answer from internal canon (1–2 paragraphs)
2. **Confidence Level:** High/Medium/Low/Conflicted + brief justification
3. **Reasoning:** Which mental models, domain rules, or constraints apply?
4. **Gaps:** What we'd need to know to be more confident (bulleted list)
5. **Related Canon:** Links to _core/models.md, domain files, or quadrants.md entries used
6. **Recommendation:** Accept / Research / Defer (with rationale)

Example output structure:
```
## Answer
[Full answer based on internal canon]

## Confidence: Medium
[Why medium, not high or low]

## Reasoning
- Applied mental model: [X from _core/models.md]
- Domain rule: [Y from docs/domains/]
- Constraint: [Z from _core/self-model.md]

## Gaps
- Need [specific data] to verify [assumption]
- Unknown: Whether [X] applies to Javier's situation
- Related KU: See quadrants.md #3

## Related Canon
- _core/models.md: "Cash Flow Hierarchy"
- docs/domains/finance-economics.md: "Operating Rules"
- _core/quadrants.md: Known Unknowns section

## Recommendation
**Research:** External research would materially improve confidence.
- Specific research questions: [list 2–3 concrete questions to answer]
- Time estimate: [2–4 hours if research is worth doing]
- Expected outcome: [What would we know after research?]
```

---

## Autonomy Rules

**LLM can do autonomously:**
- Load internal canon files
- Identify relevant frameworks and mental models
- Draft answer from internal sources
- Assess confidence level and identify gaps
- Recommend whether external research is worth doing
- Format output with all sections

**LLM cannot do (human or requires review):**
- Override existing KK with speculation
- Decide to conduct external research without human approval
- Update canon files (models.md, domains/) without human decision
- Treat "low confidence" answer as sufficient when high confidence would materially change the decision

**When answer has conflicts:**
- If new info conflicts with existing KK: flag clearly for human review
- Don't silently choose which authority to trust
- List both perspectives, ask human to resolve

**Escalation:**
- If confidence is low and question is high-stakes (financial, legal, family): explicitly recommend human oversight
- If gaps are fundamental to the decision: don't present low-confidence answer as adequate

---

## Quality Checklist

Before delivering answer:

- [ ] All relevant context files loaded and considered
- [ ] Answer is fully grounded in internal canon
- [ ] Confidence level is honest (not over-confident)
- [ ] Gaps are explicit and actionable
- [ ] Recommendation is clear (accept/research/defer)
- [ ] Reasoning is shown (which models/rules apply?)
- [ ] Related canon is cited
- [ ] No external assumptions beyond what's in context

---

## Related Files

- Meta-skill version: `/docs/skills/_custom/internal-first-research.md`
- Decision protocol: `/docs/pipelines/decision-protocol.md`
- Context files: `_core/self-model.md`, `_core/quadrants.md`, `_core/models.md`
- Domain files: `/docs/domains/*.md`
- CLAUDE.md section: "Internal-First Research Protocol"

---

## Notes for Future Iteration

- After 10+ research cycles, evaluate which gaps are most frequently encountered
- Consider maintaining a "research queue" in _core/quadrants.md for deferred questions
- Could automate gap mapping to external resources/sources over time
- May evolve to suggest which external sources would best address gaps

---

*Last updated: 2026-04-17*
