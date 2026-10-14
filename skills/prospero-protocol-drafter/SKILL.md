---
name: prospero-protocol-drafter
description: Drafts submission-ready PROSPERO registration protocols for systematic reviews and meta-analyses using PICO/PIRD frameworks, eligibility criteria, and PRISMA-aligned methods fields.
version: "1.0.0"
metadata:
  author: Ritu Shah
  domain: Evidence Synthesis / Protocol Registration
  frameworks: ['PROSPERO', 'PRISMA', 'PICO', 'PIRD']
---


# Skill: PROSPERO Protocol Drafter

[![Domain](https://img.shields.io/badge/Domain-Protocol%20Registration-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## Description

Produces a complete, submission-ready PROSPERO protocol before screening begins. Covers review title, PICO or PIRD question, eligibility, databases, risk-of-bias tools, and synthesis plan (narrative vs quantitative).

## When to use

- User asks to register or draft a PROSPERO protocol
- Starting a new systematic review or DTA meta-analysis
- User provides a review title and question but no registered methods

## Execution protocol

1. **Clarify review type**: intervention SR/MA, diagnostic test accuracy (DTA), prevalence/prognosis, or narrative-only SR.
2. **Lock the question framework**:
   - Intervention/exposure: **PICO**
   - Diagnostic accuracy: **PIRD** (Population, Index test, Reference standard, Diagnosis/target condition)
3. **Draft all PROSPERO fields** without fabricating hit counts or results.
4. **Prespecify synthesis**: if diagnostics/outcomes are expected to be heterogeneous, state *narrative/tabular only — no meta-analysis* explicitly.
5. **Save** to `protocols/prospero_protocol.md` and note CRD number when available.

## Required protocol sections

| Section | Must include |
|---|---|
| Review title | Full, searchable title |
| Review question | PICO or PIRD table |
| Searches | Databases + grey literature plan |
| Condition / domain | Clinical condition under study |
| Inclusion / exclusion | Population, exposure/index, outcomes, designs, language, dates |
| Data extraction | Dual extraction plan |
| Risk of bias | NOS / JBI / RoB 2 / ROBINS-I / QUADAS-2 as applicable |
| Strategy for data synthesis | Meta-analysis model **or** explicit narrative-only rationale |
| Dissemination | Target journals / preprint plan |

## Hard rules

- Do **not** invent PROSPERO registration numbers.
- Do **not** draft Results before searches and extraction exist.
- Date windows must be explicit (e.g. 1 Jan 2000 – 18 Jun 2026).
- Language filters: prefer apply at screening, document interface filters if used.

## Output contract

- `protocols/prospero_protocol.md` — full field set
- Optional one-page summary for collaborators
