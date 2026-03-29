# FACIN_IA - Plugin de Agente para Distribuicao entre Equipes

Autor: Guttenberg Ferreira Passos

Especificacao do empacotamento do FACIN_IA como plugin de agente para GitHub Copilot, com foco em distribuicao mais simples entre equipes por plugin local ou marketplace Git.

## 1. Objetivo

Empacotar o FACIN_IA como plugin para que equipes possam instalar, habilitar e usar o metodo sem copiar manualmente as pastas de customizacao para cada repositorio.

## 2. Estrutura do plugin

O plugin foi materializado em:

- `plugins/facin-ia/.github/plugin/plugin.json`
- `plugins/facin-ia/agents/facin-ia.md`
- `plugins/facin-ia/commands/facin-ia-diagnostico.md`
- `plugins/facin-ia/skills/facin-ia/`
- `plugins/facin-ia/README.md`

O repositório tambem publica um marketplace em:

- `.github/plugin/marketplace.json`

## 3. Componentes entregues

### 3.1 Agente

O plugin inclui o agente `FACIN_IA`, especializado em governanca de IA, maturidade, especificacao antes de codigo e adaptacao metodologica.

### 3.2 Skill

O plugin inclui a skill `facin-ia`, contendo metodo resumido, template de especificacao e checklist de avaliacao.

### 3.3 Comando

O plugin inclui o comando `facin-ia-diagnostico`, voltado a diagnosticos FACIN_IA baseados em evidencias.

## 4. Formas de instalacao

### 4.1 Plugin local

Quando a equipe possui o repositorio clonado localmente, o plugin pode ser registrado por caminho usando `chat.pluginLocations`.

Exemplo:

```json
{
  "chat.plugins.enabled": true,
  "chat.pluginLocations": {
    "C:/Programas/Prodemge/FACIN_IA/plugins/facin-ia": true
  }
}
```

### 4.2 Marketplace Git

Quando a equipe deseja distribuicao centralizada, o repositório pode ser usado como marketplace por meio de `chat.plugins.marketplaces`.

Exemplo:

```json
{
  "chat.plugins.enabled": true,
  "chat.plugins.marketplaces": [
    "https://github.com/gutpassos/FACIN_IA.git"
  ]
}
```

Depois disso, o plugin `facin-ia` pode ser instalado e habilitado na interface de plugins do VS Code.

## 4.3 Relacao com PyPI e GitHub Template

O plugin nao substitui as outras formas de adocao do FACIN_IA.

O repositório passa a incluir tambem uma base de pacote Python com CLI e preparacao para GitHub Template, descrita em `docs/FACIN_IA_Distribuicao_PyPI_Template.md`.

O posicionamento entre as opcoes fica assim:

1. customizacao direta: copia manual dos artefatos para um repositório existente;
2. plugin: distribuicao operacional do agente dentro do VS Code;
3. PyPI: provisionamento automatizado da estrutura em repositórios existentes;
4. GitHub Template: criacao de novos repositórios ja nascendo com o FACIN_IA embarcado.

## 5. Instrucoes de uso

Depois de instalado e habilitado, a equipe pode usar:

1. o agente `FACIN_IA` no seletor de agentes do chat;
2. a skill `/facin-ia` para carregar a base metodologica;
3. o comando `/facin-ia:facin-ia-diagnostico` para diagnostico padronizado.

## 6. Exemplo de uso

```text
/facin-ia:facin-ia-diagnostico Avaliar a maturidade de governanca de IA de um orgao com base em politica institucional, atas de comite, catalogo de dados, logs operacionais e relatorios de auditoria.
```

## 7. Beneficios do empacotamento

1. padronizacao entre equipes;
2. reducao de copia manual de arquivos;
3. distribuicao por marketplace ou caminho local;
4. evolucao versionada do agente, da skill e do comando;
5. menor friccao para adocao institucional do FACIN_IA.
6. coexistencia com a trilha de pacote Python e template, ampliando as formas de distribuicao.

## 8. Limites atuais

1. o suporte a agent plugins no VS Code esta em preview;
2. a equipe precisa habilitar `chat.plugins.enabled`;
3. a instalacao por marketplace depende da descoberta do repositorio como catalogo de plugins.

## 9. Criterios de aceitacao

O empacotamento sera considerado concluido quando:

1. o diretorio `plugins/facin-ia/` estiver autocontido;
2. o manifesto `plugin.json` declarar agente, comando e skill validos;
3. o marketplace do repositorio listar o plugin `facin-ia`;
4. houver instrucoes claras de instalacao e uso no plugin;
5. a documentacao publicada existir em Markdown, HTML e PDF.