# FACIN_IA

Modelo de maturidade e governança aplicada à inteligência artificial para organizações públicas e ambientes de desenvolvimento intensivos em IA.

O projeto adapta o Framework de Arquitetura Corporativa para Interoperabilidade no apoio à Governança (FACIN), Modelo de Responsabilidade Organizacional (MRO) e Spec-Driven Development (SDD) para avaliar como estratégia, dados, operação, risco, transparência e valor público são governados ao longo do ciclo de vida da IA.

Autor: Guttenberg Ferreira Passos  
Modelo LLM utilizado: GPT-5.4  
Ambiente validado: figmm

## O que o FACIN_IA entrega

O repositório combina duas frentes complementares:

1. um modelo institucional de avaliação de maturidade em governança de IA, com artefatos executivos, analíticos e operacionais;
2. uma forma reutilizável de levar o método para outros repositórios por customização do GitHub Copilot, plugin de agente e preparação para distribuição como pacote PyPI ou GitHub Template.

Na prática, o FACIN_IA pode ser usado tanto como referencial metodológico quanto como camada operacional para apoiar diagnóstico, especificação antes de código, definição de indicadores, evidências, controles e adaptação do método para outros contextos institucionais.

## Formas de adoção do FACIN_IA

O projeto passa a documentar três opções distintas de uso.

### Opção 1. Customização direta do repositório

Esta é a forma mais simples para equipes que já possuem um repositório e querem incorporar o método manualmente, sem depender de empacotamento adicional.

Estrutura disponível hoje:

- `.github/agents/FACIN_IA.agent.md`
- `.github/skills/facin-ia/SKILL.md`
- `.github/prompts/facin-ia-diagnostico.prompt.md`
- `.github/skills/facin-ia/template-especificacao.md`
- `.github/skills/facin-ia/metodo-facin-ia.md`
- `.github/skills/facin-ia/checklist-avaliacao.md`

Como instalar em outro projeto:

1. copie as pastas `.github/agents/`, `.github/skills/facin-ia/` e `.github/prompts/` para o repositório de destino;
2. abra o projeto no VS Code com GitHub Copilot habilitado;
3. selecione o agente `FACIN_IA` no chat;
4. use a skill `/facin-ia` para carregar o método;
5. use o prompt `/facin-ia-diagnostico` para diagnósticos baseados em evidências.

Quando usar esta opção:

- quando a equipe quer controle total sobre os arquivos de customização;
- quando a adoção será feita em poucos repositórios;
- quando a organização prefere distribuir o método sem depender de plugin em preview.

### Opção 2. Plugin de agente para o GitHub Copilot

Esta opção já está materializada no repositório e foi pensada para reduzir a cópia manual de arquivos entre equipes.

Estrutura disponível hoje:

- `plugins/facin-ia/`
- `.github/plugin/marketplace.json`

O plugin inclui:

- agente especializado `FACIN_IA`;
- skill `facin-ia`;
- comando de slash `facin-ia-diagnostico`.

#### Instalação como plugin local

Use esta modalidade quando a equipe possui o repositório clonado localmente.

No `settings.json` do VS Code:

```json
{
	"chat.plugins.enabled": true,
	"chat.pluginLocations": {
		"C:/Programas/Prodemge/FACIN_IA/plugins/facin-ia": true
	}
}
```

Depois:

1. abra o chat do GitHub Copilot;
2. localize o plugin entre os plugins de agente;
3. habilite o plugin `facin-ia`;
4. selecione o agente `FACIN_IA` ou execute o comando `/facin-ia:facin-ia-diagnostico`.

#### Instalação via marketplace Git

Use esta modalidade quando a organização quiser distribuição centralizada.

No `settings.json` do VS Code:

```json
{
	"chat.plugins.enabled": true,
	"chat.plugins.marketplaces": [
		"https://github.com/gutpassos/FACIN_IA.git"
	]
}
```

Depois:

1. abra a interface de plugins do chat;
2. localize o plugin `facin-ia` a partir do marketplace;
3. instale e habilite o plugin;
4. use o agente, a skill e o comando disponibilizados pelo pacote.

Quando usar esta opção:

- quando a equipe quer padronização com menor esforço de replicação;
- quando há interesse em versionar a distribuição do método;
- quando o ambiente aceita uso de agent plugins em preview.

### Opção 3. Pacote PyPI e GitHub Template

