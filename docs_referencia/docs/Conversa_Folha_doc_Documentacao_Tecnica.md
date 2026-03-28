# Documentação Técnica do Projeto Conversa_Folha_doc

Autor: Guttenberg Ferreira Passos  
Modelo LLM de referência: GPT-5.4  
Ambiente Conda homologado: figmm

## 1. Objetivo técnico

O projeto Conversa_Folha_doc consolida a solução Conversa_Folha com uma estrutura documental inspirada no repositório FACIN_IA, resultando em um pacote técnico e executivo orientado à operação responsável de inteligência artificial aplicada à consulta de dados de folha de pagamento.

O objetivo da solução é permitir que usuários autorizados formulem perguntas em linguagem natural e obtenham respostas estruturadas com apoio de agentes de IA, utilizando uma base relacional SQLite alimentada por dados tabulares previamente preparados.

Além da capacidade funcional, o projeto foi expandido para incorporar controles mínimos de governança, rastreabilidade, transparência, observabilidade, conformidade com a LGPD e mitigação de risco algorítmico, alinhando-se ao contexto de governança do MRO da PRODEMGE.

## 2. Escopo da solução

O escopo funcional contempla:

- interface conversacional em Streamlit;
- orquestração de agentes com LangGraph;
- uso de modelos via Groq e OpenAI;
- acesso a banco SQLite local com dados de folha;
- documentação executiva, técnica, de maturidade e de governança;
- geração automatizada de artefatos em Markdown, HTML e PDF;
- testes automatizados para componentes críticos;
- trilhas locais de auditoria e observabilidade.

Não faz parte do escopo atual:

- autenticação corporativa integrada;
- gestão centralizada de segredos;
- telemetria corporativa unificada;
- fluxo formal de aprovação institucional em ambiente produtivo;
- monitoramento contínuo por plataforma externa de observabilidade.

## 3. Arquitetura da aplicação

### 3.1 Visão geral

A aplicação é composta pelos seguintes blocos:

1. Interface Streamlit para captura da interação do usuário.
2. Grafo de execução LangGraph para roteamento entre agentes.
3. Agente Groq para interpretação inicial e apoio conversacional.
4. Agente OpenAI configurado com GPT-5.4 para respostas e composição analítica.
5. Camada de acesso ao banco SQLite com validação prévia de consultas.
6. Módulo de governança para auditoria, observabilidade e controle de risco.
7. Pipeline documental para geração de artefatos em múltiplos formatos.

### 3.2 Estrutura principal de arquivos

- app.py: aplicação principal em Streamlit.
- governance_controls.py: controles de acesso, auditoria, observabilidade e validação SQL.
- cria_db.py: criação e carga do banco SQLite.
- criacao_banco.sql: esquema do banco de dados.
- folha_pe_200linhas.csv: base tabular usada na carga inicial.
- scripts/generate_artifacts.py: gerador de documentação em Markdown, HTML e PDF.
- tests/: testes automatizados.
- spec/: documentação-fonte em Markdown.
- docs/: artefatos gerados.
- errors/: registros de problemas identificados e correções adotadas.

## 4. Fluxo de execução

O fluxo operacional da aplicação ocorre da seguinte forma:

1. O usuário informa nome, instituição e finalidade de uso.
2. O usuário aceita o termo de ciência sobre uso assistido por IA.
3. Opcionalmente, um código de acesso local pode ser exigido por variável de ambiente.
4. A sessão é registrada com identificador próprio.
5. As mensagens são encaminhadas ao fluxo orquestrado.
6. Quando necessário, consultas SQL são validadas antes da execução.
7. As respostas produzidas são registradas em trilha de auditoria.
8. As chamadas de modelo são registradas em trilha de observabilidade, com estimativas de custo, latência e volume textual.

## 5. Modelo de dados e acesso ao banco

O banco SQLite é criado a partir de [criacao_banco.sql](criacao_banco.sql) e populado por [cria_db.py](cria_db.py) com base no arquivo [folha_pe_200linhas.csv](folha_pe_200linhas.csv).

O projeto adota uma abordagem restritiva para consultas SQL:

- apenas instruções SELECT são permitidas;
- consultas com múltiplas instruções são bloqueadas;
- comentários SQL são bloqueados;
- palavras-chave destrutivas ou de modificação são proibidas;
- apenas tabelas homologadas podem ser acessadas.

Essa decisão reduz a superfície de risco associada à geração de consultas por modelos de linguagem.

## 6. Governança implementada no código

### 6.1 Controle de acesso e identificação

A aplicação passou a exigir identificação mínima do usuário para uso consciente da solução. São coletados:

- nome;
- instituição;
- finalidade declarada.

Também foi previsto suporte a código de acesso local por meio da variável de ambiente `CONVERSA_FOLHA_ACCESS_KEY`, útil para ambientes de demonstração controlada.

