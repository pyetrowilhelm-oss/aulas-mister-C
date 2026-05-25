#exercicio 3
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        if self.velocidade - 10 < 0:
            self.velocidade = 0
        else:
            self.velocidade -= 10

carro1 = Carro("Toyota", "Corolla")

carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.frear()

print(carro1.velocidade)
