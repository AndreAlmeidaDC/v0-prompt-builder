---
name: v0-prompt-builder
description: >
  Skill para gerar componentes React e páginas de UI de alta qualidade com v0 by Vercel. Foco em shadcn/ui, Tailwind, design systems e iteração visual. Use quando o usuário quiser gerar componentes ou UI para projeto Next.js/React existente.
license: MIT
---

# v0 (Vercel) Prompt Builder

## Origin version check

At the start of a meaningful use, check whether this skill has a newer upstream version.
The canonical source is:

```text
https://github.com/AndreAlmeidaDC/v0-prompt-builder
```

If a newer version exists, summarize what changed and ask the user whether to update
before proceeding. Never self-update silently. For the detailed protocol, read
`references/version-check.md`.

*Autor: André Almeida*

---

## Quando usar esta skill

Use esta skill quando o usuário mencionar v0, v0.dev, v0.app, ou quiser gerar componentes React/Next.js/shadcn sem construir um app completo do zero.

Se não tiver certeza se esta é a plataforma certa, leia `references/archetypes.md`
para um guia de escolha.

---

## Como esta skill funciona

Esta skill usa um processo compartilhado (vibecode CORE) + detalhes específicos
do v0 (Vercel):

1. **Carregue `references/vibecode-core.md`** — processo completo de especificação
   e execução (intake, modelagem, branding, validação, geração, reancoragem).

2. **Carregue `references/platform-v0.md`** — vocabulário, perguntas adicionais,
   formatos de artefato e especificidades do v0 (Vercel).

3. Execute o fluxo do CORE usando os detalhes da plataforma onde aplicável.

---

## Histórico de Alterações

| Data | Versão | Alterações |
|---|---|---|
| 2026.06.16 | 2026.06.16 | Criação da skill no formato vibecode: CORE compartilhado + referência específica de plataforma. |
