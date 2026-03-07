# FACIN_IA - Modelo de Avaliação de Maturidade

## Objetivo

Este documento consolida o modelo de avaliação de maturidade da Governança Aplicada à Inteligência Artificial para a PRODEMGE, com base nas diretrizes do FACIN_IA, no FACIN e no Modelo de Responsabilidade Organizacional (MRO).

## Contexto institucional adotado

A parametrização foi ajustada para uma empresa pública de tecnologia que:

1. opera serviços digitais críticos para o Estado;
2. sustenta ambientes, integrações, dados e plataformas corporativas;
3. precisa combinar continuidade operacional, conformidade, segurança e valor público.

Por esse motivo, o modelo atribui maior peso a Dados e Infraestrutura, Desenvolvimento e Operação de IA e Ética, Transparência e Gestão de Risco.

## Adaptação das dimensões do FACIN e do MRO para IA

| Dimensão FACIN_IA | Adaptação para IA no contexto da PRODEMGE | Ênfase de governança |
| --- | --- | --- |
| Estratégia e Governança de IA | carteira de casos de uso, patrocínio executivo, comitê de IA, regras de decisão e rastreabilidade | alinhamento estratégico e responsabilização |
| Dados e Infraestrutura | catálogo, linhagem, segurança, disponibilidade e confiabilidade dos ambientes de IA | resiliência, confiabilidade e soberania informacional |
| Talento e Cultura | papéis formais, trilhas de capacitação, segregação entre ideação e produção, responsabilidade humana | responsabilização e prontidão institucional |
| Desenvolvimento e Operação de IA | SDD, testes, versionamento, observabilidade, resposta a incidentes e reversão controlada | previsibilidade operacional |
| Ética, Transparência e Gestão de Risco | AIA, supervisão humana, transparência, mitigação de viés e conformidade | legitimidade, segurança jurídica e controle |
| Impacto Social e Valor | eficiência, acessibilidade, satisfação, confiança e entrega de valor público | resultado institucional e social |

## Pesos ajustados por dimensão

| Dimensão | Peso |
| --- | --- |
| Estratégia e Governança de IA | 15% |
| Dados e Infraestrutura | 20% |
| Talento e Cultura | 10% |
| Desenvolvimento e Operação de IA (DevOps/MLOps) | 25% |
| Ética, Transparência e Gestão de Risco | 20% |
| Impacto Social e Valor | 10% |

## Fórmula de pontuação ajustada

Pontuação da dimensão:

$$
Pontuacao_{dim} = \frac{\sum (Nota_{indicador} \times Peso_{indicador})}{\sum Peso_{indicador}}
$$

Índice geral:

$$
Índice\ Geral = \sum (Pontuacao_{dim} \times Peso_{dim})
$$

Regra de barreira institucional:

1. para atingir Nível 4, as dimensões Dados e Infraestrutura, Desenvolvimento e Operação de IA e Ética, Transparência e Gestão de Risco devem ter nota mínima 3,5;
2. para atingir Nível 5, todas as dimensões devem ter nota mínima 4,0 e nenhum indicador crítico pode ficar abaixo de 3,0.

## Faixas ajustadas de maturidade

| Faixa do índice geral | Nível |
| --- | --- |
| 1,0 a 1,9 | Nível 1 - Inicial |
| acima de 1,9 a 2,7 | Nível 2 - Em Desenvolvimento |
| acima de 2,7 a 3,5 | Nível 3 - Otimizado |
| acima de 3,5 a 4,3 | Nível 4 - Consolidado |
| acima de 4,3 a 5,0 | Nível 5 - Estabelecido |

## Matriz de indicadores e pesos internos

### Estratégia e Governança de IA

| Código | Peso | Entrada | Escala automática |
| --- | --- | --- | --- |
| EG1 | 30 | percentual | N1 < 30; N2 >= 30; N3 >= 50; N4 >= 75; N5 >= 90 |
| EG2 | 30 | percentual | N1 < 30; N2 >= 30; N3 >= 50; N4 >= 75; N5 >= 90 |
| EG3 | 40 | percentual | N1 < 30; N2 >= 30; N3 >= 50; N4 >= 75; N5 >= 90 |

### Dados e Infraestrutura

