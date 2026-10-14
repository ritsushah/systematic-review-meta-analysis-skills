---
name: meta-regression-analyst
description: Fits study-level meta-regression models (continuous or categorical moderators) with Knapp-Hartung adjustments and multiplicity-aware interpretation.
version: "1.0.0"
metadata:
  author: Ritu Shah
  domain: Meta-Analysis / Meta-Regression
  frameworks: ['metafor', 'Knapp-Hartung', 'REML']
---


# Skill: Meta-Regression Analyst

[![Domain](https://img.shields.io/badge/Domain-Meta--Regression-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## Description

Explains between-study variance using study-level moderators when sufficient studies and a priori hypotheses exist.

## When to use

- Protocol prespecifies meta-regression
- Rough guide: *k* ≥ 10 for a continuous moderator (more for multivariable)
- Moderators must be study-level (not patient-level ecological fallacy ignored)

## Execution protocol

1. Confirm moderators and coding from protocol.
2. Fit random-effects meta-regression (REML default) with Knapp–Hartung / Hartung–Knapp SE adjustment when available.
3. Report coefficient, CI, p, R² analog (proportion of τ² explained).
4. Check residual heterogeneity and influential studies.
5. Multivariable models only if *k* supports them; otherwise one-moderator models.

## Hard rules

- No fishing for significant moderators.
- Do not treat study-level aggregates as individual-level effects.
- Never invent moderator coefficients.

## Output contract

- `output/tables/meta_regression.csv`
- Bubble-plot inputs optional under `output/figures/`
