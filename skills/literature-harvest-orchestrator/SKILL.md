---
name: literature-harvest-orchestrator
description: Executes multi-database literature searches, handles institutional OpenAthens/SSO vendor access, exports RIS/JSON, and logs identification counts without fabricating hits.
version: "1.0.0"
metadata:
  author: Ritu Shah
  domain: Evidence Synthesis / Retrieval
  frameworks: ['PubMed E-utilities', 'Embase', 'Web of Science', 'ScienceDirect', 'OpenAthens']
---


# Skill: Literature Harvest Orchestrator

[![Domain](https://img.shields.io/badge/Domain-Retrieval-00f0ff?style=flat-square)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-green?style=flat-square)](#)

## Description

Runs the registered search strategies across public APIs and institutional vendor interfaces, exports bibliographic records, and writes an auditable search execution log.

## When to use

- Search strategies exist and the user asks to run the search
- Institutional SSO (OpenAthens / ADFS) is needed for Embase, WoS, or ScienceDirect
- Hit counts and raw exports must be archived for PRISMA

## Execution protocol

1. Run **PubMed** via E-utilities (or website) with date + language filters as registered.
2. For licensed databases, prefer the user's **already-signed-in browser session** (Cursor browser / DevTools console harvest). Avoid separate headless browsers when SSO is fragile.
3. Apply date limits in platform-native formats:
   - PubMed: `YYYY/MM/DD`
   - WoS: `PY=2000-2026`
   - ScienceDirect: year field `2000-2026` (not full ISO dates)
4. Export records to `data/raw/{database}/` as JSON and/or `data/imports/{database}/` as RIS/CSV.
5. Update `data/logs/search_execution_log.md` with hits, retrieved *n*, method, and date.

## Vendor harvest tips (learned patterns)

| Database | Working approach |
|---|---|
| Embase | Signed-in REST `/rest/searchresults/results` |
| Web of Science | Internal `/api/wosnx/core/runQuerySearch` + `wos_sid` from localStorage |
| ScienceDirect | Form search on `/search`; `/search/api` may 403 under automation — fall back to DOM scrape / manual console script |

## Hard rules

- **Never fabricate hit counts.**
- Do not commit passwords, `.env` secrets, or SSO tokens.
- Prefer Rocket ID without domain prefix when ADFS auto-appends the campus domain.
- If a vendor blocks automation, document the blocker and give the user a console harvest script path.

## Output contract

- `data/raw/{pubmed,embase,web_of_science,sciencedirect}/*`
- `data/logs/search_execution_log.md`
- `data/logs/identification_counts_YYYY-MM-DD.json`