| Código | Peso | Entrada | Escala automática |
| --- | --- | --- | --- |
| DI1 | 35 | percentual | N1 < 35; N2 >= 35; N3 >= 55; N4 >= 75; N5 >= 90 |
| DI2 | 40 | percentual | N1 < 40; N2 >= 40; N3 >= 60; N4 >= 80; N5 >= 95 |
| DI3 | 25 | percentual | N1 < 97,0; N2 >= 97,0; N3 >= 98,0; N4 >= 99,0; N5 >= 99,7 |

### Talento e Cultura

| Código | Peso | Entrada | Escala automática |
| --- | --- | --- | --- |
| TC1 | 35 | percentual | N1 < 30; N2 >= 30; N3 >= 50; N4 >= 75; N5 >= 90 |
| TC2 | 25 | horas por colaborador-chave/ano | N1 < 6; N2 >= 6; N3 >= 12; N4 >= 20; N5 >= 32 |
| TC3 | 40 | percentual | N1 < 30; N2 >= 30; N3 >= 50; N4 >= 75; N5 >= 90 |

### Desenvolvimento e Operação de IA (DevOps/MLOps)

| Código | Peso | Entrada | Escala automática |
| --- | --- | --- | --- |
| DO1 | 25 | percentual | N1 < 35; N2 >= 35; N3 >= 55; N4 >= 80; N5 >= 95 |
| DO2 | 30 | percentual | N1 < 35; N2 >= 35; N3 >= 55; N4 >= 80; N5 >= 95 |
| DO3 | 25 | percentual | N1 < 35; N2 >= 35; N3 >= 55; N4 >= 80; N5 >= 95 |
| DO4 | 20 | horas | N1 > 72; N2 <= 72; N3 <= 36; N4 <= 12; N5 <= 4 |

### Ética, Transparência e Gestão de Risco

| Código | Peso | Entrada | Escala automática |
| --- | --- | --- | --- |
| ER1 | 40 | percentual | N1 < 35; N2 >= 35; N3 >= 60; N4 >= 80; N5 >= 95 |
| ER2 | 25 | percentual | N1 < 35; N2 >= 35; N3 >= 55; N4 >= 80; N5 >= 95 |
| ER3 | 35 | percentual | N1 < 60; N2 >= 60; N3 >= 75; N4 >= 90; N5 >= 98 |

### Impacto Social e Valor

| Código | Peso | Entrada | Escala automática |
| --- | --- | --- | --- |
| IV1 | 40 | percentual | N1 < 30; N2 >= 30; N3 >= 50; N4 >= 75; N5 >= 90 |
| IV2 | 25 | percentual | N1 < 35; N2 >= 35; N3 >= 55; N4 >= 80; N5 >= 95 |
| IV3 | 35 | escala de 1 a 5 | N1 < 2,8; N2 >= 2,8; N3 >= 3,4; N4 >= 4,0; N5 >= 4,5 |

## Interpretação de cada indicador

### Estratégia e Governança de IA

**EG1 - Cobertura de política e estratégia de IA**

Esse indicador mede o quanto o uso de IA já está formalmente reconhecido pela organização, com diretrizes, objetivos, prioridades e limites definidos. Na prática, ele mostra se a IA ainda depende de iniciativas isoladas ou se já existe orientação institucional clara para decidir onde usar, como usar e com quais critérios de controle. Quanto maior o percentual, menor a dependência de decisões casuísticas e maior a coerência entre iniciativas. Sob a ótica do MRO, ele evidencia se a responsabilidade organizacional sobre o uso da IA foi institucionalizada em diretrizes e instâncias formais de decisão. Na referência do FACIN, ele demonstra maturidade na formalização de diretrizes, critérios e instâncias de governança.

**EG2 - Governança do portfólio de casos de uso de IA**

Esse indicador mede a qualidade da gestão da carteira de iniciativas de IA. O foco não é apenas saber quantos casos existem, mas quantos deles possuem patrocinador, justificativa, classificação de risco e prioridade formal. A relevância dele está em evitar experimentação dispersa, projetos sem dono e iniciativas sem alinhamento estratégico. Um valor alto indica que a organização decide com método quais casos avançam, quais exigem mais controle e quais realmente geram valor institucional. No MRO, isso corresponde à existência de responsabilidade explícita sobre priorização, patrocínio e prestação de contas do portfólio. No FACIN, ele reflete capacidade de governar o portfólio com critérios objetivos e alinhamento institucional.

**EG3 - Rastreabilidade de decisões e artefatos de IA**

