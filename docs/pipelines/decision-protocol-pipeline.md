---
title: Decision Protocol Pipeline
type: pipeline
audience: self, ai
status: active
last-updated: 2026-04-17
related:
  - /_core/self-model.md
  - /docs/governance/autonomy-matrix.md
  - /DECISIONS.md
  - /_core/models.md
---

# Decision Protocol Pipeline

Protocol for making major decisions with explicit reasoning, constraint checking,
and reversibility assessment. This is a hard rule: no major decision without
running this protocol.

---

## Purpose

Most decisions can be made quickly without ceremony. But major decisions
(irreversible, high-stakes, affecting multiple domains, or out-of-pattern)
require structure to avoid costly mistakes. This protocol forces the
hard thinking before commitment.

**Hard rule:** If you're uncertain whether a decision needs this protocol, it does.

---

## Trigger

- Any decision affecting family stability or finances
- Any legal, regulatory, or compliance decision
- Any structural change to personal-os or major systems
- Any commitment that's hard or impossible to reverse
- Any decision conflicting with existing roles, constraints, or values
- Any decision outside the autonomy matrix (requires human instead of LLM)
- Any decision that feels important or carries real stakes

**Not needed for:**
- Routine tasks or daily choices
- Reversible decisions with low consequence
- Decisions already covered by existing domain rules or autonomy matrix
- Decisions that can be revisited frequently without cost

---

## Steps

### Step 1: Load Self-Model Constraints
**Who:** LLM (with human awareness)  
**Time:** 1–2 minutes

Load `_core/self-model.md` and extract relevant constraints:

**Hard constraints (non-negotiable):**
- Budget: No single subscription SPoF
- Time: System must fit around family/work
- Family: Family stability wins over everything else
- Risk tolerance: Not willing to risk family, financial stability, legal exposure

