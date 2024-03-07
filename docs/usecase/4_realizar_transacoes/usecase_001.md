# Realizar Transações - Registrar Compra de Ativo
____

**Ator Principal:** Usuário

**Interessados:**
- Usuário: Deseja registrar uma compra de ativo financeiro em sua carteira.
- Sistema: Responsável por fornecer uma interface para que os usuários registrem transações de compra de ativos financeiros.

**Pré-condições:**
- O usuário está autenticado no sistema.
- O usuário possui uma carteira criada no sistema.
- O ativo que o usuário deseja comprar está disponível e pode ser adicionado à carteira.

**Pós-condições:**
- A transação de compra é registrada no sistema e reflete a posse do ativo na carteira do usuário.

**Cenário Principal:**
1. O usuário acessa a seção de realização de transações no sistema.
2. O usuário seleciona a opção para registrar uma nova transação de compra.
3. O usuário seleciona a carteira na qual deseja registrar a compra do ativo.
4. O usuário busca ou seleciona o ativo que deseja comprar.
5. O usuário especifica a quantidade do ativo que deseja comprar e o preço de compra por unidade.
6. O usuário fornece informações adicionais, se necessário, como a data e hora da transação.
7. O usuário confirma a transação clicando em "Registrar Compra" ou similar.
8. O sistema verifica se os dados fornecidos pelo usuário são válidos e se há fundos suficientes disponíveis na carteira para realizar a compra.
9. Se todas as verificações forem bem-sucedidas, o sistema registra a transação de compra na carteira do usuário, atualizando as informações de posse do ativo e os saldos da carteira.
10. O sistema exibe uma mensagem de confirmação indicando que a compra do ativo foi registrada com sucesso.

**Extensões:**
- Se os dados fornecidos pelo usuário forem inválidos ou incompletos:
    - O sistema exibe uma mensagem de erro informando ao usuário que os dados fornecidos são inválidos e solicita que o usuário revise e corrija as informações antes de tentar registrar a compra novamente.

**Observações:**
- É importante que o sistema valide as informações fornecidas pelo usuário para garantir a integridade e precisão dos registros de transações no sistema.
- Medidas de segurança devem ser implementadas para garantir que apenas transações legítimas sejam registradas no sistema e que as informações da carteira do usuário sejam atualizadas corretamente após a realização da compra do ativo.