# Systematic Review & Meta-Analysis Skills

[![Skills Standard](https://img.shields.io/badge/Standard-Skills-00f0ff?style=flat-square)](https://agentskills.io)
[![Total Skills](https://img.shields.io/badge/Skills-18%20Production%20Skills-purple?style=flat-square)](#)
[![Compatibility](https://img.shields.io/badge/Compatible-Cursor%20%2F%20Claude%20Code%20%2F%20Antigravity-0d1117?style=flat-square)](#)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)

Open-source **skills** for end-to-end **systematic reviews**, **PRISMA / PRISMA-DTA reporting**, and **meta-analysis** — pairwise intervention MA, diagnostic test accuracy (bivariate/HSROC), effect sizes, heterogeneity, publication bias, meta-regression, network MA, and journal-ready plots.

Built for reproducible evidence synthesis in Cursor, Claude Code, Antigravity, Codex, Gemini CLI, and similar hosts — without fabricating hit counts or pooled estimates.

**Author:** Ritu Shah · **Repo:** `ritsushah/systematic-review-meta-analysis-skills`

---

## Available skills

### Systematic review pipeline

| Skill                                 | Domain                | Frameworks / tools                           | Docs                                                          |
| :------------------------------------ | :-------------------- | :------------------------------------------- | :------------------------------------------------------------ |
| **`prospero-protocol-drafter`**       | Protocol registration | PROSPERO, PICO/PIRD, PRISMA                  | [`SKILL.md`](skills/prospero-protocol-drafter/SKILL.md)       |
| **`prisma-search-strategist`**        | Search design         | PubMed, Embase, WoS, ScienceDirect, PRISMA-S | [`SKILL.md`](skills/prisma-search-strategist/SKILL.md)        |
| **`literature-harvest-orchestrator`** | Retrieval             | E-utilities, OpenAthens, vendor APIs         | [`SKILL.md`](skills/literature-harvest-orchestrator/SKILL.md) |
| **`grey-literature-citation-chaser`** | Supplementary search  | Trials registries, Scholar, citation chase   | [`SKILL.md`](skills/grey-literature-citation-chaser/SKILL.md) |
| **`record-deduplicator`**             | Deduplication         | DOI / PMID / title–year                      | [`SKILL.md`](skills/record-deduplicator/SKILL.md)             |
| **`dual-screener`**                   | Screening             | PRISMA eligibility, Cohen’s κ                | [`SKILL.md`](skills/dual-screener/SKILL.md)                   |
| **`data-extraction-matrix`**          | Extraction            | SR tables, DTA 2×2                           | [`SKILL.md`](skills/data-extraction-matrix/SKILL.md)          |
| **`risk-of-bias-appraiser`**          | Quality appraisal     | QUADAS-2, RoB 2, ROBINS-I, NOS, JBI          | [`SKILL.md`](skills/risk-of-bias-appraiser/SKILL.md)          |
| **`prisma-flow-reporter`**            | PRISMA flow           | PRISMA 2020 / PRISMA-DTA                     | [`SKILL.md`](skills/prisma-flow-reporter/SKILL.md)            |
| **`manuscript-synthesizer`**          | Manuscript            | PRISMA-compliant drafting                    | [`SKILL.md`](skills/manuscript-synthesizer/SKILL.md)          |

### Meta-analysis

| Skill                                | Domain            | Frameworks / tools                      | Docs                                                         |
| :----------------------------------- | :---------------- | :-------------------------------------- | :----------------------------------------------------------- |
| **`effect-size-calculator`**         | Effect sizes      | OR/RR/RD/HR/MD/SMD, Fisher _z_          | [`SKILL.md`](skills/effect-size-calculator/SKILL.md)         |
| **`intervention-meta-analyst`**      | Pairwise MA       | metafor / meta, forest, funnel          | [`SKILL.md`](skills/intervention-meta-analyst/SKILL.md)      |
| **`dta-meta-analyst`**               | DTA meta-analysis | bivariate / HSROC, SROC, Deeks          | [`SKILL.md`](skills/dta-meta-analyst/SKILL.md)               |
| **`heterogeneity-subgroup-analyst`** | Heterogeneity     | τ², I², prediction intervals, subgroups | [`SKILL.md`](skills/heterogeneity-subgroup-analyst/SKILL.md) |
| **`publication-bias-assessor`**      | Reporting bias    | Egger, Deeks, trim-and-fill             | [`SKILL.md`](skills/publication-bias-assessor/SKILL.md)      |
| **`meta-regression-analyst`**        | Meta-regression   | REML, Knapp–Hartung                     | [`SKILL.md`](skills/meta-regression-analyst/SKILL.md)        |
| **`network-meta-analyst`**           | Network MA        | netmeta, gemtc, CINeMA                  | [`SKILL.md`](skills/network-meta-analyst/SKILL.md)           |
| **`forest-sroc-plotter`**            | Visualization     | Forest, SROC/HSROC, funnel              | [`SKILL.md`](skills/forest-sroc-plotter/SKILL.md)            |

---

## Recommended pipeline order

```text
prospero-protocol-drafter
        ↓
prisma-search-strategist
        ↓
literature-harvest-orchestrator  (+ grey-literature-citation-chaser)
        ↓
record-deduplicator
        ↓
dual-screener
        ↓
data-extraction-matrix
        ↓
risk-of-bias-appraiser
        ↓
effect-size-calculator
        ↓
intervention-meta-analyst  OR  dta-meta-analyst  OR  network-meta-analyst  OR  narrative-only
        ↓
heterogeneity-subgroup-analyst  (+ meta-regression-analyst if planned)
        ↓
publication-bias-assessor
        ↓
forest-sroc-plotter
        ↓
prisma-flow-reporter
        ↓
manuscript-synthesizer
```

---

## Getting started

### Option 1: `npx skills` (supported hosts)

```bash
npx skills add ritsushah/systematic-review-meta-analysis-skills
```

### Option 2: Clone into a skills directory

```bash
git clone https://github.com/ritsushah/systematic-review-meta-analysis-skills.git ~/.agents/skills/systematic-review-meta-analysis-skills
```

### Option 3: Cursor project skills

Copy or submodule `skills/` into `.cursor/skills/` (or your host’s skills path) in the review repository.

### Validate locally

```bash
python scan_skills.py
pytest -q
```

---

## Hard rules (all skills)

1. **No fabricated numbers** — search hits, 2×2 cells, pooled Se/Sp, OR/RR, τ²/I², or funnel statistics must come from real runs or cited sources.
2. **Protocol first** — follow PROSPERO / a priori analysis plans; label post hoc changes.
3. **PRISMA-honest flow** — counts must reconcile with harvest and screening logs.
4. **Prefer narrative synthesis** when meta-analysis assumptions fail or _k_ is too small.

---

## License

MIT © Ritu Shah
