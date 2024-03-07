# Gerenciar Portfólio - Editar Detalhes da Carteira
____

**Ator Principal:** Usuário

**Interessados:**
- Usuário: Deseja editar os detalhes de uma carteira existente para atualizar informações ou corrigir erros.
- Sistema: Responsável por fornecer uma interface para edição de detalhes de carteiras de ativos financeiros.

**Pré-condições:**
- O usuário está autenticado no sistema.
- A carteira que o usuário deseja editar existe e está associada à sua conta.

**Pós-condições:**
- Os detalhes da carteira são atualizados conforme as alterações feitas pelo usuário.

**Cenário Principal:**
1. O usuário acessa a seção de gerenciamento de portfólio no sistema.
2. O usuário visualiza a lista de suas carteiras e seleciona a carteira que deseja editar.
3. O sistema exibe os detalhes atuais da carteira, como nome e descrição.
4. O usuário modifica os detalhes da carteira conforme desejado.
5. O usuário confirma as alterações clicando em "Salvar" ou similar.
6. O sistema valida as alterações feitas pelo usuário, garantindo que o nome da carteira seja único e que todos os campos obrigatórios estejam preenchidos corretamente.
7. Se as alterações forem válidas, o sistema atualiza os detalhes da carteira com as novas informações fornecidas pelo usuário.
8. O sistema exibe uma mensagem de confirmação indicando que as alterações foram salvas com sucesso.

**Extensões:**
- Se o usuário tentar alterar o nome da carteira para um nome que já está em uso:
    - O sistema exibe uma mensagem de erro informando ao usuário que o nome da carteira já está em uso e solicita que o usuário escolha um nome diferente.

**Observações:**
- É importante permitir que o usuário edite os detalhes de suas carteiras para manter as informações atualizadas e precisas.
- O sistema deve fornecer feedback claro e instruções detalhadas durante todo o processo de edição de detalhes da carteira para garantir uma experiência de usuário positiva.
- Medidas de segurança devem ser implementadas para garantir que apenas usuários autenticados possam editar detalhes das carteiras associadas às suas contas.