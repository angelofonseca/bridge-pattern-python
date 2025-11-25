from abc import ABC, abstractmethod
from enum import Enum


class TipoCartao(Enum):
    CREDITO = 2.5
    DEBITO = 1.0


class MetodoPagamento(ABC):
    def __init__(self, taxa_transacao: float) -> None:
        self._taxa_transacao = taxa_transacao

    @abstractmethod
    def autenticar(self) -> bool:
        pass

    @abstractmethod
    def capturar_pagamento(self, valor: float) -> bool:
        pass

    @property
    def taxa_transacao(self) -> float:
        return self._taxa_transacao


class Cartao(MetodoPagamento):
    def __init__(self, tipo: TipoCartao) -> None:
        super().__init__(taxa_transacao=tipo.value)
        self.tipo = tipo
        self._autenticado = False

    def autenticar(self) -> bool:
        self._autenticado = True
        print(f"Cartão de {self.tipo.name.capitalize()}: autenticado")
        return True

    def capturar_pagamento(self, valor: float) -> bool:
        if self.tipo == TipoCartao.CREDITO:
            print(f"Cartão de Crédito: R$ {valor:.2f} capturado")
        else:
            print(f"Cartão de Débito: R$ {valor:.2f} debitado da conta")
        return True


class Pix(MetodoPagamento):
    def __init__(self) -> None:
        super().__init__(taxa_transacao=0.0)
        self._autenticado = False

    def autenticar(self) -> bool:
        self._autenticado = True
        print("Pix: QR Code gerado")
        return True

    def capturar_pagamento(self, valor: float) -> bool:
        print(f"Pix: R$ {valor:.2f} recebido instantaneamente")
        return True


class Boleto(MetodoPagamento):
    def __init__(self) -> None:
        super().__init__(taxa_transacao=1.5)
        self._autenticado = False

    def autenticar(self) -> bool:
        self._autenticado = True
        print("Boleto: código de barras gerado")
        return True

    def capturar_pagamento(self, valor: float) -> bool:
        print(f"Boleto: R$ {valor:.2f} aguardando compensação (3 dias úteis)")
        return True


class CarteiraDigital(MetodoPagamento):
    def __init__(self) -> None:
        super().__init__(taxa_transacao=0.5)
        self._autenticado = False

    def autenticar(self) -> bool:
        self._autenticado = True
        print("Carteira Digital: biometria confirmada")
        return True

    def capturar_pagamento(self, valor: float) -> bool:
        print(f"Carteira Digital: R$ {valor:.2f} transferido do saldo")
        return True


class ProcessadorPagamento:
    def __init__(self, metodo: MetodoPagamento) -> None:
        self.metodo = metodo

    def processar(self, valor: float) -> None:
        if self.metodo.autenticar():
            taxa = self.metodo.taxa_transacao
            total = valor + (valor * taxa / 100)
            print(f"Total com taxa: R$ {total:.2f}")
            self.metodo.capturar_pagamento(total)


class ProcessadorPagamentoParcelado(ProcessadorPagamento):
    def processar_com_parcelas(self, valor: float, parcelas: int) -> None:
        if self.metodo.autenticar():
            taxa = self.metodo.taxa_transacao
            total = valor + (valor * taxa / 100)
            valor_parcela = total / parcelas
            print(f"{parcelas}x de R$ {valor_parcela:.2f}")
            self.metodo.capturar_pagamento(total)


if __name__ == "__main__":
    print("=== Pagamento simples com Cartão de Crédito ===")
    cartao_credito = Cartao(TipoCartao.CREDITO)
    processador = ProcessadorPagamento(cartao_credito)
    processador.processar(100.0)

    print("\n=== Pagamento parcelado com Pix ===")
    pix = Pix()
    processador_parcelado = ProcessadorPagamentoParcelado(pix)
    processador_parcelado.processar_com_parcelas(300.0, 3)

    print("\n=== Pagamento simples com Boleto ===")
    boleto = Boleto()
    processador_boleto = ProcessadorPagamento(boleto)
    processador_boleto.processar(250.0)

    print("\n=== Pagamento parcelado com Cartão de Débito ===")
    cartao_debito = Cartao(TipoCartao.DEBITO)
    processador_debito = ProcessadorPagamentoParcelado(cartao_debito)
    processador_debito.processar_com_parcelas(400.0, 4)

    print("\n=== Pagamento simples com Carteira Digital ===")
    carteira = CarteiraDigital()
    processador_carteira = ProcessadorPagamento(carteira)
    processador_carteira.processar(150.0)
