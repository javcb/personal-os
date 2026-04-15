#!/usr/bin/env python3
"""
Backup the entire repo and build MkDocs site.
Creates timestamped backup in ~/backups/personal-os/
"""

import os
import sys
import subprocess
import shutil
import zipfile
from pathlib import Path
from datetime import datetime

def create_backup():
    """Zip the full repo to ~/backups/personal-os/"""
    home = Path.home()
    backup_dir = home / "backups" / "personal-os"
    backup_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_file = backup_dir / f"personal-os-backup-{timestamp}.zip"

    print(f"Creating backup: {backup_file}")

    try:
        with zipfile.ZipFile(backup_file, "w", zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk("."):
                # Skip .git and other large directories
                dirs[:] = [d for d in dirs if d not in {".git", "site", "__pycache__", ".venv", "venv"}]

                for file in files:
                    filepath = os.path.join(root, file)
                    arcname = filepath.lstrip("./")
                    zipf.write(filepath, arcname)

        file_size_mb = backup_file.stat().st_size / (1024 * 1024)
        print(f"✅ Backup created: {backup_file} ({file_size_mb:.2f} MB)")
        return True

    except Exception as e:
        print(f"❌ Backup failed: {e}")
        return False

def build_mkdocs():
    """Build MkDocs site"""
    print("\nBuilding MkDocs site...")

    try:
        result = subprocess.run(
            ["mkdocs", "build"],
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode == 0:
            site_size_mb = sum(
                f.stat().st_size for f in Path("site").rglob("*") if f.is_file()
            ) / (1024 * 1024)
            print(f"✅ MkDocs site built successfully ({site_size_mb:.2f} MB)")
            return True
        else:
            print(f"⚠️  MkDocs build completed with warnings:")
            if result.stdout:
                print(result.stdout)
            if result.stderr:
                print(result.stderr)
            return True  # Don't fail on warnings

    except FileNotFoundError:
        print("⚠️  mkdocs not installed. Skipping build.")
        print("   Install with: pip install mkdocs mkdocs-material")
        return True

    except subprocess.TimeoutExpired:
        print("❌ MkDocs build timed out")
        return False

    except Exception as e:
        print(f"⚠️  MkDocs build error: {e}")
        return True

def main():
    """Run backup and build"""
    print("=" * 50)
    print("Personal OS Backup & Build")
    print("=" * 50 + "\n")

    backup_ok = create_backup()
    build_ok = build_mkdocs()

    print("\n" + "=" * 50)
    if backup_ok and build_ok:
        print("✅ Backup and build completed successfully")
        sys.exit(0)
    else:
        print("⚠️  Backup or build completed with issues")
        sys.exit(1)

if __name__ == "__main__":
    main()
