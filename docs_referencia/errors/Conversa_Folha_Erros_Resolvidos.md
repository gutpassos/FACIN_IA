# Conversa_Folha_doc - Erros Encontrados e Resolvidos

Autor: Guttenberg Ferreira Passos  
Modelo LLM de referência do projeto: Claude Opus 4.6  
Ambiente validado: figmm  
Data: 29 de março de 2026

---

## 1. Finalidade

Registro de erros, lacunas e oportunidades de melhoria identificados durante a análise e documentação do projeto Conversa com a Folha, incluindo impacto e resolução ou recomendação adotada.

---

## 2. Erros Identificados

### ERR-001: Dados pessoais (CPF) armazenados em texto claro

| Aspecto | Descrição |
| --- | --- |
| Achado | O arquivo `folha_pe_200linhas.csv` e o banco SQLite `folha_pagamento.db` armazenam CPFs completos em texto claro (ex: 202.535.960-24) |
| Impacto | Risco de exposição de dados pessoais; não conformidade com princípio de minimização da LGPD |
| Resolução | Recomendado: implementar mascaramento de CPF na exibição e considerar hash ou pseudonimização no armazenamento |
| Status | Documentado — ação pendente |

### ERR-002: Envio de dados pessoais a APIs externas sem anonimização

| Aspecto | Descrição |
| --- | --- |
| Achado | Os resultados de consultas SQL contendo CPF, nome e remuneração são incluídos nas mensagens enviadas às APIs Groq e OpenAI como contexto para o agente formular a resposta |
| Impacto | Transferência internacional de dados pessoais sem garantias adequadas (Art. 33 LGPD) |
| Resolução | Recomendado: implementar camada de anonimização antes do envio ou migrar para LLM local |
| Status | Documentado — ação prioritária pendente |

### ERR-003: Ausência de autenticação na interface Streamlit

| Aspecto | Descrição |
| --- | --- |
| Achado | A interface web não possui mecanismo de autenticação. Qualquer pessoa com acesso à URL pode consultar os dados |
| Impacto | Acesso não autorizado aos dados de folha de pagamento |
| Resolução | Recomendado: implementar autenticação via Streamlit Authenticator ou similar |
| Status | Documentado — ação pendente |

### ERR-004: Ausência de testes automatizados

| Aspecto | Descrição |
| --- | --- |
| Achado | Não há módulos de teste (pytest ou similar) no repositório. Toda validação é feita manualmente |
| Impacto | Risco de regressão em alterações futuras; impossibilidade de CI/CD |
| Resolução | Recomendado: implementar suite de testes cobrindo ferramenta SQL, roteamento e fluxo do grafo |
| Status | Documentado — ação pendente |

### ERR-005: Referência a "CRM" no código (inconsistência de nomenclatura)

| Aspecto | Descrição |
| --- | --- |
| Achado | O código do `app.py` contém referências a "CRM" em comentários e prints do agente Groq (linhas `# Define a função do nó do agente Groq responsável por interagir com o CRM` e `print(f"Nó Groq (CRM) está chamando a ferramenta...")`) |
| Impacto | Inconsistência de documentação; código possivelmente adaptado de outro projeto sem revisão completa |
| Resolução | Observação documentada. O código original não foi alterado conforme diretriz do projeto |
| Status | Documentado — código original preservado |

### ERR-006: Logs via print() sem persistência

| Aspecto | Descrição |
| --- | --- |
| Achado | Todo o logging do sistema é feito via `print()`, sendo volátil e perdido ao encerrar a aplicação |
| Impacto | Impossibilidade de auditoria posterior; sem rastreabilidade persistente |
| Resolução | Recomendado: implementar módulo `logging` do Python com persistência em arquivo |
| Status | Documentado — ação pendente |

### ERR-007: Prompt do agente OpenAI referencia colunas inexistentes

| Aspecto | Descrição |
| --- | --- |
| Achado | O prompt do agente OpenAI menciona colunas que não existem no schema real: `cpf_mascarado`, `orgao_lotacao`, `status`, `ano_mes`, `remuneracao_basica_bruta`, `verbas_indenizatorias`, `total_descontos`, `salario_liquido` |
| Impacto | O agente OpenAI pode gerar SQL com colunas inexistentes, causando erros de execução |
| Resolução | Observação documentada. O código original não foi alterado conforme diretriz do projeto |
| Status | Documentado — código original preservado |

---

## 3. Registro de Resolução

| ERR | Data | Ação | Arquivo Afetado |
| --- | --- | --- | --- |
| ERR-001 | 29/03/2026 | Documentado na avaliação LGPD e risco RA-02 | Conversa_Folha_Avaliacao_Maturidade.md |
| ERR-002 | 29/03/2026 | Documentado como risco crítico RA-04 | Conversa_Folha_Avaliacao_Maturidade.md |
| ERR-003 | 29/03/2026 | Documentado no roadmap Fase 2 | Conversa_Folha_Avaliacao_Maturidade.md |
| ERR-004 | 29/03/2026 | Documentado no indicador DO2 e roadmap | Conversa_Folha_Avaliacao_Maturidade.md |
| ERR-005 | 29/03/2026 | Documentado — código original preservado | Nenhum (somente leitura) |
| ERR-006 | 29/03/2026 | Documentado no indicador DO3 e roadmap | Conversa_Folha_Avaliacao_Maturidade.md |
| ERR-007 | 29/03/2026 | Documentado — código original preservado | Nenhum (somente leitura) |

---

## 4. Observações

1. Todos os erros foram identificados durante a análise estática do código e a avaliação de maturidade FACIN_IA.
2. Os erros ERR-005 e ERR-007 são inconsistências no código original que foram preservadas conforme diretriz do projeto (somente leitura).
3. Nenhum arquivo do código original na pasta `Conversa_Folha/` foi alterado.
4. As resoluções pendentes estão vinculadas ao roadmap de melhoria na avaliação de maturidade.
