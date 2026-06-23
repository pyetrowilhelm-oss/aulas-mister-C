class Instrumento:
    def __init__(self, nome):
        self.nome = nome
    def tocar(self):
        print(f"{self.nome} esta tocando")

class Violao(Instrumento):
    def tocar(self):
        print(f"{self.nome}: Tlim tlim")

class Bateria(Instrumento):
    def tocar(self):
        print(f"{self.nome}: Bum tcha")

class Piano(Instrumento):
    def tocar(self):
        print(f"{self.nome}: Plim plim")

instrumentos = [
    Violao("Violao"),
    Bateria("Bateria"),
    Piano("Piano")
]

for instrumento in instrumentos:
    instrumento.tocar()
