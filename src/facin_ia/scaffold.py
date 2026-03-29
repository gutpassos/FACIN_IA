from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


def _text(content: str) -> str:
    return dedent(content).lstrip("\n").rstrip() + "\n"


FACIN_AGENT = _text(
    """
    ---
    name: FACIN_IA
    description: Especialista em governanca de IA baseada em FACIN, MRO e Spec-Driven Development.
    argument-hint: Descreva o projeto, orgao, iniciativa de IA ou problema de governanca e o resultado esperado.
    ---

    # FACIN_IA

    Voce e o agente FACIN_IA. Sua funcao e transformar demandas relacionadas a IA em especificacoes governadas, rastreaveis e auditaveis antes de qualquer proposta de implementacao tecnica.

    ## Regras operacionais

    1. Estruture analises em seis dimensoes: estrategia, dados, talento, operacao, risco e impacto.
    2. Nunca trate prompt, modelo, dado e decisao como itens soltos; trate-os como artefatos governados.
    3. Exija evidencias minimas para qualquer avaliacao de maturidade.
    4. Diferencie ideacao, validacao e operacao em producao.
    5. Para risco medio ou alto, exija controles formais, transparencia e rastreabilidade.
    """
)

FACIN_PROMPT = _text(
    """
    ---
    name: facin-ia-diagnostico
    description: Diagnosticar a maturidade FACIN_IA de um projeto, orgao, produto ou iniciativa de IA a partir de evidencias.
    argument-hint: Informe o contexto avaliado, o objetivo do diagnostico e as evidencias disponiveis.
    agent: FACIN_IA
    ---

    # Diagnostico FACIN_IA por evidencias

    Execute um diagnostico estruturado por evidencias.

    ## Saida obrigatoria

    1. Resumo executivo
    2. Evidencias consideradas
    3. Diagnostico por dimensao
    4. Maturidade consolidada
    5. Recomendacoes priorizadas
    6. Evidencias adicionais requeridas
    7. Proximos artefatos recomendados
    """
)

FACIN_SKILL = _text(
    """
    ---
    name: facin-ia
    description: Aplicar o metodo FACIN_IA para diagnosticar maturidade, criar especificacoes antes de codigo e definir indicadores, evidencias e controles.
    argument-hint: Informe o contexto do projeto, orgao ou iniciativa de IA e o artefato desejado.
    ---

    # FACIN_IA Skill

    Use esta skill para governanca de IA, maturidade institucional, especificacao orientada por artefatos e adaptacao do metodo FACIN_IA.

    ## Processo recomendado

    1. Identifique o tipo de demanda.
    2. Colete contexto institucional minimo.
    3. Estruture a analise nas seis dimensoes do FACIN_IA.
    4. Produza artefatos reutilizaveis em vez de texto solto.
    5. Associe recomendacoes a evidencia minima, responsavel e risco mitigado.
    """
)

FACIN_METHOD = _text(
    """
    # Metodo resumido FACIN_IA

    ## Principios

    1. A inteligencia artificial executa especificacoes governadas.
    2. O codigo e artefato derivado.
    3. Prompt, modelo, dado, decisao e politica devem ser rastreaveis.
    4. Observabilidade e segregacao entre ideacao e producao sao obrigatorias.

    ## Dimensoes obrigatorias

    1. Estrategia e Governanca de IA
    2. Dados e Infraestrutura
    3. Talento e Cultura
    4. Desenvolvimento e Operacao de IA
    5. Etica, Transparencia e Gestao de Risco
    6. Impacto Social e Valor

    ## Niveis de maturidade

    - Nivel 1 - Inicial
    - Nivel 2 - Em Desenvolvimento
    - Nivel 3 - Otimizado
    - Nivel 4 - Consolidado
    - Nivel 5 - Estabelecido
    """
)

FACIN_TEMPLATE = _text(
    """
    # Template de especificacao FACIN_IA

    ## 1. Identificacao do projeto

    - nome:
    - orgao ou unidade:
    - objetivo:
    - responsavel:

    ## 2. Problema de negocio

    - dor principal:
    - publico afetado:
    - resultado esperado:

    ## 3. Uso de IA

    - tipo de capacidade:
    - dados utilizados:
    - modelos ou servicos:
    - riscos principais:

    ## 4. Controles e evidencias

    - controles obrigatorios:
    - evidencias minimas:
    - trilha de auditoria:

    ## 5. Criterios de aceitacao

    - criterio 1:
    - criterio 2:
    - criterio 3:
    """
)

