# Configurar Alerta de Preço
___


**Escopo:** Dashboard Financeiro

**Nível:** Objetivo do usuário

**Ator Primário:** Usuário Investidor

**Precondições:** O usuário deve estar autenticado e deve ter pelo menos uma carteira com ativos.

**Garantia de Sucesso (Pós-condições):** O alerta de preço é configurado com sucesso, e o usuário receberá notificações conforme especificado.

**Fluxo de Eventos Principais:**
1. O usuário faz login no dashboard financeiro.
2. O usuário navega até a seção de gerenciamento de alertas.
3. O sistema exibe os ativos disponíveis na carteira do usuário para os quais os alertas podem ser configurados.
4. O usuário seleciona um ativo e define um preço-alvo para o alerta.
5. O usuário seleciona o tipo de alerta (preço acima ou abaixo do preço-alvo) e define as preferências de notificação.
6. O sistema valida as informações e salva a nova configuração de alerta na tabela `PriceAlert`.
7. O sistema confirma a criação do alerta ao usuário.

**Extensões (ou Fluxos Alternativos):**
a. Se o usuário inserir um preço-alvo que não seja válido (por exemplo, um valor negativo):
   - a1. O sistema exibe uma mensagem de erro e solicita a correção.
   - a2. O usuário corrige o preço-alvo.
   - a3. O sistema valida novamente e, se correto, prossegue com a configuração do alerta.

b. Se o usuário desejar cancelar um alerta existente:
   - b1. O usuário seleciona um alerta configurado anteriormente.
   - b2. O usuário opta por cancelar o alerta.
   - b3. O sistema atualiza o status do alerta para inativo na tabela `PriceAlert`.

**Regras de Negócio Especiais:**
- Um alerta de preço deve estar sempre vinculado a um ativo específico da carteira do usuário.
- Os alertas devem ter um preço-alvo e um tipo (acima ou abaixo) definido.

**Requisitos Especiais:**
- A funcionalidade de alerta deve permitir que o usuário configure múltiplos alertas para diferentes ativos.
- A interface de usuário para configuração de alertas deve ser intuitiva e fornecer feedback claro após cada ação.

**Lista de Variações Tecnológicas e de Dados:**
- O sistema deve ser capaz de monitorar os preços dos ativos em tempo real para ativar os alertas conforme necessário.

**Frequência de Ocorrência:**
- A configuração de alertas pode não ser tão frequente quanto a verificação da performance do portfólio, mas é uma funcionalidade crítica que os usuários acessarão regularmente para gerenciar seus investimentos.
