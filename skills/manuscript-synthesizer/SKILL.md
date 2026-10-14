---
name: manuscript-synthesizer
description: Writes PRISMA-compliant systematic review or meta-analysis manuscripts (title, abstract, methods, results, discussion) strictly from extracted data without fabricating estimates.
version: "1.0.0"
metadata:
  author: Ritu Shah
  domain: Evidence Synthesis / Manuscript
  frameworks: ['PRISMA 2020', 'PRISMA-DTA', 'ICMJE']
---


# Skill: Manuscript Synthesizer

[![Domain](https://img.shields.io/badge/Domain-Manuscript-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## Description

Drafts a journal-oriented manuscript from protocol + extraction + RoB + (optional) pooled analyses. Supports narrative SR and DTA/intervention meta-analysis formats.

## Execution protocol

1. Confirm which sections have locked data (never invent Results).
2. Draft Title, Abstract, Introduction, Methods from protocol.
3. Draft Results only from `PRISMA_flow.json`, extraction tables, RoB, and analysis outputs.
4. Discussion: principal findings, comparison with prior reviews, limitations (including single-reviewer screening if applicable), implications.
5. Declarations: funding, conflicts, data availability, CRediT placeholders.
6. Export Markdown + PDF/DOCX for submission polishing.

## Hard rules

- **No hallucinated pooled Se/Sp/OR.**
- If vendor searches pending, say so — do not imply completeness.
- Keep narrative-only reviews free of meta-analytic language.
- Author names/affiliations remain placeholders until the user supplies them.

## Output contract

- `manuscript/<Study>_SystematicReview.md`
- Optional `manuscript/<Study>_SystematicReview.pdf`
