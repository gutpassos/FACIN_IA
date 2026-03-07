# FACIN_IA

Projeto de Indicadores de Maturidade de Governança Aplicada à Inteligência Artificial

Autor: Guttenberg Ferreira Passos
Modelo LLM utilizado: GPT-5.4
Ambiente de trabalho validado: figmm
Data: 7 de março de 2026

## 1. Identificação do Projeto

- Projeto: FACIN_IA
- Domínio: Governança de Inteligência Artificial aplicada a políticas públicas e desenvolvimento de software
- Responsável: Guttenberg Ferreira Passos
- Base metodológica: FACIN, Modelo de Responsabilidade Organizacional (MRO) e Spec-Driven Development (SDD)
- Princípio fundamental: a Inteligência Artificial executa especificações governadas; o código é artefato derivado; a especificação é o contrato primário

## 2. Especificação Funcional

O projeto FACIN_IA define um modelo de maturidade para avaliar a Governança Aplicada à Inteligência Artificial em organizações públicas e em ambientes de desenvolvimento de software intensivos em IA. O modelo adapta elementos do FACIN e do MRO para um contexto em que dados, modelos, prompts, decisões automatizadas e papéis humanos precisam ser coordenados por meio de regras explícitas, rastreabilidade e mecanismos permanentes de observabilidade.

O objetivo funcional é permitir que uma organização:

1. alinhe o uso de IA à estratégia institucional e à cadeia de valor pública;
2. estabeleça papéis, responsabilidades e fluxos de decisão claros para o ciclo de vida da IA;
3. trate prompt, modelo, dado, política e decisão como artefatos governados;
4. avalie maturidade de governança por indicadores mensuráveis e comparáveis ao longo do tempo;
5. priorize melhoria contínua com base em risco, impacto social e valor entregue.

## 3. Especificação Técnica

O FACIN_IA organiza a avaliação em seis dimensões obrigatórias das diretrizes do projeto:

1. Estratégia e Governança de IA
2. Dados e Infraestrutura
3. Talento e Cultura
4. Desenvolvimento e Operação de IA (DevOps/MLOps)
5. Ética, Transparência e Gestão de Risco
6. Impacto Social e Valor

Cada dimensão recebe indicadores de maturidade qualificados por:

1. natureza do indicador: estrutural, processo ou resultado;
2. tipo de sinal: leading ou lagging;
3. polaridade: maior é melhor ou menor é melhor;
4. fórmula de medição;
5. evidências mínimas exigidas;
6. periodicidade de apuração;
7. regra de leitura em cinco níveis de maturidade.

### 3.1 Regra Geral de Pontuacao

- Nivel 1 - Inicial: inexistente, ad hoc ou informal.
- Nivel 2 - Em Desenvolvimento: existe de forma parcial, piloto ou dependente de individuos.
- Nivel 3 - Otimizado: processo formalizado, repetivel e aplicado nas iniciativas principais.
- Nivel 4 - Consolidado: integrado a governanca institucional, monitorado por metricas e com responsabilizacao definida.
- Nivel 5 - Estabelecido: otimizado continuamente, auditavel, interoperavel e orientado a aprendizado institucional.

### 3.2 Metodo de Calculo da Maturidade

- Cada indicador recebe nota de 1 a 5.
- A nota da dimensao e a media simples de seus indicadores.
- O indice geral de maturidade e a media ponderada das dimensoes.

Pesos sugeridos:

- Estrategia e Governanca de IA: 20%
- Dados e Infraestrutura: 15%
- Talento e Cultura: 15%
- Desenvolvimento e Operacao de IA (DevOps/MLOps): 20%
- Etica, Transparencia e Gestao de Risco: 20%
- Impacto Social e Valor: 10%

Faixas sugeridas para o indice geral:

- 1,0 a 1,8: Nivel 1 - Inicial
- acima de 1,8 a 2,6: Nivel 2 - Em Desenvolvimento
- acima de 2,6 a 3,4: Nivel 3 - Otimizado
- acima de 3,4 a 4,2: Nivel 4 - Consolidado
- acima de 4,2 a 5,0: Nivel 5 - Estabelecido

## 4. Adaptacao das Dimensoes do FACIN e do MRO para IA

