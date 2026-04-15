# personal-os

A private personal knowledge system built on GitHub + MkDocs.

This repository contains your personal context vault (_core/), knowledge base (docs/),
and automated governance scripts to maintain quality and consistency.
Built with governance checks, backup automation, and content deduplication tools.

## Governed Areas

Some directories in this repo are **governed subtrees**: self-contained areas with their own
local documentation, rules, and change history. These areas explain themselves and enforce
consistency through required manifest files.

**Current governed subtrees:**

| Area | Purpose | Required Files |
|------|---------|---|
| `docs/governance/` | Governance rules and philosophy for the entire repo | `GOVERNANCE-README.md`, `GOVERNANCE-RULES.md`, `GOVERNANCE-CHANGE-LOG.md` |

For details on how governed subtrees work and how to add new ones, see [docs/governance/GOVERNANCE-RULES.md](docs/governance/GOVERNANCE-RULES.md) Section 4.

---

See DECISIONS.md for design choices and architectural overview.