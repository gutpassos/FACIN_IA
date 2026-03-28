# Conversa_Folha_doc - Integrações

Autor: Guttenberg Ferreira Passos  
Modelo LLM de referência: GPT-5.4  
Ambiente validado: figmm  
Data: 28 de março de 2026

## 1. Integrações do Sistema

| Integração | Tipo | Finalidade |
| --- | --- | --- |
| API da Groq | serviço externo | responder via agente Groq |
| API da OpenAI | serviço externo | responder via agente OpenAI |
| Banco SQLite local | dados | consultar folha de pagamento |
| Arquivo CSV folha_pe_200linhas.csv | dados | carga inicial do banco |
| Arquivo criacao_banco.sql | schema | criação das tabelas |

## 2. Contratos observados

1. o usuário interage por linguagem natural na interface Streamlit;
2. a ferramenta query_folha_database aceita apenas uma string SQL com SELECT;
3. o banco retorna linhas que são serializadas em texto tabular simples;
4. a aplicação depende de duas chaves de API para inicialização da interface.

## 3. Pontos de atenção

1. não há abstração institucional de identidade ou segredo;
2. não há API intermediária para controle adicional do acesso aos dados;
3. a divergência entre schema real e parte do prompt do agente OpenAI exige revisão documental permanente.
