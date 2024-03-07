# Modelo Conceitual Versão 2
___

1. **Usuário (User)**
   - Atributos não mudam da descrição basica.

2. **Carteira (Portfolio)**
   - Atributos não mudam da descrição basica.
   - **Valor Total (TotalValue)**: Valor total da carteira com base no último preço conhecido dos ativos.

3. **Ativo (Asset)**
   - Atributos não mudam da descrição basica.

4. **Detalhes do Ativo na Carteira (PortfolioAssetDetails)**
   - Atributos não mudam da descrição basica.

5. **Transação (Transaction)**
   - Atributos não mudam da descrição basica.

6. **Histórico de Preços do Ativo (AssetPriceHistory)**
   - **ID do Histórico (HistoryID)**: Identificador único para cada entrada histórica.
   - **ID do Ativo (AssetID)**: Chave estrangeira ligada ao ativo.
   - **Data/Hora (DateTime)**: Data e hora do registro histórico.
   - **Preço de Fechamento (ClosingPrice)**: Preço de fechamento do ativo.
   - **Preço de Abertura (OpeningPrice)**: Preço de abertura do ativo.
   - **Alta do Dia (High)**: O preço mais alto do ativo no dia.
   - **Baixa do Dia (Low)**: O preço mais baixo do ativo no dia.
   - **Volume (Volume)**: Volume negociado do ativo no dia.

7. **Projeção de Ativo (AssetProjection)**
   - **ID da Projeção (ProjectionID)**: Identificador único para cada projeção.
   - **ID do Ativo (AssetID)**: Chave estrangeira ligada ao ativo.
   - **Data da Projeção (ProjectionDate)**: Data para a qual a projeção é relevante.
   - **Preço Projetado (ProjectedPrice)**: Preço projetado para o ativo.
   - **Intervalo de Confiança (ConfidenceInterval)**: Intervalo de confiança da projeção de preço.

8. **Notificação (Notification)**
   - **ID da Notificação (NotificationID)**: Identificador único para cada notificação.
   - **ID do Usuário (UserID)**: Chave estrangeira ligada ao usuário.
   - **Mensagem (Message)**: Conteúdo da notificação.
   - **Data/Hora (DateTime)**: Data e hora em que a notificação deve ser enviada.
   - **Lida (Read)**: Se a notificação foi lida ou não.

9. **Alerta de Preço (PriceAlert)**
   - **ID do Alerta (AlertID)**: Identificador único para cada alerta de preço.
   - **ID do Usuário (UserID)**: Chave estrangeira ligada ao usuário.
   - **ID do Ativo (AssetID)**: Chave estrangeira ligada ao ativo para o qual o alerta é configurado.
   - **Preço Alvo (TargetPrice)**: Preço alvo que dispara o alerta.
   - **Direção (Direction)**: Indica se o alerta é para quando o preço fica acima ou abaixo do preço alvo.

10. **Log de Atividades (ActivityLog)**
    - **ID do Log (LogID)**: Identificador único para cada entrada de log.
    - **ID do Usuário (UserID)**: Chave estrangeira ligada ao usuário.
    - **Ação (Action)**: Descrição da ação realizada pelo usuário.
    - **Data/Hora (DateTime)**: Data e hora da ação.

11. **Preferências do Usuário (UserPreferences)**
    - **ID da Preferência (PreferenceID)**: Identificador único para as preferências do usuário.
    - **ID do Usuário (UserID)**: Chave estrangeira ligada ao usuário.
    - **Configurações (Settings)**: Configurações diversas, como idioma, formato de moeda, tema do dashboard etc.
