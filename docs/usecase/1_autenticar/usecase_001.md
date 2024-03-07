# Visualizar a Performance do Portfólio
____

**Escopo:** Dashboard Financeiro

**Nível:** Objetivo do usuário

**Ator Primário:** Usuário Investidor

**Precondições:** O usuário deve estar autenticado no sistema.

**Garantia de Sucesso (Pós-condições):** O usuário visualiza um relatório da performance atual de seu portfólio, incluindo a rentabilidade total, distribuição de ativos e histórico de transações.

**Fluxo de Eventos Principais:**
1. O usuário faz login no dashboard financeiro.
2. Após a autenticação bem-sucedida, o usuário seleciona a opção para visualizar seu portfólio.
3. O sistema recupera as carteiras associadas ao usuário a partir da tabela `Portfolio`.
4. Para cada carteira, o sistema recupera os detalhes dos ativos, suas quantidades e valores de aquisição da tabela `PortfolioAssetDetails`.
5. O sistema consulta o histórico de preços mais recente para cada ativo na carteira na tabela `AssetPriceHistory`.
6. Com base nos dados atuais e históricos, o sistema calcula a rentabilidade total e a distribuição dos ativos no portfólio.
7. O sistema consulta e compila o histórico de transações do usuário a partir da tabela `Transaction`.
8. O sistema apresenta um relatório consolidado ao usuário, exibindo a performance atual do portfólio, o histórico de transações e a distribuição de ativos.

**Extensões (ou Fluxos Alternativos):**
a. Se o sistema não conseguir recuperar as informações do portfólio (por exemplo, devido a um problema de conexão com a base de dados):
   - a1. O sistema exibe uma mensagem de erro.
   - a2. O sistema loga o erro na tabela `ActivityLog` para análise posterior.
   - a3. O sistema oferece ao usuário a opção de tentar novamente ou de entrar em contato com o suporte.

b. Se o usuário desejar receber notificações sobre alterações significativas de preço em ativos específicos do portfólio:
   - b1. O usuário configura um novo alerta de preço usando a interface do usuário.
   - b2. O sistema registra o alerta na tabela `PriceAlert`.
   - b3. Quando o preço do ativo atinge o ponto de disparo, o sistema notifica o usuário conforme as configurações definidas em `UserPreferences`.

**Regras de Negócio Especiais:**
- A rentabilidade é calculada como a diferença percentual entre o valor atual do ativo e seu valor de aquisição.
- A distribuição de ativos no portfólio deve ser visualmente representada, facilitando a compreensão da diversificação.

**Requisitos Especiais:**
- A interface do usuário deve ser responsiva e clara.
- Os cálculos de performance do portfólio devem ser realizados em tempo real.

**Lista de Variações Tecnológicas e de Dados:**
- Os preços dos ativos podem ser atualizados em tempo real ou através de intervalos regulares, dependendo da disponibilidade e da frequência das fontes de dados externas.

**Frequência de Ocorrência:**
- Os usuários podem verificar a performance de seus portfólios várias vezes ao dia, especialmente em dias de negociação ativos.
