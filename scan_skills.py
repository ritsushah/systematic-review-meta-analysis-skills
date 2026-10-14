#!/usr/bin/env python3
"""
Systematic Review & Meta-Analysis Skills Validator & Indexer CLI
Author: Ritu Shah
"""

from __future__ import annotations

import os
import sys

import yaml


REQUIRED_FRONTMATTER = ("name", "description", "version")


def scan_skills(skills_dir: str = "skills") -> int:
    if not os.path.exists(skills_dir):
        print(f"Error: {skills_dir} directory not found.")
        return 1

    valid_count = 0
    errors: list[str] = []
    names: list[str] = []

    print("==================================================")
    print(" Systematic Review & Meta-Analysis Skills Validator")
    print("==================================================\n")

    for root, _dirs, files in os.walk(skills_dir):
        for file in files:
            if file != "SKILL.md":
                continue
            filepath = os.path.join(root, file)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                if not content.startswith("---"):
                    errors.append(f"{filepath}: Missing YAML frontmatter marker '---'")
                    continue

                parts = content.split("---", 2)
                if len(parts) < 3:
                    errors.append(f"{filepath}: Invalid frontmatter structure")
                    continue

                frontmatter = yaml.safe_load(parts[1])
                if not isinstance(frontmatter, dict):
                    errors.append(f"{filepath}: Frontmatter must be a YAML mapping")
                    continue

                missing = [k for k in REQUIRED_FRONTMATTER if not frontmatter.get(k)]
                if missing:
                    errors.append(f"{filepath}: Missing required fields: {', '.join(missing)}")
                    continue

                name = str(frontmatter["name"]).strip()
                folder = os.path.basename(root)
                if name != folder:
                    errors.append(
                        f"{filepath}: frontmatter name '{name}' must match directory '{folder}'"
                    )
                    continue

                if name in names:
                    errors.append(f"{filepath}: Duplicate skill name '{name}'")
                    continue
                names.append(name)

                version = frontmatter.get("version", "?")
                print(f"  [VALID] {name:<36} (v{version}) - {root}")
                valid_count += 1

            except Exception as e:  # noqa: BLE001 — surface parse errors to CLI
                errors.append(f"{filepath}: Exception parsing YAML - {e}")

    print(f"\nTotal Valid Skills Processed: {valid_count}")
    if errors:
        print(f"Encountered {len(errors)} Errors:")
        for err in errors:
            print(f"  [ERROR] {err}")
        return 1

    print(" All skills passed schema validation successfully!")
    return 0


def main() -> None:
    raise SystemExit(scan_skills())


if __name__ == "__main__":
    main()
