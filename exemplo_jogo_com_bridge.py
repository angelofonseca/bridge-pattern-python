from abc import ABC, abstractmethod


class Plataforma(ABC):
    @abstractmethod
    def input_pular(self) -> str:
        pass

    @abstractmethod
    def input_atirar(self) -> str:
        pass

    @abstractmethod
    def input_mover(self) -> str:
        pass

    @abstractmethod
    def input_especial(self) -> str:
        pass

    @abstractmethod
    def get_nome(self) -> str:
        pass


class PlayStation(Plataforma):
    def input_pular(self) -> str:
        return "X"

    def input_atirar(self) -> str:
        return "R2"

    def input_mover(self) -> str:
        return "Analógico Esquerdo"

    def input_especial(self) -> str:
        return "X + O + Quadrado"

    def get_nome(self) -> str:
        return "PlayStation"


class Xbox(Plataforma):
    def input_pular(self) -> str:
        return "A"

    def input_atirar(self) -> str:
        return "RT"

    def input_mover(self) -> str:
        return "Analógico Esquerdo"

    def input_especial(self) -> str:
        return "A + B + X"

    def get_nome(self) -> str:
        return "Xbox"


class Controle:
    def __init__(self, plataforma: Plataforma):
        self.plataforma = plataforma

    def pular(self):
        print(
            f"[{self.plataforma.get_nome()}] Pressionando "
            f"{self.plataforma.input_pular()} para pular"
        )

    def atirar(self):
        print(
            f"[{self.plataforma.get_nome()}] Usando "
            f"{self.plataforma.input_atirar()} para atirar"
        )

    def mover(self, direcao: str):
        print(
            f"[{self.plataforma.get_nome()}] Usando "
            f"{self.plataforma.input_mover()} para mover: {direcao}"
        )


class ControleAvancado(Controle):
    def combo_especial(self):
        print(
            f"[{self.plataforma.get_nome()}] 🔥 COMBO ESPECIAL: "
            f"{self.plataforma.input_especial()}!"
        )


class ControleAcessibilidade(Controle):
    def mira_assistida(self):
        print(
            f"[{self.plataforma.get_nome()}] ♿ MIRA ASSISTIDA: "
            f"{self.plataforma.input_atirar()} (auto-aim ativado)"
        )


ps = PlayStation()
xbox = Xbox()

print("\n--- Cenário 1: Controle Básico em diferentes plataformas ---")

print("\n🎮 Jogador 2: Controle Básico no PlayStation")
controle_ps = Controle(ps)
controle_ps.mover("esquerda")
controle_ps.pular()
controle_ps.atirar()

print("\n--- Cenário 2: Controle Avançado em diferentes plataformas ---")

print("\n🎮 Jogador 3: Controle Avançado no Xbox")
controle_xbox = ControleAvancado(xbox)
controle_xbox.mover("direita")
controle_xbox.pular()
controle_xbox.combo_especial()

print("\n--- Cenário 3: Controle de Acessibilidade ---")

print("\n🎮 Jogador 6: Controle Acessível no PlayStation")
controle_acess_ps = ControleAcessibilidade(ps)
controle_acess_ps.mira_assistida()

print("\n--- Cenário 4: Flexibilidade - Trocar plataforma ---")
print("\n🎮 Jogador começa no PlayStation...")
jogador = ControleAvancado(ps)
jogador.pular()

print("\n🔄 Mudando para Xbox...")
jogador.plataforma = xbox
jogador.pular()

print("\n" + "=" * 70)
print("✅ BENEFÍCIOS DO PADRÃO BRIDGE:")
print("=" * 70)
print("1. SEM EXPLOSÃO DE CLASSES:")
print("   - 3 controles + 4 plataformas = 7 classes")
print("   - Sem Bridge seriam: 3 × 4 = 12 classes!")
print("   - Economia: 12 - 7 = 5 classes a menos")
print()
print("2. FACILIDADE DE EXTENSÃO:")
print("   - Nova plataforma? +1 classe (ex: Mobile)")
print("   - Novo controle? +1 classe (ex: ControleExpert)")
print("   - Crescimento linear, não exponencial!")
print()
print("3. REUTILIZAÇÃO DE CÓDIGO:")
print("   - Lógica de pulo está em 1 lugar só (Controle.pular)")
print("   - Cada plataforma define seus inputs em 1 lugar")
print("   - Mudança em 1 lugar afeta todos os usos")
print()
print("4. DESACOPLAMENTO:")
print("   - Controles não sabem detalhes das plataformas")
print("   - Plataformas não sabem detalhes dos controles")
print("   - Pode trocar plataforma em tempo de execução!")
print()
print("5. SINGLE RESPONSIBILITY:")
print("   - Controle: define AÇÕES de alto nível")
print("   - Plataforma: define INPUTS específicos")
print("=" * 70)
