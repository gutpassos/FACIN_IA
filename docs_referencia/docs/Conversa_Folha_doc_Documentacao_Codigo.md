# Conversa_Folha_doc - Documentação do Código

Autor: Guttenberg Ferreira Passos  
Modelo LLM de referência: GPT-5.4  
Ambiente validado: figmm  
Data: 28 de março de 2026

## 1. Escopo

Esta documentação cobre exclusivamente os fontes consultivos da pasta Conversa_Folha e o schema SQL associado, sem alteração do legado.

## 2. Inventário dos módulos Python

| Módulo | Linhas | Classes | Funções | Propósito |
| --- | ---: | ---: | ---: | --- |
| Conversa_Folha/app.py | 779 | 1 | 7 | Aplicação Streamlit que orquestra LangGraph, Groq e OpenAI para responder perguntas sobre folha de pagamento com consultas SQL somente leitura. |
| Conversa_Folha/cria_db.py | 142 | 0 | 3 | Script de preparação do banco SQLite que aplica o schema SQL, carrega a base CSV e exporta arquivos auxiliares. |

## 3. Módulos documentados

### 3.1 Conversa_Folha/app.py

- Propósito: Aplicação Streamlit que orquestra LangGraph, Groq e OpenAI para responder perguntas sobre folha de pagamento com consultas SQL somente leitura.
- Linhas analisadas: 779
- Quantidade de imports: 13
- Quantidade de constantes globais: 1
- Quantidade de classes: 1
- Quantidade de funções: 7

#### Imports

- from dotenv import load_dotenv
- from langchain.tools import tool
- from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage
- from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
- from langchain_groq import ChatGroq
- from langchain_openai import ChatOpenAI
- from langgraph.graph import StateGraph, END, START
- from langgraph.prebuilt import ToolNode
- from typing import Annotated, List, TypedDict
- operator
- os
- sqlite3
- streamlit

#### Constantes Globais

- DB_FILE

#### Classes

| Classe | Linha | Descrição |
| --- | ---: | --- |
| AgentState | 77 | Descrição inferida a partir da estrutura do código |

#### Funções

| Função | Assinatura | Retorno | Linha | Descrição |
| --- | --- | --- | ---: | --- |
| query_folha_database | (sql_query: str) | str | 85 | Executa uma consulta SQL SOMENTE do tipo SELECT no banco de dados Folha de Folha de Pagamento SQLite |
| cria_agente_runnable | (llm, system_prompt) | não informado | 197 | Descrição inferida a partir da estrutura do código |
| groq_agent_node | (state: AgentState) | não informado | 217 | Descrição inferida a partir da estrutura do código |
| openai_agent_node | (state: AgentState) | não informado | 272 | Descrição inferida a partir da estrutura do código |
| route_junction_node | (state: AgentState) | dict | 331 | Descrição inferida a partir da estrutura do código |
| router_logic | (state: AgentState) | str | 336 | Descrição inferida a partir da estrutura do código |
| compila_grafo | () | não informado | 402 | Descrição inferida a partir da estrutura do código |

### 3.2 Conversa_Folha/cria_db.py

- Propósito: Script de preparação do banco SQLite que aplica o schema SQL, carrega a base CSV e exporta arquivos auxiliares.
- Linhas analisadas: 142
- Quantidade de imports: 4
- Quantidade de constantes globais: 2
- Quantidade de classes: 0
- Quantidade de funções: 3

#### Imports

- from datetime import datetime, timedelta
- os
- pandas
- sqlite3

#### Constantes Globais

- DB_FILE
- SQL_FILE

#### Classes

- O módulo não declara classes no nível superior.

#### Funções

| Função | Assinatura | Retorno | Linha | Descrição |
| --- | --- | --- | ---: | --- |
| cria_database | () | não informado | 15 | Descrição inferida a partir da estrutura do código |
| popula_tabelas | (conn, cursor) | não informado | 81 | Descrição inferida a partir da estrutura do código |
| main | () | não informado | 114 | Descrição inferida a partir da estrutura do código |

## 4. Schema SQL associado

| Tabela | Colunas |
| --- | --- |
| tb_servidores | id INTEGER PRIMARY KEY AUTOINCREMENT; nome TEXT; cpf TEXT; matricula TEXT UNIQUE; orgao TEXT; cargo TEXT |
| tb_folha_pagamento | id INTEGER PRIMARY KEY AUTOINCREMENT; matricula TEXT; competencia TEXT; vencimentos REAL; descontos REAL; liquido REAL |

## 5. Fluxos relevantes

1. cria_db.py recria o banco, aplica o schema SQL e carrega o CSV;
2. app.py inicializa a interface, compila o grafo e roteia mensagens entre agentes;
3. query_folha_database protege a camada de dados ao permitir somente SELECT.
