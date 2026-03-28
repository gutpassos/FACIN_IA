# Conversa_Folha_doc - Manual de Usuário

Autor: Guttenberg Ferreira Passos  
Modelo LLM de referência: GPT-5.4  
Ambiente validado: figmm  
Data: 28 de março de 2026

## 1. Objetivo

Orientar o uso do sistema Conversa com a Folha em seu formato atual, baseado em Streamlit e banco SQLite local.

## 2. Público-alvo

1. usuários internos autorizados a consultar informações de folha;
2. equipes técnicas que homologam a solução;
3. gestores que analisam respostas geradas pelo sistema.

## 3. Pré-requisitos

1. ambiente Python configurado;
2. banco folha_pagamento.db gerado previamente por cria_db.py;
3. chaves da Groq e da OpenAI informadas na barra lateral da aplicação;
4. acesso local aos arquivos do projeto.

## 4. Passo a passo de uso

1. iniciar a aplicação Streamlit da pasta Conversa_Folha;
2. informar Groq API Key e OpenAI API Key na barra lateral;
3. aguardar a inicialização do grafo de agentes;
4. enviar pergunta em linguagem natural sobre folha de pagamento;
5. analisar a resposta e validar casos críticos com a área responsável.

## 5. Exemplos de perguntas

1. Quantos servidores existem cadastrados?
2. Qual é a remuneração líquida do Servidor 3?
3. Qual é o valor da folha da Secretaria da Saúde em determinada competência?
4. Quantos servidores ocupam o cargo de Assistente?

## 6. Limites de uso

1. a aplicação não deve ser tratada como decisão administrativa final;
2. a ferramenta de dados aceita somente consultas SELECT;
3. resultados críticos devem ser confirmados por validação humana;
4. o sistema não deve ser usado para obter dados além do perfil autorizado.

## 7. Mensagens de exceção esperadas

1. alerta de ausência das chaves de API;
2. erro quando o banco folha_pagamento.db não existir;
3. erro controlado quando uma consulta SQL inválida for gerada;
4. mensagem de indisponibilidade do backend de modelo quando houver falha externa.

## 8. Privacidade e segurança

1. respostas podem conter dados pessoais e devem ser tratadas com cautela;
2. chaves de API não devem ser compartilhadas;
3. o uso deve respeitar LGPD e regras institucionais aplicáveis;
4. consultas e respostas críticas devem ser auditáveis quando o sistema for institucionalizado.
