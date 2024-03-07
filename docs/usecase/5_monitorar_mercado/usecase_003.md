# Monitorar Mercado - Cancelar ou Editar Alerta de Preço
____

**Ator Principal:** Usuário

**Interessados:**
- Usuário: Deseja cancelar ou editar um alerta de preço previamente configurado para um ativo financeiro.
- Sistema: Responsável por fornecer uma interface para que os usuários possam cancelar ou editar seus alertas de preço.

**Pré-condições:**
- O usuário está autenticado no sistema.
- O usuário possui pelo menos um alerta de preço previamente configurado.

**Pós-condições:**
- O alerta de preço é cancelado ou editado conforme as ações do usuário.

**Cenário Principal:**
1. O usuário acessa a seção de monitoramento de mercado ou configurações de alerta no sistema.
2. O sistema exibe uma lista de todos os alertas de preço configurados pelo usuário.
3. O usuário localiza o alerta de preço que deseja cancelar ou editar.
4. O usuário seleciona a opção para cancelar ou editar o alerta.
5. Se o usuário selecionar editar:
    1. O sistema permite que o usuário faça as alterações desejadas no alerta, como ajustar o preço alvo ou o tipo de alerta.
    2. O usuário confirma as alterações clicando em "Salvar" ou similar.
6. Se o usuário selecionar cancelar:
    - O sistema confirma a ação com o usuário e, em seguida, cancela o alerta de preço selecionado.

**Extensões:**
- Se o usuário decidir não cancelar ou editar o alerta de preço:
    - O sistema mantém as configurações do alerta inalteradas e retorna à visualização dos alertas de preço.

**Observações:**
- Permitir que os usuários cancelem ou editem alertas de preço é essencial para garantir que eles possam ajustar suas configurações de monitoramento de mercado de acordo com suas necessidades e preferências em constante mudança.
- O sistema deve fornecer uma interface fácil de usar que permita aos usuários cancelar ou editar seus alertas de preço de forma rápida e intuitiva.
- É importante que o sistema confirme todas as ações de cancelamento ou edição com o usuário para evitar ações acidentais e garantir uma experiência de usuário segura e satisfatória.