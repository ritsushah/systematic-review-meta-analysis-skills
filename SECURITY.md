# Security Policy

## Supported versions

| Version | Supported |
| ------- | --------- |
| 1.x     | Yes       |

## Reporting a vulnerability

If you discover a security issue (for example, a skill that encourages committing credentials or executing untrusted remote code), please open a **private** security advisory on GitHub or contact the repository owner.

Please do **not** open a public issue for credential-handling flaws.

## Project stance

- Skills must not instruct hosts to commit `.env` files, passwords, or API tokens
- Harvest scripts should use the user’s interactive institutional session rather than embedding secrets
- CI only validates skill schema and unit tests; it does not execute live database harvests
