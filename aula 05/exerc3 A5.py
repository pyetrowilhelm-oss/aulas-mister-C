#exercicio 3
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir(self):
        print(self.nome, self.salario)

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def salario_total(self):
        return self.salario + self.bonus

gerente1 = Gerente("Carlos", 5000, 1500)

gerente1.exibir()
print(gerente1.salario_total())
