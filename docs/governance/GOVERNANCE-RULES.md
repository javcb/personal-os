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
- Governance singleton files (`GOVERNANCE-README.md`, `GOVERNANCE-RULES.md`, `GOVERNANCE-CHANGE-LOG.md`) must be located exclusively in `docs/governance/`.
- Broken internal markdown links now block commits (enforced via `check_broken_links`).

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

- **Duplicate filenames are forbidden repo-wide by default.** All filenames must be globally unique.
- **Only exception: `.gitkeep`** (git convention for preserving empty directories).
- Markdown files must use **lowercase kebab-case** naming (e.g., `academic-context.md`, not `AcademicContext.md` or `academic_context.md`).
  - Exception: Reserved/singleton names are allowed to be uppercase (e.g., `README.md`, `GOVERNANCE-RULES.md`).
  - Reserved names: `README.md`, `CLAUDE.md`, `inbox.md`, `DECISIONS.md`, `.gitattributes`, `GOVERNANCE-README.md`, `GOVERNANCE-RULES.md`, `GOVERNANCE-CHANGE-LOG.md`.
- Rationale: 
  - Globally unique filenames improve clarity for humans and AI. They reduce ambiguity during retrieval.
  - Consistent naming conventions (kebab-case) make files discoverable and predictable.
  - Reserved uppercase names signal structural importance (e.g., governance, configuration, decision logs).

### Planned rules

- (TBD) Directory names follow the same kebab-case pattern. Not yet enforced.

---

## 4. Governed Subtrees

A **governed subtree** is a directory that functions as its own self-contained system with its own documentation, rules, and change log. Each governed subtree has reserved manifest filenames that are globally unique and must appear only within that subtree.

### Active rules

- **docs/governance/** is the first and currently only governed subtree.
  - **Required files** (all three must exist):
    - `GOVERNANCE-README.md` — Philosophy and usage of the governance layer
    - `GOVERNANCE-RULES.md` — All governance rules and how to update them
    - `GOVERNANCE-CHANGE-LOG.md` — Dated record of governance changes
  - These filenames are globally unique and may not appear outside this directory.
  - These files document the governance system itself and must be kept in sync with the enforcement code in `scripts/governance-check.py`.

### How to add a new governed subtree (future)

Other directories (e.g., `_core/`, `docs/pipelines/`) may become governed subtrees in the future if they develop their own rules and documentation.

**To designate a new governed subtree:**

1. In `scripts/governance-check.py`, update the `GOVERNED_SUBTREES` configuration:
   ```python
   GOVERNED_SUBTREES = {
       "docs/governance": { ... },  # existing
       "your/new/subtree": {
           "required_files": {
               "YOUR-README.md",
               "YOUR-RULES.md",
               "YOUR-CHANGE-LOG.md",
           }
       }
   }
   ```

2. Create all required manifest files in that directory with proper YAML frontmatter.

3. Update the "Governed Areas" table in the root `README.md` to list the new subtree.

4. Add an entry to this section (Section 4) in `GOVERNANCE-RULES.md` documenting the new subtree.

5. Update `GOVERNANCE-CHANGE-LOG.md` with a dated entry explaining the new designation.

6. Run `python3 scripts/governance-check.py` to verify all required files exist and enforcement passes.

**Rationale:** Making governed subtrees explicit prevents silent missing documentation and teaches future-me exactly which folders are "special areas" with their own local structure.

---

## 5. Durable Documentation & Frontmatter

### Active rules

- Every `.md` file in `docs/` must start with valid YAML frontmatter enclosed in `---` markers.
- Required frontmatter fields (minimum): `title`, `type`, `status`.
- Frontmatter must be well-formed (exactly two `---` delimiters; valid YAML syntax).

### Planned rules

- (TBD) Recommend (but don't enforce) additional frontmatter fields for discoverability: `domain`, `audience`, `quadrant`, `last-updated`, `related`.
- (TBD) All files in `_core/` should have frontmatter (similar to docs/ files). Currently not enforced.

---

## 6. Content Quality & File Completeness

### Active rules

- Empty or stub files are forbidden: all `.md` files must have at least 5 meaningful lines (non-empty, non-comment lines).
  - **Exception**: Files containing only YAML frontmatter (no body content) are allowed (e.g., placeholder files that will be filled later).
- **Broken internal markdown links now block commits.** All markdown links (in format `[description](relative/path)`) must point to files that exist. External links (http/https) and anchors (#) are skipped.
  - Rationale: Broken links degrade usability and documentation quality. Fix them before committing.

### Planned rules

- (Speculative) Generated or AI-written content should be marked in frontmatter (e.g., `generated-by: claude-code`, `ai-generated: true`). Useful for auditing but not yet enforced.

---

## How to Update These Rules

1. If you're adding a new **active rule** (code enforcement):
   - Add it to this file under the relevant category, with a clear description.
   - Implement the check in `scripts/governance-check.py`.
   - Update `docs/governance/GOVERNANCE-CHANGE-LOG.md` with date, rule name, and reason.
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
