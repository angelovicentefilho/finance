# Autenticar no Sistema - Login de Usuário
___

**Ator Principal:** Usuário investidor

**Interessados:**
- Usuário: Quer acessar o sistema utilizando suas credenciais de login.
- Sistema: Responsável por autenticar o usuário e conceder acesso às funcionalidades do sistema.

**Pré-condições:**
- O sistema está em funcionamento.
- O usuário possui credenciais válidas para acesso (nome de usuário e senha).

**Pós-condições:**
- Se as credenciais forem válidas, o usuário é autenticado e pode acessar as funcionalidades do sistema.
- Se as credenciais forem inválidas, uma mensagem de erro é exibida, e o usuário é solicitado a tentar novamente ou a recuperar sua senha.

**Cenário Principal:**
1. O usuário acessa a página inicial do sistema.
2. O sistema exibe os campos para entrada das credenciais de login (nome de usuário e senha).
3. O usuário insere seu nome de usuário e senha nos campos correspondentes.
4. O usuário solicita a autenticação ao clicar no botão de "Entrar" ou similar.
5. O sistema verifica se as credenciais fornecidas são válidas.
6. Se as credenciais forem válidas, o sistema autentica o usuário e redireciona para a página principal do sistema.
7. Se as credenciais forem inválidas, o sistema exibe uma mensagem de erro informando que as credenciais estão incorretas e solicita que o usuário tente novamente.

**Extensões:**
- Se o usuário esquecer sua senha:
    1. O usuário clica no link ou botão de "Esqueceu a senha?" na página de login.
    2. O sistema redireciona o usuário para a página de recuperação de senha.
    3. O usuário fornece informações necessárias para recuperar a senha (por exemplo, endereço de e-mail registrado).
    4. O sistema envia instruções de recuperação para o e-mail do usuário.
    5. O usuário segue as instruções fornecidas para redefinir sua senha e, em seguida, tenta fazer login novamente.

**Observações:**
- A autenticação deve ser feita de forma segura, utilizando técnicas como criptografia de senha e proteção contra ataques de força bruta.
- É importante fornecer mensagens de erro claras e orientadoras para ajudar o usuário a resolver problemas de autenticação.
- Medidas adicionais de segurança, como autenticação de dois fatores, podem ser implementadas para fortalecer a segurança do processo de login.