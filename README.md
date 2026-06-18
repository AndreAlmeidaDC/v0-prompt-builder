# v0-prompt-builder

Skill de IA que faz o **v0 da Vercel** entregar componentes React prontos para o seu
projeto, e não rascunhos genéricos. A diferença está em como você especifica — e a skill
te ensina a especificar no nível que o v0 recompensa.

---

## O problema que esta skill resolve

O v0 é provavelmente o melhor gerador de UI React do mercado. Mas ele responde ao nível
de detalhe que recebe: peça "um dashboard bonito" e você ganha algo genérico, sem os
estados que seu app precisa, fora da identidade visual do seu projeto, que vai precisar
ser refeito. Peça com precisão — comportamento, estados, tokens de design, componentes
shadcn nomeados — e você ganha algo que cola direto no seu código.

A maioria das pessoas opera no primeiro modo e conclui que "o v0 é legal mas não serve
para produção". O problema não é o v0; é a especificação.

Há também um passo que quase todo mundo pula: configurar o design system antes de gerar.
Sem isso, cada componente sai com um visual ligeiramente diferente, e você passa mais
tempo harmonizando do que teria passado configurando os tokens uma vez.

## Como a skill foi pensada

A skill trata o v0 pelo que ele realmente é: **um gerador de UI de altíssima qualidade,
não um app builder**. Por isso o fluxo dela é diferente das skills de app completo — é
focado em componente, estado e sistema de design, não em produto e banco de dados.

### Explorando as forças do v0

- **O v0 gera shadcn/ui e Tailwind excepcionalmente bem.** A skill aproveita isso
  especificando componentes shadcn pelo nome e descrevendo intenção visual no vocabulário
  que o v0 entende melhor.
- **O v0 tem design mode** (ajuste visual direto, sem gastar crédito de prompt). A skill
  te ensina a usar design mode para refino estético e reservar prompts novos só para
  mudanças estruturais — economizando créditos.
- **O v0 integra com shadcn/ui Registry.** A skill te guia a configurar a registry e os
  tokens uma vez, para que todo componente nasça consistente com a sua marca.
- **O v0 aceita imagem como referência.** A skill te orienta a colar screenshots ou
  mockups quando o visual-alvo é mais fácil de mostrar do que descrever.

### Mitigando as fraquezas do v0

- **Output genérico por especificação fraca.** Mitigado com um método de especificação
  de componente que cobre comportamento, todos os estados (default, hover, focus,
  disabled, loading, error, empty, success), props e intenção visual.
- **Inconsistência visual entre componentes.** Mitigada forçando o passo de configurar o
  design system antes do primeiro componente, não depois do quinto.
- **Desperdício de crédito em re-prompts.** Mitigado distinguindo claramente o que se
  resolve em design mode (sem custo) do que exige novo prompt.
- **Expectativa errada de que o v0 entrega um app.** Mitigada deixando explícito que o
  v0 gera componentes para integrar no seu projeto; backend, dados e testes são seu
  trabalho. A skill te aponta para outra ferramenta quando o que você quer é um app
  completo.

## O que a skill faz, passo a passo

**Passo 1 — Design system.** Te guia a mapear seus tokens (cores, radius, tipografia)
para o tema shadcn/ui e, se aplicável, configurar a Registry. Feito uma vez, todos os
componentes herdam.

**Passo 2 — Especificação de componente.** Para cada componente: comportamento, estados,
props, intenção visual e componentes shadcn nomeados. Um de cada vez.

**Passo 3 — Iteração visual.** Gerar, ver no preview, ajustar em design mode (sem
crédito), e fazer novo prompt só para mudanças estruturais. Copiar o código final para
o seu projeto.

**Reancoragem.** Se um componente sai fora do design system, a skill identifica o que
recolar (tokens, componente shadcn alvo) para recuperar a consistência sem regenerar
do zero.

## Como usar

1. Carregue esta skill no seu chat de IA (Claude, ChatGPT, etc.)
2. Faça o Passo 1 (design system) uma vez para o projeto
3. Para cada componente, use o Passo 2 para especificar e o Passo 3 para iterar
4. Copie o código gerado para o seu projeto Next.js/React

A skill gera os prompts; você faz a ponte de copiar e colar para o v0. Ela não
se conecta ao v0 nem executa nada por você — é uma ferramenta de raciocínio e
especificação, não de automação.

