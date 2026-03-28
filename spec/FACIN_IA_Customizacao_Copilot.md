# FACIN_IA - Customização para GitHub Copilot

Autor: Guttenberg Ferreira Passos

Especificação da customização reutilizável do FACIN_IA para uso no GitHub Copilot em projetos que precisam estruturar governança de IA, maturidade institucional, especificação antes de código e diagnósticos baseados em evidências.

## 1. Objetivo

Esta customização transforma o método FACIN_IA em artefatos diretamente utilizáveis no VS Code com GitHub Copilot, permitindo que equipes reutilizem a metodologia sem repetir o mesmo contexto em cada conversa.

O objetivo é disponibilizar uma base operacional para:

1. estruturar diagnósticos de maturidade em governança de IA;
2. orientar a criação de especificações antes de código;
3. padronizar a avaliação de evidências, riscos, controles e rastreabilidade;
4. apoiar a adaptação do método para diferentes órgãos, produtos, serviços ou projetos.

## 2. Componentes da customização

O pacote atual da customização FACIN_IA é composto por três tipos principais de artefatos.

### 2.1 Agente customizado

Arquivo:

- `.github/agents/FACIN_IA.agent.md`

Função:

- definir a persona especializada do FACIN_IA;
- orientar a análise nas seis dimensões obrigatórias do método;
- exigir especificação, evidência e rastreabilidade antes de qualquer recomendação técnica mais profunda;
- padronizar o comportamento do Copilot para tarefas de governança aplicada à IA.

### 2.2 Skill metodológica

Arquivos:

- `.github/skills/facin-ia/SKILL.md`
- `.github/skills/facin-ia/metodo-facin-ia.md`
- `.github/skills/facin-ia/template-especificacao.md`
- `.github/skills/facin-ia/checklist-avaliacao.md`

Função:

- encapsular o método FACIN_IA como capacidade reutilizável;
- disponibilizar regras, princípios, checklist e template de especificação;
- reduzir repetição de instruções em múltiplos projetos;
- servir como base normativa para análises, diagnósticos e planos de adequação.

### 2.3 Prompt reutilizável de diagnóstico

Arquivo:

- `.github/prompts/facin-ia-diagnostico.prompt.md`

Função:

- permitir execução padronizada de diagnósticos FACIN_IA por slash command;
- guiar a avaliação com base em evidências;
- exigir saída estruturada com resumo executivo, maturidade por dimensão, recomendações e evidências adicionais requeridas.

## 3. Estrutura conceitual aplicada

A customização preserva integralmente a estrutura metodológica do FACIN_IA, incluindo as seis dimensões obrigatórias:

1. Estratégia e Governança de IA
2. Dados e Infraestrutura
3. Talento e Cultura
4. Desenvolvimento e Operação de IA (DevOps/MLOps)
5. Ética, Transparência e Gestão de Risco
6. Impacto Social e Valor

Também preserva os princípios centrais do método:

1. a IA executa especificações governadas;
2. o código é artefato derivado;
3. prompt, modelo, dado e decisão são artefatos rastreáveis;
4. ideação e produção devem permanecer segregadas;
5. observabilidade e trilha de auditoria são obrigatórias.

## 4. Casos de uso suportados

A customização foi desenhada para apoiar tarefas como:

1. diagnóstico de maturidade de governança de IA em órgãos públicos;
2. avaliação de projetos ou produtos intensivos em IA a partir de evidências;
3. elaboração de especificação funcional e técnica antes de desenvolvimento;
4. revisão de controles de risco, ética, transparência e responsabilização;
5. adaptação do método FACIN_IA para outros contextos institucionais.

## 5. Instalação em outros projetos

Na forma atual, a reutilização ocorre por cópia dos artefatos de customização para o repositório de destino.

Passos:

1. copiar `.github/agents/` para o novo repositório;
2. copiar `.github/skills/facin-ia/` para o novo repositório;
3. copiar `.github/prompts/` caso o time queira usar também o diagnóstico padronizado;
4. abrir o projeto no VS Code com GitHub Copilot habilitado;
5. selecionar o agente `FACIN_IA` no chat;
6. opcionalmente invocar `/facin-ia` para carregar a skill;
7. para avaliação orientada por evidências, invocar `/facin-ia-diagnostico`.

## 6. Forma de uso recomendada

### 6.1 Uso do agente FACIN_IA

Recomendado quando a demanda envolver:

- desenho de governança;
- avaliação de maturidade;
- criação de especificação antes de código;
- definição de indicadores, critérios e evidências;
- análise de riscos e controles de IA.

### 6.2 Uso da skill FACIN_IA

Recomendado quando o modelo precisar carregar explicitamente:

- o método resumido;
- o template de especificação;
- o checklist de avaliação.

### 6.3 Uso do prompt facin-ia-diagnostico

Recomendado quando a tarefa for um diagnóstico padronizado e rastreável, com foco em evidências fornecidas pelo usuário.

## 7. Saída esperada do diagnóstico

O diagnóstico conduzido pela customização FACIN_IA deve, quando aplicável, incluir:

1. resumo executivo;
2. evidências consideradas;
3. maturidade por dimensão;
4. nível consolidado ou avaliação inconclusiva;
5. recomendações priorizadas;
6. evidências adicionais requeridas;
7. próximos artefatos recomendados.

## 8. Benefícios para equipes

O uso da customização traz os seguintes ganhos práticos:

1. redução de repetição de contexto em diferentes chats e projetos;
2. maior consistência nas análises de maturidade e governança;
3. padronização de linguagem, critérios e artefatos;
4. melhoria da rastreabilidade metodológica;
5. aceleração da adoção do FACIN_IA em múltiplos times.

## 9. Limites da implementação atual

Na versão atual, a distribuição é feita como customização local de repositório e não como plugin instalável centralmente.

Isso significa que:

1. a instalação ainda depende de copiar as pastas de customização;
2. a atualização entre múltiplos projetos exige replicação controlada das mudanças;
3. um empacotamento futuro como plugin de agente pode simplificar a distribuição organizacional.

## 10. Critérios de aceitação

Esta customização será considerada aderente ao objetivo proposto quando:

1. o agente FACIN_IA estiver disponível para seleção no VS Code;
2. a skill facin-ia puder ser carregada como capacidade reutilizável;
3. o prompt `/facin-ia-diagnostico` puder ser executado como slash command;
4. a análise produzida preservar as seis dimensões e os princípios do método;
5. a documentação permitir instalação e uso em outros projetos;
6. os artefatos publicados estiverem disponíveis em Markdown, HTML e PDF.

## 11. Conclusão

A customização FACIN_IA converte o método em um conjunto operacional de agente, skill e prompt reutilizável, permitindo levar a governança aplicada à IA para o uso cotidiano do GitHub Copilot sem perder rigor metodológico, rastreabilidade nem padronização institucional.