# Login do usuário
___

flowchart TD
    A[Início] --> B(Usuário insere credenciais)
    B --> C{Credenciais válidas?}
    C -->|Sim| D[Usuário é autenticado no sistema]
    C -->|Não| E[Exibir mensagem de erro]
    E --> B
    D --> F{Deseja salvar informações de login?}
    F -->|Sim| G[Salvar informações de login]
    F -->|Não| H[Tela principal do sistema]
    G --> H
