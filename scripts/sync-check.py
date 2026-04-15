#!/usr/bin/env python3
"""
Detect duplicate or highly similar .md files in the repo.
Reports matches but does NOT auto-delete.
"""

import os
import sys
from pathlib import Path
from difflib import SequenceMatcher

def get_text_files():
    """Collect all .md files in the repo"""
    files = []
    for root, dirs, filenames in os.walk("."):
        dirs[:] = [d for d in dirs if d != ".git"]

        for filename in filenames:
            if filename.endswith(".md"):
                filepath = os.path.join(root, filename)
                files.append(filepath)

    return files

def get_content(filepath):
    """Read and normalize file content"""
    try:
        content = Path(filepath).read_text(encoding="utf-8", errors="ignore")
        # Normalize whitespace for comparison
        return " ".join(content.split())
    except Exception as e:
        print(f"Warning: Could not read {filepath}: {e}")
        return ""

def similarity_ratio(str1, str2):
    """Calculate similarity between two strings (0-1)"""
    return SequenceMatcher(None, str1, str2).ratio()

def main():
    """Find and report similar files"""
    files = get_text_files()

    if not files:
        print("No .md files found")
        return

    print(f"Checking {len(files)} files for similarity...")
    print()

    similar_groups = []
    checked = set()

    for i, file1 in enumerate(files):
        if file1 in checked:
            continue

        content1 = get_content(file1)
        if not content1:
            continue

        group = [file1]

        for file2 in files[i + 1 :]:
            if file2 in checked:
                continue

            content2 = get_content(file2)
            if not content2:
                continue

            ratio = similarity_ratio(content1, content2)

            if ratio > 0.8:  # >80% similarity threshold
                group.append((file2, ratio))
                checked.add(file2)

        if len(group) > 1:
            similar_groups.append(group)
            checked.add(file1)

    if similar_groups:
        print(f"⚠️  Found {len(similar_groups)} group(s) of similar files:\n")

        for idx, group in enumerate(similar_groups, 1):
            base_file = group[0]
            print(f"Group {idx}: {base_file}")

            for other_file, ratio in group[1:]:
                similarity_pct = int(ratio * 100)
                print(f"  └─ {other_file} ({similarity_pct}% match)")

            print()

        print("⚠️  Manual review recommended. No files were deleted.")
    else:
        print("✅ No significantly similar files detected")

if __name__ == "__main__":
    main()
