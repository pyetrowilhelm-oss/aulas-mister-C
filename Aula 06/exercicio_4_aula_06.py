class Pagamento:
    def processar(self, valor):
        return valor

class Dinheiro(Pagamento):
    def processar(self, valor):
        return valor - (valor * 0.05)

class Cartao(Pagamento):
    def processar(self, valor):
        return valor + (valor * 0.02)

class Pix(Pagamento):
    def processar(self, valor):
        return valor

formas_pagamento = [
    Dinheiro(),
    Cartao(),
    Pix()
]

for forma_pagamento in formas_pagamento:
    print(forma_pagamento.processar(100))
