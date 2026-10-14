---
name: heterogeneity-subgroup-analyst
description: Quantifies between-study heterogeneity (τ², I², Q, prediction intervals) and runs protocol-prespecified subgroup analyses and leave-one-out diagnostics for meta-analyses.
version: "1.0.0"
metadata:
  author: Ritu Shah
  domain: Meta-Analysis / Heterogeneity
  frameworks: ['metafor', 'meta', 'prediction intervals', 'Cochrane Handbook']
---


# Skill: Heterogeneity & Subgroup Analyst

[![Domain](https://img.shields.io/badge/Domain-Heterogeneity-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## Description

Assesses statistical and clinical heterogeneity after a pooled model is fit, and executes only **prespecified** subgroup comparisons.

## When to use

- After `intervention-meta-analyst` or `dta-meta-analyst` produces a primary pool
- Protocol lists subgroups (assay brand, region, risk of bias, fever day, dose)

## Execution protocol

1. Report Q, df, p; τ² (and method: REML/DL/PM); I²; and a **95% prediction interval** when random-effects is used and *k* is adequate.
2. Interpret heterogeneity clinically (not only “I² high”).
3. Run subgroups that were **registered**; label any exploratory cuts as post hoc.
4. Leave-one-out / influence diagnostics; identify outliers with justification.
5. For DTA, report heterogeneity on the logit-sensitivity and logit-specificity scales (or HSROC parameters), not a single naive I² on accuracy.

## Hard rules

- Do not data-dredge subgroups to chase significance.
- Sparse subgroups (*k* < 3–4) → narrative comparison only.
- Never invent τ²/I² values.

## Output contract

- `output/tables/heterogeneity_summary.csv`
- `output/tables/subgroup_results.csv`
- Optional influence plot data under `output/figures/`
