# Realizar Transações - Visualizar Histórico de Transações
____

**Ator Principal:** Usuário

**Interessados:**
- Usuário: Deseja visualizar um histórico detalhado de todas as transações realizadas em sua carteira.
- Sistema: Responsável por fornecer uma interface para que os usuários visualizem e analisem seu histórico de transações.

**Pré-condições:**
- O usuário está autenticado no sistema.
- O usuário possui uma carteira criada no sistema.

**Pós-condições:**
- O usuário obtém acesso ao histórico completo de todas as transações realizadas em sua carteira.

**Cenário Principal:**
1. O usuário acessa a seção de histórico de transações no sistema.
2. O sistema exibe uma lista detalhada de todas as transações realizadas na carteira do usuário.
3. Cada transação é listada com informações como tipo de transação (compra/venda), ativo envolvido, quantidade, preço, data/hora da transação, entre outros detalhes relevantes.
4. O usuário pode interagir com a lista de transações para visualizar detalhes adicionais, filtrar transações por tipo, ativo, data, ou realizar pesquisas específicas.
5. O usuário pode navegar pelas páginas do histórico de transações para visualizar transações anteriores, se houver muitas transações para serem exibidas em uma única página.

**Extensões:**
- Se não houver transações disponíveis no histórico:
    - O sistema exibe uma mensagem indicando que não há transações disponíveis para exibição no momento.

**Observações:**
- A visualização do histórico de transações é fundamental para permitir que os usuários acompanhem e analisem suas atividades de compra e venda ao longo do tempo.
- O sistema deve fornecer uma interface clara e intuitiva para que os usuários possam acessar e analisar facilmente seu histórico de transações.
- Recursos adicionais, como a capacidade de exportar o histórico de transações para análises externas ou a geração de relatórios personalizados, podem ser considerados para aumentar a utilidade e flexibilidade da funcionalidade de visualização do histórico de transações.