FACIN_CHECKLIST = _text(
    """
    # Checklist de avaliacao FACIN_IA

    - Existe objetivo de negocio claramente definido.
    - Ha patrocinio institucional e responsabilizacao.
    - Dados, modelos e prompts sao rastreaveis.
    - Existem criterios de aceitacao antes do codigo.
    - Ha controles proporcionais ao risco.
    - Existe plano de evidencias e revisao periodica.
    """
)

PLUGIN_AGENT = _text(
    """
    ---
    name: FACIN_IA
    description: Agente do metodo FACIN_IA para governanca aplicada a IA.
    ---

    # Plugin FACIN_IA

    Use este agente para diagnosticos, especificacoes antes de codigo e estruturacao de governanca de IA.
    """
)

PLUGIN_COMMAND = _text(
    """
    ---
    name: facin-ia-diagnostico
    description: Executar diagnostico FACIN_IA baseado em evidencias.
    agent: FACIN_IA
    ---

    # Comando FACIN_IA

    Execute um diagnostico de maturidade FACIN_IA com base em evidencias apresentadas pelo usuario.
    """
)

PLUGIN_README = _text(
    """
    # Plugin FACIN_IA

    Plugin de agente para GitHub Copilot com foco em governanca aplicada a IA.

    ## Instalacao local

    Adicione o caminho deste diretorio em chat.pluginLocations no settings.json do VS Code.

    ## Componentes

    - agente FACIN_IA
    - skill facin-ia
    - comando facin-ia-diagnostico
    """
)

MARKETPLACE_JSON = _text(
    """
    {
      "name": "facin-ia-marketplace",
      "metadata": {
        "description": "Marketplace do FACIN_IA para distribuicao de plugin de governanca de IA.",
        "version": "1.0.0",
        "pluginRoot": "./plugins"
      },
      "owner": {
        "name": "Guttenberg Ferreira Passos"
      },
      "plugins": [
        {
          "name": "facin-ia",
          "source": "facin-ia",
          "description": "Plugin do metodo FACIN_IA com agente, skill e comando de diagnostico.",
          "version": "1.0.0"
        }
      ]
    }
    """
)

PLUGIN_JSON = _text(
    """
    {
      "name": "facin-ia",
      "description": "Plugin do metodo FACIN_IA para GitHub Copilot com agente, skill e comando de diagnostico.",
      "version": "1.0.0",
      "license": "MIT",
      "agents": [
        "./agents/facin-ia.md"
      ],
      "commands": [
        "./commands/facin-ia-diagnostico.md"
      ],
      "skills": [
        "./skills/facin-ia/"
      ]
    }
    """
)

TEMPLATE_SETUP = _text(
    """
    # FACIN_IA Template Setup

    Use este roteiro apos criar um novo repositorio a partir do template.

    ## Passos iniciais

    1. Atualize nome, descricao e mantenedores do projeto.
    2. Revise README, objetivos e escopo institucional.
    3. Ajuste agentes, prompts e skills para o contexto do novo repositorio.
    4. Defina evidencias, indicadores e papeis responsaveis.
    5. Revise os templates de issue e pull request conforme o fluxo da equipe.

    ## Validacao minima

    - GitHub Copilot habilitado no VS Code.
    - Agente FACIN_IA acessivel no chat.
    - Artefatos de especificacao e rastreabilidade revisados.
    - Riscos e controles mapeados para o contexto do projeto.
    """
)

PULL_REQUEST_TEMPLATE = _text(
    """
    ## Resumo

    - objetivo desta mudanca:
    - artefatos FACIN_IA afetados:

    ## Governanca e rastreabilidade

    - evidencia revisada:
    - risco enderecado:
    - impacto esperado:

    ## Checklist

    - [ ] especificacao atualizada quando necessario
    - [ ] criterios de aceitacao revisados
    - [ ] riscos e controles reavaliados
    - [ ] evidencias anexadas ou referenciadas
    """
)

