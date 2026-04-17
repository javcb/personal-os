---
title: Finance & Economics
type: domain-context
audience: self
status: active
domain: finance-economics
last-updated: 2026-04-17
related:
  - /docs/domains/professional-advisory.md
  - /docs/domains/legal-regulatory.md
  - /docs/domains/strategy-planning.md
  - /_core/models.md
---

# Finance & Economics

Domain for managing personal wealth, tax planning, investment decisions, and financial strategy as a CPA.

---

## Purpose & Scope

**Why this domain matters:**

As a CPA and finance professional, financial resilience is foundational to family stability and long-term legacy. This domain covers personal and household financial decision-making, tax optimization, wealth management, and financial strategy. It bridges technical tax knowledge with life priorities and risk tolerance.

**What is in scope:**
- Personal and household budgeting
- Tax planning and filing strategy
- Investment decisions and asset allocation
- Debt management and credit
- Insurance and risk coverage
- Long-term wealth and estate planning
- Cash flow and liquidity management
- Financial goal setting and tracking

**What is explicitly out of scope:**
- Client financial advisory work (see professional-advisory domain)
- Regulatory compliance for businesses (see legal-regulatory)
- General economics or market commentary
- Other people's finances (except household aggregation)

---

## Key Models & Frameworks

**Mental models you apply in this domain:**
- **Cash flow hierarchy**: Operating cash flow → emergency reserves → debt service → investments → lifestyle inflation. Each layer is a prerequisite for the next.
- **Tax-efficient sequencing**: Understanding marginal tax brackets, timing of income/losses, and investment location (taxable vs. tax-deferred) to minimize lifetime tax burden.
- **Risk tolerance vs. actual behavior**: Theoretical risk tolerance differs from real-world behavior under stress. Actual portfolio must account for behavioral discipline, not aspiration.
- **Time value of money**: Present value of future cash flows; understanding discount rates and opportunity costs in investment decisions.
- **Reversibility**: Distinguish between reversible financial decisions (changing allocation) and irreversible ones (selling appreciated assets, taking debt). Irreversible decisions require full protocol.

**Key concepts:**
- **Hard constraints**: No single subscription can be a single point of failure; default to free, portable, open formats. Applies to financial tools and processes.
- **Resilience over growth**: Build stable income and reserves before chasing returns. Family stability and independence matter more than wealth maximization.
- **Documentation discipline**: No major financial or legal decision without written rationale. Written decisions are auditable, reversible, and teachable to family.

---

## Operating Rules & Decision Protocols

**Rules that govern work in this domain:**

1. **No financial decision without written rationale** — Every financial choice affecting family stability must have documented assumptions, options considered, and decision criteria. This includes transfers, allocations, and structural changes.

2. **Irreversible decisions require full protocol** — Major decisions (selling appreciating assets, taking on long-term debt, changing contribution strategies) must run through the 5-Stage Decision Protocol and include a cooling-off period before execution.

3. **Tax optimization is ongoing, not seasonal** — Year-round tax planning (harvest losses, time income, charitable giving) is more effective than once-a-year filing cleanup. Build this into quarterly reviews.

4. **Privacy audit on anything touching client information** — Ensure no personal financial data, client data, or business financials are mixed or exposed in systems.

5. **Default to conservative estimates** — In projections and scenarios, use conservative tax assumptions, inflation rates, and return assumptions. Better to over-reserve than under-plan.

**Decision protocol (if applicable):**

If a financial opportunity or decision arises:
1. Write down the decision: what are the options, what are the financial and non-financial trade-offs?
2. Check _core/models.md for relevant frameworks (tax efficiency, reversibility, risk tolerance).
3. Run through 5-Stage Decision Protocol (CLAUDE.md).
4. If irreversible, allow 48-hour cooling-off period before committing.
5. Document the rationale and file in _core/ for future reference.
6. If the decision touches family or legal implications, verify with professional advisors before finalizing.

---

## Autonomy Boundaries

**Reference from autonomy-matrix.md:**

| Action Type | Autonomy | Notes |
|---|---|---|
| Analysis | AI → Review | Financial data requires verification; AI can process but Javier's expertise must validate conclusions |
| Drafting/Proposals | AI → Review | AI can draft scenarios, frameworks, decision templates; Javier reviews and adjusts |
| Execution | Human | All financial transactions, transfers, and commitments are Javier's only |
| Final Decision | Human | Financial decisions carry direct tax and wealth consequences; Javier decides |

**What this means in practice:**

LLMs can analyze financial questions (calculate scenarios, explain tax concepts, summarize options) but must flag for review. LLMs can draft decision templates or scenario analyses. But no LLM should execute financial transactions, propose specific allocations to Javier, or make final calls on spending/saving/investing trade-offs. The CPA expertise and family context are Javier's domain.

---

## Pipelines & Knowledge Ingestion

**Pipelines that feed this domain:**

- **Tax & Regulatory Updates Pipeline** → Monitors tax law changes, deadline updates, IRS guidance; ingests to docs/knowledge-extracts/finance-economics/tax-updates/
- **Investment & Economic Research Pipeline** → Aggregates investment research, economic indicators, market analysis; stores in docs/knowledge-extracts/finance-economics/research/
- **Financial Planning Pipeline** → Tracks annual reviews, goal progress, rebalancing decisions; documents in docs/knowledge-extracts/finance-economics/planning/

**Knowledge sources:**

- IRS.gov, Treasury guidance, tax law updates — kept current quarterly
- Investment research platforms and economic data — reviewed quarterly
- Professional networks and CPA community resources — ongoing

**Integration triggers:**

- When tax law changes: Run tax-updates pipeline; propose amendments to this domain file.
- When new financial goal emerges: Add to _core/initiatives.md; cross-reference in strategy-planning.md
- Quarterly: Review prior quarter's financial decisions, document learnings, update this domain context.

---

## Related Skills & Workflows

**Meta-skills that apply here:**

- `internal-first-research.md` — Use when researching tax questions or financial scenarios; check this domain's canon first, then external sources.
- `session-debrief.md` — Any financial decision or analysis should surface as durable takeaway if it affects future planning.

**Domain-specific workflows:**

- (Planned) Annual tax planning workflow
- (Planned) Quarterly financial review and rebalancing
- (Planned) Major financial decision template (reversibility check, trade-off analysis)

**Pipelines:**

- /docs/pipelines/knowledge-ingestion.md — General pipeline for ingesting financial content

---

## Where to Look

**High-velocity reference for this domain:**

| What | Where |
|---|---|
| Tax rules, thresholds, deadlines | docs/knowledge-extracts/finance-economics/ (when created) |
| Investment decision framework | _core/models.md (investment section, when created) |
| Current financial state & goals | _core/self-model.md (Financial Context section) |
| Prior financial decisions and rationale | docs/knowledge-extracts/finance-economics/decisions/ (when created) |
| Long-term financial strategy | _core/roadmap.md (strategy-planning phase) |
| Professional advisor contacts | _core/self-model.md (trusted advisors, when added) |

---

## Quick Reference (Optional)

**Checklist for financial decisions in this domain:**

- [ ] Is this reversible or irreversible? (If irreversible, use full decision protocol)
- [ ] Have I checked the latest tax guidance or investment context?
- [ ] What are the financial AND non-financial trade-offs?
- [ ] Does this align with long-term family financial resilience goals?
- [ ] Have I written down the decision and rationale?
- [ ] If touching family or legal, have I consulted professional advisors?

---

*Domain-context files are living documents. Review quarterly or after major financial changes.*