| Dimensao FACIN_IA | Base no FACIN | Base no MRO | Adaptacao para o contexto de IA | Resultado esperado |
| --- | --- | --- | --- | --- |
| Estrategia e Governanca de IA | Estrategia, Negocios, Programas e Projetos | Estrutura organizacional, cadeia de valor, responsabilidade por resultados | Vincula casos de uso de IA aos objetivos estrategicos, define comites, patrocinadores, regras de priorizacao, portfolio de IA e responsabilizacao por decisoes | IA tratada como capacidade estrategica e nao como experimento isolado |
| Dados e Infraestrutura | Dados, Infraestrutura, Seguranca | Conhecimento, qualificacao da demanda, suporte operacional | Governa fontes de dados, catalogos, linhagem, ambientes, observabilidade tecnica, seguranca da informacao e disponibilidade para treinamento e inferencia | Base confiavel, segura e rastreavel para operacao de IA |
| Talento e Cultura | Negocios, Sociedade, Programas e Projetos | Papel, equipe, habilidade, ator, experiencia | Define papeis organizacionais de IA, trilhas de capacitacao, separacao entre ideacao e producao, e responsabilidades humanas sobre supervisao e decisao | Cultura institucional apta a operar IA com responsabilidade |
| Desenvolvimento e Operacao de IA (DevOps/MLOps) | Aplicacoes, Infraestrutura, Programas e Projetos | Processos de trabalho, capacidade produtiva, qualificacao da demanda | Aplica SDD, versionamento de modelos e prompts, testes, validacoes, implantacao controlada, monitoramento, reversao controlada e gestao de incidentes | Ciclo de vida de IA previsivel, auditavel e observavel |
| Etica, Transparencia e Gestao de Risco | Seguranca, Dados, Sociedade | Responsabilidade, regras, conhecimento e papeis de controle | Introduz avaliacao de impacto algoritmico, conformidade legal, transparencia ativa, explicabilidade proporcional ao risco, mitigacao de vieses e supervisao humana | Risco reduzido e responsabilizacao demonstravel |
| Impacto Social e Valor | Sociedade, Estrategia, Negocios | Cadeia de valor, entrega de servicos, produtividade e resultado | Mede valor publico, inclusao, confianca, acessibilidade, melhoria do servico e retorno institucional da IA | Uso de IA legitimado por beneficio social e institucional mensuravel |

## 5. Indicadores Prioritarios de Maturidade

### 5.1 Estrategia e Governanca de IA

| Codigo | Indicador | Qualificacao | Formula de medicao | Evidencias minimas | Periodicidade | Regra de leitura |
| --- | --- | --- | --- | --- | --- | --- |
| EG1 | Cobertura de politica e estrategia de IA | Estrutural, leading, maior e melhor | (unidades ou processos com politica, objetivos e diretrizes de IA formalizados / total de unidades ou processos com uso de IA) x 100 | politica aprovada, mapa estrategico, normativos, plano de IA | semestral | N1: <20%; N2: 20-39%; N3: 40-69%; N4: 70-89%; N5: >=90% |
| EG2 | Governanca do portfolio de casos de uso de IA | Processo, antecipador, maior e melhor | (casos de uso com patrocinador, estudo de viabilidade, classificacao de risco e prioridade formal / total de casos de uso de IA) x 100 | portfolio de IA, atas de comite, criterios de priorizacao | trimestral | N1: <20%; N2: 20-39%; N3: 40-69%; N4: 70-89%; N5: >=90% |
| EG3 | Rastreabilidade de decisoes e artefatos de IA | Processo, antecipador, maior e melhor | (decisoes relevantes com registro de prompt, modelo, versao, dados, responsavel e justificativa / total de decisoes relevantes de IA) x 100 | repositorio de prompts, registro de modelos, registro decisorio, historico de mudancas | mensal | N1: <20%; N2: 20-39%; N3: 40-69%; N4: 70-89%; N5: >=90% |

### 5.2 Dados e Infraestrutura

