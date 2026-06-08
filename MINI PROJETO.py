# mini projeto oo - sistema de folha de pagamento

class Funcionario:
    def __init__(self, nome, matricula, salario_fixo):
        self.__nome = nome
        self.__matricula = matricula
        self.__salario_fixo = salario_fixo

    def get_nome(self):
        return self.__nome

    def get_matricula(self):
        return self.__matricula

    def get_salario_fixo(self):
        return self.__salario_fixo

    def set_salario_fixo(self, salario_fixo):
        if salario_fixo >= 0:
            self.__salario_fixo = salario_fixo
        else:
            print("Erro: salario nao pode ser negativo")


class CLT(Funcionario):
    def __init__(self, nome, matricula, salario_fixo):
        super().__init__(nome, matricula, salario_fixo)

    def calcular_salario(self):
        return self.get_salario_fixo()

    def exibir(self):
        print(f"Nome: {self.get_nome()} | Matricula: {self.get_matricula()} | Tipo: CLT | Salario: R$ {self.calcular_salario():.2f}")


class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario_fixo, vendas):
        super().__init__(nome, matricula, salario_fixo)
        self.vendas = vendas

    def calcular_salario(self):
        return self.get_salario_fixo() + (self.vendas * 0.10)

    def exibir(self):
        print(f"Nome: {self.get_nome()} | Matricula: {self.get_matricula()} | Tipo: Vendedor | Salario: R$ {self.calcular_salario():.2f}")


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_fixo):
        super().__init__(nome, matricula, salario_fixo)
        self.bonus = 1500.00

    def calcular_salario(self):
        return self.get_salario_fixo() + self.bonus

    def exibir(self):
        print(f"Nome: {self.get_nome()} | Matricula: {self.get_matricula()} | Tipo: Gerente | Salario: R$ {self.calcular_salario():.2f}")


func1 = CLT("DAMBROS O GENIO", "001", 3000.00)
func2 = Vendedor("FELIPE LOBO", "002", 2000.00, 12000.00)
func3 = Gerente("ENZO SATAN", "003", 5000.00)

funcionarios = [func1, func2, func3]

for i in funcionarios:
    i.exibir()
