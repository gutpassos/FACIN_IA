# Conversa_Folha_doc - Avaliação de Maturidade

Autor: Guttenberg Ferreira Passos  
Modelo LLM de referência: GPT-5.4  
Ambiente validado: figmm  
Data: 28 de março de 2026

## 1. Objetivo

Avaliar a maturidade do sistema Conversa com a Folha e de sua camada de governança documental pelas seis dimensões do FACIN_IA, incorporando MRO_RACI, LGPD, Resolução CD/ANPD nº 19, de 23 de agosto de 2024, e risco algorítmico.

## 2. Escala Adotada

| Nível | Nome | Leitura |
| --- | --- | --- |
| 1 | Inicial | processo fortemente manual e pouco formalizado |
| 2 | Em Desenvolvimento | há estrutura mínima, porém com lacunas materiais |
| 3 | Definido | papéis, artefatos e rotinas já estão descritos |
| 4 | Gerenciado | métricas, controles e revisão recorrente já funcionam |
| 5 | Estabelecido | governança institucionalizada e melhoria contínua |

## 3. Resultado Consolidado

| Dimensão FACIN_IA | Nível atual | Nível alvo | Leitura resumida |
| --- | ---: | ---: | --- |
| Estratégia e Governança de IA | 2 | 4 | há intenção de governança, mas sem institucionalização formal do sistema |
| Dados e Infraestrutura | 2 | 4 | SQLite local e CSV atendem prototipação, não sustentação robusta |
| Talento e Cultura | 2 | 3 | conhecimento técnico existe, porém dependente de poucos atores |
| Desenvolvimento e Operação de IA | 2 | 4 | aplicação funciona, mas carece de observabilidade e controles operacionais |
| Ética, Transparência e Gestão de Risco | 2 | 4 | riscos são identificáveis, porém os controles ainda são parciais |
| Impacto Social e Valor | 3 | 4 | o caso de uso é claro e tem valor público potencial |

### 3.1 Nota-síntese

A maturidade geral atual é 2,2 de 5. O projeto já ultrapassou o estágio improvisado, mas ainda opera com baixa institucionalização de segurança, privacidade, observabilidade e responsabilização contínua.

## 4. Avaliação por Dimensão

### 4.1 Estratégia e Governança de IA

Evidências:

1. existe um caso de uso público claramente delimitado;
2. há documentação de referência e agora uma camada FACIN_IA dedicada;
3. o projeto já explicita autor, ambiente e modelo de referência.

Lacunas:

1. não há evidência de política institucional formal para uso do sistema;
2. não há comitê, rito decisório ou aprovação operacional formal anexados ao projeto.

### 4.2 Dados e Infraestrutura

Evidências:

1. schema do banco é simples e explícito;
2. a origem dos dados via CSV está identificada;
3. a aplicação restringe a ferramenta a consultas SELECT.

Lacunas:

1. o banco é local e não há trilha de governança de dados em produção;
2. não há classificação formal de dados, retenção ou mascaramento implementados.

### 4.3 Talento e Cultura

Evidências:

1. o projeto demonstra domínio de Streamlit, LangGraph, SQLite e LLMs;
2. a iniciativa agora possui artefatos de transferência de conhecimento.

Lacunas:

1. a operação parece dependente de configuração manual;
2. não há trilha formal de treinamento, homologação de usuários ou sustentação distribuída.

### 4.4 Desenvolvimento e Operação de IA

Evidências:

1. o fluxo multiagente está descrito e operacionalizado no código;
2. a documentação do código e do uso foi publicada.

Lacunas:

1. não há telemetria, readiness formal ou testes operacionais registrados;
2. não há separação robusta entre configuração, credenciais e execução.

### 4.5 Ética, Transparência e Gestão de Risco

Evidências:

1. o sistema informa dependência de dados e limita consultas a SELECT;
2. o pacote documental agora registra risco algorítmico e conformidade.

Lacunas:

1. o prompt do agente OpenAI descreve colunas divergentes do schema real;
2. não há processo institucional de revisão de respostas, logs e incidentes.

### 4.6 Impacto Social e Valor

Evidências:

1. o problema de negócio é objetivo e relevante para gestão pública;
2. a solução pode acelerar consultas e explicações sobre folha.

Lacunas:

