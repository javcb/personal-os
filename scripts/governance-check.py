#!/usr/bin/env python3
"""
Governance check for personal-os repo.
Enforces structural and content quality standards.

This script is the enforcement arm of personal-os governance.
Human-readable rules and policy are in: docs/governance/GOVERNANCE-RULES.md

Important: If you change the behavior of this script, also update:
  - docs/governance/GOVERNANCE-RULES.md (document what changed)
  - docs/governance/GOVERNANCE-CHANGE-LOG.md (date and reason for the change)
  - Commit all three changes together.

For details on governance philosophy, see: docs/governance/GOVERNANCE-README.md
"""

import os
import sys
import re
from pathlib import Path
from collections import defaultdict

# Fix Windows console encoding for unicode
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Governance configuration: root-level files allowed by policy
ROOT_ALLOWED_FILES = {
    "README.md",           # Repo overview
    "CLAUDE.md",           # AI tool instructions
    "inbox.md",            # Unprocessed ideas
    "DECISIONS.md",        # Architectural decision log
    ".gitattributes",      # Git configuration
}

# Governed subtrees: directories that function as their own self-contained systems
# with their own documentation, rules, and change logs.
# Each subtree has reserved manifest filenames (globally unique) that must appear
# only within that subtree and must all be present together.
#
# To add a new governed subtree (e.g., _core/):
#   1. Add an entry here with the directory path and manifest filenames
#   2. Update GOVERNANCE-RULES.md to document the new subtree
#   3. Update GOVERNANCE-CHANGE-LOG.md with the change
#
GOVERNED_SUBTREES = {
    "docs/governance": {
        "manifests": {
            "README": "GOVERNANCE-README.md",
            "RULES": "GOVERNANCE-RULES.md",
            "CHANGE_LOG": "GOVERNANCE-CHANGE-LOG.md",
        },
        "description": "Personal-os governance layer: rules, philosophy, and change history"
    },
}

# Governance singletons: all reserved manifest filenames across all governed subtrees
# These filenames are globally unique and may only appear in their designated subtrees
GOVERNANCE_SINGLETONS = {
    "GOVERNANCE-README.md",
    "GOVERNANCE-RULES.md",
    "GOVERNANCE-CHANGE-LOG.md",
}

# Filename pattern: lowercase kebab-case for regular content files
# Exceptions: the explicitly reserved names above
RESERVED_NAMES = ROOT_ALLOWED_FILES | GOVERNANCE_SINGLETONS

def check_root_md_files():
    """Check 1: Root-level .md files restricted to allowlist"""
    root = Path(".")
    violations = []

    for file in root.glob("*.md"):
        if file.name not in ROOT_ALLOWED_FILES:
            violations.append(
                f"Root .md file '{file.name}' not allowed. "
                f"Allowed: {', '.join(sorted(ROOT_ALLOWED_FILES))}. "
                f"See docs/governance/GOVERNANCE-RULES.md Section 2."
            )

    # Check .gitattributes
    gitattributes = root / ".gitattributes"
    if gitattributes.exists() and gitattributes.name not in ROOT_ALLOWED_FILES:
        violations.append(
            f"Root config file '{gitattributes.name}' not allowed. "
            f"See docs/governance/GOVERNANCE-RULES.md Section 2."
        )

    return violations

def check_duplicate_filenames():
    """Check 2: No duplicate filenames repo-wide (except .gitkeep)"""
    filenames = defaultdict(list)
    violations = []
    # Only .gitkeep is allowed to duplicate (git convention for preserving empty dirs)
    ignore_files = {".gitkeep"}

    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d != ".git"]
        for file in files:
            if file in ignore_files:
                continue
            filenames[file].append(os.path.join(root, file))

    for filename, paths in filenames.items():
        if len(paths) > 1:
            violations.append(
                f"Duplicate filename '{filename}' found at multiple locations: {', '.join(paths)}. "
                f"Filenames must be globally unique. See docs/governance/GOVERNANCE-RULES.md Section 3."
            )

    return violations

