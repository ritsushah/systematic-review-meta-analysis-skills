"""Schema and content tests for systematic-review-meta-analysis-skills."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
README = ROOT / "README.md"

REQUIRED = ("name", "description", "version")
MIN_SKILLS = 18
REQUIRED_SECTIONS = (
    "Description",
    "Execution protocol",
    "Hard rules",
    "Output contract",
)


def _iter_skill_files():
    assert SKILLS_DIR.exists(), "skills directory must exist"
    files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    assert files, "no SKILL.md files found"
    return files


def _load_frontmatter(path: Path) -> tuple[dict, str]:
    content = path.read_text(encoding="utf-8")
    assert content.startswith("---"), f"{path} must start with '---'"
    parts = content.split("---", 2)
    assert len(parts) >= 3, f"{path} must have valid YAML frontmatter"
    data = yaml.safe_load(parts[1])
    assert isinstance(data, dict), f"{path} frontmatter must be a mapping"
    return data, parts[2]


def test_skills_frontmatter_schema():
    names = []
    for filepath in _iter_skill_files():
        data, body = _load_frontmatter(filepath)
        for key in REQUIRED:
            assert key in data and data[key], f"{filepath} missing '{key}'"
        name = str(data["name"]).strip()
        folder = filepath.parent.name
        assert name == folder, f"{filepath}: name '{name}' != folder '{folder}'"
        assert name not in names, f"duplicate skill name: {name}"
        names.append(name)
        assert isinstance(data["version"], (str, int, float))
        meta = data.get("metadata") or {}
        assert "author" in meta, f"{filepath} missing metadata.author"
        assert "domain" in meta, f"{filepath} missing metadata.domain"
        assert "frameworks" in meta, f"{filepath} missing metadata.frameworks"
        for section in REQUIRED_SECTIONS:
            assert re.search(section, body, re.I), f"{filepath} missing section '{section}'"

    assert len(names) >= MIN_SKILLS, f"Must contain at least {MIN_SKILLS} valid skills"


def test_readme_lists_every_skill():
    readme = README.read_text(encoding="utf-8")
    for filepath in _iter_skill_files():
        name = filepath.parent.name
        assert name in readme, f"README.md must mention skill '{name}'"


def test_scan_skills_cli_exits_zero():
    import subprocess
    import sys

    result = subprocess.run(
        [sys.executable, str(ROOT / "scan_skills.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Total Valid Skills Processed" in result.stdout


def test_ci_workflow_exists():
    ci = ROOT / ".github" / "workflows" / "ci.yml"
    assert ci.exists()
    text = ci.read_text(encoding="utf-8")
    assert "scan_skills.py" in text
    assert "pytest" in text
