# Gerenciar Portfolio - Remover Ativo do Portfólio
____

**Ator Principal:** Usuário

**Interessados:**
- Usuário: Deseja remover um ativo específico de sua carteira de investimentos.
- Sistema: Responsável por fornecer uma interface para remoção segura de ativos do portfólio do usuário.

**Pré-condições:**
- O usuário está autenticado no sistema.
- O usuário possui uma carteira criada no sistema.
- O ativo que o usuário deseja remover está presente na carteira.

**Pós-condições:**
- O ativo é removido com sucesso da carteira do usuário no sistema.

**Cenário Principal:**
1. O usuário acessa a seção de gerenciamento de portfólio no sistema.
2. O usuário seleciona a carteira da qual deseja remover o ativo.
3. O sistema exibe a lista de ativos presentes na carteira.
4. O usuário seleciona o ativo que deseja remover.
5. O usuário confirma a remoção do ativo clicando em "Remover" ou similar.
6. O sistema verifica se o ativo selecionado está presente na carteira do usuário e se há quantidade suficiente para remoção.
7. Se todas as verificações forem bem-sucedidas, o sistema remove o ativo da carteira do usuário e atualiza as informações relevantes do portfólio.
8. O sistema exibe uma mensagem de confirmação indicando que o ativo foi removido com sucesso da carteira.

**Extensões:**
- Se o usuário tentar remover um ativo que não está presente na carteira:
    - O sistema exibe uma mensagem de erro informando ao usuário que o ativo não está presente na carteira e não pode ser removido.

**Observações:**
- A capacidade de remover ativos do portfólio é importante para permitir que os usuários ajustem suas carteiras conforme necessário, seja para realizar lucros, rebalancear o portfólio ou eliminar ativos não desejados.
- O sistema deve fornecer uma interface clara e intuitiva para facilitar a remoção de ativos da carteira, minimizando assim possíveis erros por parte do usuário.
- Medidas de segurança devem ser implementadas para garantir que apenas ativos presentes na carteira do usuário possam ser removidos e que as informações do portfólio sejam atualizadas corretamente após a remoção do ativo.