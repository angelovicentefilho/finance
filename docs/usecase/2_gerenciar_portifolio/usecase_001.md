# Gerenciar Portfólio - Criar uma Nova Carteira
____

**Ator Principal:** Usuário

**Interessados:**
- Usuário: Deseja criar uma nova carteira para gerenciar seus ativos financeiros.
- Sistema: Responsável por fornecer uma interface para criação e gerenciamento de carteiras de ativos financeiros.

**Pré-condições:**
- O usuário está autenticado no sistema.
- O usuário não possui uma carteira com o mesmo nome.

**Pós-condições:**
- Uma nova carteira é criada e associada ao usuário, pronta para adicionar ativos financeiros.

**Cenário Principal:**
1. O usuário acessa a seção de gerenciamento de portfólio no sistema.
2. O usuário seleciona a opção de "Criar Nova Carteira".
3. O sistema exibe um formulário para o usuário preencher os detalhes da nova carteira, como nome e descrição opcional.
4. O usuário preenche os detalhes da carteira conforme desejado.
5. O usuário confirma a criação da nova carteira clicando em "Criar" ou similar.
6. O sistema valida os dados fornecidos pelo usuário, garantindo que o nome da carteira seja único e que todos os campos obrigatórios estejam preenchidos.
7. Se os dados forem válidos, o sistema cria a nova carteira e a associa ao usuário.
8. O sistema exibe uma mensagem de confirmação indicando que a carteira foi criada com sucesso.

**Extensões:**
- Se o usuário tentar criar uma carteira com um nome que já está em uso:
    - O sistema exibe uma mensagem de erro informando ao usuário que o nome da carteira já está em uso e solicita que o usuário escolha um nome diferente.

**Observações:**
- É importante permitir que o usuário forneça uma descrição opcional ao criar uma nova carteira para ajudar na organização e identificação das carteiras no futuro.
- O sistema deve fornecer feedback claro e instruções detalhadas durante todo o processo de criação de uma nova carteira para garantir uma experiência de usuário positiva.
- Medidas de segurança devem ser implementadas para garantir que apenas usuários autenticados possam criar novas carteiras e que o nome da carteira seja único para evitar conflitos.