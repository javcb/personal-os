---
title: Governance Rules
type: reference
status: active
---

# Governance Rules

Rules are organized by category and split into two groups:

- **Active rules**: Currently enforced by `scripts/governance-check.py`. Violations block commits.
- **Planned rules**: Documented intent for future enforcement. Not yet enforced. Marked clearly as TBD.

---

## Governance v1 — Current Scope

**Governance v1** focuses on structural hygiene and establishing a clear governance subtree pattern. The following are currently enforced:

- **Root-level file restrictions**: Explicit allowlist of `.md` files permitted at repo root
- **Globally unique filenames**: No duplicates repo-wide (except `.gitkeep`)
- **Docs frontmatter**: Required YAML metadata (title, type, status) in docs/
- **No build artifacts**: Blocks `.log` and `-REPORT.md` files
- **Content completeness**: Minimum 5 meaningful lines per `.md` file (frontmatter-only exempted)
- **Link integrity**: All internal Markdown links must point to existing files
- **Naming conventions**: Lowercase kebab-case for normal files; reserved uppercase names for special documents
- **Governed subtrees**: Established pattern and enforcement for docs/governance/ as the only designated governed subtree

Governance v1 is about **structure and place**, not yet about deep content semantics, authorship metadata, or domain-specific schema validation.

---

## Not Yet Governed (Explicitly Deferred)

The following ideas are intentionally **not** implemented in Governance v1. These are captured here so Future Javier can prioritize them later:

- **_core/ as a governed subtree**: Could have CORE-README.md, CORE-RULES.md, CORE-CHANGE-LOG.md for context vault governance
- **Additional governed subtrees**: docs/pipelines/, docs/templates/, docs/knowledge-extracts/, docs/domains/, etc.
- **Review-by enforcement**: Warning when review-by: dates are overdue (requires timestamp checks)
- **Type-specific schemas**: Extra required frontmatter fields for type: pipeline, type: knowledge-extract, type: meta-skill, type: domain-context, etc.
- **No orphan docs**: Enforce that every non-template doc is reachable from some index or overview
- **Content-level linting**: Grammar, style, tone consistency beyond structural frontmatter
- **Authorship tracking**: Enforcing author: or authored-by: fields in context files
- **Vault-specific rules**: Special handling for _core/ files (frozen content, immutability markers, etc.)
- **Domain enforcement**: Ensuring files are in the correct domain folder based on frontmatter domain: field

These are valid future enhancements but are parked to keep Governance v1 lean and focused.

---

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

## 7. Roadmap Governance

### Active rules

- **`_core/roadmap.md` is human-curated.** LLMs may propose updates via session-debrief output, but Javier reviews and edits the file directly.
- **Automated generation or direct LLM edits to roadmap are not permitted.**
- LLMs read the roadmap at session start to understand current phase and priorities.
- LLM proposals to update roadmap flow through session-debrief structured format (see `/docs/skills/_custom/session-debrief.md`).
- Javier reviews all debrief proposals and decides whether to update the roadmap asynchronously.

### Rationale

Roadmap prioritization is a human judgment call. Prioritization decisions involve tradeoffs, sequencing, and resource allocation that require human judgment and context. Keeping the roadmap human-curated preserves Javier's agency over system direction and prevents the system from autonomously re-prioritizing work based on local optimization.

### Enforcement

**Convention only** (not script-enforced in Governance v1). LLMs are expected to follow this rule by design (session-debrief output is structured for human review, not automatic application). Revisit for script enforcement in a later governance version if violations occur.

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

---

## Governance Backlog

This section tracks governance enhancements intentionally deferred from v1. These are not yet implemented but represent likely future improvements. See "Not Yet Governed (Explicitly Deferred)" above for descriptions.

**Backlog items (in rough priority order):**

1. **Make _core/ a governed subtree** — Establish CORE-README.md, CORE-RULES.md, CORE-CHANGE-LOG.md for context vault governance. Useful once context vault gets complex enough to need its own local structure.

2. **Enforce review-by: dates** — Add a warning (and optionally a failure) if review-by: dates on context files are in the past. Helps identify stale guidance that needs refreshing.

3. **Type-specific schema enforcement** — Require additional frontmatter fields for specific file types (e.g., domain: for domain-context files, trigger: for pipeline files). Improves metadata completeness.

4. **No orphan docs** — Enforce that every non-template doc is reachable from some index or overview. Prevents silent doc decay.

5. **Designate additional governed subtrees** — As docs/pipelines/, docs/templates/, docs/knowledge-extracts/ mature, consider making them governed subtrees with their own manifest files.

6. **Content-level linting** — Add style, grammar, or tone checks beyond frontmatter presence. Low priority unless content becomes a bottleneck.

7. **Vault immutability markers** — Allow _core/ files to be marked as "frozen" so their content cannot change (only metadata/dates can be refreshed). Useful for capturing stable, decision-level content.

8. **Domain enforcement** — Verify that files with domain: field are in the corresponding docs/domains/ folder structure. Prevents cross-domain contamination.

**When to pick up these items:**
- Governance v1 stabilizes the core structure and allows other work (LLM interfaces, feedback loops, domain expansion) to proceed without constant governance changes.
- Backlog items can be tackled once structural foundation is solid.
- Prioritize based on pain: which missing check would catch the most mistakes or save the most cognitive load?
