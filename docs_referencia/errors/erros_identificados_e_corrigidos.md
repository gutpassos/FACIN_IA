# Erros Identificados e Corrigidos no Projeto Conversa_Folha_doc

## 1. Finalidade do registro

Este documento consolida os principais problemas identificados ao longo da estruturação do projeto e as respectivas correções aplicadas. O objetivo é preservar rastreabilidade técnica e evidenciar a evolução da solução.

## 2. Problemas técnicos corrigidos

### 2.1 Referência incorreta ao script de criação do banco

Problema identificado:

- a aplicação fazia referência incorreta ao processo de preparação do banco.

Correção aplicada:

- o fluxo e a orientação ao usuário foram ajustados em [app.py](app.py) para refletir corretamente o uso de [cria_db.py](cria_db.py).

### 2.2 Inconsistência na configuração do modelo OpenAI

Problema identificado:

- a configuração anterior não refletia o modelo solicitado para o projeto documental.

Correção aplicada:

- o modelo de referência foi alinhado para GPT-5.4 na configuração e na documentação.

### 2.3 Reconexão desnecessária ao banco em processo de carga

Problema identificado:

- o script de criação do banco reabria conexão de forma desnecessária durante a carga de dados.

Correção aplicada:

- o fluxo de [cria_db.py](cria_db.py) foi ajustado para reutilizar adequadamente a conexão.

### 2.4 Ausência inicial de documentação estruturada

Problema identificado:

- o projeto original não possuía um pacote documental consolidado em múltiplos formatos.

Correção aplicada:

- foi criada a estrutura `spec/`, `docs/`, `errors/` e o script [scripts/generate_artifacts.py](scripts/generate_artifacts.py) para geração automatizada de artefatos.

## 3. Lacunas de qualidade corrigidas

### 3.1 Ausência de testes automatizados

Problema identificado:

- não havia cobertura mínima automatizada para componentes críticos.

Correção aplicada:

- foram criados testes com pytest para governança, criação do banco e geração documental.

### 3.2 Ausência de pipeline de integração contínua

Problema identificado:

- o projeto não possuía validação automatizada em repositório.

Correção aplicada:

- foi criado o workflow [ci.yml](.github/workflows/ci.yml) com validação de sintaxe e execução dos testes.

## 4. Lacunas de governança corrigidas

### 4.1 Ausência de observabilidade sobre uso de modelos

Problema identificado:

- não havia rastreamento de prompts, latência, custo estimado, volume textual e falhas.

Correção aplicada:

- foi criado o módulo [governance_controls.py](governance_controls.py) com trilha local de observabilidade.

### 4.2 Controles insuficientes de acesso

Problema identificado:

- a aplicação permitia uso sem identificação mínima e sem mecanismo opcional de restrição local.

Correção aplicada:

- foram introduzidos identificação mínima do usuário, aceite explícito de ciência e suporte a código de acesso local por variável de ambiente.

### 4.3 Controles insuficientes de auditoria

Problema identificado:

- não havia trilha adequada de eventos relevantes de uso.

Correção aplicada:

- foram implementados registros locais de acesso, interações e respostas associadas à sessão.

### 4.4 Falta de transparência ao usuário

Problema identificado:

- a interface não deixava suficientemente claro o caráter assistido por IA e a necessidade de validação humana.

Correção aplicada:

- foram adicionados avisos explícitos na interface e reforço documental sobre limites, supervisão humana e uso responsável.

### 4.5 Risco de consultas SQL inadequadas

Problema identificado:

- a ausência de validação restritiva ampliava o risco de uso indevido de consultas geradas.

Correção aplicada:

- a execução passou a aceitar apenas consultas SELECT compatíveis com regras de segurança definidas no módulo de governança.

## 5. Lacunas regulatórias e de responsabilidade tratadas documentalmente

### 5.1 Ausência de seção de conformidade com LGPD

Problema identificado:

- a documentação anterior não tratava de forma explícita finalidade, minimização, rastreabilidade e responsabilidade sobre dados.

Correção aplicada:

- foram adicionadas seções específicas de LGPD nos documentos executivos, técnicos, de maturidade e de governança.

### 5.2 Ausência de seção de risco algorítmico

Problema identificado:

- a documentação anterior não explicitava riscos de erro, interpretação inadequada ou confiança indevida em saídas automatizadas.

Correção aplicada:

- foram incluídas seções específicas de risco algorítmico com medidas mitigadoras e reforço de validação humana.

## 6. Problema editorial corrigido

### 6.1 Redação parcialmente em ASCII sem acentuação plena

Problema identificado:

- parte dos documentos estava redigida em português sem acentuação completa, reduzindo qualidade editorial e acabamento final.

Correção aplicada:

- a documentação foi revisada de ponta a ponta para adoção consistente de português do Brasil com acentuação completa.

## 7. Resultado consolidado

Após as correções, o projeto passou a apresentar:

- documentação estruturada e multilíngue de formatos;
- testes automatizados e pipeline de CI;
- trilhas locais de auditoria e observabilidade;
- controles mínimos de acesso e transparência;
- tratamento explícito de LGPD e risco algorítmico;
- melhoria editorial integral em português do Brasil.

Esse conjunto de correções sustenta a elevação do projeto para um patamar mais robusto de qualidade, governança e maturidade.