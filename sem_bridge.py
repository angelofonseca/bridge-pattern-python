class PagamentoSimplesComCartaoCredito:
    def processar(self, valor: float) -> None:
        print("Cartão de Crédito: autenticado")
        total = valor + (valor * 2.5 / 100)
        print(f"Total com taxa: R$ {total:.2f}")
        print(f"Cartão de Crédito: R$ {total:.2f} capturado")


class PagamentoSimplesComPix:
    def processar(self, valor: float) -> None:
        print("Pix: QR Code gerado")
        total = valor + (valor * 0.0 / 100)
        print(f"Total com taxa: R$ {total:.2f}")
        print(f"Pix: R$ {total:.2f} recebido instantaneamente")


class PagamentoSimplesComBoleto:
    def processar(self, valor: float) -> None:
        print("Boleto: código de barras gerado")
        total = valor + (valor * 1.5 / 100)
        print(f"Total com taxa: R$ {total:.2f}")
        print(f"Boleto: R$ {total:.2f} aguardando compensação (2 dias úteis)")


class PagamentoSimplesComCartaoDebito:
    def processar(self, valor: float) -> None:
        print("Cartão de Débito: senha validada")
        total = valor + (valor * 1.0 / 100)
        print(f"Total com taxa: R$ {total:.2f}")
        print(f"Cartão de Débito: R$ {total:.2f} debitado da conta")


class PagamentoSimplesComCarteiraDigital:
    def processar(self, valor: float) -> None:
        print("Carteira Digital: biometria confirmada")
        total = valor + (valor * 0.5 / 100)
        print(f"Total com taxa: R$ {total:.2f}")
        print(f"Carteira Digital: R$ {total:.2f} transferido do saldo")


class PagamentoParceladoComCartaoCredito:
    def processar_com_parcelas(self, valor: float, parcelas: int) -> None:
        print("Cartão de Crédito: autenticado")
        total = valor + (valor * 2.5 / 100)
        valor_parcela = total / parcelas
        print(f"{parcelas}x de R$ {valor_parcela:.2f}")
        print(f"Cartão de Crédito: R$ {total:.2f} capturado")


class PagamentoParceladoComPix:
    def processar_com_parcelas(self, valor: float, parcelas: int) -> None:
        print("Pix: QR Code gerado")
        total = valor + (valor * 0.0 / 100)
        valor_parcela = total / parcelas
        print(f"{parcelas}x de R$ {valor_parcela:.2f}")
        print(f"Pix: R$ {total:.2f} recebido instantaneamente")


class PagamentoParceladoComBoleto:
    def processar_com_parcelas(self, valor: float, parcelas: int) -> None:
        print("Boleto: código de barras gerado")
        total = valor + (valor * 1.5 / 100)
        valor_parcela = total / parcelas
        print(f"{parcelas}x de R$ {valor_parcela:.2f}")
        print(f"Boleto: R$ {total:.2f} aguardando compensação (3 dias úteis)")


class PagamentoParceladoComCartaoDebito:
    def processar_com_parcelas(self, valor: float, parcelas: int) -> None:
        print("Cartão de Débito: senha validada")
        total = valor + (valor * 1.0 / 100)
        valor_parcela = total / parcelas
        print(f"{parcelas}x de R$ {valor_parcela:.2f}")
        print(f"Cartão de Débito: R$ {total:.2f} debitado da conta")


class PagamentoParceladoComCarteiraDigital:
    def processar_com_parcelas(self, valor: float, parcelas: int) -> None:
        print("Carteira Digital: biometria confirmada")
        total = valor + (valor * 0.5 / 100)
        valor_parcela = total / parcelas
        print(f"{parcelas}x de R$ {valor_parcela:.2f}")
        print(f"Carteira Digital: R$ {total:.2f} transferido do saldo")


if __name__ == "__main__":
    print("=== Pagamento simples com Cartão de Crédito ===")
    simples_credito = PagamentoSimplesComCartaoCredito()
    simples_credito.processar(100.0)

    print("\n=== Pagamento parcelado com Pix ===")
    parcelado_pix = PagamentoParceladoComPix()
    parcelado_pix.processar_com_parcelas(300.0, 3)

    print("\n=== Pagamento simples com Boleto ===")
    simples_boleto = PagamentoSimplesComBoleto()
    simples_boleto.processar(250.0)

    print("\n=== Pagamento parcelado com Cartão de Débito ===")
    parcelado_debito = PagamentoParceladoComCartaoDebito()
    parcelado_debito.processar_com_parcelas(400.0, 4)

    print("\n=== Pagamento simples com Carteira Digital ===")
    simples_carteira = PagamentoSimplesComCarteiraDigital()
    simples_carteira.processar(150.0)
