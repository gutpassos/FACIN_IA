# FACIN_IA

Modelo de maturidade para Governança Aplicada à Inteligência Artificial em organizações públicas e ambientes de desenvolvimento intensivos em IA.

O projeto adapta o Framework de Arquitetura Corporativa para Interoperabilidade no apoio à Governança (FACIN), Modelo de Responsabilidade Organizacional (MRO) e Spec-Driven Development (SDD) para avaliar como estratégia, dados, operação, risco, transparência e valor público são governados ao longo do ciclo de vida da IA.

Autor: Guttenberg Ferreira Passos  
Modelo LLM utilizado: GPT-5.4  
Ambiente validado: figmm

## Uso como agente

Este repositório agora inclui uma customização reutilizável do GitHub Copilot para uso do método FACIN_IA em outros projetos.

Estrutura adicionada:

- `.github/agents/FACIN_IA.agent.md`: agente especializado em governança de IA.
- `.github/skills/facin-ia/SKILL.md`: skill portátil com a metodologia FACIN_IA.
- `.github/prompts/facin-ia-diagnostico.prompt.md`: prompt reutilizável para diagnóstico baseado em evidências.
- `plugins/facin-ia/`: pacote do plugin de agente FACIN_IA para distribuição entre equipes.
- `.github/plugin/marketplace.json`: marketplace do repositório para distribuição do plugin.
- `.github/skills/facin-ia/template-especificacao.md`: template oficial de especificação.
- `.github/skills/facin-ia/metodo-facin-ia.md`: resumo operacional do método.
- `.github/skills/facin-ia/checklist-avaliacao.md`: checklist de avaliação e aderência.

Para reutilizar em outro projeto:

1. Copie a pasta `.github/agents/` e a pasta `.github/skills/facin-ia/` para o repositório de destino.
2. Abra o repositório no VS Code com GitHub Copilot habilitado.
3. Selecione o agente `FACIN_IA` na lista de agentes do chat.
4. Opcionalmente, invoque a skill `/facin-ia` para carregar diretamente o método.
5. Para diagnósticos padronizados, invoque o prompt `/facin-ia-diagnostico` e informe o contexto e as evidências.

Para distribuição como plugin de agente:

1. Use o pacote em `plugins/facin-ia/` como plugin local via `chat.pluginLocations`.
2. Ou registre este repositório como marketplace via `.github/plugin/marketplace.json` usando `chat.plugins.marketplaces`.
3. Depois instale e habilite o plugin `facin-ia` no VS Code.

O agente foi desenhado para apoiar diagnóstico de maturidade, desenho de governança, especificação antes de código, definição de indicadores e adaptação metodológica para outros contextos institucionais.

## O que este repositório entrega

- um modelo de avaliação de maturidade em seis dimensões de governança de IA;
- uma versão executiva para apresentação institucional;
- uma síntese institucional do trabalho e de seus fundamentos conceituais;
- uma especificação de planilha com cálculo automático de pontuação;
- artefatos prontos em Markdown, HTML, PDF e XLSX para consulta e uso direto.

## Leitura recomendada

1. [docs/FACIN_IA_Versao_Executiva.md](docs/FACIN_IA_Versao_Executiva.md): visão rápida para apresentação e alinhamento institucional em Markdown.
2. [docs/FACIN_IA_Sintese.md](docs/FACIN_IA_Sintese.md): síntese do trabalho, dos conceitos-base e da aplicação prática com IA assistida.
3. [docs/FACIN_IA_Modelo_Avaliacao.md](docs/FACIN_IA_Modelo_Avaliacao.md): modelo completo de avaliação, pesos, fórmulas e faixas de maturidade.
4. [docs/FACIN_IA_Customizacao_Copilot.md](docs/FACIN_IA_Customizacao_Copilot.md): documentação da customização reutilizável do FACIN_IA para GitHub Copilot.
5. [docs/FACIN_IA_Plugin_Agente.md](docs/FACIN_IA_Plugin_Agente.md): documentação do plugin de agente FACIN_IA e das formas de instalação.
6. [docs/FACIN_IA_Avaliacao_Automatica.xlsx](docs/FACIN_IA_Avaliacao_Automatica.xlsx): planilha automatizada para aplicação prática do modelo.

