#!/usr/bin/env python3
"""
Governance check for personal-os repo.
Enforces structural and content quality standards.

This script is the enforcement arm of personal-os governance.
Human-readable rules and policy are in: docs/governance/rules.md

Important: If you change the behavior of this script, also update:
  - docs/governance/rules.md (document what changed)
  - docs/governance/change-log.md (date and reason for the change)
  - Commit all three changes together.

For details on governance philosophy, see: docs/governance/README.md
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

def check_root_md_files():
    """Check 1: No .md files at root except README.md, CLAUDE.md, inbox.md, DECISIONS.md"""
    root = Path(".")
    # Whitelisted root-level files: content files + config files required at root
    # DECISIONS.md is a root-level structural log; .gitattributes is git configuration
    allowed = {"README.md", "CLAUDE.md", "inbox.md", "DECISIONS.md", ".gitattributes"}
    violations = []

    # Check .md files
    for file in root.glob("*.md"):
        if file.name not in allowed:
            violations.append(f"Root .md file not allowed: {file.name}")

    # Check .gitattributes
    gitattributes = root / ".gitattributes"
    if gitattributes.exists() and gitattributes.name not in allowed:
        violations.append(f"Root config file not allowed: {gitattributes.name}")

    return violations

def check_duplicate_filenames():
    """Check 2: No duplicate filenames anywhere in the repo"""
    filenames = defaultdict(list)
    violations = []
    # Intentional duplicates: directory-scoped files are allowed (README.md per dir)
    ignore_files = {".gitkeep", "README.md", "index.md"}

    for root, dirs, files in os.walk("."):
        # Skip .git directory
        dirs[:] = [d for d in dirs if d != ".git"]

        for file in files:
            if file in ignore_files:
                continue

            filenames[file].append(os.path.join(root, file))

    for filename, paths in filenames.items():
        if len(paths) > 1:
            violations.append(f"Duplicate filename '{filename}' at: {', '.join(paths)}")

    return violations

def check_frontmatter_in_docs():
    """Check 3: Every .md in docs/ has YAML frontmatter with title, type, status"""
    violations = []
    docs_path = Path("docs")

    if not docs_path.exists():
        return violations

    for md_file in docs_path.rglob("*.md"):
        # Skip .gitkeep and other non-content files
        if md_file.name in {".gitkeep"}:
            continue

        content = md_file.read_text(encoding='utf-8')

        # Check for YAML frontmatter
        if not content.startswith("---"):
            violations.append(f"Missing frontmatter: {md_file}")
            continue

        # Extract frontmatter
        try:
            _, frontmatter, _ = content.split("---", 2)
        except ValueError:
            violations.append(f"Malformed frontmatter: {md_file}")
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
            violations.append(f"Missing frontmatter fields {missing} in {md_file}")

    return violations

def check_build_artifacts():
    """Check 4: No build artifacts (*.log, *-REPORT.md)"""
    violations = []

    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d != ".git"]

        for file in files:
            if file.endswith(".log") or file.endswith("-REPORT.md"):
                violations.append(f"Build artifact found: {os.path.join(root, file)}")

    return violations

def check_empty_stubs():
    """Check 5: No empty stub files (under 5 meaningful lines)"""
    violations = []

    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d != ".git"]

        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                content = Path(filepath).read_text(encoding='utf-8')

                # Count meaningful lines (non-empty, non-whitespace)
                meaningful_lines = [
                    line for line in content.split("\n")
                    if line.strip() and not line.strip().startswith("#")
                ]

                # Skip if it's a frontmatter-only file (this is acceptable)
                if content.startswith("---"):
                    continue

                if len(meaningful_lines) < 5 and content.strip():
                    # Only flag if it's not just frontmatter
                    if not (content.count("---") >= 2):
                        violations.append(f"Stub file too short: {filepath} ({len(meaningful_lines)} meaningful lines)")

    return violations

def check_broken_links():
    """Check 6: Broken internal links (report only, don't fail)"""
    warnings = []

    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d != ".git"]

        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                content = Path(filepath).read_text(encoding='utf-8')

                # Find markdown links: [text](path)
                links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)

                for text, link in links:
                    # Skip external links
                    if link.startswith("http") or link.startswith("#"):
                        continue

                    # Resolve relative path
                    target = Path(root) / link

                    if not target.exists():
                        warnings.append(f"Broken link in {filepath}: [{text}]({link})")

    return warnings

def main():
    """Run all checks and report violations"""
    all_violations = []
    all_warnings = []

    checks = [
        ("Root .md files", check_root_md_files),
        ("Duplicate filenames", check_duplicate_filenames),
        ("Docs frontmatter", check_frontmatter_in_docs),
        ("Build artifacts", check_build_artifacts),
        ("Empty stubs", check_empty_stubs),
    ]

    # Run all checks
    for check_name, check_func in checks:
        try:
            violations = check_func()
            if violations:
                for violation in violations:
                    all_violations.append((check_name, violation))
        except Exception as e:
            all_warnings.append((check_name, str(e)))

    # Collect broken links as warnings (don't fail)
    try:
        warnings = check_broken_links()
        if warnings:
            for warning in warnings:
                all_warnings.append(("Broken links", warning))
    except Exception as e:
        all_warnings.append(("Broken links check", str(e)))

    # Print formatted output
    print("\n" + "=" * 72)

    if all_violations:
        print("🚫 COMMIT BLOCKED BY GOVERNANCE")
        print("=" * 72)
        print(f"\n[FAIL] Governance violations found ({len(all_violations)} error{'s' if len(all_violations) != 1 else ''}):\n")

        # Group violations by check
        violations_by_check = {}
        for check_name, violation in all_violations:
            if check_name not in violations_by_check:
                violations_by_check[check_name] = []
            violations_by_check[check_name].append(violation)

        for check_name, violations in violations_by_check.items():
            print(f"  {check_name}:")
            for violation in violations:
                print(f"    • {violation}")
            print()

    if all_warnings:
        print("[WARN] Governance warnings (commit not blocked):\n")
        for check_name, warning in all_warnings:
            print(f"  {check_name}:")
            print(f"    • {warning}")
            print()

    # Summary
    print("=" * 72)
    if all_violations:
        print(f"[SUMMARY] {len(all_violations)} error{'s' if len(all_violations) != 1 else ''}, "
              f"{len(all_warnings)} warning{'s' if len(all_warnings) != 1 else ''}.")
        print("\nFix the errors above and commit again.")
        print("=" * 72 + "\n")
        sys.exit(1)
    else:
        if all_warnings:
            print(f"[SUMMARY] 0 errors, {len(all_warnings)} warning{'s' if len(all_warnings) != 1 else ''}. Commit allowed.")
        else:
            print("[SUMMARY] All governance checks passed. No errors or warnings.")
        print("=" * 72 + "\n")
        sys.exit(0)

if __name__ == "__main__":
    main()
