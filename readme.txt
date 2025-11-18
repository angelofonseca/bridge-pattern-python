1. Hierarquia de Implementação (você explicou esta)
Device (interface abstrata)
Tv, Radio (implementações concretas)
2. Hierarquia de Abstração (faltou mencionar)
RemoteControl (abstração base)
AdvancedRemoteControl (extensão da abstração)
O diferencial do Bridge:
Desacoplamento: As duas hierarquias podem evoluir independentemente
Composição sobre herança: RemoteControl contém um Device (composição), em vez de herdar dele
Flexibilidade: Você pode combinar qualquer controle com qualquer dispositivo (RemoteControl + Tv, AdvancedRemoteControl + Radio, etc.)
Explicação complementada:
"No padrão Bridge, temos duas hierarquias independentes: a hierarquia de implementação (Device e suas classes concretas como Tv e Radio) e a hierarquia de abstração (RemoteControl e suas extensões como AdvancedRemoteControl).

A interface Device define métodos abstratos que devem ser obrigatoriamente desenvolvidos pelas classes que a implementam. Cada classe concreta pode desenvolver esses métodos com suas necessidades específicas, respeitando a intenção definida pelo método.

O 'bridge' (ponte) é a composição: RemoteControl mantém uma referência a um Device, permitindo que você combine qualquer tipo de controle com qualquer tipo de dispositivo, sem precisar criar subclasses para cada combinação (evitando explosão de classes)."

Exemplo prático do benefício:
Sem Bridge, você precisaria de classes como:

TvRemoteControl
RadioRemoteControl
AdvancedTvRemoteControl
AdvancedRadioRemoteControl
Com Bridge, você tem:

2 controles × 2 dispositivos = 4 combinações possíveis com apenas 4 classes (em vez de 4 classes específicas)
Dica: Quando explicar Bridge, sempre mencione as duas hierarquias e o desacoplamento entre elas! 🎯