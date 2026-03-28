---
name: facin-ia
description: Aplicar o metodo FACIN_IA para diagnosticar maturidade de governanca de IA, criar especificacoes antes de codigo, definir indicadores, evidencias, rastreabilidade, controles de risco e adaptar a metodologia a outros projetos ou organizacoes.
argument-hint: Informe o contexto do projeto, orgao ou iniciativa de IA e o artefato desejado.
---

# FACIN_IA Skill

Autor: Guttenberg Ferreira Passos

Use esta skill quando a tarefa envolver governanca de IA, maturidade institucional, especificacao orientada por artefatos ou adaptacao do metodo FACIN_IA a um novo contexto.

## Objetivo

Aplicar o principio central do FACIN_IA:

> A inteligencia artificial executa especificacoes governadas. O codigo e artefato derivado. A especificacao e o contrato primario.

## Quando carregar esta skill

Carregue esta skill quando o usuario pedir para:

- avaliar maturidade de governanca de IA;
- definir politica, modelo operacional ou papeis de IA;
- criar especificacao funcional e tecnica para uso de IA;
- definir indicadores, evidencias e niveis de maturidade;
- revisar rastreabilidade de prompts, modelos, dados e decisoes;
- adaptar o metodo para outro orgao, empresa ou produto.

## Processo recomendado

1. Identifique o tipo de demanda: diagnostico, desenho de governanca, especificacao, auditoria, adaptacao ou roadmap.
2. Colete o contexto institucional minimo: objetivo, servico, risco, publico afetado, stack, dados e ambiente operacional.
3. Estruture a analise nas seis dimensoes do FACIN_IA.
4. Sempre que possivel, produza artefatos reutilizaveis em vez de texto solto.
5. Para cada recomendacao, associe evidencia minima, periodicidade, responsavel e risco mitigado.
6. Se houver pedido de implementacao tecnica, derive primeiro a especificacao e somente depois proponha codigo, pipeline ou automacao.

## Estrutura minima de resposta

Quando aplicavel, entregue as secoes abaixo:

1. Identificacao do projeto
2. Especificacao funcional
3. Especificacao tecnica
4. Criterios de aceitacao
5. Testes derivados
6. Restricoes de IA
7. Log de interacoes com IA

## Dimensoes obrigatorias

Use sempre estas seis dimensoes para analise de maturidade ou governanca:

1. Estrategia e Governanca de IA
2. Dados e Infraestrutura
3. Talento e Cultura
4. Desenvolvimento e Operacao de IA (DevOps/MLOps)
5. Etica, Transparencia e Gestao de Risco
6. Impacto Social e Valor

## Niveis de maturidade

- Nivel 1 - Inicial
- Nivel 2 - Em Desenvolvimento
- Nivel 3 - Otimizado
- Nivel 4 - Consolidado
- Nivel 5 - Estabelecido

## Recursos desta skill

- [Metodo resumido](./metodo-facin-ia.md)
- [Template de especificacao](./template-especificacao.md)
- [Checklist de avaliacao](./checklist-avaliacao.md)

## Regras de saida

- Nao trate IA como recurso isolado; trate como capacidade governada.
- Nao aceite recomendacoes sem evidencia, rastreabilidade ou responsavel.
- Nao proponha operacao em producao para casos medio ou alto risco sem controles formais.
- Quando houver lacunas de contexto, declare o que falta e quais premissas estao sendo assumidas.

## Observacao

Esta skill foi extraida do projeto FACIN_IA para reutilizacao em outros repositorios. Se o repositorio atual nao contiver materiais proprios do metodo, use os recursos desta pasta como base normativa principal.