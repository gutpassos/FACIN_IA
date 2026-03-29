# FACIN_IA Template Setup

Este repositório pode ser usado como GitHub Template para novos projetos que já devam nascer com a base do FACIN_IA embarcada.

## Passos após criar um repositório a partir do template

1. Atualize nome, descrição, mantenedores e contexto institucional do novo projeto.
2. Revise o [README.md](README.md) e ajuste os objetivos, o escopo e a forma de adoção do FACIN_IA.
3. Revise os artefatos em `.github/agents/`, `.github/prompts/` e `.github/skills/` para refletir o novo domínio de negócio.
4. Defina evidências mínimas, indicadores, responsáveis e controles exigidos para o contexto do projeto.
5. Revise os templates de issue e pull request em `.github/` conforme o fluxo de governança da equipe.

## Fluxo recomendado para o usuário

1. Use `Use this template` no GitHub.
2. Crie o novo repositório.
3. Clone o repositório criado.
4. Abra o projeto no VS Code com GitHub Copilot habilitado.
5. Se necessário, complemente a estrutura com `facin-ia init --profile template-base`.

## Validação mínima

- o agente `FACIN_IA` deve estar disponível no chat;
- a skill `facin-ia` deve estar acessível;
- o prompt `facin-ia-diagnostico` deve estar instalado;
- os artefatos de governança e rastreabilidade devem ter sido revisados para o contexto do novo projeto.
