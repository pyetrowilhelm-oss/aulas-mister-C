#exercicio 4
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor

    def extrato(self):
        print(self.titular, self.saldo)

conta1 = ContaBancaria("Ana", 1000.0)

conta1.depositar(500)
conta1.sacar(200)
conta1.sacar(2000)
conta1.extrato()
