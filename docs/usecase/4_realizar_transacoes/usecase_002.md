# Realizar Transações - Registrar Venda de Ativos
___

**Ator Principal:** Usuário

**Interessados:**
- Usuário: Deseja registrar uma venda de ativo financeiro de sua carteira.
- Sistema: Responsável por fornecer uma interface para que os usuários registrem transações de venda de ativos financeiros.

**Pré-condições:**
- O usuário está autenticado no sistema.
- O usuário possui uma carteira criada no sistema.
- O ativo que o usuário deseja vender está presente em sua carteira.

**Pós-condições:**
- A transação de venda é registrada no sistema e reflete a redução do ativo na carteira do usuário.

**Cenário Principal:**
1. O usuário acessa a seção de realização de transações no sistema.
2. O usuário seleciona a opção para registrar uma nova transação de venda.
3. O usuário seleciona a carteira da qual deseja vender o ativo.
4. O usuário busca ou seleciona o ativo que deseja vender.
5. O usuário especifica a quantidade do ativo que deseja vender e o preço de venda por unidade.
6. O usuário fornece informações adicionais, como a data e hora da transação.
7. O usuário confirma a transação clicando em "Registrar Venda" ou similar.
8. O sistema verifica se os dados fornecidos pelo usuário são válidos e se a quantidade de ativos disponíveis na carteira é suficiente para realizar a venda.
9. Se todas as verificações forem bem-sucedidas, o sistema registra a transação de venda na carteira do usuário, atualizando as informações de posse do ativo e os saldos da carteira.
10. O sistema exibe uma mensagem de confirmação indicando que a venda do ativo foi registrada com sucesso.

**Extensões:**
- Se os dados fornecidos pelo usuário forem inválidos ou incompletos:
    - O sistema exibe uma mensagem de erro informando ao usuário que os dados fornecidos são inválidos e solicita que o usuário revise e corrija as informações antes de tentar registrar a venda novamente.

**Observações:**
- É crucial que o sistema valide as informações fornecidas pelo usuário para garantir a precisão e integridade dos registros de transações no sistema.
- Medidas de segurança devem ser implementadas para garantir que apenas transações legítimas sejam registradas no sistema e que as informações da carteira do usuário sejam atualizadas corretamente após a realização da venda do ativo.