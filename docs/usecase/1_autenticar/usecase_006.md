# Autenticar no Sistema - Registro de Novo Usuário
____


**Ator Principal:** Usuário

**Interessados:**
- Usuário: Deseja registrar uma nova conta no sistema para acessar suas funcionalidades.
- Sistema: Responsável por fornecer um processo seguro e eficaz de registro de novos usuários.

**Pré-condições:**
- O sistema está acessível e funcional.
- O usuário não possui uma conta registrada no sistema com o mesmo endereço de e-mail.

**Pós-condições:**
- O usuário é registrado com sucesso no sistema e pode acessar suas funcionalidades após a confirmação do registro.

**Cenário Principal:**
1. O usuário acessa a página de registro do sistema.
2. O usuário preenche o formulário de registro com as informações necessárias, incluindo nome, endereço de e-mail e senha.
3. O usuário confirma os dados inseridos e solicita o registro clicando no botão "Registrar" ou similar.
4. O sistema valida os dados fornecidos pelo usuário, verificando se o endereço de e-mail é único e se os campos obrigatórios estão preenchidos corretamente.
5. Se os dados forem válidos, o sistema registra o novo usuário e envia um e-mail de confirmação para o endereço de e-mail fornecido.
6. O usuário verifica sua caixa de entrada de e-mail e segue as instruções fornecidas no e-mail de confirmação para ativar sua conta.
7. O usuário clica no link de confirmação fornecido no e-mail, confirmando assim o registro e ativando sua conta.
8. O sistema redireciona o usuário para a página de login, onde ele pode acessar sua conta utilizando o e-mail e senha registrados.

**Extensões:**
- Se os dados fornecidos pelo usuário forem inválidos ou incompletos:
    - O sistema exibe mensagens de erro indicando quais campos precisam ser corrigidos ou preenchidos adequadamente e solicita que o usuário revise e corrija as informações antes de tentar registrar novamente.

**Observações:**
- Durante o processo de registro, é importante garantir que a senha escolhida pelo usuário atenda aos requisitos de segurança mínimos para proteger a conta contra acesso não autorizado.
- O sistema deve implementar medidas de segurança, como verificação de e-mail, para garantir que apenas usuários legítimos possam registrar novas contas e acessar as funcionalidades do sistema.
- É fundamental fornecer feedback claro e instruções detalhadas ao usuário durante todo o processo de registro para garantir uma experiência de usuário positiva e sem problemas.