1. o valor ainda depende de validação funcional e controle de riscos;
2. não há indicadores de adoção, qualidade ou confiança publicados.

## 5. Matriz MRO_RACI

| Frente | PAT | GP | ARQ | DOC | DADOS | PRIV | NEG | OPS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Escopo e prioridade do sistema | A | R | C | I | I | C | C | I |
| Governança documental FACIN_IA | I | C | A | R | I | C | I | C |
| Dados, schema e rastreabilidade | I | C | C | C | A | C | C | I |
| Privacidade, LGPD e resolução ANPD | I | C | C | I | C | A | C | I |
| Regras de negócio e validação funcional | I | C | C | C | C | I | A | I |
| Publicação dos artefatos | I | A | C | R | I | I | I | C |
| Revisão de riscos e manutenção | I | A | C | R | C | C | C | C |

Legenda:

1. R: executa;
2. A: responde pelo resultado final;
3. C: consultado;
4. I: informado.

## 6. Conformidade LGPD e Resolução CD/ANPD nº 19/2024

### 6.1 Leitura normativa

Como a solução trata dados de folha de pagamento e dados pessoais de servidores, sua avaliação documental deve ser lida à luz da LGPD e da RESOLUÇÃO CD/ANPD Nº 19, DE 23 DE AGOSTO DE 2024, com especial atenção para finalidade, minimização, transparência proporcional, responsabilização e gestão de riscos em sistemas apoiados por IA.

### 6.2 Estado atual

| Tema | Situação atual | Leitura |
| --- | --- | --- |
| Finalidade e contexto de uso | parcialmente atendido | o propósito do sistema é claro, mas sem ato formal anexado |
| Minimização de dados | parcialmente atendido | há limitação de consulta, porém o schema inclui CPF em texto claro |
| Controle de acesso | parcialmente atendido | a aplicação depende de execução local e não evidencia perfis institucionais |
| Transparência | parcialmente atendido | existe documentação, mas sem trilha operacional de resposta e revisão |
| Retenção e descarte | não evidenciado | ausência de política explícita |
| Tratamento de incidentes | não evidenciado | não há runbook de incidente ou privacidade |
| Revisão humana e contestabilidade | parcialmente atendido | recomenda-se validação humana, mas sem processo formal publicado |

### 6.3 Ações necessárias

1. formalizar finalidade, base legal e perfis de uso do sistema;
2. revisar a necessidade de retorno e exposição de identificadores pessoais;
3. definir trilha de logs, retenção, descarte e resposta a incidentes;
4. documentar processo de contestação e revisão humana para respostas críticas;
5. alinhar futuras evoluções técnicas com avaliação de impacto e privacidade proporcional.

## 7. Risco Algorítmico

| Risco | Probabilidade | Impacto | Leitura |
| --- | --- | --- | --- |
| Resposta incorreta baseada em prompt divergente do schema | Média | Alto | pode gerar interpretação errada da folha |
| Alucinação de informação não presente no banco | Média | Alto | risco elevado em ambiente público |
| Exposição indevida de dados pessoais | Média | Alto | afeta privacidade e conformidade |
| Dependência de usuário em resposta sem revisão | Média | Médio | pode induzir decisões precipitadas |
| Baixa explicabilidade operacional | Média | Médio | reduz auditabilidade e contestação |

Classificação atual do risco algorítmico: Médio-Alto.

Medidas mitigatórias recomendadas:

1. reforçar revisão humana em consultas críticas;
2. alinhar prompts e documentação ao schema real;
3. registrar logs de entrada, consulta e resposta quando houver operação institucional;
4. reduzir exposição de atributos pessoais desnecessários;
5. explicitar limites de confiança e uso em todos os canais de acesso.

## 8. Roadmap de Elevação de Maturidade

| Prioridade | Ação | Efeito esperado |
| --- | --- | --- |
| Imediata | manter documentação sincronizada com o código e o schema | evita divergência informacional |
| Alta | formalizar perfis de acesso, logs e retenção | eleva conformidade e responsabilidade |
| Alta | alinhar prompts, regras e testes ao schema real | reduz risco algorítmico |
| Média | criar rotina periódica de revisão FACIN_IA | melhora governança contínua |
| Média | definir indicadores de uso e qualidade | fortalece valor público mensurável |
