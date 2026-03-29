# FACIN_IA

Governança de inteligência artificial para projetos com GitHub Copilot, com foco em maturidade, evidências, risco, especificação antes de código e padronização institucional.

Este arquivo resume o posicionamento do FACIN_IA como mecanismo de adoção do método em outros projetos. O detalhamento completo do repositório e dos artefatos está em [README.md](README.md).

## O que o FACIN_IA faz

O FACIN_IA transforma o repositório em uma base governada para uso de IA assistida, apoiando atividades como:

- diagnóstico de maturidade de governança de IA;
- definição de indicadores, evidências e controles;
- especificação orientada por governança antes de código;
- adaptação do método para órgãos, produtos e equipes;
- padronização do uso do GitHub Copilot com foco institucional.

## Opções de adoção

O FACIN_IA passa a ser descrito em três opções separadas.

### 1. Customização direta no repositório

Indicado para equipes que querem copiar a estrutura metodológica diretamente para um projeto existente.

Arquivos principais:

- `.github/agents/FACIN_IA.agent.md`
- `.github/skills/facin-ia/`
- `.github/prompts/facin-ia-diagnostico.prompt.md`

Instalação para o usuário:

1. copiar as pastas de `.github` para o projeto alvo;
2. abrir o projeto no VS Code com GitHub Copilot habilitado;
3. selecionar o agente `FACIN_IA`;
4. usar a skill `/facin-ia` e o prompt `/facin-ia-diagnostico`.

### 2. Plugin de agente

Indicado para distribuição entre equipes com menor esforço manual.

Estrutura disponível:

- `plugins/facin-ia/`
- `.github/plugin/marketplace.json`

Instalação como plugin local:

```json
{
	"chat.plugins.enabled": true,
	"chat.pluginLocations": {
		"C:/Programas/Prodemge/FACIN_IA/plugins/facin-ia": true
	}
}
```

Instalação via marketplace Git:

```json
{
	"chat.plugins.enabled": true,
	"chat.plugins.marketplaces": [
		"https://github.com/gutpassos/FACIN_IA.git"
	]
}
```

Depois da habilitação, o usuário pode:

1. selecionar o agente `FACIN_IA`;
2. invocar a skill `/facin-ia`;
3. executar `/facin-ia:facin-ia-diagnostico`.

### 3. Pacote PyPI e GitHub Template

Indicado para ampliar escala de adoção e oferecer uma experiência de instalação mais simples para usuários finais.

Esta terceira trilha já possui base estrutural no repositório, com pacote Python inicial, CLI de scaffolding e arquivos auxiliares para uso do repositório como template.

#### Pacote PyPI

A base do pacote foi estruturada em `pyproject.toml` e `src/facin_ia/`.

Fluxo atual a partir do código-fonte:

```bash
pip install .
facin-ia init --profile customizacao
```

Fluxo previsto após publicação no PyPI:

```bash
pip install facin-ia
facin-ia init --profile customizacao
```

Como funciona para o usuário:

1. instalar o pacote Python;
2. executar a CLI no diretório do projeto alvo;
3. escolher o perfil de instalação, como customização simples, plugin ou estrutura completa;
4. deixar que a ferramenta gere os arquivos `.github`, prompts, skills e agentes;
5. abrir o projeto no VS Code e usar o FACIN_IA já provisionado.

#### GitHub Template

Nesta modalidade, o repositório já foi preparado com arquivos-base como `TEMPLATE_SETUP.md`, `.github/PULL_REQUEST_TEMPLATE.md` e `.github/ISSUE_TEMPLATE/` para operar como template oficial de novos projetos.

Como funciona para o usuário:

1. criar um repositório a partir de `Use this template` no GitHub;
2. clonar o novo repositório;
3. abrir no VS Code;
4. usar imediatamente o agente e os artefatos do FACIN_IA.

#### Diferença em relação ao plugin

- plugin resolve distribuição operacional dentro do VS Code;
- PyPI resolve instalação automatizada em repositórios existentes;
- GitHub Template resolve bootstrap de novos projetos com padronização desde o primeiro commit.

## Requisitos gerais

- GitHub Copilot habilitado no VS Code;
- Git para clonagem e versionamento;
- Python para uso do pacote local ou, futuramente, da publicação no PyPI;
- uso preferencial no ambiente figmm quando houver necessidade de instalação controlada.

## Posicionamento

O FACIN_IA não deve ser tratado apenas como plugin.

Ele é uma camada de governança para desenvolvimento com IA, que pode ser distribuída por customização direta, plugin, pacote PyPI ou GitHub Template, conforme o cenário de adoção.
