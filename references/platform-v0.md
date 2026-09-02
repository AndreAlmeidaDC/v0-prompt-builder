# Platform Reference — v0

**Última verificação:** 2026-09-02, documentação oficial do v0.

O v0 atual é um ambiente de desenvolvimento com agente, editor, preview, Vercel Sandbox, terminal, integração Git e suporte a aplicações full-stack. O modelo antigo de “gerador de UI sem backend” está obsoleto.

Fontes oficiais principais:

- https://v0.dev/docs/full-stack-apps
- https://api2.v0.dev/docs/sandbox
- https://api2.v0.dev/docs/terminal-commands
- https://api2.v0.dev/docs/github
- https://api2.v0.dev/docs/databases
- https://api2.v0.dev/docs/agentic-features

## Modos recomendados

### 1. Existing repository

Conecte o repositório e inspecione `package.json`, framework, rotas, estilos, testes, Git e ambientes antes de propor mudanças. O v0 cria branch por chat e registra mudanças em commits; use PR para revisão em vez de trabalhar diretamente na principal.

### 2. Greenfield full-stack app

O v0 tende a produzir resultados mais confiáveis com Next.js, incluindo server actions e API routes, mas não force migração em projeto existente. Comece pela menor vertical de valor. Adicione banco, auth ou integração somente quando o comportamento exigir.

### 3. UI and design system

Use para componentes, páginas, tokens, shadcn e composição visual. Declare estados, dados, responsividade, acessibilidade e o que deve ser preservado. Screenshot é referência, não autorização para copiar marca ou conteúdo.

### 4. Repair and review

Peça primeiro inspeção, reprodução do problema e plano. Não permita refatoração ampla dentro de correção pontual. Exija teste do sintoma original.

## Sandbox e terminal

Cada chat executa em Vercel Sandbox isolado com projeto, servidor, preview e terminal. O terminal pode inspecionar Git, executar testes e usar CLIs.

Modos de permissão:

- **Ask:** adequado para repositórios sensíveis, credenciais, banco real ou comandos remotos;
- **Auto:** padrão para trabalho normal em sandbox com regras claras;
- **Full:** somente em projeto descartável, sem credenciais, dados críticos ou produção; requer revisão posterior do histórico.

Full não é atalho para confiança. Defina previamente comandos permitidos, áreas graváveis e ações proibidas.

## Git workflow

1. confirme branch e base;
2. registre escopo e arquivos permitidos;
3. implemente uma mudança;
4. rode sensores;
5. revise diff;
6. abra PR;
7. só faça merge ou deploy com aprovação.

Nunca peça ao agente para resolver conflito apagando mudanças desconhecidas.

## Full-stack e dados

O v0 pode criar rotas de backend e conectar bancos como Supabase, Neon, Upstash e outros serviços do marketplace. Isso não torna backend obrigatório.

Antes de persistência, defina:

- entidade e ownership;
- autenticação e autorização;
- validação client/server/database;
- isolamento entre usuários/tenants;
- secrets server-side;
- migração, backup e rollback;
- ambiente de preview versus produção.

Variável pública de cliente não é secret. Nunca exponha credencial privilegiada por prefixo público.

## MCP e integrações

Marketplace e MCP ampliam as ferramentas disponíveis ao agente. Para cada integração, registre:

- ações de leitura e escrita;
- dados acessados;
- escopos OAuth;
- confirmação humana;
- ambiente;
- logging e rollback.

Não dê Full permission a um agente com ferramentas privilegiadas e credenciais reais.

## Prompt de planejamento

```text
Inspecione o projeto e produza um plano sem editar arquivos.

Objetivo: [resultado]
Escopo permitido: [áreas]
Preservar: [comportamentos]
Riscos: [dados, auth, integração, produção]

Entregue:
1. fatos observados;
2. hipótese do problema ou arquitetura;
3. arquivos afetados;
4. etapas pequenas;
5. verificação por etapa;
6. rollback;
7. dúvidas que não podem ser respondidas pelo repositório.
```

## Prompt atômico

```text
Implemente somente [mudança única] na branch atual.

Preserve: [itens]
Arquivos permitidos: [lista ou área]
Comportamento esperado: [contrato]
Estados/edge cases: [lista]
Critérios de aceite: [observáveis]
Verificação: [comandos e fluxo]

Não faça refatoração fora do escopo, não altere produção e não faça merge ou deploy.
Ao terminar, mostre diff resumido, comandos executados, resultados e pontos cegos.
```

## Verificação mínima

- diff e escopo;
- lint/typecheck/build conforme projeto;
- testes relevantes;
- browser para fluxo alterado;
- console e rede;
- acessibilidade quando houver UI;
- segurança e autorização quando houver dados;
- preview não conectado acidentalmente a produção.

## Claims voláteis

Modelos, integrações, limites e preços mudam. Não grave valores fixos no prompt. Verifique a documentação oficial na data do uso.
