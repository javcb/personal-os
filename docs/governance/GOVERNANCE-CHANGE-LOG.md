---
title: Governance Change Log
type: reference
status: active
---

# Governance Change Log

Record of changes to governance rules, policies, and enforcement code.

---

**2026-04-15** – Completed introduction of "governed subtrees" concept: now discoverable in root README and fully documented.
- Added "Governed Areas" section to root README.md listing all current governed subtrees and their required files.
- Enhanced GOVERNANCE-RULES.md Section 4 with explicit step-by-step process for adding new governed subtrees in the future.
- Clarified that GOVERNED_SUBTREES configuration in scripts/governance-check.py is the authoritative source.
- Rationale: Future-me and AI tools now have a central place (root README) to see which directories are "special areas" with their own structure, without needing to grep the codebase or remember governance rules.

**2026-04-15** – Introduced "governed subtrees" concept and enforced it for docs/governance/.
- Defined "governed subtree" in GOVERNANCE-RULES.md (Section 4): a directory that functions as its own self-contained system with its own documentation, rules, and change log.
- docs/governance/ is now the first and only governed subtree. It is required to have all three manifest files:
  - GOVERNANCE-README.md
  - GOVERNANCE-RULES.md
  - GOVERNANCE-CHANGE-LOG.md
- Added `GOVERNED_SUBTREES` configuration in `scripts/governance-check.py` (top-level constants section) to make it easy to add new governed subtrees in the future.
- Added Check 4 `check_governed_subtree_manifests()` to enforce that all required manifest files are present in each governed subtree.
- This is a foundation for future structure: _core/, docs/pipelines/, or other directories can become governed subtrees by declaring their own manifest filenames.
- Rationale: Some directories may evolve into their own self-contained systems with governance needs. This provides a pattern and enforcement mechanism without forcing boilerplate on every folder.

**2026-04-15** – Comprehensive governance hardening: enforcement is now self-documenting and blocking.
- Enhanced `scripts/governance-check.py` from 6 to 8 active checks:
  - Check 1: Root-level files (improved messaging)
  - Check 2: Duplicate filenames (tightened: only .gitkeep exempt)
  - Check 3: Governance singletons (new) — ensures GOVERNANCE-*.md files are only in docs/governance/
  - Check 4: Docs frontmatter (improved messaging)
  - Check 5: Build artifacts (improved messaging)
  - Check 6: Empty stubs (improved messaging)
  - Check 7: Broken links (upgraded from WARN to FAIL) — now blocks commits
  - Check 8: Naming conventions (new) — enforces lowercase kebab-case for markdown files, with reserved names allowed to be uppercase
- Created `.git/hooks/pre-push` as a second enforcement layer (mirrors pre-commit governance checks).
- Updated `GOVERNANCE-RULES.md`:
  - Section 1: Added governance singleton rule and broken links rule
  - Section 3: Moved kebab-case naming from Planned to Active rules
  - Section 5: Documented that broken links now block commits
- Improved all failure messages in governance-check.py:
  - Each violation now references the relevant section in GOVERNANCE-RULES.md
  - Messages explain "why" the rule exists, not just "what" is wrong
  - Exceptions are explicitly listed in error messages
- Configuration: Added TOP-level constants (ROOT_ALLOWED_FILES, GOVERNANCE_SINGLETONS, RESERVED_NAMES) for easy maintenance.
- Rationale: Governance should be strict, self-documenting, and teach the repo model through enforcement. Silent failures are no longer acceptable.

**2026-04-15** – Tightened duplicate filename enforcement and renamed governance docs to globally unique filenames.
- Renamed governance documentation files to globally unique names: `README.md` → `GOVERNANCE-README.md`, `rules.md` → `GOVERNANCE-RULES.md`, `change-log.md` → `GOVERNANCE-CHANGE-LOG.md`.
- Updated all references to renamed files in: `scripts/governance-check.py`, `.git/hooks/pre-commit`, and within governance docs themselves.
- Tightened duplicate filename enforcement: removed `README.md` and `index.md` from exceptions. Only `.gitkeep` is now exempt (git convention for preserving empty directories).
- Added section to `GOVERNANCE-README.md` explaining why globally unique filenames matter: they reduce ambiguity, improve retrieval for humans and AI, and make central documents unmistakable.
- Updated `GOVERNANCE-RULES.md` Section 3 (Naming Conventions) to document the new active rule: duplicate filenames forbidden repo-wide by default, with rationale.
- Rationale: Filenames themselves should communicate identity. This prevents silent sprawl and reduces cognitive load for navigation and search.

---

**2026-04-15** – Initial governance shell created (README.md, rules.md, change-log.md).
- Documented six currently-active checks from `scripts/governance-check.py`: root .md files, duplicate filenames, docs frontmatter, build artifacts, empty stubs, and broken links.
- Marked TBD / Planned rules for future enforcement (frontmatter in _core/, root-level Python files, naming conventions, generated content markers).
- Added header comment to `scripts/governance-check.py` pointing to `docs/governance/GOVERNANCE-RULES.md` as source of truth.
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
