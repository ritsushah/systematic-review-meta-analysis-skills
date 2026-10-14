---
name: network-meta-analyst
description: Plans and runs network meta-analysis (frequentist or Bayesian) including network geometry, consistency checks, league tables, and SUCRA/P-scores when the protocol specifies NMA.
version: "1.0.0"
metadata:
  author: Ritu Shah
  domain: Meta-Analysis / Network
  frameworks: ['netmeta', 'gemtc', 'BUGSnet', 'CINeMA']
---


# Skill: Network Meta-Analyst

[![Domain](https://img.shields.io/badge/Domain-Network%20Meta--Analysis-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## Description

Synthesizes direct and indirect comparisons across a connected treatment network when pairwise MA is insufficient and the protocol specifies NMA.

## When to use

- ≥3 interventions forming a connected network
- Transitivity assumption is clinically plausible
- Protocol registers NMA (do not invent an NMA post hoc)

## Execution protocol

1. Build network geometry (nodes = treatments, edges = comparisons).
2. Assess transitivity (effect modifiers balanced across comparisons).
3. Fit consistency model (frequentist `netmeta` or Bayesian `gemtc`/`BUGSnet`).
4. Global/local inconsistency (design-by-treatment, node-splitting).
5. League table, relative effects vs reference, P-scores/SUCRA.
6. CINeMA or equivalent confidence grading when feasible.

## Hard rules

- Do not run NMA on disconnected networks without separating components.
- Sparse networks: prefer pairwise + narrative.
- Never fabricate league-table cells.

## Output contract

- `output/tables/nma_league.csv`
- `output/tables/nma_rankings.csv`
- `output/figures/network_geometry.png`
