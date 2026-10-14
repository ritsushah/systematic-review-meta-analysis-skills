---
name: dual-screener
description: Runs title/abstract and full-text eligibility screening against a priori criteria, logs exclusion reasons, and supports dual-reviewer workflows with Cohen's kappa.
version: "1.0.0"
metadata:
  author: Ritu Shah
  domain: Evidence Synthesis / Screening
  frameworks: ['PRISMA', 'Covidence', 'Rayyan', 'Cohen kappa']
---


# Skill: Dual Screener

[![Domain](https://img.shields.io/badge/Domain-Screening-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## Description

Applies registered inclusion/exclusion criteria at title/abstract and full-text stages, archives decisions, and computes inter-rater agreement when two reviewers are available.

## Execution protocol

1. Load unique records + eligibility criteria from the protocol.
2. Title/abstract screen: include / exclude / unsure.
3. Full-text screen for includes/unsures with **prespecified exclusion taxonomy** (wrong population, wrong index/reference, no 2×2 / no extractable outcome, wrong design, duplicate, language, etc.).
4. If single-reviewer pass is used (automation), label it clearly and do **not** invent κ.
5. If dual reviewers exist, resolve conflicts by discussion/third reviewer and report Cohen's κ.

## Hard rules

- Decisions must cite the criterion violated (not vibes).
- Animal / in vitro / wrong organism exclusions need explicit reasons.
- Do not invent full-text findings you have not read.
- Conference abstracts: follow protocol (often exclude if insufficient data).

## Output contract

- `data/screening/title_abstract_screen_YYYY-MM-DD.csv`
- `data/screening/fulltext_screen_YYYY-MM-DD.csv`
- Optional `data/screening/kappa.json`
