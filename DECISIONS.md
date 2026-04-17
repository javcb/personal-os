# Decisions Log

A record of structural and design decisions made for the personal-os project.
Each decision includes the date, the choice made, and the reasoning.
Use this to understand major architectural choices and when they were made.

## Entries

[2026-04-15]: Repo structure initialized with _core/ context vault, docs/ knowledge base, and governance scripts to enforce quality standards.
Reason: Establish clear separation between mutable context (_core/) and permanent knowledge (docs/), with automated checks to maintain integrity.

[2026-04-15]: Pre-commit hook and governance checks verified as working; attempted root-level violation was correctly rejected.
Reason: Ensure governance system is active and will prevent accidental structural violations during normal development.

[2026-04-15]: Fixed pre-commit hook shebang to #!/bin/sh and added explicit python path detection for GitHub Desktop compatibility.
Reason: GitHub Desktop doesn't inherit shell PATH, causing python3 lookup to fail; using which to find python explicitly prevents silent failures.

[2026-04-15]: Governance verified — pre-commit hook confirmed working; attempted root-level file rejected with clear violation messages.
Reason: Confirmed the governance layer is functioning end-to-end: violations are detected, reported clearly, and commits are blocked until violations are resolved.

[2026-04-15]: Created meta-skills directory with session-debrief.md and decision-protocol.md — behavior-level, tool-agnostic skill guides.
Reason: Personal OS needs durable skill definitions that work with any tool (AI or human). Meta-skills are about how to approach work, not what tools to use.

[2026-04-15]: Removed docs/meta-skills/ folder — duplicate of docs/skills/_custom/ per CLAUDE.md canonical path.
Reason: Consolidate to single canonical location. CLAUDE.md defines meta-skills belong in docs/skills/_custom/. Governance verified clean.

[2026-04-15]: Improved governance error messaging — blocked commits now clearly explain violations instead of failing opaquely.
Reason: When governance checks fail, users need to understand what broke and why. Added clear headers ("🚫 COMMIT BLOCKED BY GOVERNANCE"), categorized output by check, separated FAIL (blocks) from WARN (advisory), added summary with error/warning counts. Works with terminal and GitHub Desktop.

[2026-04-15]: Added first operational pipeline and template — knowledge ingestion is the first live machine in personal-os.
Reason: Personal OS requires executable pipelines that convert external material into durable, context-aware knowledge. Knowledge Ingestion Pipeline is the canonical machine for this work. Created docs/templates/knowledge-extract.md (template for structured extraction) and docs/pipelines/knowledge-ingestion.md (operational spec with triggers, context load, steps, output locations, rules, and failure modes). Both pass governance.

[2026-04-15]: Added how-to-resume and prompt-index files so Future Javier can restart work from inside personal-os without hunting for old threads.
Reason: Work continuity requires that resumption instructions and prompt locations live in the repo itself, not in separate chat transcripts or external notes. Created _core/how-to-resume.md (daily session pattern, next-action tracking, rules for self) and _core/context/prompt-index.md (pointer map to key prompts without duplicating full prompt text). Added orientation note to _core/roadmap.md. All files pass governance.

[2026-04-15]: Froze governance at v1 (structural hygiene + docs/governance subtree) and parked governance backlog intentionally.
Reason: Governance v1 covers structure and place (file layout, naming, frontmatter, link integrity, governed subtrees). Content-level rules (_core/ subtree, review-by dates, type-specific schemas, orphan-doc detection) are valid but deferred so other work (LLM interfaces, feedback loops, domain expansion) can proceed without constant governance churn. Backlog is explicit and prioritized in GOVERNANCE-RULES.md so Future Javier can pick items deliberately rather than reactively adding checks mid-stream.

[2026-04-17]: _core/roadmap.md is canonical for current state + next priorities; LLMs read it at session start, propose updates via session-debrief, Javier reviews and edits directly.
Reason: Roadmap is the primary resumption mechanism for LLMs. Centralizing state and priorities in a single, structured document eliminates context reconstruction overhead. LLMs become proposal generators, not decision-makers; Javier retains full control over priorities and direction.

[2026-04-17]: Roadmap stays human-curated — session-debrief proposes changes, Javier decides; do not automate roadmap generation from debrief output.
Reason: Automation risks removing prioritization decisions from human control. Roadmap updates involve judgments about tradeoffs, sequencing, and resource allocation that should remain with Javier. Manual curation preserves agency and ensures the system reflects actual intentions, not algorithm defaults.