| Codigo | Indicador | Qualificacao | Formula de medicao | Evidencias minimas | Periodicidade | Regra de leitura |
| --- | --- | --- | --- | --- | --- | --- |
| DI1 | Cobertura de catalogo e linhagem de dados e modelos | Estrutural, antecipador, maior e melhor | (conjuntos de dados, atributos, modelos e interfaces de servico catalogados com origem, base legal e linhagem / total de ativos de IA) x 100 | catalogo de dados, inventario de modelos, linhagem de dados, dicionario de dados | mensal | N1: <20%; N2: 20-39%; N3: 40-69%; N4: 70-89%; N5: >=90% |
| DI2 | Conformidade de protecao de dados e acessos | Processo, antecipador, maior e melhor | (ativos de IA com controle de acesso, retencao, criptografia e revisao de privilegios aderentes / total de ativos de IA) x 100 | matriz de acesso, registros de eventos, politica de retencao, controles tecnicos | mensal | N1: <30%; N2: 30-49%; N3: 50-74%; N4: 75-89%; N5: >=90% |
| DI3 | Disponibilidade da infraestrutura critica de IA | Resultado, retrospectivo, maior e melhor | (tempo disponivel da infraestrutura critica de IA / tempo total observado) x 100 | paineis, acordos de nivel de servico, registros de indisponibilidade, monitoramento | mensal | N1: <95,0%; N2: 95,0-96,9%; N3: 97,0-98,4%; N4: 98,5-99,4%; N5: >=99,5% |

### 5.3 Talento e Cultura

| Codigo | Indicador | Qualificacao | Formula de medicao | Evidencias minimas | Periodicidade | Regra de leitura |
| --- | --- | --- | --- | --- | --- | --- |
| TC1 | Cobertura de papeis criticos de IA formalmente atribuidos | Estrutural, antecipador, maior e melhor | (papeis criticos ocupados e formalizados: dono do caso de uso, gestor de dados, risco, operacao de ML, revisor humano / total de papeis criticos previstos) x 100 | matriz RACI, organograma, designacoes formais | trimestral | N1: <20%; N2: 20-39%; N3: 40-69%; N4: 70-89%; N5: >=90% |
| TC2 | Capacitacao aplicada em governanca e operacao de IA | Processo, leading, maior e melhor | media de horas anuais de capacitacao aplicada por colaborador-chave de IA | trilhas formativas, certificados, plano anual de capacitacao | semestral | N1: <4h; N2: 4-8h; N3: >8-16h; N4: >16-24h; N5: >24h |
| TC3 | Aderencia a segregacao entre ideacao e producao | Processo, antecipador, maior e melhor | (implantacoes de IA em producao revisadas/aprovadas por ator distinto do autor da ideacao principal / total de implantacoes em producao) x 100 | fluxo de aprovacao, esteira, atas, registros de mudanca | mensal | N1: <20%; N2: 20-39%; N3: 40-69%; N4: 70-89%; N5: >=90% |

### 5.4 Desenvolvimento e Operacao de IA (DevOps/MLOps)

| Codigo | Indicador | Qualificacao | Formula de medicao | Evidencias minimas | Periodicidade | Regra de leitura |
| --- | --- | --- | --- | --- | --- | --- |
| DO1 | Cobertura de especificacao antes de codigo ou ajuste de modelo | Processo, antecipador, maior e melhor | (iniciativas de IA com modelo padrao completo de especificacao antes de desenvolvimento / total de iniciativas iniciadas) x 100 | backlog, especificacoes aprovadas, repositorio de requisitos | mensal | N1: <20%; N2: 20-39%; N3: 40-69%; N4: 70-89%; N5: >=90% |
| DO2 | Cobertura de testes e validacoes de IA na esteira | Processo, antecipador, maior e melhor | (esteiras com testes funcionais, de seguranca, qualidade, vies, deriva e contingencia / total de esteiras de IA) x 100 | integracao e entrega continuas, relatórios de testes, evidencias de aprovacao | mensal | N1: <20%; N2: 20-39%; N3: 40-69%; N4: 70-89%; N5: >=90% |
| DO3 | Cobertura de observabilidade obrigatoria | Processo, antecipador, maior e melhor | (servicos de IA com registros de entrada e saida, prompts, modelos, alertas, trilha de auditoria e monitoramento ativo / total de servicos de IA) x 100 | paineis, rastros, registros, alertas, roteiros operacionais | mensal | N1: <20%; N2: 20-39%; N3: 40-69%; N4: 70-89%; N5: >=90% |
| DO4 | Tempo medio de resposta a incidentes de IA (MTTR) | Resultado, retrospectivo, menor e melhor | soma do tempo entre deteccao e mitigacao dos incidentes / total de incidentes no periodo | sistema de incidentes, analises pos-incidente, registros operacionais | mensal | N1: >168h; N2: 72-168h; N3: >24-72h; N4: >8-24h; N5: <=8h |

