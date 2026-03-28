# Conversa_Folha_doc - Tecnologias

Autor: Guttenberg Ferreira Passos  
Modelo LLM de referência: GPT-5.4  
Ambiente validado: figmm  
Data: 28 de março de 2026

## 1. Stack do Sistema Atual

| Tecnologia | Papel |
| --- | --- |
| Python 3.12 | linguagem principal do projeto |
| Streamlit | interface conversacional web |
| LangGraph | orquestração do grafo de agentes |
| LangChain | abstrações de mensagens, prompts e tools |
| ChatGroq | integração com modelo Groq |
| ChatOpenAI | integração com modelo OpenAI |
| SQLite | persistência local de folha |
| pandas | carga do CSV para o banco |

## 2. Stack da Camada Documental

| Tecnologia | Papel |
| --- | --- |
| Python | automação documental |
| markdown | conversão de Markdown para HTML |
| reportlab | geração de PDF |
| AST da biblioteca padrão | análise estática dos módulos Python |

## 3. Diretrizes de uso

1. o ambiente oficial de execução é figmm;
2. o modelo de referência documental é GPT-5.4;
3. a presente iniciativa não pressupõe aderência a runtime corporativo específico;
4. a automação documental deve continuar simples, reproduzível e auditável.
