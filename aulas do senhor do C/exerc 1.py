#exercicio 1
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

produto1 = Produto("Notebook", 3500.0)
produto2 = Produto("Mouse", 150.0)

print(produto1.nome, produto1.preco)
print(produto2.nome, produto2.preco)