## Estrutura do repositório

- `.github/agents/FACIN_IA.agent.md`: definição do agente customizado FACIN_IA.
- `.github/skills/facin-ia/SKILL.md`: skill portátil do método FACIN_IA.
- `.github/prompts/facin-ia-diagnostico.prompt.md`: prompt reutilizável para diagnóstico FACIN_IA baseado em evidências.
- `.github/plugin/marketplace.json`: marketplace Git para distribuição do plugin FACIN_IA.
- `plugins/facin-ia/`: pacote do plugin FACIN_IA com agente, comando, skill e instruções de uso.
- `.github/skills/facin-ia/metodo-facin-ia.md`: resumo das regras, dimensões e escala de maturidade.
- `.github/skills/facin-ia/template-especificacao.md`: template oficial de especificação orientada por governança.
- `.github/skills/facin-ia/checklist-avaliacao.md`: checklist rápido de aderência metodológica.
- [spec/FACIN_IA_Customizacao_Copilot.md](spec/FACIN_IA_Customizacao_Copilot.md): documentação-fonte da customização FACIN_IA para GitHub Copilot.
- [spec/FACIN_IA_Plugin_Agente.md](spec/FACIN_IA_Plugin_Agente.md): documentação-fonte do plugin de agente FACIN_IA.
- [spec/FACIN_IA_Modelo_Avaliacao.md](spec/FACIN_IA_Modelo_Avaliacao.md): documentação-fonte do modelo de avaliação.
- [spec/FACIN_IA_Planilha_Avaliacao.md](spec/FACIN_IA_Planilha_Avaliacao.md): especificação funcional da planilha de avaliação.
- [spec/FACIN_IA_Sintese.md](spec/FACIN_IA_Sintese.md): documentação-fonte da síntese institucional do trabalho.
- [spec/FACIN_IA_Versao_Executiva.md](spec/FACIN_IA_Versao_Executiva.md): versão executiva em Markdown.
- [docs/FACIN_IA_Modelo_Avaliacao.md](docs/FACIN_IA_Modelo_Avaliacao.md): cópia publicada em Markdown do modelo de avaliação.
- [docs/FACIN_IA_Modelo_Avaliacao.html](docs/FACIN_IA_Modelo_Avaliacao.html): versão navegável do modelo de avaliação.
- [docs/FACIN_IA_Modelo_Avaliacao.pdf](docs/FACIN_IA_Modelo_Avaliacao.pdf): versão em PDF do modelo.
- [docs/FACIN_IA_Customizacao_Copilot.md](docs/FACIN_IA_Customizacao_Copilot.md): cópia publicada em Markdown da customização FACIN_IA para GitHub Copilot.
- [docs/FACIN_IA_Customizacao_Copilot.html](docs/FACIN_IA_Customizacao_Copilot.html): versão navegável da customização FACIN_IA para GitHub Copilot.
- [docs/FACIN_IA_Customizacao_Copilot.pdf](docs/FACIN_IA_Customizacao_Copilot.pdf): versão em PDF da customização FACIN_IA para GitHub Copilot.
- [docs/FACIN_IA_Plugin_Agente.md](docs/FACIN_IA_Plugin_Agente.md): cópia publicada em Markdown da documentação do plugin FACIN_IA.
- [docs/FACIN_IA_Plugin_Agente.html](docs/FACIN_IA_Plugin_Agente.html): versão navegável da documentação do plugin FACIN_IA.
- [docs/FACIN_IA_Plugin_Agente.pdf](docs/FACIN_IA_Plugin_Agente.pdf): versão em PDF da documentação do plugin FACIN_IA.
- [docs/FACIN_IA_Planilha_Avaliacao.md](docs/FACIN_IA_Planilha_Avaliacao.md): cópia publicada em Markdown da especificação da planilha.
- [docs/FACIN_IA_Planilha_Avaliacao.html](docs/FACIN_IA_Planilha_Avaliacao.html): versão navegável da especificação da planilha.
- [docs/FACIN_IA_Planilha_Avaliacao.pdf](docs/FACIN_IA_Planilha_Avaliacao.pdf): versão em PDF da especificação da planilha.
- [docs/FACIN_IA_Sintese.md](docs/FACIN_IA_Sintese.md): cópia publicada em Markdown da síntese institucional.
- [docs/FACIN_IA_Sintese.html](docs/FACIN_IA_Sintese.html): versão navegável da síntese institucional.
- [docs/FACIN_IA_Sintese.pdf](docs/FACIN_IA_Sintese.pdf): versão em PDF da síntese institucional.
- [docs/FACIN_IA_Versao_Executiva.md](docs/FACIN_IA_Versao_Executiva.md): cópia publicada em Markdown da versão executiva.
- [docs/FACIN_IA_Versao_Executiva.html](docs/FACIN_IA_Versao_Executiva.html): versão executiva em HTML.
- [docs/FACIN_IA_Versao_Executiva.pdf](docs/FACIN_IA_Versao_Executiva.pdf): versão executiva em PDF.
- [docs/FACIN_IA_Avaliacao_Automatica.xlsx](docs/FACIN_IA_Avaliacao_Automatica.xlsx): planilha automatizada para cálculo da maturidade.
- [scripts/generate_artifacts.py](scripts/generate_artifacts.py): gerador dos artefatos Markdown, HTML, PDF e XLSX.
- [errors/erro_weasyprint_pdf.txt](errors/erro_weasyprint_pdf.txt): registro do erro inicial de geração de PDF com WeasyPrint no Windows.
- [Diretrizes FACIN_IA.txt](Diretrizes%20FACIN_IA.txt): diretrizes obrigatórias do projeto.
- [FACIN_IA_Projeto.md](FACIN_IA_Projeto.md): documento consolidado da elaboração do projeto.

