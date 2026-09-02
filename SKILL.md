---
name: v0-prompt-builder
description: >
  Guides planning, building, repairing, testing and releasing full-stack apps, existing Git repositories, pages and design systems with the current v0 by Vercel. Use when the user mentions v0, v0.app, Vercel Sandbox, v0 Git workflows or asks for structured v0 prompts. Inspect existing projects before choosing a stack and require approval for production-impacting actions.
license: MIT
---

# v0 Prompt Builder

This skill reflects the current full-stack v0 product model, not the legacy UI-only generator.

## Origin version check

Canonical source:

```text
https://github.com/AndreAlmeidaDC/v0-prompt-builder
```

At meaningful use, follow `references/version-check.md`. Never self-update silently.

## Load order

1. Read `references/vibecode-core.md`.
2. Read `references/platform-v0.md`.
3. Use `references/archetypes.md` only when platform choice is genuinely open.
4. Apply the smallest project mode that fits the request.

## Non-negotiable boundaries

- Existing repository state beats assumed stack.
- Project knowledge and plan are separate from execution prompts.
- Backend, database and auth are optional until required by behavior.
- One implementation slice per prompt.
- Use branch/PR workflow and fresh verification.
- Ask/Auto/Full permissions are a risk decision, not a convenience toggle.
- Do not merge, deploy, connect production data, spend money or perform public actions without explicit approval.

## Output

Provide one of:

- project knowledge block;
- planning prompt;
- atomic implementation prompt;
- diagnostic/reanchoring prompt;
- verification prompt;
- release checklist.

Do not dump all of them when only one is needed.

## Change history

| Date | Version | Change |
|---|---|---|
| 2026-09-02 | 2026.09.02 | Rebuilt for current full-stack v0: Vercel Sandbox, terminal permissions, Git/PR, databases, integrations, proportional architecture and verified execution. |
