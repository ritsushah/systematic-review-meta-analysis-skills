---
name: publication-bias-assessor
description: Evaluates small-study effects and reporting bias for meta-analyses using funnel plots, Egger/Deeks tests, trim-and-fill (sensitivity only), and qualitative missing-evidence assessment.
version: "1.0.0"
metadata:
  author: Ritu Shah
  domain: Meta-Analysis / Reporting Bias
  frameworks: ['metafor', 'metabias', 'Deeks', 'Egger', 'trim-and-fill']
---


# Skill: Publication Bias Assessor

[![Domain](https://img.shields.io/badge/Domain-Publication%20Bias-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## Description

Assesses risk that pooled results are distorted by small-study effects or selective non-reporting.

## When to use

- Conventional MA with *k* ≥ 10 for Egger-type tests (smaller *k*: funnel visual + qualitative only)
- DTA reviews: Deeks’ funnel test on diagnostic odds ratio when *k* adequate
- Protocol requires reporting-bias discussion

## Execution protocol

1. Contour-enhanced funnel plot (effect vs SE or 1/√ESS for DTA).
2. Egger regression (intervention/continuous) or **Deeks’ test** (DTA).
3. Optional trim-and-fill **only as sensitivity**, never as primary result.
4. Qualitative: compare registry/grey yields vs published set; note industry funding patterns if extracted.
5. State when tests are underpowered.

## Hard rules

- Do not claim “no publication bias” from a non-significant Egger test alone.
- Skip formal tests when *k* is small; say so.
- No fabricated funnel coordinates.

## Output contract

- `output/figures/funnel_*.png` or Deeks plot
- `output/tables/publication_bias_tests.csv`
- Discussion paragraph inputs (limitations)