## Escopo metodológico

O modelo organiza a maturidade em seis dimensões obrigatórias:

1. Estratégia e Governança de IA
2. Dados e Infraestrutura
3. Talento e Cultura
4. Desenvolvimento e Operação de IA (DevOps/MLOps)
5. Ética, Transparência e Gestão de Risco
6. Impacto Social e Valor

Cada dimensão é avaliada por indicadores com fórmula, evidência mínima, periodicidade e regra de leitura em cinco níveis de maturidade.

## Contexto adotado

A parametrização foi ajustada para a PRODEMGE, considerando o contexto de empresa pública estadual de tecnologia que opera serviços digitais críticos, infraestrutura corporativa e plataformas de governo. O modelo pode ser recalibrado para outros órgãos, preservando a mesma estrutura metodológica.

## Escala de maturidade

- Nível 1 - Inicial
- Nível 2 - Em Desenvolvimento
- Nível 3 - Otimizado
- Nível 4 - Consolidado
- Nível 5 - Estabelecido

## Como regenerar os artefatos

O gerador está em [scripts/generate_artifacts.py](scripts/generate_artifacts.py). Ele produz:

- cópias em Markdown dos arquivos em spec/ na pasta docs/;
- HTML a partir dos arquivos em spec/;
- PDF a partir dos arquivos em spec/;
- planilha XLSX de avaliação automática em docs/.

Dependências Python utilizadas no script:

- markdown
- openpyxl
- reportlab

Execução:

```bash
python scripts/generate_artifacts.py
```

## Premissas de governança do projeto

- IA executa especificações governadas.
- Prompt, modelo, dado e decisão são artefatos rastreáveis.
- Observabilidade e segregação entre ideação e produção são obrigatórias.
- Casos de maior risco exigem avaliação ética e controles formais.
- Instalações, quando necessárias, devem ocorrer somente no ambiente figmm.