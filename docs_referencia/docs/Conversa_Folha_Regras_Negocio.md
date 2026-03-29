# Conversa_Folha_doc - Regras de Negócio

Autor: Guttenberg Ferreira Passos  
Modelo LLM de referência do projeto: Claude Opus 4.6  
Ambiente validado: figmm  
Data: 29 de março de 2026

---

## 1. Finalidade

Este documento formaliza as regras de negócio implementadas no sistema Conversa com a Folha, abrangendo classificação de perguntas, roteamento de agentes, execução de consultas, segurança de dados, processamento de respostas e rastreabilidade.

---

## 2. Contexto de Negócio

### 2.1 Objetivo do Sistema

O Conversa com a Folha é uma ferramenta interativa de consulta e simulação sobre dados de folha de pagamento de servidores públicos. O sistema permite ao usuário realizar perguntas em linguagem natural que são traduzidas em consultas SQL e executadas sobre as tabelas `tb_servidores` e `tb_folha_pagamento`.

### 2.2 Premissas de Negócio

1. O sistema é um **assistente de consulta**, não um decisor autônomo.
2. Os dados disponíveis são de **exemplo** (200 registros), servindo como prova de conceito.
3. As respostas são baseadas exclusivamente nos dados do banco local.
4. Os agentes de IA devem gerar apenas consultas SQL SELECT.
5. O sistema opera com dois agentes concorrentes para diversidade de respostas.
6. As chaves de API são responsabilidade do usuário.

---

## 3. Regras de Roteamento de Agentes

### RN-01: Roteamento por Menção Explícita

Quando o usuário inclui menção explícita a um agente, o sistema direciona para o agente mencionado:

| Menção | Agente Direcionado | Modelo |
| --- | --- | --- |
| `@groq` | Groq Agent | llama-3.1-8b-instant |
| `@openai` | OpenAI Agent | gpt-3.5-turbo |

### RN-02: Roteamento por Alternância

Na ausência de menção explícita, o roteamento alterna entre os agentes com base na contagem de `AIMessage` no histórico:

| Contagem de AIMessages | Agente Selecionado |
| --- | --- |
| Par (0, 2, 4, ...) | Groq Agent |
| Ímpar (1, 3, 5, ...) | OpenAI Agent |

### RN-03: Roteamento para Ferramentas

Quando a última mensagem é uma `AIMessage` com `tool_calls`, o roteamento direciona automaticamente para o nó de ferramentas (`tools`).

### RN-04: Encerramento de Ciclo

Quando a última mensagem é uma `AIMessage` sem `tool_calls`, o ciclo é encerrado e a resposta é entregue ao usuário.

### RN-05: Ciclo de Retorno

Após a execução do agente ou da ferramenta, o fluxo retorna ao roteador para decisão do próximo passo, formando ciclos de consulta-resposta.

---

## 4. Regras de Consulta SQL

### RN-06: Restrição a SELECT

A ferramenta `query_folha_database` aceita **exclusivamente** consultas SQL que iniciam com a palavra `SELECT` (case-insensitive). Qualquer outra operação é rejeitada.

| Operação | Permitida | Comportamento |
| --- | --- | --- |
| SELECT | ✅ Sim | Execução normal |
| UPDATE | ❌ Não | Retorna erro de segurança |
| DELETE | ❌ Não | Retorna erro de segurança |
| INSERT | ❌ Não | Retorna erro de segurança |
| DROP | ❌ Não | Retorna erro de segurança |
| ALTER | ❌ Não | Retorna erro de segurança |

### RN-07: Tabelas Disponíveis

Os agentes devem consultar apenas as tabelas documentadas no schema da ferramenta:

| Tabela | Colunas Disponíveis |
| --- | --- |
| tb_servidores | id, nome, cpf, matricula, orgao, cargo |
| tb_folha_pagamento | id, matricula, competencia, vencimentos, descontos, liquido |

### RN-08: Relacionamento entre Tabelas

A relação entre as tabelas é feita pela coluna `matricula`:

```sql
SELECT ... FROM tb_servidores s 
JOIN tb_folha_pagamento f ON s.matricula = f.matricula
```

### RN-09: Limite de Resultados

A ferramenta retorna no máximo **15 resultados** por consulta. Se houver mais, indica a quantidade omitida:

```
... (mais X resultados omitidos)
```

### RN-10: Validação do Banco de Dados

Antes de executar qualquer consulta, a ferramenta verifica se o arquivo `folha_pagamento.db` existe. Caso não exista, retorna erro orientando a criação do banco.

---

## 5. Regras de Processamento de Dados

### RN-11: Carga Inicial de Dados

O script `cria_db.py` realiza a carga inicial seguindo a sequência:

1. Verifica existência do arquivo SQL (`criacao_banco.sql`)
2. Remove banco anterior se existir (criação limpa)
3. Executa o script SQL para criar tabelas
4. Lê o arquivo `folha_pe_200linhas.csv` via pandas
5. Insere dados de servidores (deduplica por campos únicos)
6. Insere dados de folha de pagamento
7. Gera arquivos auxiliares em Excel e CSV

### RN-12: Estrutura do CSV de Entrada

O arquivo `folha_pe_200linhas.csv` deve conter as colunas:

