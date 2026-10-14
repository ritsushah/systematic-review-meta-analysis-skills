---
name: effect-size-calculator
description: Computes study-level effect sizes and sampling variances for meta-analysis (OR, RR, RD, HR, MD, SMD/Hedges g, correlation-to-Fisher-z) from raw study data without fabricating values.
version: "1.0.0"
metadata:
  author: Ritu Shah
  domain: Meta-Analysis / Effect Sizes
  frameworks: ['metafor', 'esc', 'compute.es', 'Cochrane Handbook']
---


# Skill: Effect Size Calculator

[![Domain](https://img.shields.io/badge/Domain-Effect%20Sizes-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## Description

Converts extracted study statistics into a common effect-size metric and sampling variance for pooling. Supports binary, continuous, time-to-event, and correlation outcomes.

## When to use

- Before pairwise, DTA (logit-Se/Sp), or network meta-analysis
- Studies report different summary stats (2×2, means/SDs, HR + CI, correlations)
- Protocol specifies OR/RR/MD/SMD/HR

## Execution protocol

1. Confirm the **protocol effect measure** (do not switch post hoc without documenting a deviation).
2. For each study arm/outcome, extract only reported numerators, denominators, means, SDs, CIs, or p-values.
3. Compute:
   - Binary: logOR / logRR / RD + variance (continuity correction only if protocol allows)
   - Continuous: MD or Hedges’ *g* (bias-corrected SMD) + variance
   - Survival: logHR from reported HR and 95% CI
   - Correlation: Fisher’s *z* + variance
4. Flag studies with missing cells as `NR`; never impute means/SDs unless the protocol defines a method.
5. Export a tidy analysis-ready table (`yi`, `vi`, study labels, moderators).

## Hard rules

- No fabricated effect sizes or back-calculated cells without a transparent formula and source numbers.
- Do not convert incomparable outcomes into one metric without justification.
- Document continuity corrections and direction of effects (intervention beneficial = lower or higher).

## Output contract

- `data/analysis/effect_sizes.csv` with columns: `study_id`, `yi`, `vi`, `measure`, `n`, moderators
- Methods note listing formulas/software
