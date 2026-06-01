#exercicio 1
class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def set_nome(self, nome):
        if len(nome) > 0:
            self.__nome = nome
        else:
            print("Erro: nome nao pode ser vazio")

    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print("Erro: preco nao pode ser negativo")

produto1 = Produto("Notebook", 3500.0)
produto2 = Produto("Mouse", 150.0)

print(produto1.get_nome(), produto1.get_preco())
print(produto2.get_nome(), produto2.get_preco())

produto1.set_preco(-100)
produto2.set_nome("")