def check_governance_singletons():
    """Check 3: Governance singleton files must be in docs/governance/ only"""
    violations = []

    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d != ".git"]
        for file in files:
            if file in GOVERNANCE_SINGLETONS:
                full_path = Path(root) / file
                expected_path = Path("docs") / "governance" / file
                # Normalize for comparison (handles Windows backslashes)
                if full_path.resolve() != expected_path.resolve():
                    violations.append(
                        f"Governance singleton '{file}' found at {full_path}. "
                        f"Must be located only in docs/governance/. "
                        f"See docs/governance/GOVERNANCE-RULES.md Section 1."
                    )

    return violations

def check_governed_subtree_manifests():
    """Check 4: Each governed subtree must have all required manifest files"""
    violations = []

    for subtree_path, config in GOVERNED_SUBTREES.items():
        subtree_dir = Path(subtree_path)
        if not subtree_dir.exists():
            # Subtree directory doesn't exist yet; skip check
            continue

        manifests = config["manifests"]
        for manifest_key, manifest_filename in manifests.items():
            manifest_path = subtree_dir / manifest_filename
            if not manifest_path.exists():
                violations.append(
                    f"Governed subtree '{subtree_path}' missing required manifest: {manifest_filename}. "
                    f"All manifest files must exist: {', '.join(manifests.values())}. "
                    f"See docs/governance/GOVERNANCE-RULES.md Section 4."
                )

    return violations

def check_frontmatter_in_docs():
    """Check 5: Every .md in docs/ has YAML frontmatter with title, type, status"""
    violations = []
    docs_path = Path("docs")

    if not docs_path.exists():
        return violations

    for md_file in docs_path.rglob("*.md"):
        if md_file.name in {".gitkeep"}:
            continue

        content = md_file.read_text(encoding='utf-8')

        # Check for YAML frontmatter
        if not content.startswith("---"):
            violations.append(
                f"Missing frontmatter in {md_file}. "
                f"All .md files in docs/ must have YAML frontmatter. "
                f"See docs/governance/GOVERNANCE-RULES.md Section 4."
            )
            continue

        # Extract frontmatter
        try:
            _, frontmatter, _ = content.split("---", 2)
        except ValueError:
            violations.append(
                f"Malformed frontmatter in {md_file}. "
                f"Frontmatter must be enclosed in exactly two '---' delimiters. "
                f"See docs/governance/GOVERNANCE-RULES.md Section 4."
            )
            continue

        # Check required fields
        required_fields = {"title", "type", "status"}
        found_fields = set()

        for line in frontmatter.split("\n"):
            if ":" in line:
                field = line.split(":")[0].strip()
                found_fields.add(field)

        missing = required_fields - found_fields
        if missing:
            violations.append(
                f"Missing frontmatter fields in {md_file}: {', '.join(sorted(missing))}. "
                f"Required fields: {', '.join(sorted(required_fields))}. "
                f"See docs/governance/GOVERNANCE-RULES.md Section 4."
            )

    return violations

def check_build_artifacts():
    """Check 6: No build artifacts (.log, -REPORT.md)"""
    violations = []

    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d != ".git"]
        for file in files:
            if file.endswith(".log") or file.endswith("-REPORT.md"):
                violations.append(
                    f"Build artifact '{os.path.join(root, file)}' found. "
                    f"Machine-generated files (.log, -REPORT.md) are forbidden. "
                    f"See docs/governance/GOVERNANCE-RULES.md Section 1."
                )

    return violations

def check_empty_stubs():
    """Check 7: No empty or stub .md files (must have >= 5 meaningful lines)"""
    violations = []

    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d != ".git"]
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                content = Path(filepath).read_text(encoding='utf-8')

                # Count meaningful lines (non-empty, non-whitespace, non-comment)
                meaningful_lines = [
                    line for line in content.split("\n")
                    if line.strip() and not line.strip().startswith("#")
                ]

                # Skip if it's frontmatter-only (acceptable placeholder)
                if content.startswith("---"):
                    continue

                if len(meaningful_lines) < 5 and content.strip():
                    # Only flag if it's not just frontmatter
                    if not (content.count("---") >= 2):
                        violations.append(
                            f"Stub file {filepath} has only {len(meaningful_lines)} meaningful lines. "
                            f"All .md files must have at least 5 meaningful lines (frontmatter-only files exempt). "
                            f"See docs/governance/GOVERNANCE-RULES.md Section 5."
                        )

    return violations

