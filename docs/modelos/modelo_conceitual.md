# Modelo Conceitual Básico
_____

1. **Usuário (User)**
   - **ID do Usuário (UserID)**: Identificador único para cada usuário.
   - **Nome (Name)**: Nome do usuário.
   - **Email (Email)**: Email do usuário, utilizado para login.
   - **Senha (Password)**: Senha criptografada do usuário.

2. **Carteira (Portfolio)**
   - **ID da Carteira (PortfolioID)**: Identificador único para cada carteira.
   - **ID do Usuário (UserID)**: Chave estrangeira ligada ao usuário proprietário da carteira.
   - **Nome da Carteira (PortfolioName)**: Nome da carteira.
   - **Descrição (Description)**: Uma descrição opcional da carteira.

3. **Ativo (Asset)**
   - **ID do Ativo (AssetID)**: Identificador único para cada ativo.
   - **Nome do Ativo (AssetName)**: Nome do ativo, como Bitcoin ou Apple.
   - **Tipo do Ativo (AssetType)**: Tipo do ativo, como ação, criptomoeda, etc.
   - **Símbolo do Ativo (Ticker)**: Símbolo de mercado do ativo, como BTC ou AAPL.

4. **Detalhes do Ativo na Carteira (PortfolioAssetDetails)**
   - **ID da Carteira (PortfolioID)**: Chave estrangeira ligada à carteira.
   - **ID do Ativo (AssetID)**: Chave estrangeira ligada ao ativo.
   - **Quantidade (Quantity)**: Quantidade do ativo na carteira.
   - **Data da Compra (PurchaseDate)**: Data em que o ativo foi adicionado à carteira.
   - **Preço de Compra (PurchasePrice)**: Preço de compra do ativo.

5. **Transação (Transaction)**
   - **ID da Transação (TransactionID)**: Identificador único para cada transação.
   - **ID da Carteira (PortfolioID)**: Chave estrangeira ligada à carteira na qual a transação ocorreu.
   - **ID do Ativo (AssetID)**: Chave estrangeira ligada ao ativo transacionado.
   - **Tipo de Transação (TransactionType)**: Compra ou venda.
   - **Quantidade (Quantity)**: Quantidade do ativo transacionado.
   - **Preço (Price)**: Preço pelo qual o ativo foi transacionado.
   - **Data da Transação (TransactionDate)**: Data e hora da transação.

6. **Preço do Ativo (AssetPrice)**
   - **ID do Ativo (AssetID)**: Chave estrangeira ligada ao ativo.
   - **Data/Hora (DateTime)**: Data e hora do preço registrado.
   - **Preço de Fechamento (ClosingPrice)**: Preço de fechamento do ativo.
   - **Preço de Abertura (OpeningPrice)**: Preço de abertura do ativo.
   - **Alta do Dia (High)**: O preço mais alto do ativo no dia.
   - **Baixa do Dia (Low)**: O preço mais baixo do ativo no dia.
