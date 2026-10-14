# Architecture

## Goal

Provide composable skills that map 1:1 onto stages of a PRISMA-compliant systematic review and meta-analysis so a coding host can run a reproducible pipeline.

## Layout

```text
systematic-review-meta-analysis-skills/
├── skills/<skill-name>/SKILL.md
├── scan_skills.py               # Schema validator CLI
├── tests/test_skills.py
├── docs/architecture.md
├── HOST_INTEGRATION.md          # Host loading notes
├── pyproject.toml
└── .github/workflows/ci.yml
```

Each skill is a Markdown file with YAML frontmatter (`name`, `description`, `version`, `metadata`) plus an execution protocol the host must follow.

## Layers

1. **Protocol & search** — PROSPERO, PRISMA-S strategies, harvest, grey literature
2. **Study processing** — dedupe, dual screen, extraction, risk of bias
3. **Meta-analysis** — effect sizes → pairwise / DTA / NMA → heterogeneity → bias → plots
4. **Reporting** — PRISMA flow + manuscript synthesis

## Validation

`python scan_skills.py` and `pytest` enforce frontmatter schema, required sections, and README coverage for every skill.
