---
name: intervention-meta-analyst
description: Runs conventional pairwise meta-analysis for interventions/exposures (fixed/random effects), forest and funnel plots, heterogeneity (I²), and sensitivity analyses.
version: "1.1.0"
metadata:
  author: Ritu Shah
  domain: Meta-Analysis / Pairwise Intervention
  frameworks: ['metafor', 'meta', 'RevMan', 'forest', 'funnel', 'Cochrane Handbook']
---

# Skill: Intervention Meta-Analyst

[![Domain](https://img.shields.io/badge/Domain-Pairwise%20Meta--Analysis-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.1.0-green?style=flat-square)](#)

## Description

Performs pairwise meta-analysis of a single comparison (intervention vs control or exposure contrast) on a common effect measure, with random-effects as the default when clinical diversity is expected.

## When to use

- Homogeneous enough PICO for a single pairwise pool
- Effect sizes already prepared by `effect-size-calculator` (`yi`, `vi`)
- Protocol specifies fixed or random effects and the primary measure (OR, RR, MD, SMD, HR)

## Execution protocol

1. Confirm eligible study rows and primary effect measure from the protocol.
2. Fit the primary model (REML random-effects default unless protocol mandates fixed-effect).
3. Report pooled estimate, 95% CI, *k*, total *N*, and model details.
4. Hand off heterogeneity (τ², I², prediction interval) to `heterogeneity-subgroup-analyst`.
5. Prespecified sensitivity analyses (e.g., exclude high RoB, alternative continuity correction).
6. Funnel / Egger via `publication-bias-assessor` when *k* ≥ 10.
7. Forest plot via `forest-sroc-plotter`.

## Hard rules

- No pooling across incompatible outcomes or populations without protocol justification.
- Do not switch effect measures post hoc to chase significance.
- Never invent study weights, CIs, or pooled effects.
- If *k* < 2 or effects are non-combinable → narrative synthesis only.

## Output contract

- `output/tables/pairwise_pooled.csv`
- `output/tables/pairwise_study_effects.csv`
- Model object or tidy exports for plotting and bias skills
- Methods note: estimator, software, package versions
