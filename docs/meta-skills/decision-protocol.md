---
title: decision-protocol
type: meta-skill
status: active
last-updated: 2026-04-15
---

# Decision Protocol

Use this 5-stage protocol before committing to any **architectural decision**.

## What Counts as "Architectural"

**Architectural decisions** are irreversible or expensive to reverse:
- Repo structure, naming conventions, file organization
- Core tooling choices (language, framework, build system)
- Governance rules, processes, or enforcement mechanisms
- Protocol definitions (communication, escalation, approvals)

**Does NOT include:**
- Task-specific choices (which files to edit for this feature)
- Temporary workarounds
- Reversible edits or experiments
- Decisions already made by higher authority

---

## The Protocol

```
Inform → Compare → Critique → Connect → Commit/Pause
```

### Stage 1: Inform

**What it does:** Establish facts, constraints, unknowns, and decision scope.

**Trigger question:** "What do we actually know, and what are we guessing?"

**Failure if skipped:** Decisions rest on assumptions disguised as facts. Later you discover facts that would have changed everything.

**Example (repo governance decision):**  
Facts: We have multiple scripts that need to run before commit. We want to prevent bad commits.  
Constraints: Pre-commit hooks must work on GitHub Desktop and Terminal. They must fail fast.  
Unknowns: Do we know the failure modes of each tool? Do we know if Python is always available?

---

### Stage 2: Compare

**What it does:** Evaluate at least 2 plausible options against explicit criteria.

**Trigger question:** "What's the second option, and why would we pick it instead?"

**Failure if skipped:** The first acceptable option becomes "the best" by default. No exploration. No defensibility.

**Example (governance enforcement):**  
Option A: Pre-commit hook that runs Python checks locally.  
Option B: GitHub Actions workflow that runs checks on every push.  
Criteria: Speed (how fast does feedback come?), reliability (does it work on all machines?), UX (do developers see failures clearly?).

---

### Stage 3: Critique

**What it does:** Stress-test the leading option. Find failure modes, reversibility limits, costs, and edge cases.

**Trigger questions:**  
- "What would break this choice?"
- "When would we regret it?"
- "What happens if this assumption is wrong?"

**Failure if skipped:** Risks emerge later when correction is expensive. You ship knowing there's a problem but hoping it won't matter.

**Example (pre-commit hook):**  
Critique: Python might not be in PATH on GitHub Desktop. Hook could silently fail. We'd think we're protected when we're not.  
Reversibility: Once hooks are in place, developers expect protection. Removing them later feels like a regression.  
Cost of being wrong: Silent failure leads to committing violations undetected.

---

### Stage 4: Connect

**What it does:** Verify alignment with your principles, prior decisions, and downstream effects.

**Trigger question:** "Does this contradict anything we've already decided?"

**Failure if skipped:** Local optimization creates global friction. Individual decisions work in isolation but clash downstream.

**Example (repo governance):**  
Connect: We decided in DECISIONS.md that governance should be transparent and fail clearly. A silent-fail hook violates that principle.  
Downstream: If the pre-commit hook is opaque, future developers won't trust it. We'd need to compensate with CI checks.

---

### Stage 5: Commit/Pause

**The trigger question:** **Is there one question that would change everything?**

If **YES** → Pause. Answer that question first. Go back to Stage 1 with new facts.  
If **NO** → Commit. Write explicit rationale and set a next review checkpoint.

**Failure if skipped:** Action happens without conviction, or delay happens without reason. You can't tell the difference between "we decided this was right" and "we're stuck."

**Example (governance hook):**  
Change-everything question: "Can we guarantee Python is always available in the commit hook environment?"  
Answer: No, not without configuration.  
Next step: Add explicit PATH detection and graceful fallback. Now commit with that rationale.

---

## Pause Triggers

Auto-trigger a Stage 5 re-loop (go back to Inform) if you encounter:

- **Unknown fact emerges:** "Oh, GitHub Desktop doesn't inherit shell PATH"
- **New stakeholder input:** Someone whose decision would break if they knew this
- **Constraint violation:** The decision violates a principle you haven't questioned in a while
- **Reversibility drops:** "Actually, changing this later will be much harder than we thought"

These are red flags that Stage 1–4 need revisiting.

---

## How to Log It

Document final decisions in `DECISIONS.md`:

```
[2026-04-15]: Pre-commit hook enforces governance checks before commit — catches structural violations early.
Why: Stage 5 question ("Is PATH guaranteed?") led us to explicit python detection with fallback.
```

Include:
- What was decided
- Why (especially if it answered a Stage 5 question)
- When to revisit (if there's a natural checkpoint)

---

## Emergency Exception

If Stage 1 facts are already known and Stage 5 reveals no change-everything questions, you can compress Stages 2–4 into **rapid compare**: still required, still explicit, just faster (5 minutes instead of 30).

Do NOT skip to Commit without at least acknowledging Stages 2–4, even if you compress them.
