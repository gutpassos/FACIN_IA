# Governança MRO e Matriz RACI do Projeto Conversa_Folha_doc

Autor: Guttenberg Ferreira Passos  
Contexto institucional de referência: PRODEMGE  
Abordagem de governança: MRO para soluções com IA

## 1. Finalidade do documento

Este documento apresenta a estrutura de governança proposta para o projeto Conversa_Folha_doc com base no contexto de implantação responsável de soluções de inteligência artificial, considerando o modelo de governança observado no MRO da PRODEMGE e as evidências disponibilizadas na pasta `evidencias`.

O objetivo é demonstrar que o projeto não apenas possui capacidade funcional, mas também incorpora papéis, responsabilidades, controles e mecanismos mínimos de prestação de contas, transparência e mitigação de riscos.

## 2. Contexto de governança

O projeto foi reposicionado para refletir preocupações típicas de governança pública e corporativa em IA, especialmente:

- responsabilidade sobre o uso da solução;
- clareza de papéis ao longo do ciclo de vida;
- transparência para usuários;
- rastreabilidade de decisões e interações;
- mitigação de riscos de uso indevido, erro e interpretação automatizada;
- aderência progressiva a conformidade regulatória e institucional.

No cenário atual, Guttenberg Ferreira Passos atua como engenheiro de IA responsável pela implementação técnica e pela consolidação documental do projeto, ao mesmo tempo em que o documento reconhece a necessidade de papéis adicionais para uma operação institucional plena.

## 3. Premissas adotadas

Para fins desta matriz e desta proposta de governança, foram consideradas as seguintes premissas:

1. O projeto ainda opera em contexto controlado e não em produção corporativa plena.
2. Há um responsável técnico principal pela solução.
3. O uso de IA exige supervisão humana e validação das saídas.
4. A solução deve evoluir com controles de acesso, auditoria, observabilidade, conformidade e gestão de riscos.
5. A governança precisa ser documentada mesmo quando parte dos papéis ainda não estiver institucionalmente formalizada.

## 4. Papéis considerados

Foram considerados os seguintes papéis de referência:

- Engenheiro de IA: responsável técnico pela construção, integração, manutenção e evolução da solução.
- Gestor do produto ou patrocinador de negócio: responsável pelo direcionamento funcional e pela validação de valor.
- Usuário de negócio: responsável por utilizar a solução dentro do escopo previsto e validar o resultado no processo de trabalho.
- Segurança da informação: responsável por orientar controles de acesso, registro, proteção e uso adequado.
- Privacidade e jurídico: responsável por orientar conformidade LGPD, finalidade, tratamento de dados e salvaguardas regulatórias.
- Governança corporativa ou comitê de IA: responsável por acompanhamento, priorização e diretrizes de adoção responsável.
- Operações ou sustentação: responsável por monitoramento, continuidade e suporte operacional.

## 5. Matriz RACI

Legenda:

- R: responsável pela execução.
- A: autoridade final e accountable.
- C: consultado.
- I: informado.

| Atividade | Engenheiro de IA | Gestor de negócio | Usuário de negócio | Segurança da informação | Privacidade/Jurídico | Governança/Comitê de IA | Operações/Sustentação |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Definir objetivo e escopo da solução | R | A | C | I | I | C | I |
| Definir dados e fontes autorizadas | R | A | C | C | C | I | I |
| Implementar aplicação e integrações | R | I | I | C | I | I | C |
| Configurar modelos e prompts | R | C | I | I | I | C | I |
| Implementar controles de acesso | R | I | I | A | C | C | C |
| Implementar trilha de auditoria | R | I | I | A | C | C | C |
| Implementar observabilidade | R | I | I | C | I | C | A |
| Avaliar conformidade LGPD | C | I | I | C | A | I | I |
| Avaliar risco algorítmico | R | C | I | C | C | A | I |
| Validar aderência ao uso de negócio | C | A | R | I | I | C | I |
| Homologar solução para uso controlado | R | A | C | C | C | C | I |
| Monitorar incidentes e falhas | C | I | I | C | I | I | A |
| Revisar evolução de maturidade | R | C | I | C | C | A | I |

## 6. Interpretação da matriz

A matriz evidencia que o projeto não deve depender exclusivamente do executor técnico quando evoluir para contexto institucional. No estágio atual, o Engenheiro de IA acumula responsabilidades relevantes, mas a governança adequada demanda distribuição de autoridade entre áreas de negócio, segurança, privacidade, operação e instâncias colegiadas.

Esse ponto é especialmente importante para evitar fragilidade organizacional, concentração excessiva de decisão técnica e ausência de segregação de funções.

## 7. Controles implementados em resposta às lacunas identificadas

Com base na avaliação anterior do projeto, foram tratados os seguintes pontos:

### 7.1 Ausência de testes automatizados e pipeline

Correção implementada:

- criação de testes automatizados com pytest;
- criação de pipeline CI no GitHub Actions.

### 7.2 Ausência de observabilidade de prompts, latência, custo e falhas

Correção implementada:

- criação de trilha de observabilidade local;
- registro de modelo, duração, estimativas de tokens, custo e erro.

### 7.3 Controles insuficientes de risco, transparência, acesso e auditoria

Correção implementada:

- identificação mínima do usuário;
- aceite explícito de uso assistido por IA;
- opção de código de acesso local;
- trilha de auditoria de eventos;
- mensagens de transparência ao usuário;
- validação restritiva de SQL;
- documentação de riscos e limites.

## 8. Conformidade com LGPD na ótica de governança

Sob a ótica de governança, a solução passou a explicitar:

- finalidade de uso declarada;
- minimização de dados coletados na interface;
- necessidade de rastreabilidade;
- necessidade de supervisão humana;
- recomendação de avaliação institucional de base legal e retenção em cenário produtivo.

Isso não substitui uma avaliação formal de impacto à proteção de dados, mas já posiciona o projeto com maior responsabilidade documental e operacional.

## 9. Risco algorítmico na ótica do MRO

O risco algorítmico foi tratado como elemento de governança e não apenas como tema técnico. Foram reconhecidos riscos de:

- resposta incorreta;
- inferência inadequada;
- uso fora de contexto;
- dependência indevida de automação;
- interpretação equivocada por usuários.

As contramedidas adotadas combinam documentação, transparência, validação humana, trilhas de auditoria e delimitação técnica do escopo da solução.

## 10. Evidências consideradas

Foram consideradas evidências do próprio projeto e materiais disponibilizados em `evidencias`, bem como referências de implementação de governança MRO informadas durante a elaboração documental.

As evidências sustentam a narrativa de que:

- houve capacitação em IA aplicada;
- houve preocupação com governança pública e corporativa;
- a solução foi evoluída para além de um protótipo técnico simples.

## 11. Conclusão

O projeto Conversa_Folha_doc passou a apresentar uma estrutura de responsabilização mais clara, compatível com um cenário de adoção responsável de IA em contexto organizacional controlado.

Embora ainda existam lacunas para institucionalização plena, a inclusão da matriz RACI, dos controles de auditoria, observabilidade, transparência, LGPD e risco algorítmico fortalece substancialmente o projeto sob a ótica do MRO e da governança aplicada à inteligência artificial.