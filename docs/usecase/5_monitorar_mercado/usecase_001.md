# Monitorar Mercado - Configurar Alerta de Preço
___

**Ator Principal:** Usuário

**Interessados:**
- Usuário: Deseja receber notificações quando o preço de um ativo financeiro atingir um determinado valor.
- Sistema: Responsável por fornecer uma interface para que os usuários configurem e gerenciem alertas de preço para os ativos financeiros de seu interesse.

**Pré-condições:**
- O usuário está autenticado no sistema.
- O usuário possui uma lista de ativos financeiros de interesse.

**Pós-condições:**
- O alerta de preço é configurado no sistema e o usuário receberá notificações conforme especificado.

**Cenário Principal:**
1. O usuário acessa a seção de monitoramento de mercado ou configurações de alerta no sistema.
2. O usuário seleciona o ativo financeiro para o qual deseja configurar um alerta de preço.
3. O usuário especifica o preço alvo para o qual deseja receber uma notificação (por exemplo, preço de disparo).
4. O usuário seleciona o tipo de alerta desejado (por exemplo, quando o preço atinge ou ultrapassa o valor especificado).
5. O usuário pode opcionalmente configurar outras preferências relacionadas ao alerta, como o tipo de notificação (e-mail, SMS, notificação push), horário de notificação, entre outros.
6. O usuário confirma a configuração do alerta clicando em "Salvar" ou similar.
7. O sistema verifica se os dados fornecidos pelo usuário são válidos e se o ativo selecionado está disponível para monitoramento.
8. Se todas as verificações forem bem-sucedidas, o sistema configura o alerta de preço para o ativo especificado conforme as preferências do usuário.
9. Quando o preço do ativo atinge o valor especificado, o sistema envia uma notificação ao usuário de acordo com as preferências configuradas.

**Extensões:**
- Se o usuário desejar editar ou excluir um alerta de preço existente:
    1. O usuário acessa a lista de alertas de preço configurados.
    2. O usuário seleciona o alerta que deseja editar ou excluir.
    3. O usuário realiza as modificações desejadas ou seleciona a opção para excluir o alerta.
    4. O sistema atualiza as configurações do alerta de acordo com as ações do usuário.

**Observações:**
- Os alertas de preço são uma ferramenta importante para os investidores acompanharem o mercado e tomarem decisões oportunas com base em movimentos de preços significativos.
- O sistema deve oferecer opções flexíveis para que os usuários possam personalizar seus alertas de acordo com suas preferências e necessidades específicas.
- As notificações de alerta devem ser entregues de forma confiável e oportuna para garantir que os usuários sejam informados rapidamente sobre mudanças de preço relevantes.