| Coluna | Tipo | Descrição |
| --- | --- | --- |
| nome | texto | Nome do servidor |
| cpf | texto | CPF formatado |
| matricula | texto | Matrícula funcional (ex: A-1000) |
| orgao | texto | Órgão de lotação |
| cargo | texto | Cargo ocupado |
| competencia | texto | Mês de referência (AAAAMM) |
| vencimentos | numérico | Valor bruto |
| descontos | numérico | Valor dos descontos |
| liquido | numérico | Valor líquido |

### RN-13: Órgãos do Sistema

| Órgão | Sigla Implícita |
| --- | --- |
| Secretaria da Saúde | Saúde |
| Secretaria da Fazenda | Fazenda |
| Secretaria da Educação | Educação |
| Secretaria de Administração | Administração |

### RN-14: Cargos do Sistema

| Cargo | Nível Implícito |
| --- | --- |
| Assistente | Nível inicial |
| Técnico | Nível intermediário |
| Analista | Nível superior |
| Gestor | Nível gerencial |

### RN-15: Competências Disponíveis

Os dados de exemplo cobrem as competências de 202401 a 202404 (janeiro a abril de 2024).

---

## 6. Regras de Segurança

### RN-16: Registro de Tentativas de SQL Não-SELECT

Toda tentativa de execução de SQL não-SELECT é registrada no console com a mensagem:
```
!!! ERRO DE SEGURANÇA: Tentativa de executar SQL não-SELECT !!!
```

### RN-17: Gerenciamento de Conexões

Toda conexão SQLite deve ser fechada no bloco `finally`, independentemente do resultado da execução. Isso previne vazamento de recursos.

### RN-18: Proteção de Chaves de API

- As chaves são informadas via widgets `type="password"` (ocultadas)
- As chaves são mantidas apenas em `st.session_state` (memória de sessão)
- As chaves não são persistidas em disco
- As chaves não devem ser publicadas no repositório

### RN-19: Validação de Chaves Obrigatórias

O sistema requer ambas as chaves (Groq e OpenAI) para prosseguir. Se qualquer uma estiver ausente, o fluxo é interrompido com `st.stop()`.

---

## 7. Regras de Interação com o Usuário

### RN-20: Mensagem de Boas-Vindas

Na primeira inicialização, o sistema exibe:
> "Olá! Sou seu assistente de Folha de Pagamento. Pergunte-me sobre servidores ou remunerações."

### RN-21: Histórico de Conversa

O histórico é mantido em `st.session_state.chat_history` como lista de `BaseMessage`. O histórico persiste durante a sessão.

### RN-22: Instruções do Prompt de Sistema

Cada agente recebe instruções específicas via prompt de sistema:

| Regra do Prompt | Descrição |
| --- | --- |
| Usar ferramenta SQL | Gerar consultas SELECT para responder perguntas |
| Consultar schema | Referenciar tabelas e colunas documentadas |
| Ser direto | Basear respostas nos dados retornados |
| Não inventar dados | Não gerar informações fictícias |
| Reportar erros | Informar ao usuário quando a ferramenta retornar erro |

---

## 8. Regras de Tratamento de Erros

### RN-23: Erros de API

Quando um agente falha na comunicação com a API (Groq ou OpenAI):

1. O erro é exibido via `st.error()`
2. Uma `AIMessage` de erro interno é criada
3. A mensagem de erro é incluída no estado para continuidade do fluxo

### RN-24: Erros de SQL

Quando a consulta SQL falha no SQLite:

1. O erro é registrado no console
2. Uma mensagem formatada é retornada ao agente
3. O agente pode reformular a consulta ou informar o usuário

### RN-25: Banco de Dados Ausente

Se o arquivo `folha_pagamento.db` não existir no momento da inicialização:

1. O sistema exibe `st.error()` com instrução
2. `st.info()` orienta a executar `cria_db.py`
3. O fluxo é interrompido com `st.stop()`

---

## 9. Regras de Negócio para Consultas

### RN-26: Consultas por Órgão

Os agentes devem respeitar os nomes exatos dos órgãos ao gerar SQL:

```sql
WHERE orgao = 'Secretaria da Saúde'    -- correto
WHERE orgao = 'Saude'                   -- incorreto
```

### RN-27: Consultas por Competência

O formato de competência no banco é `AAAAMM` (6 dígitos):

```sql
WHERE competencia = '202401'            -- janeiro de 2024
WHERE competencia LIKE '2024%'          -- ano de 2024
```

### RN-28: Cálculos de Folha

O valor líquido é definido como: `liquido = vencimentos - descontos`

Para totalizações de folha:
```sql
SELECT SUM(liquido) FROM tb_folha_pagamento WHERE ...
SELECT SUM(vencimentos) as total_bruto FROM tb_folha_pagamento WHERE ...
```

### RN-29: Simulações de Reajuste

Para simulações de reajuste percentual, os agentes devem calcular:
```sql
SELECT nome, vencimentos * 1.10 as vencimentos_reajustados FROM ...
```

---

## 10. Observações

1. As regras de negócio estão implementadas nos módulos `app.py` e `cria_db.py`.
2. A segurança SQL é a principal medida de proteção no nível de dados.
3. O sistema é uma prova de conceito e não deve ser utilizado com dados reais sem controles adicionais.
4. As regras de roteamento podem ser ajustadas sem alteração da arquitetura central.
