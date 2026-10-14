---
name: risk-of-bias-appraiser
description: Applies study-level risk-of-bias tools (QUADAS-2, RoB 2, ROBINS-I, Newcastle-Ottawa Scale, JBI checklists) and produces summary and traffic-light tables.
version: "1.0.0"
metadata:
  author: Ritu Shah
  domain: Evidence Synthesis / Quality Appraisal
  frameworks: ['QUADAS-2', 'RoB 2', 'ROBINS-I', 'NOS', 'JBI']
---


# Skill: Risk of Bias Appraiser

[![Domain](https://img.shields.io/badge/Domain-Risk%20of%20Bias-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## Description

Selects the correct RoB tool for each design and produces domain-level judgments with signaling questions and overall concern ratings.

## Tool selection

| Design | Tool |
|---|---|
| Diagnostic accuracy | **QUADAS-2** |
| Randomized trials | **RoB 2** |
| Non-randomized interventions | **ROBINS-I** |
| Observational cohorts/case-control | **NOS** |
| Case reports / case series | **JBI** checklists |

## Execution protocol

1. Confirm design per included study.
2. Operationalize signaling questions for the review topic (e.g. QUADAS-2: fever ≤7 days, index blinded to reference).
3. Rate domains Low / Some concerns / High (or NOS stars / JBI yes-no-unclear).
4. Export summary table + optional traffic-light figure data.
5. Dual appraisal when available; resolve disagreements.

## Hard rules

- Do not assign Low RoB without evidence from the paper.
- Applicability concerns (QUADAS-2) are separate from bias.
- Report tool versions and citations.

## Output contract

- `data/extraction/rob_YYYY-MM-DD.csv`
- Optional `output/figures/quadas2_traffic_light.png` / summary plot inputs
