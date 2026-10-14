# Contributing to Systematic Review & Meta-Analysis Skills

Thank you for improving `systematic-review-meta-analysis-skills`.

## Adding a skill

1. Create `skills/<kebab-case-name>/SKILL.md`.
2. Frontmatter must include `name` (matching the folder), `description`, `version`, and `metadata.author` / `domain` / `frameworks`.
3. Body must include: Description, When to use, Execution protocol, Hard rules, Output contract.
4. List the skill in `README.md`.
5. Run `python scan_skills.py` and `pytest -q`.

## Principles

- No fabricated search counts or pooled estimates in examples that look like real results.
- Prefer Cochrane / PRISMA / PROSPERO-aligned wording.
- Keep skills focused: one job per skill.

## License

Contributions are accepted under the MIT License (copyright Ritu Shah).