### 5.5 Etica, Transparencia e Gestao de Risco

| Codigo | Indicador | Qualificacao | Formula de medicao | Evidencias minimas | Periodicidade | Regra de leitura |
| --- | --- | --- | --- | --- | --- | --- |
| ER1 | Cobertura de avaliacao etica e de risco algoritmico | Processo, antecipador, maior e melhor | (casos de uso medio/alto risco com avaliacao de impacto, mitigacoes e aprovacao / total de casos medio/alto risco) x 100 | AIA, matriz de risco, pareceres, plano de mitigacao | trimestral | N1: <20%; N2: 20-39%; N3: 40-69%; N4: 70-89%; N5: >=90% |
| ER2 | Transparencia ao usuario e ao afetado pela IA | Resultado, antecipador, maior e melhor | (servicos com aviso de uso de IA, finalidade, canais de recurso e explicacao proporcional / total de servicos com IA voltados a usuarios) x 100 | telas, termos de uso, comunicados, manual do usuario | trimestral | N1: <20%; N2: 20-39%; N3: 40-69%; N4: 70-89%; N5: >=90% |
| ER3 | Conformidade etica e regulatoria apos auditoria | Resultado, retrospectivo, maior e melhor | (avaliacoes, auditorias ou revisoes sem nao conformidade critica / total de avaliacoes, auditorias ou revisoes) x 100 | auditorias, pareceres juridicos, planos de acao | semestral | N1: <50%; N2: 50-64%; N3: 65-79%; N4: 80-94%; N5: >=95% |

### 5.6 Impacto Social e Valor

| Codigo | Indicador | Qualificacao | Formula de medicao | Evidencias minimas | Periodicidade | Regra de leitura |
| --- | --- | --- | --- | --- | --- | --- |
| IV1 | Taxa de metas de valor atingidas por iniciativas de IA | Resultado, retrospectivo, maior e melhor | (iniciativas de IA que atingiram metas pactuadas de eficiencia, qualidade ou alcance / total de iniciativas avaliadas) x 100 | estudo de viabilidade, painel de beneficios, relatorios gerenciais | trimestral | N1: <20%; N2: 20-39%; N3: 40-69%; N4: 70-89%; N5: >=90% |
| IV2 | Cobertura de acessibilidade e inclusao nos servicos com IA | Resultado, antecipador, maior e melhor | (servicos com IA aderentes a requisitos de acessibilidade, linguagem clara e canais alternativos / total de servicos com IA) x 100 | testes de acessibilidade, jornadas de usuario, evidencias de inclusao | trimestral | N1: <20%; N2: 20-39%; N3: 40-69%; N4: 70-89%; N5: >=90% |
| IV3 | Confianca e satisfacao do usuario com servicos apoiados por IA | Resultado, retrospectivo, maior e melhor | media ponderada de satisfacao/confiança em escala de 1 a 5 | pesquisas, ouvidoria, analises de experiencia, entrevistas | trimestral | N1: <2,5; N2: 2,5-2,9; N3: 3,0-3,7; N4: >3,7-4,3; N5: >4,3 |

## 6. Qualificacao Sintetica dos Indicadores

Os indicadores foram qualificados segundo tres camadas complementares:

1. Estrutural: verificam se a organizacao criou as bases minimas de governanca, como politicas, papeis, catalogos e responsabilidades.
2. Processo: medem a disciplina operacional, a repetibilidade do ciclo de vida, a conformidade dos fluxos e a observabilidade obrigatoria.
3. Resultado: mostram se a governanca efetivamente reduz risco, sustenta confiabilidade e gera valor publico mensuravel.

Adicionalmente, o conjunto foi equilibrado entre indicadores antecipadores e retrospectivos:

