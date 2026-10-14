---
name: dta-meta-analyst
description: Runs diagnostic test accuracy meta-analysis (bivariate random-effects / HSROC), produces forest plots, SROC curves, and Deeks funnel asymmetry tests from 2×2 tables.
version: "1.1.0"
metadata:
  author: Ritu Shah
  domain: Meta-Analysis / Diagnostic Test Accuracy
  frameworks: ['mada', 'metafor', 'metandi', 'HSROC', 'bivariate', 'Deeks']
---

# Skill: DTA Meta-Analyst

[![Domain](https://img.shields.io/badge/Domain-DTA%20Meta--Analysis-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.1.0-green?style=flat-square)](#)

## Description

Pools sensitivity and specificity jointly from study-level 2×2 tables using a bivariate random-effects model or HSROC, and produces SROC / summary operating points with appropriate uncertainty.

## When to use

- Index test vs reference standard with extractable TP, FP, FN, TN
- Protocol specifies DTA meta-analysis (PRISMA-DTA)
- At least ~4–5 studies with usable 2×2 data (fewer → narrative accuracy ranges only)

## Execution protocol

1. Confirm analysis-ready 2×2 table (`study_id`, TP, FP, FN, TN) with no fabricated cells.
2. Fit **bivariate random-effects** (Reitsma) or **HSROC** (Rutter–Gatsonis); state software (`mada`, `metandi`, `metafor`, Stata `metandi`, etc.).
3. Report pooled sensitivity and specificity with 95% CIs (and prediction regions when available).
4. Plot study-level Se/Sp, summary point, and SROC/HSROC curve; optional coupled forest via `forest-sroc-plotter`.
5. Run Deeks’ funnel test when *k* is adequate; otherwise qualitative small-study discussion only.
6. Prespecified subgroups (assay brand, fever day, region) via `heterogeneity-subgroup-analyst`.
7. If threshold effects or extreme heterogeneity dominate, prefer HSROC narrative over a single summary point.

## Hard rules

- Never invent TP/FP/FN/TN or pooled Se/Sp.
- Do not collapse Se and Sp into a single accuracy metric for the primary pool.
- Continuity corrections only if protocol allows; document them.
- If reference standards differ materially, stratify or go narrative.

## Output contract

- `output/tables/dta_pooled_estimates.csv`
- `output/tables/dta_study_level.csv`
- Inputs for `forest-sroc-plotter` and `publication-bias-assessor`
- Methods paragraph: model, software, package versions