Esta é uma terceira forma de distribuição do FACIN_IA, separada do plugin, indicada para ampliar adoção em larga escala e reduzir atrito para usuários que precisam iniciar projetos novos ou habilitar rapidamente o método em repositórios existentes.

Esta opção agora possui base estrutural no repositório. A publicação no PyPI e a marcação formal do repositório como template no GitHub ainda dependem do processo de publicação, mas o empacotamento inicial, a CLI e os arquivos-base de template já foram preparados.

#### Como funciona a opção PyPI

O repositório agora inclui uma base de pacote Python em `pyproject.toml` e `src/facin_ia/`, com uma CLI própria para instalar ou injetar a estrutura metodológica no projeto do usuário.

Estrutura preparada:

- `pyproject.toml`;
- `src/facin_ia/__init__.py`;
- `src/facin_ia/cli.py`;
- `src/facin_ia/scaffold.py`.

Perfis disponíveis na CLI:

- `customizacao`: gera a estrutura `.github` com agente, skill e prompt;
- `plugin`: gera a customização e também o pacote do plugin local;
- `template-base`: gera customização, plugin e arquivos auxiliares para uso como template.

Instalação atual a partir do código-fonte:

```bash
pip install .
facin-ia init --profile customizacao
```

Instalação prevista após publicação no PyPI:

```bash
pip install facin-ia
facin-ia init --profile customizacao
```

Fluxo de instalação:

1. o usuário instala o pacote Python no ambiente desejado;
2. executa a CLI dentro do repositório de destino;
3. escolhe o perfil desejado, como `customizacao`, `plugin` ou `template-base`;
4. a CLI materializa os arquivos `.github`, prompts, skills, agentes e, quando aplicável, a estrutura do plugin e dos arquivos de template;
5. o usuário abre o projeto no VS Code e passa a utilizar o FACIN_IA com a configuração pronta.

Benefícios desta abordagem:

- instalação rápida em repositórios já existentes;
- menor chance de erro manual na cópia da estrutura;
- possibilidade de atualização versionada do método;
- boa aderência para times que já trabalham com distribuição interna de pacotes Python.

#### Como funciona a opção GitHub Template

O repositório também foi preparado para operar como GitHub Template, com arquivos-base de onboarding e colaboração que podem seguir automaticamente para novos repositórios gerados a partir dele.

Estrutura preparada:

- `TEMPLATE_SETUP.md`;
- `.github/PULL_REQUEST_TEMPLATE.md`;
- `.github/ISSUE_TEMPLATE/facin-ia-adocao.md`;
- `.github/ISSUE_TEMPLATE/config.yml`.

Experiência esperada do usuário:

1. o usuário clica em `Use this template` no GitHub;
2. cria um novo repositório a partir do template;
3. clona o repositório gerado;
4. abre o projeto no VS Code com GitHub Copilot habilitado;
5. começa a usar o agente `FACIN_IA` e os artefatos já pré-carregados.

O template pode entregar, desde a criação do repositório:

- estrutura `.github` pronta;
- documentação inicial do método;
- pasta de plugin opcional;
- exemplos de prompts e checklist de avaliação;
- arquivos-base para especificação, governança e evidências.

Quando usar PyPI ou Template:

- PyPI é mais adequado para injetar o FACIN_IA em repositórios já existentes;
- GitHub Template é mais adequado para iniciar novos projetos já padronizados;
- as duas modalidades podem coexistir com o plugin, atendendo públicos e cenários diferentes.

#### Instalação do usuário nesta terceira opção

O fluxo agora fica assim:

1. para projetos existentes, instalar localmente a base do pacote com `pip install .` ou, após publicação, `pip install facin-ia`, e executar `facin-ia init`;
2. para projetos novos, marcar este repositório como template no GitHub e então criar o novo repositório a partir dele;
3. em ambos os casos, abrir o projeto no VS Code e usar o agente `FACIN_IA` conforme o perfil provisionado.

## O que este repositório entrega hoje

- um modelo de avaliação de maturidade em seis dimensões de governança de IA;
- uma versão executiva para apresentação institucional;
- uma síntese institucional do trabalho e de seus fundamentos conceituais;
- uma especificação de planilha com cálculo automático de pontuação;
- uma customização reutilizável do GitHub Copilot;
- um plugin de agente para distribuição entre equipes;
- artefatos prontos em Markdown, HTML, PDF e XLSX para consulta e uso direto.

## Leitura recomendada

