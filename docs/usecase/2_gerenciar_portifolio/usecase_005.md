# Gerenciar Portfolio - Adicionar Ativo ao Portfólio
___

**Ator Principal:** Usuário

**Interessados:**
- Usuário: Deseja adicionar um novo ativo ao seu portfólio de investimentos.
- Sistema: Responsável por fornecer uma interface para adicionar ativos ao portfólio e atualizar as informações relevantes do portfólio.

**Pré-condições:**
- O usuário está autenticado no sistema.
- O usuário possui uma carteira criada no sistema.

**Pós-condições:**
- O novo ativo é adicionado à carteira do usuário no sistema.

**Cenário Principal:**
1. O usuário acessa a seção de gerenciamento de portfólio no sistema.
2. O usuário seleciona a carteira à qual deseja adicionar o novo ativo.
3. O usuário busca o ativo que deseja adicionar, utilizando filtros de pesquisa, ou insere manualmente informações sobre o ativo, como nome ou símbolo.
4. O sistema exibe uma lista de resultados correspondentes à busca do usuário, contendo informações relevantes sobre os ativos encontrados.
5. O usuário seleciona o ativo que deseja adicionar à carteira.
6. O usuário especifica a quantidade do ativo que deseja adicionar à carteira e, opcionalmente, o valor médio de aquisição.
7. O usuário confirma a adição do ativo à carteira clicando em "Adicionar" ou similar.
8. O sistema verifica se as informações fornecidas pelo usuário são válidas e se há disponibilidade suficiente na carteira para adicionar o ativo.
9. Se todas as verificações forem bem-sucedidas, o sistema adiciona o novo ativo à carteira do usuário e atualiza as informações relevantes do portfólio.
10. O sistema exibe uma mensagem de confirmação indicando que o ativo foi adicionado com sucesso à carteira.

**Extensões:**
- Se o usuário tentar adicionar um ativo que não está disponível ou não existe:
    - O sistema exibe uma mensagem de erro informando ao usuário que o ativo não pôde ser encontrado ou adicionado à carteira.

**Observações:**
- A capacidade de adicionar novos ativos ao portfólio é fundamental para permitir que os usuários atualizem e ajustem suas carteiras de acordo com suas estratégias de investimento.
- O sistema deve fornecer uma interface intuitiva e eficiente para facilitar a busca, seleção e adição de ativos às carteiras dos usuários.
- É importante que o sistema valide as informações fornecidas pelo usuário para garantir a integridade e consistência dos dados do portfólio.