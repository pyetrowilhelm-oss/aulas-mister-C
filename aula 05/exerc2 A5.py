#exercicio 2
class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def informacoes(self):
        print(self.marca, self.ano)

class Carro(Veiculo):
    def __init__(self, marca, ano, portas):
        super().__init__(marca, ano)
        self.portas = portas

class Moto(Veiculo):
    def __init__(self, marca, ano, cilindradas):
        super().__init__(marca, ano)
        self.cilindradas = cilindradas

carro1 = Carro("Toyota", 2020, 4)
moto1 = Moto("Honda", 2022, 600)

carro1.informacoes()
print(carro1.portas)

moto1.informacoes()
print(moto1.cilindradas)
