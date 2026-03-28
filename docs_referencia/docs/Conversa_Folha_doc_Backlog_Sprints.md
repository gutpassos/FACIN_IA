# Conversa_Folha_doc - Backlog por Sprints

Autor: Guttenberg Ferreira Passos  
Modelo LLM de referência: GPT-5.4  
Ambiente validado: figmm  
Data: 28 de março de 2026

## 1. Objetivo

Organizar a iniciativa documental em sprints curtas, com foco em artefatos verificáveis e rastreáveis.

## 2. Sprints

### Sprint 1 - Levantamento e baseline

| ID | Item | Prioridade | Critério de aceite |
| --- | --- | --- | --- |
| S1-01 | Inventariar arquivos-fonte da pasta Conversa_Folha | Alta | inventário validado |
| S1-02 | Mapear schema SQL e carga CSV | Alta | tabelas e campos descritos |
| S1-03 | Identificar docs legados para adaptação | Alta | lista de referência consolidada |
| S1-04 | Levantar restrições de ambiente e modelo | Média | uso exclusivo de figmm e GPT-5.4 formalizados |

### Sprint 2 - Arquitetura e governança

| ID | Item | Prioridade | Critério de aceite |
| --- | --- | --- | --- |
| S2-01 | Redigir documento de projeto | Alta | projeto publicado |
| S2-02 | Redigir plano executivo e RACI | Alta | plano publicado |
| S2-03 | Produzir arquitetura da solução e arquitetura-alvo documental | Alta | diagramas e explicações publicados |
| S2-04 | Documentar tecnologias, integrações e regras de negócio | Alta | pacote funcional publicado |

### Sprint 3 - Avaliação e conformidade

| ID | Item | Prioridade | Critério de aceite |
| --- | --- | --- | --- |
| S3-01 | Aplicar as seis dimensões do FACIN_IA | Alta | avaliação por dimensão concluída |
| S3-02 | Produzir matriz MRO_RACI | Alta | matriz publicada |
| S3-03 | Consolidar LGPD, Resolução CD/ANPD nº 19/2024 e risco algorítmico | Alta | seção normativa final publicada |
| S3-04 | Registrar erros encontrados e resolvidos | Média | pasta errors publicada |

### Sprint 4 - Publicação e manutenção

| ID | Item | Prioridade | Critério de aceite |
| --- | --- | --- | --- |
| S4-01 | Gerar documentação do código por análise estática | Alta | inventário técnico disponível |
| S4-02 | Converter todos os artefatos para html e pdf | Alta | arquivos publicados |
| S4-03 | Publicar índice e dashboard executivos | Alta | navegação central disponível |
| S4-04 | Contextualizar o agente FACIN_IA ao workspace | Média | agente atualizado |

## 3. Itens Transversais

1. manter rastreabilidade entre achado, documento afetado e resolução adotada;
2. revisar aderência à restrição de não alteração do código original;
3. garantir executabilidade do gerador no ambiente figmm;
4. preservar Português do Brasil em todos os artefatos.
