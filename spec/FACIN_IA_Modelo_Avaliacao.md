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
| Estratégia e Governança de IA | carteira de casos de uso, patrocínio executivo, comitê de IA, regras de decisão e rastreabilidade | alinhamento estratégico e accountability |
| Dados e Infraestrutura | catálogo, linhagem, segurança, disponibilidade e confiabilidade dos ambientes de IA | resiliência, confiabilidade e soberania informacional |
| Talento e Cultura | papéis formais, trilhas de capacitação, segregação entre ideação e produção, responsabilidade humana | responsabilização e prontidão institucional |
| Desenvolvimento e Operação de IA | SDD, testes, versionamento, observabilidade, resposta a incidentes e rollback | previsibilidade operacional |
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
Score_{dim} = \frac{\sum (Nota_{indicador} \times Peso_{indicador})}{\sum Peso_{indicador}}
$$

Índice geral:

$$
Índice\ Geral = \sum (Score_{dim} \times Peso_{dim})
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

## Indicadores críticos para a regra de barreira

- DI2 - Conformidade de proteção de dados e acessos
- DO2 - Cobertura de testes e validações de IA no pipeline
- DO3 - Cobertura de observabilidade obrigatória
- ER1 - Cobertura de avaliação ética e de risco algorítmico
- ER3 - Conformidade ética e regulatória após auditoria

## Leitura executiva

O ajuste para a PRODEMGE desloca a maturidade de IA para um padrão mais rigoroso do que o modelo genérico. O racional é simples: em uma organização pública de tecnologia, falhas de dados, indisponibilidade, baixa observabilidade ou risco ético não afetam apenas um produto, mas uma cadeia de serviços estatais e a confiança institucional.

Assim, o modelo mede maturidade não apenas pela existência de artefatos de governança, mas pela capacidade de operar IA de forma segura, sustentável, rastreável e útil ao setor público.