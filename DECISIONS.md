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
