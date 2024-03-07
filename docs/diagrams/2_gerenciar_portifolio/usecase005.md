
```mermaid
flowchart TD
    A[Início] --> B(Usuário seleciona opção para adicionar ativo)
    B --> C{Ativo selecionado?}
    C -->|Sim| D[Definir quantidade e preço do ativo]
    D --> E{Informações válidas?}
    E -->|Sim| F[Adicionar ativo ao portfólio]
    F --> G[Atualizar portfólio]
    G --> H[Tela principal do portfólio]
    E -->|Não| I[Exibir mensagem de erro]
    I --> D
    C -->|Não| H[Tela principal do portfólio]
```
