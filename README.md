# v0-prompt-builder

Prompt and workflow skill for the current v0 by Vercel.

The old repository described v0 as a UI generator without backend. That model became obsolete. The current skill covers full-stack apps, existing Git repositories, Vercel Sandbox, terminal permissions, databases, integrations, UI/design-system work and release safety.

## Core sequence

```text
inspect -> project knowledge -> plan -> atomic change -> verification -> PR -> approved release
```

It does not force Next.js, database, authentication or deployment when the project does not need them. For existing repositories, observed stack and conventions win.

## Files

- `SKILL.md` — entry point;
- `references/vibecode-core.md` — shared proportional workflow;
- `references/platform-v0.md` — current v0 adapter;
- `references/archetypes.md` — platform choice;
- `references/version-check.md` — consent-gated updates;
- `scripts/validate_skill.py` — structural and drift checks.

## Verification

```bash
python3 scripts/validate_skill.py
```

## Status

Version `2026.09.02` is a breaking replacement of the legacy UI-only model.
