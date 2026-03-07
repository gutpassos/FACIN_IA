# FACIN_IA

Projeto de maturidade de Governança Aplicada à Inteligência Artificial, estruturado a partir do FACIN, do Modelo de Responsabilidade Organizacional (MRO) e das diretrizes de Spec-Driven Development (SDD).

Autor: Guttenberg Ferreira Passos
Modelo LLM utilizado: GPT-5.4
Ambiente validado: figmm

## Estrutura do repositório

- spec/: documentação-fonte em Markdown
- docs/: artefatos gerados em HTML, PDF e planilha XLSX
- scripts/: geradores dos artefatos
- errors/: registro dos erros encontrados durante a geração
- [Diretrizes FACIN_IA.txt](Diretrizes%20FACIN_IA.txt): diretrizes obrigatórias do projeto
- [Prompt FACIN_IA.txt](Prompt%20FACIN_IA.txt): prompt-base do trabalho
- [FACIN_IA_Projeto.md](FACIN_IA_Projeto.md): documento original consolidado

## Documentos principais

- [spec/FACIN_IA_Modelo_Avaliacao.md](spec/FACIN_IA_Modelo_Avaliacao.md): modelo de avaliação, pesos, fórmulas e faixas ajustadas
- [spec/FACIN_IA_Planilha_Avaliacao.md](spec/FACIN_IA_Planilha_Avaliacao.md): especificação da planilha com pontuação automática
- [spec/FACIN_IA_Versao_Executiva.md](spec/FACIN_IA_Versao_Executiva.md): versão executiva para apresentação institucional

## Premissa adotada

Para atender ao pedido de ajuste para um órgão público específico sem interromper o fluxo de trabalho, a parametrização foi feita para a PRODEMGE, considerando seu papel como empresa pública estadual de tecnologia, serviços digitais e sustentação de plataformas críticas de governo. Se necessário, os pesos e as faixas podem ser recalibrados para outro órgão com a mesma estrutura metodológica.

## Artefatos gerados

Os artefatos gerados ficam em docs/:

- HTML correspondente aos documentos de spec/
- PDF correspondente aos documentos de spec/
- planilha [docs/FACIN_IA_Avaliacao_Automatica.xlsx](docs/FACIN_IA_Avaliacao_Automatica.xlsx)

## Regra geral de maturidade

- Nível 1 - Inicial
- Nível 2 - Em Desenvolvimento
- Nível 3 - Otimizado
- Nível 4 - Consolidado
- Nível 5 - Estabelecido

## Observações de governança

- A IA executa especificações governadas.
- Prompt é contrato operacional.
- Prompt, modelo, dado e decisão são artefatos rastreáveis.
- Observabilidade e segregação entre ideação e produção são obrigatórias.
- Instalações devem ocorrer somente no ambiente figmm.