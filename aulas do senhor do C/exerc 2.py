#exercicio 2
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        return self.preco - (self.preco * percentual / 100)

produto1 = Produto("Notebook", 3500.0)
produto2 = Produto("Mouse", 150.0)

print(produto1.desconto(10))
print(produto2.desconto(20))