1. Antecipadores: antecipam maturidade e capacidade de controle antes da materializacao dos riscos.
2. Retrospectivos: mostram o desempenho real ja observado, inclusive incidentes, conformidade e percepcao de valor.

Essa combinacao evita dois erros comuns:

1. medir apenas conformidade documental sem capturar efeito real;
2. medir apenas resultado final sem governar as causas estruturais e processuais.

## 7. Leitura Gerencial por Dimensao

- Estrategia e Governanca de IA: verifica se a IA e tratada como capacidade institucional, com prioridade, responsabilizacao e rastreabilidade.
- Dados e Infraestrutura: verifica se o ecossistema de dados e plataformas sustenta IA de forma segura, estavel e auditavel.
- Talento e Cultura: verifica se a responsabilidade humana esta distribuida por papeis, competencias e mecanismos de segregacao.
- Desenvolvimento e Operacao de IA (DevOps/MLOps): verifica se a organizacao respeita o principio de especificacao primaria e mantem operacao observavel.
- Etica, Transparencia e Gestao de Risco: verifica se a IA opera sob responsabilizacao, supervisao, proporcionalidade e mitigacao de dano.
- Impacto Social e Valor: verifica se a IA melhora servicos, preserva inclusao e gera legitimidade institucional.

## 8. Critérios de Aceitacao

O modelo sera considerado aderente as diretrizes do FACIN_IA quando:

1. utilizar explicitamente as seis dimensoes obrigatorias das diretrizes;
2. incorporar elementos do FACIN e do MRO ao contexto de IA;
3. tratar prompt, modelo, dado e decisao como artefatos governados;
4. prever registro de prompts, versionamento de modelos e rastreabilidade de decisoes;
5. incluir mecanismos de observabilidade obrigatoria;
6. permitir classificacao em cinco niveis de maturidade;
7. gerar leitura gerencial para governanca, conformidade e valor publico.

## 9. Testes Derivados

1. Verificar se cada indicador possui formula, evidencia, periodicidade e regra de leitura.
2. Verificar se todas as seis dimensoes possuem ao menos tres indicadores.
3. Verificar se os indicadores cobrem dimensoes estruturais, de processo e de resultado.
4. Verificar se o modelo contempla segregacao entre ideacao e producao.
5. Verificar se o modelo exige rastreabilidade de prompts e versionamento de modelos.
6. Verificar se o modelo contempla transparencia, risco e impacto social.
7. Verificar se o indice geral pode ser calculado de forma reprodutivel.

## 10. Restricoes de IA

1. IA nunca inicia pelo codigo.
2. Todo uso de IA deve partir de especificacao formal ou prompt contratual versionado.
3. Prompts, modelos, conjuntos de dados e decisoes devem ser rastreaveis.
4. Casos de medio e alto risco nao podem operar sem avaliacao etica e de risco.
5. Ambientes de ideacao e producao devem permanecer segregados.
6. Observabilidade e trilha de auditoria sao obrigatorias.
7. Instalacoes, quando necessarias, devem ocorrer somente no ambiente figmm.

## 11. Log de Interacoes com IA

- Solicitacao principal: adaptar FACIN e MRO ao contexto de Inteligencia Artificial e elaborar indicadores de maturidade de governanca.
- Referencias obrigatorias utilizadas: Diretrizes FACIN_IA.txt e Prompt FACIN_IA.txt.
- Referencias conceituais complementares consultadas: fontes abertas do FACIN e do MRO citadas nas diretrizes.
- Modelo utilizado nesta elaboracao: GPT-5.4.
- Ambiente validado para uso: figmm.
- Instalacoes realizadas: nenhuma.

## 12. Conclusao Executiva

O FACIN_IA proposto transforma o FACIN e o MRO em um modelo operacional de governanca de IA centrado em seis dimensoes integradas. A principal contribuicao da adaptacao e deslocar a governanca de uma logica apenas tecnologica para uma logica sociotecnica, em que estrategia, papeis, dados, risco, operacao, transparencia e valor publico sao avaliados conjuntamente.

Com isso, a organizacao passa a ter um instrumento objetivo para medir sua capacidade de governar a IA de forma previsivel, rastreavel, etica e orientada a resultados, em aderencia direta as diretrizes formais do projeto.