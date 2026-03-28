---
name: facin-ia-diagnostico
description: Diagnosticar a maturidade FACIN_IA de um projeto, orgao, produto ou iniciativa de IA a partir de evidencias fornecidas pelo usuario.
argument-hint: Informe o contexto avaliado, o escopo, o objetivo do diagnostico e as evidencias disponiveis.
agent: FACIN_IA
---

# Diagnostico FACIN_IA por evidencias

Execute um diagnostico de maturidade FACIN_IA para o contexto informado pelo usuario.

## Entradas esperadas

Considere, quando disponivel:

- contexto institucional ou do projeto;
- escopo da avaliacao;
- objetivo do diagnostico;
- evidencias documentais, tecnicas, processuais ou gerenciais;
- restricoes, riscos ou obrigacoes normativas relevantes.

Se o usuario nao fornecer todos esses elementos, solicite apenas o minimo necessario para emitir um diagnostico defensavel.

## Referencias obrigatorias

Use como base metodologica principal:

- [Agente FACIN_IA](../agents/FACIN_IA.agent.md)
- [Skill FACIN_IA](../skills/facin-ia/SKILL.md)
- [Metodo FACIN_IA](../skills/facin-ia/metodo-facin-ia.md)
- [Checklist de avaliacao](../skills/facin-ia/checklist-avaliacao.md)
- [Template de especificacao](../skills/facin-ia/template-especificacao.md)

## Instrucoes de execucao

1. Delimite claramente o objeto avaliado: orgao, projeto, produto, servico ou caso de uso.
2. Enumere as evidencias consideradas e diferencie evidencia observada de inferencia.
3. Estruture a avaliacao nas seis dimensoes obrigatorias do FACIN_IA.
4. Atribua nivel de maturidade de 1 a 5 por dimensao somente quando houver base minima para isso.
5. Quando faltar evidencia, registre explicitamente a lacuna e reduza o grau de certeza da conclusao.
6. Identifique riscos, fragilidades de governanca, dependencias e controles ausentes.
7. Produza recomendacoes acionaveis, priorizadas e vinculadas a evidencias faltantes ou riscos observados.
8. Se as evidencias permitirem, proponha um indice geral de maturidade e explique como ele foi inferido.
9. Nao invente politicas, comites, logs, controles ou processos inexistentes.
10. Se a demanda envolver implantacao tecnica, finalize com os artefatos de especificacao que devem existir antes de qualquer codigo.

## Formato de saida obrigatorio

Entregue a resposta com as secoes abaixo:

## 1. Resumo executivo

- contexto avaliado;
- objetivo do diagnostico;
- conclusao geral em linguagem executiva.

## 2. Evidencias consideradas

- liste documentos, artefatos, relatos ou sinais utilizados;
- indique limites de confianca quando as evidencias forem incompletas.

## 3. Diagnostico por dimensao

Para cada dimensao, informe:

- nivel atribuido ou status de avaliacao inconclusiva;
- justificativa objetiva;
- evidencias observadas;
- lacunas principais;
- risco associado.

Dimensoes obrigatorias:

1. Estrategia e Governanca de IA
2. Dados e Infraestrutura
3. Talento e Cultura
4. Desenvolvimento e Operacao de IA (DevOps/MLOps)
5. Etica, Transparencia e Gestao de Risco
6. Impacto Social e Valor

## 4. Maturidade consolidada

- apresente o nivel geral estimado, se defensavel;
- explique a logica usada para consolidacao;
- explicite o grau de confianca do diagnostico.

## 5. Recomendacoes priorizadas

Separe as recomendacoes em:

- curto prazo;
- medio prazo;
- estruturantes.

Para cada recomendacao, indique:

- problema que corrige;
- evidencia ou controle esperado;
- responsavel sugerido;
- impacto esperado.

## 6. Evidencias adicionais requeridas

- liste o que falta para refinar ou auditar o diagnostico.

## 7. Proximos artefatos recomendados

- indique quais artefatos FACIN_IA devem ser produzidos a seguir, como especificacao, matriz de indicadores, avaliacao etica, plano de adequacao ou checklist de rastreabilidade.

## Exemplo de uso

Use este prompt para pedidos como:

- avaliar a maturidade de governanca de IA de um orgao publico a partir de politicas, atas, pipelines e relatorios;
- diagnosticar um projeto de IA com base em evidencias de dados, prompts, logs, comites e fluxos de aprovacao;
- comparar a situacao atual de um produto com o estado-alvo de governanca FACIN_IA.