## FAQ

**O v0 serve para fazer um app inteiro?**
Ele evoluiu para cobrir mais coisa, mas o ponto forte continua sendo UI. Se você quer um
app completo com backend, banco e deploy, uma ferramenta de app builder rende mais. A
skill te diz isso quando for o caso.

**Por que preciso configurar design system antes de gerar?**
Porque sem tokens definidos, cada componente sai com um visual um pouco diferente. Cinco
minutos configurando economizam horas harmonizando depois.

**O que é design mode e por que importa?**
É o modo do v0 onde você ajusta layout, texto e tipografia direto, sem gastar crédito de
prompt. A skill te ensina a usá-lo para refino, reservando prompts para mudança real de
estrutura.

**Preciso usar shadcn/ui?**
É o default do v0 e onde ele rende melhor. Dá para usar outras bibliotecas, mas adiciona
trabalho. A skill assume shadcn/ui salvo indicação contrária.

**A skill se conecta ao v0 automaticamente?**
Não. Ela gera as especificações e prompts; você usa no v0. Funciona em qualquer chat de IA.

**Sou designer, não dev. Ainda vale?**
Vale para gerar e iterar a UI, mas lembre que o output é código React para integrar num
projeto. Sem um desenvolvedor para fazer a integração final, o componente fica só no v0.

## Estrutura do repositório

```
SKILL.md                          # Ponto de entrada: papel e como usar
references/
  vibecode-core.md                # Processo de engenharia (compartilhado na família)
  platform-v0.md                  # Design system, Registry, estados, design mode
  archetypes.md                   # Guia de escolha de plataforma
  version-check.md                # Protocolo de auto-atualização
templates/
  PRD.md                          # Template de requisitos de produto
  DATA_MODEL.md                   # Template de modelo de dados
  USER_FLOW.md                    # Template de fluxo de usuário
scripts/
  validate_skill.py               # Validação local da skill
```

## Por que existem 6 skills e não uma só

Essa pergunta é legítima — o processo de fundo (especificar antes de gerar, modelar
dados, iterar de forma atômica, reancorar quando a IA perde o contexto) é o mesmo em
todas as plataformas. Seria tentador fazer uma skill única que cobre tudo.

Não fizemos, por três razões:

**1. Contexto desperdiçado.** Uma skill única carregaria as particularidades de seis
plataformas em toda sessão, sendo que você só usa uma. A maior parte do que entrasse no
contexto seria ruído para a sua tarefa. Skills separadas carregam só o que importa para
a plataforma que você escolheu.

**2. As plataformas divergem mais do que parecem.** O v0 gera componentes, não apps.
O a0.dev fala de telas e navegação, não de páginas e rotas. O Base44 não te dá o código.
O emergent usa MongoDB e um time de agentes; os outros não. Espremer tudo num fluxo único
exigiria tantos "se for plataforma X, faça Y" que o resultado seria confuso e frágil.

**3. Evolução independente.** Cada plataforma muda no seu ritmo. Quando uma lança um
recurso novo, a skill dela é atualizada sem tocar nas outras cinco.

O que é genuinamente compartilhado (o processo de engenharia) vive em um único arquivo,
`references/vibecode-core.md`, idêntico em todas as skills. Assim evitamos duplicação no
que importa e mantemos independência onde importa.

## Família vibecode

| Skill | Plataforma | Melhor para |
|---|---|---|
| [lovable-prompt-builder](https://github.com/AndreAlmeidaDC/lovable-prompt-builder) | Lovable | App web full-stack com fluxo guiado passo a passo |
| [bolt-prompt-builder](https://github.com/AndreAlmeidaDC/bolt-prompt-builder) | bolt.new | App web full-stack com brief único e controle total |
| **v0-prompt-builder** (esta skill) | v0 (Vercel) | Componentes React/shadcn de alta qualidade |
| [a0-prompt-builder](https://github.com/AndreAlmeidaDC/a0-prompt-builder) | a0.dev | App mobile nativo iOS/Android |
| [base44-prompt-builder](https://github.com/AndreAlmeidaDC/base44-prompt-builder) | Base44 | Ferramenta interna / protótipo com backend incluído |
| [emergent-prompt-builder](https://github.com/AndreAlmeidaDC/emergent-prompt-builder) | emergent.sh | Full-stack multi-agente (web + mobile), código seu |

## Licença

MIT — André Almeida