Esse indicador mede se decisões relevantes tomadas com apoio de IA podem ser reconstruídas posteriormente. Isso inclui saber qual prompt foi usado, qual modelo e versão estavam ativos, quais dados serviram de base, quem aprovou e qual foi a justificativa. É um dos indicadores mais importantes para auditoria, responsabilização e gestão de incidentes. Quanto maior a cobertura, maior a capacidade de investigar erros, revisar condutas e aprender institucionalmente. Na leitura do MRO, ele é o principal sinal de auditabilidade e reconstrução da cadeia de responsabilização. No FACIN, ele reforça a exigência de rastreabilidade como condição de governança efetiva.

### Dados e Infraestrutura

**DI1 - Cobertura de catálogo e linhagem de dados e modelos**

Esse indicador mede o grau de conhecimento formal sobre os ativos que sustentam a IA. Ele verifica se conjuntos de dados, atributos, modelos e interfaces de serviço estão identificados, catalogados e conectados à sua origem e ao seu uso. Sua relevância está em impedir a operação sobre ativos obscuros ou sem histórico confiável. Um resultado alto indica que a organização conhece o que usa, de onde veio, para que serve e quais dependências precisam ser controladas. Em termos de MRO, ele reforça a responsabilidade organizacional sobre a origem, o uso e as dependências dos ativos críticos de IA. No FACIN, ele expressa a necessidade de conhecer e estruturar os ativos informacionais que sustentam a governança.

**DI2 - Conformidade de proteção de dados e acessos**

Esse indicador mede se os ativos de IA operam com controles adequados de acesso, retenção, criptografia e revisão de privilégios. Ele é crítico porque protege a organização contra uso indevido de dados, exposição indevida de informações e violações regulatórias. No contexto da PRODEMGE, ele tem peso alto porque falhas nessa camada podem gerar impacto jurídico, operacional e reputacional relevante. Um valor alto mostra que a infraestrutura de IA não está apenas funcionando, mas funcionando sob controle. No MRO, ele expressa a obrigação de manter controles institucionais efetivos sobre dados, acessos e exposição a risco regulatório. No FACIN, ele corresponde à disciplina de controle e proteção dos ativos críticos sob governança.

**DI3 - Disponibilidade da infraestrutura crítica de IA**

Esse indicador mede a continuidade operacional dos ambientes e serviços que sustentam a IA. O interesse aqui não é conceitual, mas operacional: saber se a organização consegue manter a IA disponível com estabilidade compatível com serviços críticos. Sua relevância é direta para confiança institucional e qualidade do serviço. Quanto maior a disponibilidade, maior a resiliência técnica da operação. Sob a referência do MRO, ele demonstra capacidade organizacional de sustentar serviços de IA com confiabilidade compatível com responsabilidades institucionais permanentes. No FACIN, ele se relaciona à capacidade institucional de manter a operação estável e previsível.

### Talento e Cultura

**TC1 - Cobertura de papéis críticos de IA formalmente atribuídos**

Esse indicador mede se os papéis essenciais para governar IA foram explicitamente designados. Isso inclui, por exemplo, dono do caso de uso, gestor de dados, responsável por risco, operação e supervisão humana. A relevância dele está em transformar responsabilidade difusa em responsabilização verificável. A matriz RACI, o organograma e as designações formais servem como evidência justamente porque demonstram quem executa, quem responde, quem participa e quem deve ser informado. Um valor alto indica prontidão institucional, e não apenas disponibilidade técnica. No MRO, este é um dos indicadores mais diretos de responsabilização formal e atribuição inequívoca de deveres. No FACIN, ele traduz a exigência de clareza organizacional sobre funções e responsabilidades.

**TC2 - Capacitação aplicada em governança e operação de IA**

Esse indicador mede a intensidade da formação prática dos colaboradores-chave envolvidos com IA. O foco não é treinamento genérico, mas capacitação útil para governança, risco, operação, dados, segurança e supervisão. Sua relevância está em reduzir dependência de conhecimento tácito e aumentar a capacidade institucional de operar IA com consistência. Um resultado alto sinaliza que a organização está construindo competência, e não apenas usando ferramentas. Pela lógica do MRO, ele evidencia se a organização dotou seus agentes da capacidade necessária para responder adequadamente por decisões e controles relacionados à IA. No FACIN, ele expressa a maturidade de capacidades institucionais necessárias para sustentar a governança.

**TC3 - Aderência à segregação entre ideação e produção**