**Domain constraints:**
- What domain does this decision affect?
- What rules apply in that domain? (from docs/domains/*.md)
- What's the conflict resolution hierarchy? (family > financial resilience > everything else)

**Autonomy bounds:**
- Is this a decision Javier makes, or does the autonomy matrix say LLM can decide?
- If autonomy matrix says "Human", stop here and escalate.

Output: List of applicable constraints and any red flags.

### Step 2: Classify Reversibility
**Who:** LLM  
**Time:** 2–3 minutes

Is this decision reversible or irreversible?

**Reversible decisions:**
- Can be undone or changed with modest effort/cost
- Examples: changing a tool, trying an approach for 30 days, reorganizing a workflow
- Protocol requirement: Light (inform/compare/critique is sufficient)

**Irreversible or hard-to-reverse:**
- Cannot be undone or would cost significant time, money, opportunity, or relationships
- Examples: major financial commitments, legal decisions, family decisions, structural repo changes
- Protocol requirement: Full (all 5 stages required)

**Partially reversible:**
- Can be undone but at real cost
- Examples: major professional commitments, large purchases, significant lifestyle changes
- Protocol requirement: Medium (all 5 stages, but allow shorter timeframes)

Classify clearly. When in doubt, treat as irreversible.

### Step 3: Run 5-Stage Decision Protocol
**Who:** LLM (recommend), Human (decide)  
**Time:** 10–30 minutes depending on complexity

This is the core of the protocol (from _core/models.md "Critique-Before-Commit"):

**Stage 1: Inform**
- What do I need to know before evaluating this?
- What data, context, or advice is relevant?
- What unknowns would materially change the decision?
- Action: Gather the information (research, ask experts, check constraints)

**Stage 2: Compare**
- What are the legitimate alternatives?
- What would happen if I chose A vs. B vs. C?
- What are the trade-offs? (what do I gain, what do I lose?)
- What's the cost of each option (time, money, opportunity, risk)?
- Action: List 2–4 real alternatives with clear trade-offs

**Stage 3: Critique**
- What is the strongest argument AGAINST the leading option?
- What could go wrong with option A?
- What assumptions am I making that might be wrong?
- What risks am I not seeing?
- Action: Write down the best case for the opposing view

**Stage 4: Connect**
- What else in my life does this decision touch?
- How does this affect other domains? (family, finances, professional, etc.)
- Are there decisions I've made before that are relevant precedents?
- What domain rules apply? (from docs/domains/*.md)
- Action: Map dependencies and conflicts

**Stage 5: Commit or Pause**
- Is there one question whose answer would change everything?
- Do I have enough confidence to commit, or should I wait?
- If waiting: what would give me confidence? (more data, cooling-off period, expert input?)
- Action: Decide to commit OR define what would change your mind

Output of each stage should be documented (bullet points ok).

### Step 4: Check Against Autonomy Matrix
**Who:** LLM  
**Time:** 1–2 minutes

Check `docs/governance/autonomy-matrix.md`:

- Does the autonomy matrix permit Javier (or LLM) to make this decision?
- What action type is this? (Analysis, Drafting, Execution, Final Decision)
- What does the matrix say for this domain and action type?

If autonomy matrix says "Human": Javier must make this decision.  
If autonomy matrix says "AI → Review": LLM can decide but Javier reviews.  
If autonomy matrix says "AI ✓": LLM has full autonomy.

If the decision type is not in the matrix, default to "Human" (conservative).

Output: Statement of autonomy level + where to find it in the matrix.

### Step 5: Write Rationale and Log Decision
**Who:** LLM (draft), Human (approves and logs)  
**Time:** 3–5 minutes

Write the decision rationale and log it.

**Rationale format (for DECISIONS.md):**
```
[YYYY-MM-DD]: Decided to [decision]. Reason: [rationale].

Rationale detail:
- Constraints satisfied: [list how this respects self-model constraints]
- Reversibility: [reversible/irreversible/partially reversible + recovery options]
- Alternatives considered: [summary of options compared]
- Strongest argument against: [what could go wrong, what we might be wrong about]
- Domain impacts: [how does this affect other domains?]
- Autonomy: [is this permitted by autonomy matrix? who makes final call?]
```

**Hard rule:** Every major decision gets a written rationale in DECISIONS.md.
"Just felt right" is not sufficient.

Example entry:
```
[2026-04-17]: Decided to organize personal-os by domain (finance, family, etc.)
rather than by initiative. Reason: Domains are stable (tied to roles); initiatives
are temporal (tied to projects). Separating them prevents knowledge fragmentation.

Reversibility: Reversible; would require reorganizing 9 domain files and cross-references.
Alternatives: Initiative-based (tried and rejected—too temporal; knowledge doesn't stick).
Topic-based (considered and rejected—overlaps with domains anyway).
Autonomy: This is an architecture decision; Javier decides.
```

### Step 6: Implement with Checks
**Who:** LLM (with human oversight)  
**Time:** Variable

If decision is fully reversible and low-stakes: implement immediately.  
If decision is high-stakes or irreversible: implement with checkpoints.

Checkpoints for irreversible decisions:
- 48-hour cooling-off period before execution
- Explicit final confirmation from Javier before commitment
- Clear rollback plan documented before implementation
- Automatic review/assessment point (e.g., 30 days in to evaluate results)

Output: Implementation plan with any required checkpoints.

---

## Output

**Primary output:** Written rationale in DECISIONS.md
- Format: `[YYYY-MM-DD]: Decision. Reason: [rationale with detail]`
- File: `/DECISIONS.md`
- Every major decision gets logged here

**Secondary output:** Implementation plan (if needed)
- For complex decisions: step-by-step plan with checkpoints
- For reversible decisions: go-live confirmation
- For irreversible: rollback plan + assessment point

**Artifacts for review:**
- If decision required cooling-off: calendar reminder to confirm
- If high-stakes: flagged for Javier review before implementation
- If conflicts with autonomy matrix: explicit escalation to Javier

---

## Autonomy Rules

**LLM can do autonomously:**
- Run through Stages 1–4 of decision protocol
- Load constraints and autonomy matrix
- Assess reversibility
- Flag risks and alternatives
- Write draft rationale
- Recommend reversible, low-stakes decisions within autonomy matrix

**LLM cannot do (human must do):**
- Make decisions marked "Human" in autonomy matrix
- Make decisions that violate self-model constraints
- Make irreversible decisions without explicit Javier approval
- Skip cooling-off period for high-stakes irreversible decisions
- Log decision to DECISIONS.md without human approval
- Override prior decisions without protocol (create new entry, don't erase old one)

**When LLM and Javier disagree on decision:**
- Log both perspectives in DECISIONS.md
- Let Javier's decision stand
- LLM implements with full commitment (no second-guessing)

**Escalation path:**
- Reversible, low-stakes → LLM can decide, implement immediately
- Reversible, moderate-stakes → LLM recommends, Javier confirms
- Irreversible or high-stakes → Javier must make final call
- Conflicts with constraints → Automatic escalation to Javier

---

## Quality Checklist

Before marking decision protocol complete:

- [ ] All relevant constraints from _core/self-model.md considered
- [ ] Reversibility is clearly classified (reversible/irreversible/partial)
- [ ] All 5 stages of decision protocol completed (Inform → Compare → Critique → Connect → Commit)
- [ ] Autonomy matrix consulted and decision is permitted
- [ ] Strongest argument against has been explicitly considered
- [ ] Domain impacts identified (how does this affect other areas?)
- [ ] Rationale is written and specific (not vague)
- [ ] Decision is logged in DECISIONS.md
- [ ] If high-stakes/irreversible: cooling-off period and confirmation plan
- [ ] If implementation needed: rollback plan documented
- [ ] No constraints violated

---

## Related Files

- Constraints: `/_core/self-model.md`
- Autonomy boundaries: `/docs/governance/autonomy-matrix.md`
- Decision log: `/DECISIONS.md`
- Domain rules: `/docs/domains/*.md`
- Mental model: `/_core/models.md` (Critique-Before-Commit section)

---

## Notes for Future Iteration

- After 10+ logged decisions, review patterns in decision types and reversibility
- Consider creating decision templates for common decision types (financial, family, professional)
- May evolve to include decision review metrics (outcomes vs. expectations at 30/90 day marks)
- Could track cooling-off period effectiveness over time

---

*Last updated: 2026-04-17*