ISSUE_TEMPLATE = _text(
    """
    ---
    name: Solicitacao FACIN_IA
    about: Solicitar diagnostico, especificacao ou adequacao de governanca de IA
    title: "[FACIN_IA] "
    labels: ["facin-ia"]
    ---

    ## Contexto

    Descreva o projeto, servico ou iniciativa.

    ## Tipo de demanda

    - diagnostico de maturidade
    - especificacao antes de codigo
    - revisao de risco e controles
    - adaptacao metodologica

    ## Evidencias disponiveis

    Liste documentos, politicas, logs, prompts, indicadores ou outros artefatos.

    ## Resultado esperado

    Descreva a saida desejada.
    """
)

ISSUE_TEMPLATE_CONFIG = _text(
    """
    blank_issues_enabled: false
    contact_links:
      - name: Diretrizes FACIN_IA
        url: ./Diretrizes%20FACIN_IA.txt
        about: Consulte as diretrizes do metodo antes de abrir uma solicitacao.
    """
)


ASSET_GROUPS = {
    "customizacao": {
        Path(".github/agents/FACIN_IA.agent.md"): FACIN_AGENT,
        Path(".github/prompts/facin-ia-diagnostico.prompt.md"): FACIN_PROMPT,
        Path(".github/skills/facin-ia/SKILL.md"): FACIN_SKILL,
        Path(".github/skills/facin-ia/metodo-facin-ia.md"): FACIN_METHOD,
        Path(".github/skills/facin-ia/template-especificacao.md"): FACIN_TEMPLATE,
        Path(".github/skills/facin-ia/checklist-avaliacao.md"): FACIN_CHECKLIST,
    },
    "plugin": {
        Path(".github/plugin/marketplace.json"): MARKETPLACE_JSON,
        Path("plugins/facin-ia/.github/plugin/plugin.json"): PLUGIN_JSON,
        Path("plugins/facin-ia/agents/facin-ia.md"): PLUGIN_AGENT,
        Path("plugins/facin-ia/commands/facin-ia-diagnostico.md"): PLUGIN_COMMAND,
        Path("plugins/facin-ia/skills/facin-ia/SKILL.md"): FACIN_SKILL,
        Path("plugins/facin-ia/skills/facin-ia/metodo-facin-ia.md"): FACIN_METHOD,
        Path("plugins/facin-ia/skills/facin-ia/template-especificacao.md"): FACIN_TEMPLATE,
        Path("plugins/facin-ia/skills/facin-ia/checklist-avaliacao.md"): FACIN_CHECKLIST,
        Path("plugins/facin-ia/README.md"): PLUGIN_README,
    },
    "template": {
        Path("TEMPLATE_SETUP.md"): TEMPLATE_SETUP,
        Path(".github/PULL_REQUEST_TEMPLATE.md"): PULL_REQUEST_TEMPLATE,
        Path(".github/ISSUE_TEMPLATE/facin-ia-adocao.md"): ISSUE_TEMPLATE,
        Path(".github/ISSUE_TEMPLATE/config.yml"): ISSUE_TEMPLATE_CONFIG,
    },
}

PROFILE_GROUPS = {
    "customizacao": ("customizacao",),
    "plugin": ("customizacao", "plugin"),
    "template-base": ("customizacao", "plugin", "template"),
}


@dataclass
class ScaffoldResult:
    written: list[Path]
    skipped: list[Path]


def available_profiles() -> tuple[str, ...]:
    return tuple(PROFILE_GROUPS)


def build_assets(profile: str) -> dict[Path, str]:
    if profile not in PROFILE_GROUPS:
        available = ", ".join(available_profiles())
        raise ValueError(f"Perfil invalido: {profile}. Perfis disponiveis: {available}.")

    assets: dict[Path, str] = {}
    for group_name in PROFILE_GROUPS[profile]:
        assets.update(ASSET_GROUPS[group_name])
    return assets


def scaffold_project(target_dir: Path, profile: str, overwrite: bool = False) -> ScaffoldResult:
    target_dir.mkdir(parents=True, exist_ok=True)
    result = ScaffoldResult(written=[], skipped=[])

    for relative_path, content in build_assets(profile).items():
        destination = target_dir / relative_path
        if destination.exists() and not overwrite:
            result.skipped.append(destination)
            continue

        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content, encoding="utf-8")
        result.written.append(destination)

    return result