### 6.2 Transparência

A interface informa explicitamente que:

- a resposta é apoiada por inteligência artificial;
- as saídas devem ser validadas antes de uso decisório;
- o sistema opera sobre base de dados estruturada local;
- há registro de eventos para fins de rastreabilidade e governança.

### 6.3 Auditoria

O módulo [governance_controls.py](governance_controls.py) registra:

- eventos de acesso;
- perguntas enviadas;
- respostas produzidas;
- identificadores de sessão;
- carimbos de data e hora;
- contexto mínimo do evento.

Os registros são gravados localmente em logs estruturados no diretório `logs/`.

### 6.4 Observabilidade

Foi criada uma trilha específica para observabilidade de modelos, incluindo:

- nome do modelo utilizado;
- tipo de evento;
- duração estimada da chamada;
- tamanho de entrada e saída;
- estimativa de tokens;
- estimativa de custo;
- registro de falhas.

Embora não substitua uma plataforma corporativa de AIOps ou observabilidade centralizada, esse mecanismo eleva a solução a um patamar operacional mais controlado.

## 7. Conformidade com a LGPD

Do ponto de vista documental e técnico, a solução passou a explicitar medidas alinhadas à Lei Geral de Proteção de Dados Pessoais.

Elementos incorporados:

- identificação de finalidade de uso;
- minimização de dados de identificação coletados na interface;
- orientação de uso responsável e validação humana;
- rastreabilidade de eventos relevantes;
- delimitação do ambiente como contexto controlado e local;
- recomendação de evolução para controles institucionais de retenção, perfil de acesso e base legal em implantação produtiva.

O projeto não afirma conformidade institucional plena de produção. Em vez disso, documenta salvaguardas implementadas e lacunas remanescentes para futura institucionalização.

## 8. Risco algorítmico

O projeto reconhece explicitamente os seguintes riscos:

- geração de respostas incorretas ou imprecisas;
- interpretação inadequada de consultas em linguagem natural;
- simplificação excessiva de contextos administrativos;
- confiança indevida em resposta automatizada;
- uso além do escopo inicialmente previsto.

Medidas mitigadoras introduzidas:

- aviso de validação humana obrigatória;
- restrição do escopo de consulta ao banco homologado;
- trilhas de auditoria e observabilidade;
- documentação executiva e técnica com limites de uso;
- reforço do papel humano na decisão final.

## 9. Testes automatizados

Foram adicionados testes com pytest cobrindo componentes essenciais:

- validação e execução controlada de SQL;
- criação da base SQLite;
- geração de artefatos documentais.

Arquivos principais:

- [tests/test_governance_controls.py](tests/test_governance_controls.py)
- [tests/test_cria_db.py](tests/test_cria_db.py)
- [tests/test_generate_artifacts.py](tests/test_generate_artifacts.py)
- [tests/conftest.py](tests/conftest.py)

Esses testes não esgotam a validação da solução, mas corrigem a ausência anterior de verificação automatizada mínima.

## 10. Integração contínua

Foi criado o pipeline [ci.yml](.github/workflows/ci.yml) no GitHub Actions para:

- instalar dependências;
- validar a sintaxe dos arquivos Python;
- executar a suíte de testes automatizados.

Essa medida reduz risco de regressão e eleva a reprodutibilidade técnica do projeto.

## 11. Geração da documentação

O script [scripts/generate_artifacts.py](scripts/generate_artifacts.py) converte os arquivos-fonte de `spec/` em artefatos publicados no diretório `docs/` nos formatos:

- Markdown;
- HTML;
- PDF.

A geração de PDF utiliza ReportLab como alternativa estável ao uso de renderização HTML dependente de bibliotecas nativas mais complexas.

## 12. Limitações atuais

Apesar da evolução do projeto, ainda permanecem limitações relevantes:

- autenticação ainda não integrada a diretório corporativo;
- logs locais ainda não enviados a barramento central de observabilidade;
- ausência de gestão corporativa de ciclo de vida de prompts;
- ausência de catálogo formal de riscos com aceite institucional;
- ausência de segregação de ambientes com política de promoção formal;
- ausência de avaliação jurídica e de privacidade formalmente registrada.

Esses pontos impedem classificar a solução como plenamente institucionalizada em produção regulada, embora ela já se posicione em nível mais avançado de controle operacional.

## 13. Conclusão técnica

O Conversa_Folha_doc evoluiu de um protótipo conversacional com documentação básica para uma solução tecnicamente mais robusta, com testes, pipeline, trilhas de auditoria, observabilidade local, controles mínimos de acesso e documentação alinhada a governança pública.

Sob a ótica técnica, o projeto atende a um patamar de maturidade compatível com iniciativas otimizadas em ambiente controlado, mantendo clareza sobre suas limitações e sobre os passos necessários para futura adoção institucional ampliada.