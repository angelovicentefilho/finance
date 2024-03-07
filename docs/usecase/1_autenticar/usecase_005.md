# Autenticar no Sistema - Recuperação de Senha
___


**Ator Principal:** Usuário

**Interessados:**
- Usuário: Deseja recuperar o acesso à sua conta se esquecer sua senha.
- Sistema: Responsável por fornecer um processo seguro e eficaz de recuperação de senha para os usuários.

**Pré-condições:**
- O usuário possui uma conta registrada no sistema.
- O usuário esqueceu sua senha de acesso.

**Pós-condições:**
- O usuário recebe instruções para recuperar sua senha.
- O usuário pode acessar sua conta utilizando a nova senha.

**Cenário Principal:**
1. O usuário acessa a página de login do sistema.
2. O usuário identifica e clica no link ou botão de "Esqueceu a senha?" na página de login.
3. O sistema redireciona o usuário para a página de recuperação de senha.
4. O usuário fornece informações necessárias para iniciar o processo de recuperação de senha (por exemplo, endereço de e-mail registrado).
5. O sistema valida as informações fornecidas pelo usuário.
6. Se as informações forem válidas, o sistema envia um e-mail para o endereço registrado do usuário com instruções para redefinir a senha.
7. O usuário verifica sua caixa de entrada de e-mail e segue as instruções fornecidas no e-mail recebido.
8. O usuário acessa o link fornecido no e-mail para confirmar a solicitação de recuperação de senha e iniciar o processo de redefinição de senha.
9. O usuário insere uma nova senha e confirma a alteração.
10. O sistema atualiza a senha do usuário com a nova senha fornecida.
11. O sistema redireciona o usuário para a página de login, onde ele pode acessar sua conta utilizando a nova senha.

**Extensões:**
- Se as informações fornecidas pelo usuário para iniciar o processo de recuperação de senha forem inválidas:
    - O sistema exibe uma mensagem de erro informando ao usuário que as informações fornecidas não correspondem aos registros do sistema e solicita que o usuário verifique as informações e tente novamente.

**Observações:**
- É importante que o processo de recuperação de senha seja seguro e protegido contra acesso não autorizado, por exemplo, através de confirmação por e-mail ou outras formas de verificação de identidade.
- O sistema deve fornecer feedback claro e instruções detalhadas durante todo o processo de recuperação de senha para garantir que o usuário possa seguir facilmente os passos necessários para recuperar o acesso à sua conta.