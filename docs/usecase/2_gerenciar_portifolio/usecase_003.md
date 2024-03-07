# Gerenciar Portfólio - Excluir Carteira
___


**Ator Principal:** Usuário

**Interessados:**
- Usuário: Deseja excluir uma carteira existente que não é mais necessária em seu portfólio.
- Sistema: Responsável por fornecer uma interface para exclusão segura de carteiras de ativos financeiros.

**Pré-condições:**
- O usuário está autenticado no sistema.
- A carteira que o usuário deseja excluir existe e está associada à sua conta.

**Pós-condições:**
- A carteira é excluída do sistema e todos os ativos associados a ela são removidos.

**Cenário Principal:**
1. O usuário acessa a seção de gerenciamento de portfólio no sistema.
2. O usuário visualiza a lista de suas carteiras e seleciona a carteira que deseja excluir.
3. O sistema exibe uma confirmação de exclusão, solicitando ao usuário que confirme a exclusão da carteira.
4. O usuário confirma a exclusão clicando em "Excluir" ou similar.
5. O sistema verifica se a carteira não possui ativos associados a ela.
6. Se a carteira estiver vazia, o sistema exclui a carteira e todas as informações relacionadas a ela.
7. O sistema exibe uma mensagem de confirmação indicando que a carteira foi excluída com sucesso.

**Extensões:**
- Se a carteira contiver ativos associados a ela:
    - O sistema exibe uma mensagem de erro informando ao usuário que a carteira não pode ser excluída porque ainda contém ativos associados a ela. O usuário é solicitado a remover os ativos da carteira antes de tentar excluí-la novamente.

**Observações:**
- A exclusão de uma carteira deve ser tratada com cuidado, pois pode resultar na perda permanente de dados. Portanto, é importante que o sistema forneça uma confirmação explícita e que o usuário tenha a oportunidade de revisar e confirmar a exclusão antes que ela seja executada.
- Medidas de segurança devem ser implementadas para garantir que apenas usuários autorizados possam excluir carteiras e que a exclusão seja realizada de forma segura, sem comprometer outros dados no sistema.