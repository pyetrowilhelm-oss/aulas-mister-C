class Funcionario:
    def __init__(self, nome, salario_fixo):
        self.nome = nome
        self.salario_fixo = salario_fixo
    def calcular_salario(self):
        return 0

class Vendedor(Funcionario):
    def __init__(self, nome, salario_fixo, comissao):
        super().__init__(nome, salario_fixo)
        self.comissao = comissao
    def calcular_salario(self):
        return self.salario_fixo + self.comissao

class Gerente(Funcionario):
    def __init__(self, nome, salario_fixo, bonus):
        super().__init__(nome, salario_fixo)
        self.bonus = bonus
    def calcular_salario(self):
        return self.salario_fixo + self.bonus

vendedor1 = Vendedor("Joao", 1500, 800)
gerente1 = Gerente("Carlos", 5000, 1500)
print(vendedor1.nome, vendedor1.calcular_salario())
print(gerente1.nome, gerente1.calcular_salario())
