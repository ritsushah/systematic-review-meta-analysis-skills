# Host Integration Guide

Technical guidance for loading **Systematic Review & Meta-Analysis Skills** into coding hosts (Cursor, Claude Code, Google Antigravity, OpenAI Codex, Gemini CLI, LangChain).

## Supported host architectures

| Host | Recommended skill directory | Configuration hook |
| :--- | :--- | :--- |
| **Cursor** | `.cursor/skills/` or project `skills/` | Skill discovery |
| **Claude Code CLI** | `~/.agents/skills/` | Global / project skills |
| **Google Antigravity** | `.agents/skills/` | Tools registry |
| **Codex / Gemini CLI** | Project `skills/` or host docs path | Prompt / tool wiring |
| **LangChain** | Load `SKILL.md` as tool descriptions | Custom tool wrappers |

## Skill file contract

Each skill lives at `skills/<name>/SKILL.md` with:

1. YAML frontmatter: `name`, `description`, `version`, `metadata` (`author`, `domain`, `frameworks`)
2. Body sections: Description, When to use, Execution protocol, Hard rules, Output contract

## Recommended invocation

1. Read the skill’s `SKILL.md` before acting.
2. Follow the execution protocol in order.
3. Write outputs only to the paths named in the Output contract.
4. Stop and ask for human confirmation before fabricating searches or inventing pooled estimates.

## Quantitative integrity

Skills that touch literature retrieval or quantitative synthesis **must**:

- Use real API/DOM harvest counts or mark `NR`
- Compute effect sizes and pools from extracted cells only
- Prefer narrative synthesis when assumptions fail

## Security

Skills execute in the host environment. Scope network and filesystem permissions before running harvests against institutional databases or patient-level exports.
