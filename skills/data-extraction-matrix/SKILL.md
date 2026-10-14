---
name: data-extraction-matrix
description: Builds and completes piloted data-extraction matrices for systematic reviews and diagnostic accuracy studies, including 2×2 contingency tables for DTA meta-analysis.
version: "1.0.0"
metadata:
  author: Ritu Shah
  domain: Evidence Synthesis / Extraction
  frameworks: ['PRISMA', 'PRISMA-DTA', '2x2 tables']
---


# Skill: Data Extraction Matrix

[![Domain](https://img.shields.io/badge/Domain-Extraction-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## Description

Creates study-level extraction templates and fills them from full texts without inventing numeric cells. Supports clinical SR tables and DTA 2×2 tables (TP, FP, FN, TN).

## Execution protocol

1. Pilot the form on 1–2 studies; revise columns.
2. Extract dual-independently when possible; adjudicate conflicts.
3. For DTA reviews, extract **contingency cells** and assay cut-offs, fever duration, reference standard, and setting.
4. Flag missing cells as `NR` (not reported) — never impute silently.
5. Store CSV + JSON copies for analysis scripts.

## Core columns (clinical SR)

Study ID · Design · Country · Host/population · *n* · Exposure/condition · Diagnostics · Outcomes · Treatment · Notes

## Core columns (DTA)

Study ID · Setting · Index test (FIA/ELISA/…) · Reference standard · TP · FP · FN · TN · Prevalence · Fever day window · QUADAS-2 flags

## Hard rules

- No fabricated 2×2 cells.
- Prefer primary full text over abstract when they conflict; note discrepancies.
- Contact authors only if protocol allows and data are essential.

## Output contract

- `data/extraction/included_studies_YYYY-MM-DD.csv`
- `data/extraction/included_studies_YYYY-MM-DD.json`
- Optional DTA `data/extraction/contingency_2x2.csv`
