# Monitorar Mercado - Receber Notificações de Alertas de Preço
____

**Ator Principal:** Usuário

**Interessados:**
- Usuário: Deseja receber notificações em tempo real quando os alertas de preço configurados forem acionados.
- Sistema: Responsável por enviar notificações aos usuários quando os alertas de preço forem acionados.

**Pré-condições:**
- O usuário está autenticado no sistema.
- O usuário configurou alertas de preço para os ativos financeiros de seu interesse.
- O usuário concedeu permissão para receber notificações do sistema.

**Pós-condições:**
- O usuário recebe notificações em tempo real quando os alertas de preço configurados são acionados.

**Cenário Principal:**
1. O usuário configura um alerta de preço para um ativo financeiro específico, definindo o preço alvo e as preferências de notificação.
2. Quando o preço do ativo atinge ou ultrapassa o valor especificado no alerta de preço, o sistema detecta a condição e envia uma notificação ao usuário.
3. O usuário recebe a notificação em tempo real em seu dispositivo, conforme as preferências configuradas (por exemplo, notificação push, e-mail, SMS).
4. O usuário pode visualizar a notificação e tomar medidas apropriadas com base na mudança de preço do ativo, como realizar uma transação de compra ou venda, ajustar outros alertas de preço, ou simplesmente monitorar a situação do mercado.

**Extensões:**
- Se o usuário optar por não receber notificações de alertas de preço:
    - O sistema respeita as preferências do usuário e não envia notificações de alerta de preço, mesmo que os alertas estejam acionados.

**Observações:**
- As notificações de alertas de preço são essenciais para permitir que os usuários acompanhem o mercado e tomem decisões oportunas com base em mudanças de preço significativas.
- O sistema deve oferecer opções flexíveis para que os usuários possam configurar suas preferências de notificação, permitindo que eles recebam alertas de preço de acordo com suas necessidades e preferências individuais.
- As notificações devem ser entregues de forma confiável e oportuna para garantir que os usuários sejam informados rapidamente sobre mudanças de preço relevantes.