# Conversa_Folha_doc - Backlog de Sprints

Autor: Guttenberg Ferreira Passos  
Modelo LLM de referência do projeto: Claude Opus 4.6  
Ambiente validado: figmm  
Data: 29 de março de 2026

---

## 1. Finalidade

Detalhar o backlog do projeto Conversa_Folha_doc em sprints, com itens priorizados, critérios de aceite, pontos de story, esforço em pessoa-dia e qualificação MRO.

---

## 2. Escala de Estimativa

A escala de pontos segue o modelo de referência FACIN_IA (projeto Foundry), com correspondência para a qualificação da demanda pelo Modelo de Responsabilidade Organizacional (MRO_RACI).

### 2.1 Escala de Complexidade

| Escala | Significado | Pessoa-dia |
| --- | --- | --- |
| 1 ponto | Item pequeno, baixa incerteza e baixo acoplamento | 0,5 a 1 |
| 2 pontos | Item simples, com uma dependência relevante | 1 a 2 |
| 3 pontos | Item moderado, com necessidade de validação cruzada | 2 a 3 |
| 5 pontos | Item de maior complexidade técnica ou institucional | 3 a 5 |
| 8 pontos | Item crítico, com maior risco, integração ou incerteza | 5 a 8 |

### 2.2 Qualificação MRO da Demanda

A complexidade de um item é qualificada pela quantidade e tipo de papéis organizacionais (RACI) que requer:

| Pontos | Qualificação MRO | Papéis ativos (R/A/C) | Exemplo de padrão RACI |
| --- | --- | --- | --- |
| 1 | Operacional simples | 1-2 papéis | DEV=R, GPR=A, demais I |
| 2 | Operacional com dependência | 2-3 papéis | DEV=R, GPR=A, ARQ=C |
| 3 | Tático com validação cruzada | 3-4 papéis | DEV=R, GPR=A, ARQ=C, GOV=C |
| 5 | Tático-institucional | 4-5 papéis | GOV=R, GPR=A, ARQ=C, DEV=C, DPO=C |
| 8 | Estratégico-crítico | 5+ papéis | GOV=R, PAT=A, ARQ=C, DEV=C, AUD=C, DPO=C |

**Referência**: Escala adaptada do documento FACIN_IA_D_P_Foundry_Backlog_Sprints, seção 2.1 — Escala de Estimativa.

---

## 3. Visão Geral das Sprints

| Sprint | Foco | Status |
| --- | --- | --- |
| Sprint 1 | Documentação Base | Concluída |
| Sprint 2 | Documentação Avançada | Concluída |
| Sprint 3 | Avaliação de Maturidade e Gestão | Concluída |
| Sprint 4 | Conformidade, Risco e Planejamento | Concluída |
| Sprint 5 | Publicação e Dashboard | Concluída |

---

## 4. Sprint 1 — Documentação Base

| Item | Pontos | Pessoa-dia | Qualificação MRO | Critério de Aceite | Status |
| --- | ---: | ---: | --- | --- | --- |
| Criar estrutura de pastas (docs/, erros/, scripts/) | 1 | 0,5 | Operacional simples (DEV=R, GPR=A) | Pastas existem no repositório | Concluído |
| Gerar Conversa_Folha_Projeto.md | 3 | 2 | Tático com validação (DEV=R, GPR=A, ARQ=C, GOV=I) | Especificações funcional e técnica em PT-BR | Concluído |
| Gerar Conversa_Folha_Documentacao_Codigo.md | 5 | 4 | Tático-institucional (DEV=R, GPR=A, ARQ=C, GOV=I) | Inventário de módulos app.py e cria_db.py | Concluído |
| Gerar Conversa_Folha_Manual_Usuario.md | 5 | 4 | Tático-institucional (DEV=R, GPR=A, ARQ=C, AUD=C, USR=C) | Manual com instalação, configuração e operação | Concluído |

**Total Sprint 1: 14 pontos · 10,5 pessoa-dia**

---

## 5. Sprint 2 — Documentação Avançada

| Item | Pontos | Pessoa-dia | Qualificação MRO | Critério de Aceite | Status |
| --- | ---: | ---: | --- | --- | --- |
| Gerar Conversa_Folha_Arquitetura_Solucao.md | 5 | 4 | Tático-institucional (ARQ=R, GPR=A, DEV=C, GOV=I) | 5 camadas, grafo LangGraph, diagramas Mermaid | Concluído |
| Gerar Conversa_Folha_Tecnologias.md | 3 | 2 | Tático com validação (ARQ=R, DEV=C, GPR=I) | Stack completo com versões e infraestrutura | Concluído |
| Gerar Conversa_Folha_Integracoes.md | 5 | 4 | Tático-institucional (ARQ=R, GPR=A, DEV=C, GOV=I) | Groq, OpenAI, SQLite, Streamlit mapeados | Concluído |
| Gerar Conversa_Folha_Regras_Negocio.md | 5 | 4 | Tático-institucional (DEV=R, GPR=A, ARQ=C, GOV=C) | 29 regras formalizadas com evidências | Concluído |

**Total Sprint 2: 18 pontos · 14 pessoa-dia**

---

## 6. Sprint 3 — Avaliação de Maturidade e Gestão

