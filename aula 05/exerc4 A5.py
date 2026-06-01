#exercicio 4
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def apresentar(self):
        print(self.nome, self.idade, self.matricula)

class Professor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def apresentar(self):
        print(self.nome, self.idade, self.salario)

aluno1 = Aluno("Ana", 17, "2024001")
aluno2 = Aluno("Bruno", 18, "2024002")
prof1 = Professor("Carlos", 40, 5000)
prof2 = Professor("Diana", 35, 4500)

pessoas = [aluno1, aluno2, prof1, prof2]

for i in pessoas:
    i.apresentar()
