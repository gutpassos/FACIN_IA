---
name: facin-ia-diagnostico
description: Diagnosticar a maturidade FACIN_IA de um projeto, orgao, produto ou iniciativa de IA a partir de evidencias fornecidas pelo usuario.
argument-hint: Informe o contexto avaliado, o escopo, o objetivo do diagnostico e as evidencias disponiveis.
agent: FACIN_IA
---

# Diagnostico FACIN_IA por evidencias

Autor: Guttenberg Ferreira Passos

Execute um diagnostico de maturidade FACIN_IA para o contexto informado pelo usuario.

## Entradas esperadas

- contexto institucional ou do projeto;
- escopo da avaliacao;
- objetivo do diagnostico;
- evidencias documentais, tecnicas, processuais ou gerenciais;
- restricoes, riscos ou obrigacoes normativas relevantes.

Se o usuario nao fornecer tudo, solicite apenas o minimo necessario para emitir um diagnostico defensavel.

## Referencias obrigatorias

- [Agente FACIN_IA](../agents/facin-ia.md)
- [Skill FACIN_IA](../skills/facin-ia/SKILL.md)
- [Metodo FACIN_IA](../skills/facin-ia/metodo-facin-ia.md)
- [Checklist de avaliacao](../skills/facin-ia/checklist-avaliacao.md)
- [Template de especificacao](../skills/facin-ia/template-especificacao.md)

## Instrucoes de execucao

1. Delimite claramente o objeto avaliado.
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

1. Resumo executivo
2. Evidencias consideradas
3. Diagnostico por dimensao
4. Maturidade consolidada
5. Recomendacoes priorizadas
6. Evidencias adicionais requeridas
7. Proximos artefatos recomendados