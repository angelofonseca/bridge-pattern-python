class ControleBasicoPlayStation:
    def __init__(self):
        self.plataforma = "PlayStation"

    def pular(self):
        print(f"[{self.plataforma}] Pressionando " f"X para pular")

    def atirar(self):
        print(f"[{self.plataforma}] Usando " f"R2 para atirar")

    def mover(self, direcao: str):
        print(
            f"[{self.plataforma}] Usando " f"Analógico Esquerdo para mover: {direcao}"
        )


class ControleBasicoXbox:
    def __init__(self):
        self.plataforma = "Xbox"

    def pular(self):
        print(f"[{self.plataforma}] Pressionando " f"A para pular")

    def atirar(self):
        print(f"[{self.plataforma}] Usando " f"RT para atirar")

    def mover(self, direcao: str):
        print(
            f"[{self.plataforma}] Usando " f"Analógico Esquerdo para mover: {direcao}"
        )


class ControleAvancadoPlayStation:

    def __init__(self):
        self.plataforma = "PlayStation"

    def pular(self):
        print(f"[{self.plataforma}] Pressionando " f"X para pular")

    def atirar(self):
        print(f"[{self.plataforma}] Usando " f"R2 para atirar")

    def mover(self, direcao: str):
        print(
            f"[{self.plataforma}] Usando " f"Analógico Esquerdo para mover: {direcao}"
        )

    def combo_especial(self):
        print(f"[{self.plataforma}] 🔥 COMBO ESPECIAL: " f"X + O + Quadrado!")


class ControleAvancadoXbox:

    def __init__(self):
        self.plataforma = "Xbox"

    def pular(self):
        print(f"[{self.plataforma}] Pressionando " f"A para pular")

    def atirar(self):
        print(f"[{self.plataforma}] Usando " f"RT para atirar")

    def mover(self, direcao: str):
        print(
            f"[{self.plataforma}] Usando " f"Analógico Esquerdo para mover: {direcao}"
        )

    def combo_especial(self):
        print(f"[{self.plataforma}] 🔥 COMBO ESPECIAL: " f"A + B + X!")


class ControleAcessibilidadePlayStation:
    def __init__(self):
        self.plataforma = "PlayStation"

    def pular(self):
        print(f"[{self.plataforma}] Pressionando " f"X para pular")

    def atirar(self):
        print(f"[{self.plataforma}] Usando " f"R2 para atirar")

    def mover(self, direcao: str):
        print(
            f"[{self.plataforma}] Usando " f"Analógico Esquerdo para mover: {direcao}"
        )

    def mira_assistida(self):
        print(f"[{self.plataforma}] ♿ MIRA ASSISTIDA: " f"R2 (auto-aim ativado)")


class ControleAcessibilidadeXbox:
    def __init__(self):
        self.plataforma = "Xbox"

    def pular(self):
        print(f"[{self.plataforma}] Pressionando " f"A para pular")

    def atirar(self):
        print(f"[{self.plataforma}] Usando " f"RT para atirar")

    def mover(self, direcao: str):
        print(
            f"[{self.plataforma}] Usando " f"Analógico Esquerdo para mover: {direcao}"
        )

    def mira_assistida(self):
        print(f"[{self.plataforma}] ♿ MIRA ASSISTIDA: " f"RT (auto-aim ativado)")


print("\n--- Cenário 1: Controle Básico em diferentes plataformas ---")

print("\n🎮 Jogador 2: Controle Básico no PlayStation")
controle_ps = ControleBasicoPlayStation()
controle_ps.mover("esquerda")
controle_ps.pular()
controle_ps.atirar()

print("\n--- Cenário 2: Controle Avançado em diferentes plataformas ---")

print("\n🎮 Jogador 3: Controle Avançado no Xbox")
controle_xbox = ControleAvancadoXbox()
controle_xbox.mover("direita")
controle_xbox.pular()
controle_xbox.combo_especial()

print("\n--- Cenário 3: Controle de Acessibilidade ---")

print("\n🎮 Jogador 6: Controle Acessível no PlayStation")
controle_acess_ps = ControleAcessibilidadePlayStation()
controle_acess_ps.mira_assistida()

print("\n--- Cenário 4: Tentativa de trocar plataforma ---")
print("\n🎮 Jogador começa no PlayStation...")
jogador = ControleAvancadoPlayStation()
jogador.pular()

print("\n🔄 Quer mudar para Xbox...")
print("❌ IMPOSSÍVEL! Precisa criar um novo objeto:")
jogador = ControleAvancadoXbox()
jogador.pular()

print("\n" + "=" * 70)
print("❌ PROBLEMAS IDENTIFICADOS:")
print("=" * 70)
print("1. EXPLOSÃO DE CLASSES:")
print("   - 3 tipos de controle × 2 plataformas = 6 classes!")
print("   - Se adicionar PC: +3 classes (9 total)")
print("   - Se adicionar Nintendo Switch: +3 classes (12 total)")
print("   - Crescimento: N controles × M plataformas classes!")
print()
print("2. DUPLICAÇÃO DE CÓDIGO:")
print("   - Lógica do 'pular' repetida em 6 lugares")
print("   - Lógica do 'atirar' repetida em 6 lugares")
print("   - Lógica do 'mover' repetida em 6 lugares")
print("   - Difícil manter: mudança em 1 requer mudança em 6")
print()
print("3. ACOPLAMENTO FORTE:")
print("   - Controle está acoplado à plataforma")
print("   - Impossível trocar plataforma em tempo de execução")
print("   - Precisa criar NOVO objeto para mudar plataforma")
print()
print("4. DIFÍCIL EXTENSÃO:")
print("   - Nova plataforma? Crie 3 classes (uma para cada controle)")
print("   - Novo controle? Crie 2 classes (uma para cada plataforma)")
print("=" * 70)