Esse indicador mede se quem concebe ou propõe a solução de IA é diferente de quem autoriza ou revisa sua entrada em produção. Ele existe para reduzir conflito de interesse, vieses de confirmação e decisões sem controle independente. É um indicador importante porque reforça uma das diretrizes operacionais do FACIN_IA: separar criação e liberação produtiva. Quanto maior o percentual, maior a maturidade de controle e revisão institucional. No enquadramento do MRO, ele comprova a existência de instâncias independentes de validação e accountability. No FACIN, ele representa a segregação de funções como mecanismo de governança e controle.

### Desenvolvimento e Operação de IA (DevOps/MLOps)

**DO1 - Cobertura de especificação antes de código ou ajuste de modelo**

Esse indicador mede o grau de adesão ao princípio central do FACIN_IA de que a IA deve executar especificações governadas. Ele verifica se a iniciativa começou com requisitos, restrições, critérios de aceitação e definição de uso, antes da implementação técnica. Sua relevância está em reduzir improviso, retrabalho e soluções tecnicamente sofisticadas, mas mal governadas. Um valor alto mostra disciplina de entrada e melhor previsibilidade ao longo do ciclo de vida. Em leitura MRO, ele mostra que a organização atua por critérios previamente definidos, e não por decisões ad hoc sem responsabilização ex ante. No FACIN, ele está diretamente ligado ao princípio de especificação prévia e disciplina de concepção.

**DO2 - Cobertura de testes e validações de IA no pipeline**

Esse indicador mede quantas esteiras de IA incorporam testes funcionais, de segurança, de qualidade, de viés, de deriva e de contingência. Ele é central porque traduz governança em mecanismo automático de prevenção. Não basta confiar em revisão manual ou boa intenção; é preciso ter barreiras técnicas no processo de entrega. Um valor alto indica que a organização incorporou controles repetíveis e auditáveis no fluxo de operação. No MRO, ele traduz responsabilidade organizacional em controles verificáveis e rotinas obrigatórias antes da liberação produtiva. No FACIN, ele mostra a incorporação de verificações estruturadas e repetíveis no ciclo de entrega.

**DO3 - Cobertura de observabilidade obrigatória**

Esse indicador mede se os serviços de IA registram e monitoram elementos essenciais da operação, como entradas, saídas, prompts, versões, alertas e trilhas de auditoria. Ele é decisivo para detectar desvios, investigar incidentes e entender comportamento em produção. Sua relevância aumenta em ambientes públicos e críticos, em que é necessário explicar decisões e recuperar contexto com rapidez. Quanto maior a cobertura, maior a capacidade de vigilância operacional e resposta informada. Sob o MRO, ele sustenta monitoramento contínuo, prestação de contas e capacidade de apuração posterior. No FACIN, ele reforça observabilidade e rastreamento como atributos indispensáveis da operação governada.

**DO4 - Tempo médio de resposta a incidentes de IA (MTTR)**

Esse indicador mede a velocidade com que a organização consegue detectar, tratar e mitigar incidentes relacionados à IA. Diferentemente dos anteriores, ele observa efeito real já ocorrido. Sua relevância está em mostrar se a operação consegue reagir com agilidade quando algo falha, deriva ou produz comportamento inadequado. Como a polaridade é inversa, menor tempo significa melhor maturidade. Um valor baixo demonstra prontidão operacional e capacidade de contenção. Na perspectiva do MRO, ele mostra se a organização responde com a diligência esperada quando a responsabilidade institucional já foi acionada por um evento adverso. No FACIN, ele reflete capacidade de resposta e controle operacional diante de desvios e falhas.

### Ética, Transparência e Gestão de Risco

**ER1 - Cobertura de avaliação ética e de risco algorítmico**

Esse indicador mede quantos casos de médio e alto risco passam por avaliação estruturada de impacto, mitigação e aprovação antes ou durante a operação. Ele é um dos principais controles de legitimidade do modelo, porque impede que soluções sensíveis avancem sem exame proporcional de risco. Sua relevância é alta em serviços públicos, onde vieses, opacidade ou automatização inadequada podem afetar direitos e acesso a serviços. Um resultado alto mostra prudência institucional antes do dano. No MRO, ele corresponde ao dever de avaliar previamente riscos e consequências antes de autorizar decisões organizacionais sensíveis. No FACIN, ele se alinha ao tratamento formal de riscos e à exigência de controles proporcionais.

