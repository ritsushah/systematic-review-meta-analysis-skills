---
name: forest-sroc-plotter
description: Generates publication-ready forest plots, coupled sensitivity-specificity forests, HSROC/SROC curves, and funnel/Deeks plots from analysis outputs for systematic reviews and meta-analyses.
version: "1.0.0"
metadata:
  author: Ritu Shah
  domain: Meta-Analysis / Visualization
  frameworks: ['metafor', 'mada', 'ggplot2', 'forestplot']
---


# Skill: Forest / SROC Plotter

[![Domain](https://img.shields.io/badge/Domain-Visualization-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## Description

Creates journal-ready figures for pairwise and DTA meta-analyses from real model objects or tidy effect tables.

## When to use

- After pooling or when displaying study-level estimates without a pool
- Manuscript Results figures

## Execution protocol

1. Forest plot: study labels, weights, CI whiskers, diamond for pooled effect (omit diamond if narrative-only).
2. DTA: coupled forest (Se and Sp) + HSROC/SROC with summary point and confidence/credible region.
3. Funnel / Deeks plots for reporting-bias skill outputs.
4. Export PNG/PDF/SVG at ≥300 dpi; keep colorblind-safe palettes.
5. Figure captions must match numeric Results text.

## Hard rules

- Plot only computed values — no hand-drawn fake CIs.
- If no meta-analysis, do not show a pooled diamond.
- Keep study order consistent with tables.

## Output contract

- `output/figures/forest_*.png`
- `output/figures/sroc_*.png`
- `output/figures/funnel_*.png` or `deeks_*.png`
