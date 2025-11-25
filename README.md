## 🌉 Padrão Estrutural Bridge

O padrão **Bridge** separa a **abstração** (o que fazer) da **implementação** (como fazer), permitindo que ambas variem independentemente através de **composição**.

### 🔧 **Hierarquia de IMPLEMENTAÇÃO** (Baixo Nível)

Define como cada método de pagamento funciona (detalhes técnicos):

- **`MetodoPagamento`** (ABC) - Interface abstrata que define quais métodos devem existir
  - **`Cartao`** - Implementa autenticação e captura via cartão de crédito/débito
  - **`Pix`** - Implementa autenticação (QR Code) e captura instantânea
  - **`Boleto`** - Implementa geração de código de barras e compensação
  - **`CarteiraDigital`** - Implementa biometria e transferência de saldo

### 🎯 **Hierarquia de ABSTRAÇÃO** (Alto Nível)

Define o que fazer (operações para o usuário) e delega os detalhes para a implementação:

- **`ProcessadorPagamento`** - Processa pagamento simples, calcula taxas e delega autenticação/captura
- **`ProcessadorPagamentoParcelado`** - Estende ProcessadorPagamento, adiciona funcionalidade de parcelamento

### 🔗 **BRIDGE**

A ponte é a **composição** que conecta as hierarquias:

```python
class ProcessadorPagamento:
    def __init__(self, metodo: MetodoPagamento):
        self.metodo = metodo  # ← PONTE! (composição)
    
    def processar(self, valor: float):
        self.metodo.autenticar()           # ← DELEGA para implementação
        self.metodo.capturar_pagamento()   # ← DELEGA para implementação
```


## 📊 Comparação: Sem Bridge vs Com Bridge

### Exemplo: Sistema de Processamento de Pagamentos

| Aspecto | Sem Bridge | Com Bridge |
|---------|-----------|-----------|
| **Número de classes** | 2 processadores × 5 métodos = **10 classes** | 2 processadores + 5 métodos = **7 classes** |
| **Duplicação de código** | ❌ Alta (lógica repetida com frequência) | ✅ Mínima (lógica centralizada) |
| **Acoplamento** | ❌ Alto  | ✅ Baixo (separação clara) |
| **Flexibilidade** | ❌ Baixa (não pode trocar de método) | ✅ Alta (troca em runtime) |
| **Manutenção** | ❌ Difícil (mudança mais trabalhosa) | ✅ Fácil (mudança localizada) |

---

## ✅ Pontos Fortes do Padrão Bridge

### 1. **Evita Explosão de Classes**
```
Exemplo atual: 2 processadores × 5 métodos
Sem Bridge: 2 × 5 = 10 classes
Com Bridge: 2 + 5 = 7 classes

Exemplo expandido: 4 processadores × 8 métodos
Sem Bridge: 4 × 8 = 32 classes
Com Bridge: 4 + 8 = 12 classes
```

### 2. **Desacoplamento**
- Hierarquia de abstração e implementação evoluem independentemente
- Flexível para cada classe ter sua regra específica

### 3. **Facilidade de Extensão**
- Crescimento **linear** de classes

### 4. **Reutilização de Código**
- Lógica de alto nível está em um só lugar
- Implementação específica está em um só lugar

### 5. **Flexibilidade em Runtime**
```python
processador = ProcessadorPagamento(cartao_credito)  # Começa com cartão
processador.metodo = pix                             # Troca para Pix
# Mesmo objeto, comportamento diferente!
```

### 6. **SRP**
- **Processador:** responsável pela LÓGICA de processamento (calcular taxas, parcelar)
- **Método de Pagamento:** responsável pela IMPLEMENTAÇÃO específica (autenticar, capturar)

### 7. **Facilita Testes**
```python
# Pode criar método mock para testes
class MetodoPagamentoMock(MetodoPagamento):
    def autenticar(self):
        return True
    def capturar_pagamento(self, valor):
        return True
    def obter_taxa_transacao(self):
        return 0.0

processador = ProcessadorPagamento(MetodoPagamentoMock())
# Testar processador sem depender de método real!
```

---

## ❌ Pontos Fracos do Padrão Bridge

### 1. **Complexidade Inicial Aumentada**
- Para problemas simples, pode ser desnecessário
- Requer entendimento de abstração vs implementação

### 2. **Mais Classes para Gerenciar**
- Mesmo reduzindo total, ainda cria 2 hierarquias
- Estrutura mais complexa

### 3. **Confusão de Responsabilidades**
- Decidir o que vai na abstração vs implementação pode ser difícil