**ER2 - Transparência ao usuário e ao afetado pela IA**

Esse indicador mede se os serviços informam de forma adequada que usam IA, para qual finalidade, quais limites existem e por quais canais o usuário pode buscar revisão ou recurso. Ele é importante porque governança de IA não termina dentro da organização; ela também precisa ser percebida por quem sofre seus efeitos. Quanto maior o percentual, maior a aderência a princípios de transparência, explicabilidade proporcional e respeito ao usuário. Pela referência do MRO, ele amplia a responsabilização para fora da organização, permitindo explicação, contestação e controle social do uso da IA. No FACIN, ele representa a transparência como requisito de legitimidade e governança.

**ER3 - Conformidade ética e regulatória após auditoria**

Esse indicador mede o resultado das avaliações, auditorias e revisões realizadas sobre as soluções de IA. Ele verifica a proporção de exames concluídos sem não conformidade crítica. Sua relevância está em mostrar se os controles anteriores realmente funcionam quando submetidos a verificação independente. Um valor alto indica robustez real; um valor baixo indica que a governança declarada não está se sustentando na prática. No MRO, ele é a expressão mais clara de verificação independente da responsabilidade organizacional efetivamente exercida. No FACIN, ele evidencia se a governança declarada resiste à validação formal e independente.

### Impacto Social e Valor

**IV1 - Taxa de metas de valor atingidas por iniciativas de IA**

Esse indicador mede quantas iniciativas realmente entregaram os benefícios pactuados, como eficiência, qualidade, alcance ou ganho institucional. Ele é importante porque impede que a maturidade seja confundida com sofisticação técnica ou volume de projetos. Em governança pública, IA precisa gerar valor verificável. Um resultado alto indica que a carteira de IA entrega resultado concreto, e não apenas atividade. Na chave do MRO, ele vincula responsabilidade organizacional a resultados efetivamente produzidos, e não apenas a conformidade procedimental. No FACIN, ele reforça que maturidade institucional deve se converter em entrega de valor observável.

**IV2 - Cobertura de acessibilidade e inclusão nos serviços com IA**

Esse indicador mede se os serviços apoiados por IA atendem requisitos de acessibilidade, linguagem clara e canais alternativos. Sua relevância está em conectar maturidade técnica a equidade de acesso. Em contexto público, não basta que a solução funcione para a maioria; ela precisa ser utilizável por públicos diversos e não ampliar exclusões existentes. Quanto maior o percentual, maior a aderência da IA ao dever de inclusão e universalidade do serviço. No MRO, ele mostra que a responsabilidade organizacional inclui garantir que o benefício do uso da IA seja distribuído sem ampliar barreiras ou exclusões. No FACIN, ele associa governança à obrigação de inclusão, acessibilidade e serviço universal.

**IV3 - Confiança e satisfação do usuário com serviços apoiados por IA**

Esse indicador mede a percepção do usuário sobre a qualidade e a confiabilidade dos serviços que usam IA. Ele complementa os demais ao trazer a dimensão externa da governança: como a solução é percebida por quem a utiliza ou é afetado por ela. Sua relevância está em verificar se a combinação entre técnica, controle, transparência e valor está de fato sendo reconhecida na experiência concreta. Uma nota alta indica aceitação, confiança e legitimidade operacional. Pela perspectiva do MRO, esse indicador sinaliza se a responsabilidade organizacional é percebida externamente como confiável, legítima e capaz de produzir segurança no uso da IA. No FACIN, ele evidencia se a governança produz confiança institucional percebida pelo usuário.

## Indicadores críticos para a regra de barreira

- DI2 - Conformidade de proteção de dados e acessos
- DO2 - Cobertura de testes e validações de IA no pipeline
- DO3 - Cobertura de observabilidade obrigatória
- ER1 - Cobertura de avaliação ética e de risco algorítmico
- ER3 - Conformidade ética e regulatória após auditoria

## Leitura executiva

O ajuste para a PRODEMGE desloca a maturidade de IA para um padrão mais rigoroso do que o modelo genérico. O racional é simples: em uma organização pública de tecnologia, falhas de dados, indisponibilidade, baixa observabilidade ou risco ético não afetam apenas um produto, mas uma cadeia de serviços estatais e a confiança institucional.

Assim, o modelo mede maturidade não apenas pela existência de artefatos de governança, mas pela capacidade de operar IA de forma segura, sustentável, rastreável e útil ao setor público.