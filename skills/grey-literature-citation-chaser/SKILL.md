---
name: grey-literature-citation-chaser
description: Plans and executes grey-literature searches (ClinicalTrials.gov, ICTRP, Europe PMC, Google Scholar caps) and forward/backward citation chasing without double-counting PRISMA database totals.
version: "1.0.0"
metadata:
  author: Ritu Shah
  domain: Evidence Synthesis / Supplementary Search
  frameworks: ['ClinicalTrials.gov', 'Europe PMC', 'Google Scholar', 'citation chasing']
---


# Skill: Grey Literature & Citation Chaser

[![Domain](https://img.shields.io/badge/Domain-Grey%20Literature-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## Description

Supplements database searches with trials registries, preprint servers, capped Scholar harvests, and reference-list / cited-by chasing. Keeps supplementary yields out of primary database identification totals unless the protocol says otherwise.

## Execution protocol

1. Search ClinicalTrials.gov / ICTRP for ongoing or unpublished studies.
2. Query Europe PMC / medRxiv / bioRxiv for preprints when protocol allows.
3. Google Scholar: use a focused query; cap at protocol *n* (e.g. first 200); stop when relevance collapses.
4. Backward cite: reference lists of included studies.
5. Forward cite: Web of Science / Scholar cited-by for included studies.
6. Screen supplementary hits with the same eligibility criteria.
7. Document each source's hit count separately in the search log.

## Hard rules

- Do not merge grey counts into PubMed/Embase/WoS/SD totals by default.
- Scholar scraping is brittle — prefer manual export or capped API/browser harvest.
- Deduplicate supplementary records against the main unique set before screening.

## Output contract

- `data/raw/grey/*`
- Search-log subsection for supplementary sources
- Optional additional included studies with provenance `source=citation_chase`
