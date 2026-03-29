# Conversa_Folha_doc - Projeto Consolidado

Projeto de Documentação e Avaliação de Maturidade do Sistema Conversa com a Folha

Autor: Guttenberg Ferreira Passos  
Modelo LLM utilizado: Claude Opus 4.6  
Ambiente validado: figmm  
Data: 29 de março de 2026

---

## 1. Identificação do Projeto

- **Projeto**: Conversa_Folha_doc
- **Sistema avaliado**: Conversa com a Folha de Pagamento — V4
- **Domínio**: Engenharia de Software, Inteligência Artificial e Políticas Públicas
- **Responsável**: Guttenberg Ferreira Passos
- **Base metodológica**: FACIN, Modelo de Responsabilidade Organizacional (MRO), Spec-Driven Development (SDD) e arquitetura multiagente com LangGraph
- **Princípio fundamental**: A IA executa especificações governadas; o código original permanece preservado; a documentação é o contrato primário do projeto

---

## 2. Especificação Funcional

O sistema **Conversa com a Folha** implementa um sistema multiagente de inteligência artificial voltado à consulta e simulação sobre dados de folha de pagamento de servidores públicos. O sistema opera sobre um banco de dados SQLite com duas tabelas principais (`tb_servidores` e `tb_folha_pagamento`) e combina:

1. Interface web interativa via Streamlit
2. Dois agentes de IA concorrentes — Groq (Llama 3.1) e OpenAI (GPT-3.5-turbo)
3. Orquestração multiagente via LangGraph com grafo de estados
4. Ferramenta de consulta SQL segura (somente SELECT)
5. Roteamento inteligente entre agentes com alternância e menção explícita
6. Gerenciamento de memória e contexto de conversa via `st.session_state`
7. Carga de dados a partir de arquivo CSV (`folha_pe_200linhas.csv`)

O objetivo funcional desta documentação é produzir uma camada documental completa, capaz de:

1. Preservar integralmente os fontes originais da pasta `Conversa_Folha`
2. Registrar a arquitetura e o comportamento dos módulos Python existentes
3. Explicitar dependências, fluxos, riscos e pontos de integração com LLMs
4. Padronizar o projeto no template FACIN_IA
5. Disponibilizar artefatos em Markdown, HTML e PDF para uso institucional

---

## 3. Especificação Técnica

### 3.1 Estratégia de Documentação

A documentação foi implementada por composição documental nas pastas `docs/` e `erros/` do workspace, sem alteração do código original na pasta `Conversa_Folha/`.

- A pasta `Conversa_Folha/` foi mantida como fonte de análise (somente leitura)
- O template FACIN_IA serviu como referência metodológica
- As pastas `docs/` e `erros/` concentram a documentação gerada, avaliação e registro de erros

### 3.2 Componentes Documentados

| Módulo | Responsabilidade |
| --- | --- |
| Conversa_Folha/app.py | Interface Streamlit, orquestração multiagente LangGraph, ferramenta SQL, roteamento |
| Conversa_Folha/cria_db.py | Criação e carga do banco de dados SQLite a partir de CSV |
| Conversa_Folha/criacao_banco.sql | DDL de criação das tabelas `tb_servidores` e `tb_folha_pagamento` |
| Conversa_Folha/folha_pe_200linhas.csv | Base de dados de exemplo com 200 registros de folha de pagamento |
| Conversa_Folha/requirements.txt | Dependências Python do projeto |
| Conversa_Folha/README.md | Documentação básica do repositório |
| Conversa_Folha/LEIAME.txt | Instruções operacionais e exemplos de perguntas |

### 3.3 Padrão de Publicação

Os arquivos Markdown são convertidos para:

1. Markdown publicado (docs/)
2. HTML navegável (docs/)
3. PDF institucional (docs/)

### 3.4 Modelo de Dados

O sistema opera sobre um banco SQLite com duas tabelas:

| Tabela | Campos | Descrição |
| --- | --- | --- |
| tb_servidores | id, nome, cpf, matricula, orgao, cargo | Cadastro de servidores públicos |
| tb_folha_pagamento | id, matricula, competencia, vencimentos, descontos, liquido | Registros mensais de remuneração |

---

## 4. Critérios de Aceitação

O projeto será considerado aderente quando:

1. O repositório original `Conversa_Folha/` permanecer sem alteração de código
2. Existir documentação consolidada em Português do Brasil
3. A documentação estiver disponível em .md, .html e .pdf
4. Houver pasta `docs/` para publicação documental
5. Houver pasta `erros/` com erros encontrados e resolvidos
6. A avaliação de maturidade FACIN_IA estiver completa com MRO_RACI, LGPD e risco algorítmico
7. O projeto estiver nomeado como Conversa_Folha_doc
8. A autoria e o modelo Claude Opus 4.6 estiverem explicitados
9. O ambiente de trabalho figmm estiver registrado como ambiente oficial
10. Existirem documentos separados para Manual de Usuário, Arquitetura, Tecnologias, Integrações e Regras de Negócio

---

## 5. Testes Derivados

1. Verificar se os diretórios `docs/` e `erros/` existem na raiz do workspace
2. Verificar se há artefatos Markdown, HTML e PDF gerados
3. Verificar se a documentação cobre todos os módulos Python identificados
4. Verificar se nenhum arquivo Python original da pasta `Conversa_Folha/` foi editado
5. Verificar se a avaliação de maturidade segue os indicadores FACIN_IA com MRO_RACI
6. Verificar se a conformidade LGPD, Resolução ANPD 19/2024 e risco algorítmico estão documentados

---

## 6. Restrições de IA

1. IA não altera o código original da pasta `Conversa_Folha/`
2. Toda documentação deve ser produzida em Português do Brasil
3. O ambiente autorizado para execução e eventuais instalações é exclusivamente figmm
4. O modelo de referência declarado para o projeto é Claude Opus 4.6
5. A documentação deve privilegiar rastreabilidade, governança e reprodutibilidade

---

## 7. Log de Interações com IA

- Solicitação principal: documentar e avaliar maturidade do sistema Conversa com a Folha, aplicando template FACIN_IA com MRO_RACI, LGPD e risco algorítmico
- Código-fonte analisado: pasta `Conversa_Folha/` (somente leitura)
- Template aplicado: diretrizes e estrutura documental do FACIN_IA
- Ambiente utilizado: figmm
- Modelo LLM: Claude Opus 4.6
- Método de documentação: leitura estática dos fontes, análise estrutural e geração de artefatos

---

## 8. Conclusão Executiva

O projeto Conversa_Folha_doc estabelece uma camada de governança documental sobre o sistema Conversa com a Folha, convertendo uma aplicação de consulta multiagente a dados de folha de pagamento em um projeto documentado, rastreável e preparado para evolução institucional. O resultado não modifica o código legado, mas o torna inteligível, auditável e institucionalmente reutilizável, seguindo as diretrizes do template FACIN_IA.
