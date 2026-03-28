# Plugin FACIN_IA

Autor: Guttenberg Ferreira Passos

Plugin de agente para GitHub Copilot com foco em governanca aplicada a inteligencia artificial, diagnostico de maturidade, especificacao antes de codigo e avaliacao baseada em evidencias.

## O que o plugin inclui

- agente especializado `FACIN_IA`;
- skill metodologica `facin-ia`;
- comando de slash `facin-ia-diagnostico` para diagnostico padronizado.

## Instalacao no VS Code

O suporte a plugins de agente esta em preview. Antes de instalar, habilite o recurso no VS Code:

```json
{
  "chat.plugins.enabled": true
}
```

### Opcao 1. Instalar como plugin local

Use esta opcao quando a equipe tiver o repositório clonado localmente.

Adicione o caminho do plugin em `settings.json`:

```json
{
  "chat.plugins.enabled": true,
  "chat.pluginLocations": {
    "C:/Programas/Prodemge/FACIN_IA/plugins/facin-ia": true
  }
}
```

Depois disso:

1. abra o chat do GitHub Copilot;
2. verifique se o plugin aparece em `@agentPlugins` ou em `Chat: Plugins`;
3. habilite o plugin, se necessario.

### Opcao 2. Instalar via marketplace deste repositório

Este repositório inclui um marketplace em `.github/plugin/marketplace.json`.

Adicione o marketplace nas configuracoes:

```json
{
  "chat.plugins.enabled": true,
  "chat.plugins.marketplaces": [
    "https://github.com/gutpassos/FACIN_IA.git"
  ]
}
```

Depois:

1. abra a busca de extensoes com `@agentPlugins` ou use `Chat: Plugins`;
2. localize o plugin `facin-ia`;
3. instale e habilite o plugin.

## Como usar

### Agente

Selecione o agente `FACIN_IA` no chat para tarefas como:

- diagnostico de maturidade de governanca de IA;
- elaboracao de especificacao antes de codigo;
- definicao de indicadores, evidencias e controles;
- adaptacao do metodo FACIN_IA para orgaos, produtos e projetos.

### Skill

Invoque a skill `/facin-ia` para carregar o metodo, o template de especificacao e o checklist de avaliacao.

### Comando de diagnostico

Execute o comando:

```text
/facin-ia:facin-ia-diagnostico
```

Exemplo de uso:

```text
/facin-ia:facin-ia-diagnostico Avaliar a maturidade de governanca de IA de um orgao publico com base em politica institucional, atas de comite, catalogo de dados, logs operacionais e relatorios de risco.
```

## Estrutura do plugin

```text
plugins/facin-ia/
  .github/plugin/plugin.json
  agents/facin-ia.md
  commands/facin-ia-diagnostico.md
  skills/facin-ia/
    SKILL.md
    metodo-facin-ia.md
    template-especificacao.md
    checklist-avaliacao.md
  README.md
```

## Observacoes

- o plugin e autocontido para evitar dependencias em arquivos externos ao pacote;
- o metodo continua disponivel tambem como customizacao local do repositorio;
- em ambientes corporativos, a equipe pode padronizar o uso do plugin via marketplace Git interno.