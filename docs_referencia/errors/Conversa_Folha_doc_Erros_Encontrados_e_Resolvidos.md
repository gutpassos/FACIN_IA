# Conversa_Folha_doc - Erros Encontrados e Resolvidos

Autor: Guttenberg Ferreira Passos  
Modelo LLM de referência: GPT-5.4  
Ambiente validado: figmm  
Data: 28 de março de 2026

## 1. Objetivo

Registrar achados relevantes identificados durante a documentação do projeto e a resolução adotada nesta etapa, sempre sem alterar o código original.

## 2. Registro de Achados

| ID | Achado | Impacto | Resolução adotada |
| --- | --- | --- | --- |
| ERR-01 | app.py orienta executar create_folha_db.py, mas o arquivo existente é cria_db.py | confunde operação inicial e leitura técnica | erro documentado no manual, na arquitetura e neste registro; nenhum patch aplicado ao legado |
| ERR-02 | prompt do agente OpenAI menciona colunas que não existem no schema real | eleva risco de resposta incorreta e desalinhamento semântico | divergência registrada na avaliação de maturidade, integrações e risco algorítmico |
| ERR-03 | app.py usa gpt-3.5-turbo, embora a referência do projeto documental seja GPT-5.4 | diferença entre legado e governança declarada | mantido o legado intacto e explicitado que GPT-5.4 é referência documental do projeto, não alteração do código |
| ERR-04 | a interface exige simultaneamente chaves Groq e OpenAI | reduz flexibilidade operacional e dificulta uso controlado | limitação registrada em manual, integrações e avaliação de maturidade |
| ERR-05 | cria_db.py reabre conexão SQLite em popula_tabelas e ignora a conexão recebida | desenho técnico redundante e potencial de confusão | comportamento descrito na documentação do código; nenhuma alteração no fonte |
| ERR-06 | não há política explícita de retenção, mascaramento e trilha de auditoria | lacuna de conformidade e governança | tratamento feito por recomendação formal na avaliação LGPD e no roadmap de maturidade |

## 3. Leitura de Resolução

Nesta etapa, resolver significa registrar, enquadrar, rastrear e orientar o tratamento futuro do achado, respeitando a restrição de não modificar a pasta Conversa_Folha.