1. [docs/FACIN_IA_Versao_Executiva.md](docs/FACIN_IA_Versao_Executiva.md): visão rápida para apresentação e alinhamento institucional.
2. [docs/FACIN_IA_Sintese.md](docs/FACIN_IA_Sintese.md): síntese do trabalho, dos conceitos-base e da aplicação prática com IA assistida.
3. [docs/FACIN_IA_Modelo_Avaliacao.md](docs/FACIN_IA_Modelo_Avaliacao.md): modelo completo de avaliação, pesos, fórmulas e faixas de maturidade.
4. [docs/FACIN_IA_Customizacao_Copilot.md](docs/FACIN_IA_Customizacao_Copilot.md): documentação da customização reutilizável do FACIN_IA para GitHub Copilot.
5. [docs/FACIN_IA_Plugin_Agente.md](docs/FACIN_IA_Plugin_Agente.md): documentação do plugin de agente FACIN_IA e das formas de instalação.
6. [docs/FACIN_IA_Distribuicao_PyPI_Template.md](docs/FACIN_IA_Distribuicao_PyPI_Template.md): empacotamento inicial do FACIN_IA como pacote Python e preparação do repositório para GitHub Template.
7. [docs/FACIN_IA_Planilha_Avaliacao.md](docs/FACIN_IA_Planilha_Avaliacao.md): especificação funcional da planilha de avaliação.

## Estrutura principal do repositório

- `.github/agents/FACIN_IA.agent.md`: definição do agente customizado FACIN_IA.
- `.github/skills/facin-ia/SKILL.md`: skill portátil do método FACIN_IA.
- `.github/prompts/facin-ia-diagnostico.prompt.md`: prompt reutilizável para diagnóstico baseado em evidências.
- `.github/plugin/marketplace.json`: marketplace Git para distribuição do plugin FACIN_IA.
- `plugins/facin-ia/`: pacote do plugin FACIN_IA com agente, comando, skill e instruções de uso.
- [spec/FACIN_IA_Customizacao_Copilot.md](spec/FACIN_IA_Customizacao_Copilot.md): documentação-fonte da customização FACIN_IA para GitHub Copilot.
- [spec/FACIN_IA_Plugin_Agente.md](spec/FACIN_IA_Plugin_Agente.md): documentação-fonte do plugin de agente FACIN_IA.
- [spec/FACIN_IA_Distribuicao_PyPI_Template.md](spec/FACIN_IA_Distribuicao_PyPI_Template.md): documentação-fonte do empacotamento PyPI e da preparação do GitHub Template.
- [spec/FACIN_IA_Modelo_Avaliacao.md](spec/FACIN_IA_Modelo_Avaliacao.md): documentação-fonte do modelo de avaliação.
- [spec/FACIN_IA_Planilha_Avaliacao.md](spec/FACIN_IA_Planilha_Avaliacao.md): especificação funcional da planilha de avaliação.
- [spec/FACIN_IA_Sintese.md](spec/FACIN_IA_Sintese.md): documentação-fonte da síntese institucional do trabalho.
- [spec/FACIN_IA_Versao_Executiva.md](spec/FACIN_IA_Versao_Executiva.md): versão executiva em Markdown.
- `pyproject.toml`: metadados do pacote Python `facin-ia`.
- `src/facin_ia/`: pacote Python com CLI e motor de scaffolding para distribuição do FACIN_IA.
- [TEMPLATE_SETUP.md](TEMPLATE_SETUP.md): roteiro de parametrização para repositórios criados a partir do template.
- [scripts/generate_artifacts.py](scripts/generate_artifacts.py): gerador dos artefatos Markdown, HTML, PDF e XLSX.
- [errors/erro_weasyprint_pdf.txt](errors/erro_weasyprint_pdf.txt): registro do erro inicial de geração de PDF com WeasyPrint no Windows.
- [Diretrizes FACIN_IA.txt](Diretrizes%20FACIN_IA.txt): diretrizes obrigatórias do projeto.
- [FACIN_IA_Projeto.md](FACIN_IA_Projeto.md): documento consolidado da elaboração do projeto.

## Escopo metodológico

O modelo organiza a maturidade em seis dimensões obrigatórias:

1. Estratégia e Governança de IA
2. Dados e Infraestrutura
3. Talento e Cultura
4. Desenvolvimento e Operação de IA
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

- cópias em Markdown dos arquivos em `spec/` na pasta `docs/`;
- HTML a partir dos arquivos em `spec/`;
- PDF a partir dos arquivos em `spec/`;
- planilha XLSX de avaliação automática em `docs/`.

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
