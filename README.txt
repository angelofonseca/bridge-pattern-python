===============================================================================
Padrão BRIDGE:

1. HIERARQUIA DE IMPLEMENTAÇÃO
Define quais métodos devem existir, mas NÃO como serão implementados.

Estrutura:
  Device (interface abstrata)
    ├── Tv (implementação concreta)
    └── Radio (implementação concreta)

Explicação:
- A interface Device determina quais métodos devem ser implementados
  (is_enabled, enable, disable, get_volume, set_volume, etc.)
- Cada classe concreta (Tv, Radio) implementa esses métodos de acordo
  com sua lógica específica
- Exemplo: set_volume() na TV pode ajustar alto-falantes internos,
  enquanto no Radio pode ajustar amplificadores diferentes

2. HIERARQUIA DE ABSTRAÇÃO
Define operações de ALTO NÍVEL que DELEGAM trabalho para a implementação.

Estrutura:
  RemoteControl (abstração base)
    └── AdvancedRemoteControl (extensão da abstração)

Explicação:
- A abstração NÃO implementa a lógica dos dispositivos diretamente
- Ela MANTÉM UMA REFERÊNCIA para um objeto Device (a "ponte")
- Ela DELEGA as operações para esse Device
- Pode COMBINAR chamadas para criar comportamentos de alto nível
  Exemplo: toggle_power() verifica is_enabled() e chama enable() ou disable()

3. A "PONTE" (BRIDGE)
É a COMPOSIÇÃO entre as hierarquias:

    RemoteControl contém um Device (composição, não herança!)
    
Isso permite combinar qualquer controle com qualquer dispositivo:
    ✓ RemoteControl + Tv
    ✓ RemoteControl + Radio
    ✓ AdvancedRemoteControl + Tv
    ✓ AdvancedRemoteControl + Radio

4. O PROBLEMA QUE O BRIDGE RESOLVE

❌ SEM BRIDGE (explosão de classes):
   Para cada combinação controle-dispositivo, você precisaria de uma classe:
   
   TvRemoteControl
   RadioRemoteControl
   AdvancedTvRemoteControl
   AdvancedRadioRemoteControl
   SmartTvRemoteControl
   SmartRadioRemoteControl
   ... (crescimento exponencial!)

✅ COM BRIDGE:
   2 controles × 2 dispositivos = 4 combinações possíveis
   Usando apenas 4 classes (2 + 2), não 4 classes específicas!
   
   Adicionar novo dispositivo? → Crie apenas SmartSpeaker(Device)
   Adicionar novo controle? → Crie apenas VoiceRemoteControl(RemoteControl)
   TODAS as combinações funcionam automaticamente! 🎯

5. PRINCÍPIOS APLICADOS

✓ Desacoplamento: As duas hierarquias evoluem INDEPENDENTEMENTE
✓ Composição sobre Herança: RemoteControl CONTÉM um Device
✓ Single Responsibility: Cada classe tem UMA responsabilidade clara
✓ Open/Closed: Aberto para extensão, fechado para modificação

6. QUANDO USAR O BRIDGE

Use quando:
  • Você quer evitar vínculo permanente entre abstração e implementação
  • Tanto abstrações quanto implementações devem ser extensíveis por subclasses
  • Mudanças na implementação não devem impactar clientes
  • Você tem "explosão de classes" devido a combinações
  • Quer compartilhar implementação entre múltiplos objetos (com referência)

7. EXEMPLO PRÁTICO NO CÓDIGO

# Criar dispositivos
tv = Tv()
radio = Radio()

# Criar controles e conectar aos dispositivos (a "ponte")
remote_tv = RemoteControl(tv)           # Controle simples para TV
remote_radio = RemoteControl(radio)     # Controle simples para Rádio
advanced_tv = AdvancedRemoteControl(tv) # Controle avançado para TV

# Usar (a abstração delega para a implementação)
remote_tv.toggle_power()    # RemoteControl chama tv.enable()
remote_tv.volume_up()       # RemoteControl chama tv.set_volume()
advanced_tv.mute()          # AdvancedRemoteControl chama tv.set_volume(0)

===============================================================================