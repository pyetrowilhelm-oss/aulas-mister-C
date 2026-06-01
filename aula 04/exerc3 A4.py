#exercicio 3
class ContaBancaria:
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Erro: valor deve ser positivo")

    def sacar(self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente")
        else:
            self.__saldo -= valor

    def get_saldo(self):
        return self.__saldo

    def extrato(self):
        print(self.__titular, self.__saldo)

conta1 = ContaBancaria("Ana")

conta1.depositar(1000)
conta1.sacar(200)
conta1.sacar(2000)
conta1.depositar(-50)
conta1.extrato()