| Item | Pontos | Pessoa-dia | Qualificação MRO | Critério de Aceite | Status |
| --- | ---: | ---: | --- | --- | --- |
| Gerar Conversa_Folha_Avaliacao_Maturidade.md | 8 | 6 | Estratégico-crítico (GOV=R, PAT=A, ARQ=C, DEV=C, AUD=C, DPO=I) | 18 indicadores, 6 dimensões, índice geral 1,32 | Concluído |
| Incluir Matriz MRO_RACI | 3 | 2 | Tático com validação (GOV=R, GPR=A, PAT=C, DEV=I) | 8 papéis × 21 atividades mapeados | Concluído |
| Incluir Conformidade LGPD | 5 | 4 | Tático-institucional (GOV=R, PAT=A, DPO=C, AUD=C, DEV=I) | Análise por artigo, Resolução ANPD 19/2024 | Concluído |
| Incluir Risco Algorítmico | 5 | 4 | Tático-institucional (GOV=R, PAT=A, ARQ=C, DEV=C, DPO=C) | 10 riscos com classificação e controles | Concluído |
| Gerar Conversa_Folha_Erros_Resolvidos.md | 3 | 2 | Tático com validação (DEV=R, GPR=A, ARQ=C) | 7 erros documentados com impacto | Concluído |
| Gerar Conversa_Folha_Backlog_Sprints.md | 2 | 1 | Operacional com dependência (DEV=R, GPR=A, GOV=C) | Backlog completo com 5 sprints | Concluído |
| Gerar Conversa_Folha_Backlog_Kanban.md | 2 | 1 | Operacional com dependência (DEV=R, GPR=A, GOV=C) | Quadro Kanban com métricas | Concluído |

**Total Sprint 3: 28 pontos · 20 pessoa-dia**

---

## 7. Sprint 4 — Conformidade, Risco e Planejamento

| Item | Pontos | Pessoa-dia | Qualificação MRO | Critério de Aceite | Status |
| --- | ---: | ---: | --- | --- | --- |
| Gerar Conversa_Folha_Plano_Executivo.md | 5 | 4 | Tático-institucional (GPR=R, PAT=A, ARQ=C, GOV=C) | RACI, cronograma, marcos, riscos | Concluído |
| Gerar Conversa_Folha_Kanban_Executivo.md | 2 | 1 | Operacional com dependência (GPR=R, GOV=C) | Visão executiva com semáforo de status | Concluído |
| Gerar Conversa_Folha_Indice_Executivo.md | 2 | 1 | Operacional com dependência (DEV=R, GPR=A) | Navegação centralizada | Concluído |
| Revisar conformidade LGPD completa | 5 | 4 | Tático-institucional (GOV=R, PAT=A, DPO=C, AUD=C) | 8 aspectos avaliados | Concluído |
| Avaliar riscos algorítmicos | 5 | 4 | Tático-institucional (GOV=R, PAT=A, ARQ=C, DEV=C, DPO=C) | Matriz de risco com mitigações | Concluído |
| Documentar controles e lacunas | 3 | 2 | Tático com validação (GOV=R, GPR=A, DEV=C, DPO=C) | Plano de adequação em 3 fases | Concluído |

**Total Sprint 4: 22 pontos · 16 pessoa-dia**

---

## 8. Sprint 5 — Publicação e Dashboard

| Item | Pontos | Pessoa-dia | Qualificação MRO | Critério de Aceite | Status |
| --- | ---: | ---: | --- | --- | --- |
| Gerar versões HTML de todos os documentos | 3 | 2 | Tático com validação (DEV=R, GPR=A, GOV=I) | HTML navegável com suporte Mermaid | Concluído |
| Gerar versões PDF de todos os documentos | 3 | 2 | Tático com validação (DEV=R, GPR=A, GOV=I) | PDF institucional legível | Concluído |
| Gerar README.md do projeto | 2 | 1 | Operacional com dependência (DEV=R, GPR=A) | Navegação e instruções de execução | Concluído |
| Gerar Conversa_Folha_Dashboard_Executivo.html | 3 | 2 | Tático com validação (DEV=R, GPR=A, GOV=C) | KPIs, barras de maturidade, tabelas de risco | Concluído |
| Adaptar generate_project_docs.py | 2 | 1 | Operacional com dependência (DEV=R, GPR=A) | Script funcional para MD → HTML → PDF | Concluído |

**Total Sprint 5: 13 pontos · 8 pessoa-dia**

---

## 9. Burndown Consolidado

| Sprint | Pontos | Pessoa-dia | Entregues | Status |
| --- | ---: | ---: | ---: | --- |
| Sprint 1 | 14 | 10,5 | 14 | ✅ 100% |
| Sprint 2 | 18 | 14 | 18 | ✅ 100% |
| Sprint 3 | 28 | 20 | 28 | ✅ 100% |
| Sprint 4 | 22 | 16 | 22 | ✅ 100% |
| Sprint 5 | 13 | 8 | 13 | ✅ 100% |
| **Total** | **95** | **68,5** | **95** | **✅ 100%** |

---

## 10. Observações

1. Todas as 5 sprints foram concluídas com sucesso.
2. O modelo de referência do projeto é Claude Opus 4.6 no ambiente figmm.
3. O código original na pasta `Conversa_Folha/` não foi alterado.
4. A documentação segue o template FACIN_IA e está disponível em .md, .html e .pdf.
5. Itens de evolução futura (mascaramento CPF, autenticação, LLM local) estão no backlog Kanban.
