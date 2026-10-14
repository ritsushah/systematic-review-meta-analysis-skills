---
name: record-deduplicator
description: Deduplicates bibliographic records by DOI, PMID, and normalized title+year; produces unique sets and PRISMA identification statistics.
version: "1.0.0"
metadata:
  author: Ritu Shah
  domain: Evidence Synthesis / Deduplication
  frameworks: ['DOI', 'PMID', 'PRISMA']
---


# Skill: Record Deduplicator

[![Domain](https://img.shields.io/badge/Domain-Deduplication-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## Description

Merges multi-database exports into a unique screening set using a deterministic matching order and writes PRISMA-ready counts.

## Matching order (first win)

1. Normalized DOI (strip `https://doi.org/`, lowercase)
2. PMID (digits only)
3. Normalized title + year (lowercase, strip punctuation)

When a DOI/PMID match wins, also register the title+year key so DOI-less vendor duplicates still collapse.

## Execution protocol

1. Load all database harvests into a common schema: `source, pmid, doi, title, year, journal, abstract, authors`.
2. Sort by preferred source order (e.g. PubMed → Embase → WoS → ScienceDirect) so the richest metadata is kept.
3. Deduplicate; count removed.
4. Write unique set + machine-readable PRISMA identification JSON.

## Hard rules

- Do not drop unique records that only differ by subtitle punctuation without title normalization.
- Keep provenance (`source`, original IDs) on the surviving record.
- Report both **identified** (sum of database hits) and **after deduplication**.

## Output contract

- `data/unique/unique_records_YYYY-MM-DD.csv|json`
- Updated `data/PRISMA_flow.json` identification fields
