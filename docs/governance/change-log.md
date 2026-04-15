---
title: Governance Change Log
type: reference
status: active
---

# Governance Change Log

Record of changes to governance rules, policies, and enforcement code.

---

**2026-04-15** – Initial governance shell created (README.md, rules.md, change-log.md).
- Documented six currently-active checks from `scripts/governance-check.py`: root .md files, duplicate filenames, docs frontmatter, build artifacts, empty stubs, and broken links.
- Marked TBD / Planned rules for future enforcement (frontmatter in _core/, root-level Python files, naming conventions, generated content markers).
- Added header comment to `scripts/governance-check.py` pointing to `docs/governance/rules.md` as source of truth.
- No new enforced rules; documented current behavior only.

---

## Sanity Check

After creating the governance shell, `scripts/governance-check.py` was run to verify no regressions:

```
All governance checks passed. No errors or warnings.
```

Date: 2026-04-15

---

## Planned Future Entries

(Each change to governance should add a dated entry above this line.)
