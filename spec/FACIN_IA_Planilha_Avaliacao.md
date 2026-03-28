# FACIN_IA - Planilha de Avaliação com Pontuação Automática

Autor: Guttenberg Ferreira Passos

## Objetivo

Este documento descreve a planilha de avaliação automática do FACIN_IA, disponibilizada em [docs/FACIN_IA_Avaliacao_Automatica.xlsx](../docs/FACIN_IA_Avaliacao_Automatica.xlsx).

## Estrutura da planilha

### Aba Instruções

Contém o escopo do instrumento, a regra de preenchimento e a leitura dos níveis de maturidade.

### Aba Parâmetros_Dimensões

Contém os pesos institucionais por dimensão:

| Dimensão | Peso |
| --- | --- |
| Estratégia e Governança de IA | 15 |
| Dados e Infraestrutura | 20 |
| Talento e Cultura | 10 |
| Desenvolvimento e Operação de IA (DevOps/MLOps) | 25 |
| Ética, Transparência e Gestão de Risco | 20 |
| Impacto Social e Valor | 10 |

### Aba Parâmetros_Indicadores

Lista os indicadores, pesos internos, tipo de polaridade e limiares para conversão automática do valor apurado em nota de 1 a 5.

### Aba Avaliação

O avaliador preenche:

1. valor apurado;
2. evidência principal;
3. observações.

A planilha calcula automaticamente:

1. nota do indicador;
2. nota ponderada por dimensão;
3. índice geral;
4. classificação final.

### Aba Resumo

Apresenta:

1. pontuação por dimensão;
2. índice geral ponderado;
3. classificação de maturidade;
4. situação da barreira institucional para os níveis 4 e 5.

## Fórmula de nota automática

### Indicadores em que maior valor significa melhor desempenho

$$
Nota =
\begin{cases}
1, & valor < t2 \\
2, & t2 \le valor < t3 \\
3, & t3 \le valor < t4 \\
4, & t4 \le valor < t5 \\
5, & valor \ge t5
\end{cases}
$$

### Indicadores em que menor valor significa melhor desempenho

$$
Nota =
\begin{cases}
5, & valor \le t5 \\
4, & t5 < valor \le t4 \\
3, & t4 < valor \le t3 \\
2, & t3 < valor \le t2 \\
1, & valor > t2
\end{cases}
$$

## Fórmula de pontuação por dimensão

$$
Pontuacao_{dim} = \frac{\sum (Nota_{indicador} \times Peso_{indicador})}{\sum Peso_{indicador}}
$$

## Fórmula do índice geral

$$
Índice\ Geral = \sum (Pontuacao_{dim} \times Peso_{dim})
$$

## Faixas de classificação automática

| Faixa | Classificação |
| --- | --- |
| 1,0 a 1,9 | Nível 1 - Inicial |
| acima de 1,9 a 2,7 | Nível 2 - Em Desenvolvimento |
| acima de 2,7 a 3,5 | Nível 3 - Otimizado |
| acima de 3,5 a 4,3 | Nível 4 - Consolidado |
| acima de 4,3 a 5,0 | Nível 5 - Estabelecido |

## Regra de barreira institucional

Para classificação automática da PRODEMGE:

1. se Dados e Infraestrutura, Desenvolvimento e Operação de IA ou Ética, Transparência e Gestão de Risco ficarem abaixo de 3,5, o resultado final não pode ser superior ao Nível 3;
2. se qualquer dimensão ficar abaixo de 4,0, o resultado final não pode ser Nível 5;
3. se qualquer indicador crítico ficar abaixo de 3,0, o resultado final não pode ser Nível 5.

## Uso recomendado

1. preencher a planilha por unidade, produto ou programa de IA;
2. consolidar os resultados trimestralmente;
3. usar o resumo para comitês de governança e priorização de melhoria;
4. associar cada nota a evidências verificáveis e não apenas declaratórias.