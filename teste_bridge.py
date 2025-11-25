import unittest
from com_bridge import (
    MetodoPagamento,
    ProcessadorPagamento,
)


class MetodoPagamentoMock(MetodoPagamento):
    def __init__(self, taxa=0.0):
        self.taxa = taxa
        self.autenticado = False
        self.valor_capturado = None

    def autenticar(self):
        self.autenticado = True
        return True

    def capturar_pagamento(self, valor):
        self.valor_capturado = valor
        return True

    def obter_taxa_transacao(self):
        return self.taxa


class TesteBridge(unittest.TestCase):
    def test_troca_metodo_em_runtime(self):
        metodo1 = MetodoPagamentoMock(taxa=2.0)
        metodo2 = MetodoPagamentoMock(taxa=5.0)
        
        processador = ProcessadorPagamento(metodo1)
        processador.processar(100.0)
        
        self.assertEqual(metodo1.valor_capturado, 102.0)
        self.assertTrue(metodo1.autenticado)
        
        processador.metodo = metodo2
        processador.processar(100.0)
        
        self.assertEqual(metodo2.valor_capturado, 105.0)
        self.assertTrue(metodo2.autenticado)

unittest.main(verbosity=2)