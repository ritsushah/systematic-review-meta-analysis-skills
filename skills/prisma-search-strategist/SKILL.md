---
name: prisma-search-strategist
description: Builds database-specific Boolean search strategies (PubMed/MEDLINE, Embase/Emtree, Web of Science, ScienceDirect, Scopus, Cochrane) with MeSH/Emtree mapping and PRISMA-S documentation.
version: "1.0.0"
metadata:
  author: Ritu Shah
  domain: Evidence Synthesis / Literature Search
  frameworks: ['PRISMA-S', 'PubMed', 'Embase', 'Web of Science', 'ScienceDirect']
---


# Skill: PRISMA-S Search Strategist

[![Domain](https://img.shields.io/badge/Domain-Literature%20Search-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## Description

Translates a review question into peer-reviewable, database-specific Boolean strings with controlled vocabulary (MeSH, Emtree) and free-text synonyms. Documents strategies per PRISMA-S.

## When to use

- User needs PubMed / Embase / WoS / ScienceDirect strings
- Protocol mentions databases but lacks executable syntax
- Sensitivity checks against known seed papers (DOIs/PMIDs)

## Execution protocol

1. Extract concept blocks from PICO/PIRD (usually 2–5 blocks).
2. Expand synonyms (historical names, abbreviations, brand/assay names).
3. Map controlled vocabulary:
   - PubMed: `[MeSH Terms]`, `[tiab]`
   - Embase: `/exp`, `:ti,ab`
   - Web of Science: `TS=()`
   - ScienceDirect: simpler Boolean (limited operators/wildcards)
4. Combine blocks with AND; synonyms within blocks with OR.
5. Validate against ≥1–3 known eligible seed studies when provided.
6. Write `data/search_strategies.md` with one section per database.

## Database syntax cheat sheet

| Database | Field tags | Notes |
|---|---|---|
| PubMed | `[MeSH]`, `[tiab]`, date `[Date - Publication]` | E-utilities compatible |
| Embase | `/exp`, `:ti,ab` | Map to Emtree; explode carefully |
| Web of Science | `TS=()`, `PY=` | Core Collection editions |
| ScienceDirect | `qs` / title-abs-key | Few wildcards; keep strings shorter |
| Cochrane | MeSH + ti,ab,kw | CENTRAL vs Reviews |

## Hard rules

- Never invent hit counts before execution.
- Document date of last search and who ran it.
- ScienceDirect often rejects complex nested wildcards — simplify rather than fail silently.
- Keep the exact strings used for reproducibility (copy-paste ready).

## Output contract

- `data/search_strategies.md`
- Optional seed-paper validation table
