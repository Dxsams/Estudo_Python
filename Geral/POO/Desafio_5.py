class ContaBancaria:
    def __init__(self, titular, saldo=0):  # saldo inicial opcional
        self.titular = titular
        self.__saldo = saldo  # só usa o privado
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso!")
        else:
            print("Saldo insuficiente.")

    def ver_saldo(self):
        return f"Saldo atual de {self.titular}: R${self.__saldo}"
    

# Exemplo de uso:
conta = ContaBancaria("Samuel", 200)
print(conta.ver_saldo())
conta.depositar(100)
conta.sacar(50)
print(conta.ver_saldo())
