# Conversa_Folha_doc - Regras de Negócio

Autor: Guttenberg Ferreira Passos  
Modelo LLM de referência: GPT-5.4  
Ambiente validado: figmm  
Data: 28 de março de 2026

## 1. Regras centrais da solução

1. a aplicação responde perguntas sobre servidores e remunerações com base em dados persistidos no SQLite;
2. a consulta ao banco deve ocorrer apenas via SELECT;
3. a resposta não deve inventar informações ausentes no banco;
4. o sistema alterna agentes ou respeita menções explícitas a @groq e @openai.

## 2. Regras de acesso e inicialização

1. a interface exige Groq API Key e OpenAI API Key antes de continuar;
2. a aplicação só inicia se o arquivo folha_pagamento.db existir;
3. o banco deve ser gerado previamente por cria_db.py no mesmo diretório.

## 3. Regras de resposta

1. respostas finais devem refletir os dados retornados pela ferramenta;
2. quando a ferramenta falhar, a resposta deve informar erro controlado;
3. o histórico da conversa é mantido na sessão Streamlit;
4. resultados extensos são truncados a quinze linhas na ferramenta de banco.

## 4. Regras de segurança e conformidade

1. tentativas de SQL não SELECT devem ser rejeitadas;
2. dados de folha e CPF exigem cautela de privacidade;
3. respostas críticas não devem substituir validação humana;
4. o uso institucional deve observar LGPD e políticas aplicáveis.
