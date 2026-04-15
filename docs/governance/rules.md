---
title: Governance Rules
type: reference
status: active
---

# Governance Rules

Rules are organized by category and split into two groups:

- **Active rules**: Currently enforced by `scripts/governance-check.py`. Violations block commits.
- **Planned rules**: Documented intent for future enforcement. Not yet enforced. Marked clearly as TBD.

## 1. Repository Layout & File Placement

### Active rules

- All `.md` files in `docs/` must have YAML frontmatter with (at minimum) `title`, `type`, and `status` fields.
- `.md` files at the root level are forbidden, except: `README.md`, `CLAUDE.md`, `inbox.md`, `DECISIONS.md`, and `.gitattributes`.
- Build artifacts are forbidden: no files ending in `.log` or `-REPORT.md` anywhere in the repo.

### Planned rules

- (TBD) Files in `_core/` directory should follow the same frontmatter standard as `docs/` (currently not enforced).
- (TBD) Python scripts at the root level should be forbidden (scripts belong in `scripts/`). Currently not enforced.
- (Speculative, needs Javier's confirmation) All top-level directories should have a clear purpose; catch new directories that don't fit the model.

---

## 2. Root-Level Files (Allowed / Forbidden)

### Active rules

- Allowed at root:
  - `README.md` — repo overview
  - `CLAUDE.md` — project instructions for Claude / AI tools
  - `inbox.md` — capture-only inbox for unprocessed ideas
  - `DECISIONS.md` — structured log of architectural decisions
  - `.gitattributes` — git configuration
- **Forbidden** at root: all other `.md` files.
- **Forbidden** at root: build artifacts (`.log`, `-REPORT.md`).

### Planned rules

- (Speculative) Config files (`.json`, `.yml`, `.toml`) belong in specific directories, not root (needs scope clarification).

---

## 3. Naming Conventions

### Active rules

- (TBD / Confirm later) Duplicate filenames are forbidden throughout the repo, with exceptions:
  - `.gitkeep` (allowed in any directory)
  - `README.md` (allowed once per directory)
  - `index.md` (allowed in multiple documentation directories)

### Planned rules

- (Speculative) File slugs should use kebab-case (e.g., `academic-context.md`, not `AcademicContext.md`). Not yet enforced.
- (TBD) Directory names follow the same kebab-case pattern. Not yet enforced.

---

## 4. Durable Documentation & Frontmatter

### Active rules

- Every `.md` file in `docs/` must start with valid YAML frontmatter enclosed in `---` markers.
- Required frontmatter fields (minimum): `title`, `type`, `status`.
- Frontmatter must be well-formed (exactly two `---` delimiters; valid YAML syntax).

### Planned rules

- (TBD) Recommend (but don't enforce) additional frontmatter fields for discoverability: `domain`, `audience`, `quadrant`, `last-updated`, `related`.
- (TBD) All files in `_core/` should have frontmatter (similar to docs/ files). Currently not enforced.

---

## 5. Content Quality & File Completeness

### Active rules

- Empty or stub files are forbidden: all `.md` files must have at least 5 meaningful lines (non-empty, non-comment lines).
- **Exception**: Files containing only YAML frontmatter (no body content) are allowed (e.g., placeholder files that will be filled later).
- Broken internal links are **not** enforced; they are reported as warnings and do not block commits.

### Planned rules

- (Speculative) Generated or AI-written content should be marked in frontmatter (e.g., `generated-by: claude-code`, `ai-generated: true`). Useful for auditing but not yet enforced.

---

## How to Update These Rules

1. If you're adding a new **active rule** (code enforcement):
   - Add it to this file under the relevant category, with a clear description.
   - Implement the check in `scripts/governance-check.py`.
   - Update `docs/governance/change-log.md` with date, rule name, and reason.
   - Test the check locally before committing.

2. If you're adding a **planned rule** (future enforcement):
   - Add it to this file with a `(TBD)` or `(Speculative)` marker.
   - No code change needed yet.
   - Update the change-log if this represents a significant new intent.

3. If you're removing or changing a rule:
   - Update this file first.
   - Update the code (if active rule).
   - Update the change-log.
   - Commit all three together.
