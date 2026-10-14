---
name: prisma-flow-reporter
description: Assembles PRISMA 2020 / PRISMA-DTA flow counts, diagrams, and identification tables from search logs, dedup, and screening files.
version: "1.0.0"
metadata:
  author: Ritu Shah
  domain: Evidence Synthesis / Reporting
  frameworks: ['PRISMA 2020', 'PRISMA-DTA', 'PRISMA-S']
---


# Skill: PRISMA Flow Reporter

[![Domain](https://img.shields.io/badge/Domain-PRISMA%20Reporting-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## Description

Builds the PRISMA flow from authoritative project files so manuscript numbers match the audit trail.

## Required count fields

- Records identified per database
- Records after deduplication
- Records screened (title/abstract)
- Records excluded (title/abstract)
- Full texts assessed
- Full-text exclusions (with reasons)
- Studies included in qualitative synthesis
- Studies included in quantitative synthesis (meta-analysis), if any

## Execution protocol

1. Read `identification_counts_*.json`, screening CSVs, and extraction outputs.
2. Recompute totals; fail if manuscript numbers disagree.
3. Write `data/PRISMA_flow.json` and embed a Markdown/HTML table in Results.
4. Optionally render `output/figures/prisma_flow.png`.

## Hard rules

- Grey literature and citation chasing: report separately unless protocol merges them.
- Pending vendor searches must remain labeled pending — never guessed.
- Quantitative box is 0 / N/A when synthesis is narrative-only.

## Output contract

- `data/PRISMA_flow.json`
- Results subsection table
- Optional flow figure
