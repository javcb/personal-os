---
title: Governance
type: reference
status: active
---

# Governance

This folder documents the governance rules for personal-os: the structural and content standards that keep the repo from becoming a sprawling mess.

## What is governance?

Governance means making rules explicit so that:
- I (Javier) can evolve the repo without accidentally breaking structure
- Future sessions know what's allowed and what's forbidden
- AI tools can read the rules before editing and catch mistakes before they get committed

Governance is **not** about micromanaging every file. It's about preventing silent sprawl (random files appearing in random places) and keeping the repo safe to work in over the long term.

## What does this governance cover?

- **File placement**: Where different types of files belong (_core/ for context, docs/ for permanent knowledge, etc.)
- **Naming conventions**: Patterns for file names, directory names, and slugs
- **Allowed root files**: What files are allowed to live at the repo root (README, CLAUDE.md, etc.)
- **Durable documentation**: YAML frontmatter standards so files are discoverable and maintainable
- **Future constraints**: Planned rules that will be enforced once I finalize the spec

## How does it work?

```
┌─ Local pre-commit hook (.git/hooks/pre-commit)
│  └─ Runs scripts/governance-check.py before every commit
│     └─ Checks against rules defined in docs/governance/GOVERNANCE-RULES.md
│        └─ Blocks commits if violations are found (exit code 1)
│           Allows commits if all checks pass (exit code 0)
```

Later, GitHub branch protection rules and CI workflows can enforce the same rules remotely. For now, the pre-commit hook is the enforcement layer.

## Why Globally Unique Filenames?

Central governance documents and all files in this repo use globally unique names (e.g., `GOVERNANCE-RULES.md` instead of `rules.md`). This matters because:

- **Reduces ambiguity**: When you search for "governance rules", there's no confusion about which file you need.
- **Improves retrieval**: Humans and AI tools can identify files by name alone, without needing directory context.
- **Makes central documents unmistakable**: Critical governance and decision files are self-identifying through their names.

This is why `docs/governance/` files are named `GOVERNANCE-README.md`, `GOVERNANCE-RULES.md`, etc., rather than sharing names with directory-scoped files elsewhere.

## How to use this folder

**If you're writing code or editing files:**
1. Read `docs/governance/GOVERNANCE-RULES.md` to understand what's required and what's forbidden.
2. Don't silently violate rules. If a rule would block your work, talk to it first (update the rule in GOVERNANCE-RULES.md + GOVERNANCE-CHANGE-LOG.md, and update the code that enforces it).

**If you're an AI tool (Claude, etc.) editing this repo:**
1. Read `docs/governance/GOVERNANCE-RULES.md` before you start.
2. Assume all rules are real constraints, not suggestions.
3. If a rule needs to change, update `GOVERNANCE-RULES.md` AND `GOVERNANCE-CHANGE-LOG.md` AND the code that enforces it, in the same commit.
4. If a rule is marked "TBD" or "Planned", ask Javier before enforcing it.

**If you're changing the rules:**
1. Update `docs/governance/GOVERNANCE-RULES.md` to document the change.
2. Update the enforcement code (usually `scripts/governance-check.py`).
3. Add an entry to `docs/governance/GOVERNANCE-CHANGE-LOG.md` with today's date and a one-line summary.
4. All three changes go in the same commit.

## What about later?

As this repo grows, governance might include:
- **CI/CD enforcement**: GitHub Actions running governance checks on pull requests.
- **Branch protection rules**: Enforcing that every commit passes governance.
- **Automated linting**: Pre-commit hooks that auto-fix common violations (formatting, frontmatter, etc.).

For now, these are aspirational. The local pre-commit hook + this documentation are the foundation.