def check_broken_links():
    """Check 8: Broken internal markdown links are now failures (not warnings)"""
    violations = []

    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d != ".git"]
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                content = Path(filepath).read_text(encoding='utf-8')

                # Remove inline code blocks (text between backticks) to avoid false positives
                # e.g., `[example](path)` should not be treated as a real markdown link
                content_without_code = re.sub(r'`[^`]*`', '', content)

                # Find markdown links: [text](path)
                links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content_without_code)

                for text, link in links:
                    # Skip external links and anchors
                    if link.startswith("http") or link.startswith("#"):
                        continue

                    # Resolve relative path
                    target = Path(root) / link

                    if not target.exists():
                        violations.append(
                            f"Broken link in {filepath}: [{text}]({link}) → target does not exist. "
                            f"All internal links must point to existing files. "
                            f"See docs/governance/GOVERNANCE-RULES.md Section 5."
                        )

    return violations

def check_naming_conventions():
    """Check 9: Markdown filenames follow kebab-case (except reserved names)"""
    violations = []

    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d != ".git"]
        for file in files:
            if file.endswith(".md"):
                # Skip reserved/singleton names (allowed to be uppercase)
                if file in RESERVED_NAMES:
                    continue

                # Check if filename is kebab-case (lowercase, hyphens, alphanumerics)
                # Pattern: lowercase, numbers, hyphens only; no spaces, underscores, CamelCase
                if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*\.md$', file):
                    violations.append(
                        f"Filename '{file}' does not follow kebab-case convention. "
                        f"Use lowercase with hyphens: e.g., 'my-file.md' not 'MyFile.md' or 'my_file.md'. "
                        f"Exceptions: reserved names ({', '.join(sorted(RESERVED_NAMES))}). "
                        f"See docs/governance/GOVERNANCE-RULES.md Section 3."
                    )

    return violations

def main():
    """Run all checks and report violations"""
    all_violations = []
    all_warnings = []

    checks = [
        ("Root-level files", check_root_md_files),
        ("Duplicate filenames", check_duplicate_filenames),
        ("Governance singletons", check_governance_singletons),
        ("Governed subtree manifests", check_governed_subtree_manifests),
        ("Docs frontmatter", check_frontmatter_in_docs),
        ("Build artifacts", check_build_artifacts),
        ("Empty stubs", check_empty_stubs),
        ("Broken links", check_broken_links),
        ("Naming conventions", check_naming_conventions),
    ]

    # Run all checks
    for check_name, check_func in checks:
        try:
            violations = check_func()
            if violations:
                for violation in violations:
                    all_violations.append((check_name, violation))
        except Exception as e:
            all_warnings.append((check_name, f"Check failed: {str(e)}"))

    # Print formatted output
    print("\n" + "=" * 72)

    if all_violations:
        print("🚫 COMMIT BLOCKED BY GOVERNANCE")
        print("=" * 72)
        print(f"\n[FAIL] {len(all_violations)} governance violation{'s' if len(all_violations) != 1 else ''} found:\n")

        # Group violations by check
        violations_by_check = {}
        for check_name, violation in all_violations:
            if check_name not in violations_by_check:
                violations_by_check[check_name] = []
            violations_by_check[check_name].append(violation)

        for check_name, violations in violations_by_check.items():
            print(f"  [{check_name}]")
            for violation in violations:
                print(f"    • {violation}")
            print()

    if all_warnings:
        print("[WARN] Non-blocking warnings:\n")
        for check_name, warning in all_warnings:
            print(f"  {check_name}: {warning}")
            print()

    # Summary
    print("=" * 72)
    if all_violations:
        error_word = "error" if len(all_violations) == 1 else "errors"
        warn_word = "warning" if len(all_warnings) == 1 else "warnings"
        summary = f"[SUMMARY] {len(all_violations)} {error_word}"
        if all_warnings:
            summary += f", {len(all_warnings)} {warn_word}"
        summary += "."
        print(summary)
        print("\nFix the errors above and commit again.")
        print("=" * 72 + "\n")
        sys.exit(1)
    else:
        if all_warnings:
            warn_word = "warning" if len(all_warnings) == 1 else "warnings"
            print(f"[SUMMARY] All governance checks passed. {len(all_warnings)} {warn_word}.")
        else:
            print("[SUMMARY] All governance checks passed. No errors or warnings.")
        print("=" * 72 + "\n")
        sys.exit(0)

if __name__ == "__main__":
    main()
