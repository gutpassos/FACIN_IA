# FACIN_IA - Distribuicao como pacote Python e GitHub Template

Autor: Guttenberg Ferreira Passos

Especificacao do empacotamento inicial do FACIN_IA como pacote Python com CLI de scaffolding e da preparacao do repositório para uso como GitHub Template.

## 1. Objetivo

Criar uma terceira via de distribuicao do FACIN_IA, complementar a customizacao direta e ao plugin de agente, para permitir:

1. provisionamento automatizado do metodo em repositórios existentes;
2. inicializacao de novos projetos ja com o FACIN_IA embarcado;
3. padronizacao institucional de artefatos de governanca, rastreabilidade e onboarding.

## 2. Base implementada no repositório

### 2.1 Pacote Python

O repositório passa a incluir:

- `pyproject.toml`;
- `src/facin_ia/__init__.py`;
- `src/facin_ia/cli.py`;
- `src/facin_ia/scaffold.py`;
- `src/facin_ia/__main__.py`.
- `.github/workflows/publish-python-package.yml`.

Essa estrutura permite instalar o projeto localmente com `pip install .` e executar a CLI `facin-ia`.

### 2.2 Workflow de publicacao

O repositório passa a incluir um workflow manual do GitHub Actions para publicar o pacote em TestPyPI ou PyPI.

Arquivo:

- `.github/workflows/publish-python-package.yml`

Fluxo implementado no workflow:

1. checkout do repositorio;
2. instalacao do Python e das ferramentas de build;
3. geracao dos artefatos em `dist/` com `python -m build`;
4. validacao com `python -m twine check dist/*`;
5. publicacao manual para `testpypi` ou `pypi` via `workflow_dispatch`.

O workflow foi preparado para uso com Trusted Publishing por meio dos environments `testpypi` e `pypi` no GitHub.

### 2.3 Perfis de scaffolding

A CLI foi preparada com tres perfis:

1. `customizacao`: instala agente, prompt e skill em `.github/`;
2. `plugin`: instala a customizacao e o plugin local em `plugins/facin-ia/`;
3. `template-base`: instala customizacao, plugin e arquivos auxiliares para repositórios criados a partir de template.

### 2.4 Arquivos de template

O repositório tambem passa a incluir:

- `TEMPLATE_SETUP.md`;
- `.github/PULL_REQUEST_TEMPLATE.md`;
- `.github/ISSUE_TEMPLATE/facin-ia-adocao.md`;
- `.github/ISSUE_TEMPLATE/config.yml`.

Esses arquivos preparam o repositório para colaboracao e onboarding quando usado como template do GitHub.

## 3. Instalacao para o usuario

### 3.1 Repositórios existentes

Fluxo atual:

```bash
pip install .
facin-ia init --profile customizacao
```

Fluxo previsto apos publicacao no PyPI:

```bash
pip install facin-ia
facin-ia init --profile customizacao
```

O usuario pode trocar o perfil para `plugin` ou `template-base` conforme a necessidade.

### 3.2 Publicacao do pacote pelo GitHub Actions

Fluxo previsto para o mantenedor:

1. configurar o projeto `facin-ia` no PyPI e no TestPyPI;
2. registrar o repositório como trusted publisher nas duas plataformas;
3. criar os environments `testpypi` e `pypi` no GitHub;
4. abrir a aba `Actions` do repositório;
5. executar o workflow `Publish Python Package`;
6. escolher o destino `testpypi` ou `pypi`;
7. acompanhar a publicacao ate a conclusao.

### 3.3 Novos projetos via GitHub Template

Fluxo previsto para o usuario:

1. acessar o repositório no GitHub;
2. selecionar `Use this template`;
3. criar o novo repositório;
4. clonar o repositório gerado;
5. abrir no VS Code com GitHub Copilot habilitado;
6. revisar o roteiro em `TEMPLATE_SETUP.md`.

## 4. Diferenca em relacao as outras formas de adocao

### 4.1 Em relacao a customizacao direta

A customizacao direta continua sendo a opcao mais simples e manual. O pacote Python reduz o trabalho repetitivo ao materializar os mesmos artefatos por comando.

### 4.2 Em relacao ao plugin

O plugin resolve distribuicao operacional do agente no VS Code. O pacote Python resolve provisao automatizada de estrutura no repositório. O GitHub Template resolve bootstrap de novos projetos.

## 5. Beneficios

1. menor atrito de instalacao para usuarios finais;
2. padronizacao de estrutura entre equipes e repositórios;
3. reducao de erro manual na copia de artefatos;
4. base pronta para futura publicacao no PyPI;
5. base pronta para publicacao manual controlada por GitHub Actions;
6. base pronta para marcar o repositório como template oficial no GitHub.

## 6. Limites atuais

1. o pacote e o workflow ja estao estruturados, mas a publicacao ainda depende da configuracao de trusted publisher no PyPI e no TestPyPI;
2. o repositório ja esta preparado como template, mas a marcacao como template depende da configuracao no GitHub;
3. os artefatos gerados pela CLI sao uma base inicial e podem ser refinados por contexto institucional.

## 7. Criterios de aceitacao

Esta frente sera considerada concluida quando:

1. o pacote puder ser instalado localmente com `pip install .`;
2. a CLI `facin-ia` materializar corretamente os perfis previstos;
3. o workflow de publicacao construir e validar o pacote antes do upload;
4. o repositório contiver arquivos adequados para uso como template;
5. a documentacao explicar claramente a experiencia do usuario em cada modo de distribuicao.
