#exercicio 1
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f"{self.nome} esta comendo")

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def latir(self):
        print(f"{self.nome} esta latindo")

cachorro1 = Cachorro("Rex")

cachorro1.comer()
cachorro1.latir()
