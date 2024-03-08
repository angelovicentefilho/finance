```mermaid
flowchart TD
    A[Início] --> B(Usuário acessa opção para alterar preferências de visualização)
    B --> C{Preferências selecionadas?}
    C -->|Sim| D[Salvar preferências de visualização]
    D --> E[Tela principal do usuário]
    C -->|Não| E[Tela principal do usuário]

```