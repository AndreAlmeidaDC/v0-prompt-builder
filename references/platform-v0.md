# Platform Reference — v0 by Vercel

v0 (v0.app, anteriormente v0.dev) é o gerador de UI da Vercel. Foco: componentes
React, Next.js, Tailwind CSS e shadcn/ui de altíssima qualidade. É um **gerador de
UI**, não um app builder completo. O output é código para integrar no seu projeto,
não um app deployado.

> **Atenção de arquétipo:** o v0 é fundamentalmente diferente do Lovable, bolt e a0.dev.
> Use o Fluxo Alternativo de UI do CORE (não as Fases 1-6) ao trabalhar com o v0.
> Esta referência detalha os passos desse fluxo.

---

## O que o v0 faz (e o que não faz)

**Faz:**
- Gera componentes React com shadcn/ui e Tailwind de alta qualidade
- Gera páginas e layouts completos para Next.js
- Aceita screenshot/mockup como referência visual
- Itera visualmente via "design mode" (sem gastar créditos de prompt)
- Deploy 1-click para Vercel (você integra no seu projeto)

**Não faz:**
- Não gera backend nativo (você conecta sua própria API)
- Não faz setup de banco de dados, auth ou deploy completo de app
- Não tem branding workflow embutido — design system vai via Registry
- Não assume responsividade — você pede explicitamente

---

## Passo v0-1 — Configurar o Design System

Antes de gerar qualquer componente, defina a base visual. Sem isso, o v0 gera
componentes bonitos mas fora da identidade da marca.

**Se você tem design system:**
1. Aplique seus tokens (cores, radius, espaçamento, fontes) ao shadcn/ui theme
   via `globals.css` e `tailwind.config.ts`
2. Se quiser integração profunda, configure uma **shadcn/ui Registry** (veja docs:
   v0.app/docs/design-systems). A registry permite que o v0 gere diretamente
   respeitando seus componentes e tokens.
3. Com a registry configurada, o botão "Open in v0" abre o chat com o contexto
   do seu design system pré-carregado.

**Se não tem design system ainda:**
Defina antes de gerar o primeiro componente:
- Cor primária, secundária e neutras (hex)
- Border radius padrão (nenhum / sm / md / lg / full)
- Fonte para corpo e headings
- Dark mode: sim / não / toggle

---

## Passo v0-2 — Especificar o Componente

Um componente de cada vez. Um prompt de v0 de qualidade contém:

**Comportamento:** o que o componente faz (não só o nome)
> "Um botão de submit que desabilita e mostra spinner durante o loading, e muda
> para ícone de check quando a operação é bem-sucedida."

**Estados explícitos:** liste os estados que o componente deve tratar
> Estados: default, hover, disabled, loading (com spinner), success (com check), error (com mensagem inline)

**Dados / props:** o que o componente recebe (se souber)
> "Recebe: label (string), isLoading (boolean), onSuccess (callback)"

**Componentes shadcn nomeados:** se souber quais quer usar
> "Use shadcn Button como base, Badge para status, e Tooltip para o ícone de info"

**Intenção visual:** não só "bonito" — seja específico
> "Visual clean, sem bordas grossas, ícones Lucide. Cores do design system."

**Responsividade** (não é automática — declare se precisar):
> "Em mobile: stacked vertically. Em desktop: side-by-side com gap de 24px."

**Referência visual:** screenshot ou mockup colado no chat acelera muito.

---

## Passo v0-3 — Iterar e Exportar

O loop do v0 é **visual**, diferente do loop de features do Lovable/Bolt:

1. Gere o componente
2. Veja no preview interativo do v0
3. Use o **design mode** para ajustes não-estruturais (texto, espaçamento, cores,
   tipografia) — sem gastar créditos extras de prompt
4. Para mudanças de comportamento, estados ou estrutura → novo prompt específico
5. Quando satisfeito: copie o código e integre no seu projeto

**Não tente fazer tudo num prompt só.** Se o componente tem variantes complexas,
gere a variante principal primeiro, depois adicione as outras iterativamente.

---

## Reancoragem no v0

Se o componente gerado não respeitar o design system:
1. Verifique se os tokens de tema estão aplicados (globals.css / tailwind.config.ts)
2. No próximo prompt, especifique o componente shadcn alvo e os tokens relevantes
3. Se tiver registry configurada, mencione explicitamente no prompt

---

## Créditos e Modelos (2026)

Três tiers de modelo disponíveis em todos os planos: Mini, Pro, Max.
- Free: $5 em créditos/mês (consome rápido com Pro/Max)
- Premium: $20/mês (projetos pequenos/médios)
- Design mode e preview: sem créditos extras
- Prompts concisos e estruturados gastam menos créditos

---

## Quando o v0 NÃO é a ferramenta certa

- Você quer um app completo com backend → use Lovable ou bolt.new
- Você quer app mobile nativo → use a0.dev
- Você quer backend sem código manual → use Base44
- Você não usa React/Next.js → o v0 é otimizado para este ecossistema;
  adaptar para outros frameworks é possível mas adiciona trabalho

---

## Limitações do v0

- Output é um "strong draft": acessibilidade profunda, data layer e testes são
  responsabilidade do desenvolvedor.
- Sem backend nativo — você integra a API.
- Responsividade não é assumida — declare explicitamente.
- Se não configurar design system/tokens, cada componente pode ter visual ligeiramente
  diferente dos outros.
