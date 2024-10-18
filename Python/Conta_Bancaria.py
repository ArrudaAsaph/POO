# 3. Uma Conta Bancária
# A classe deve ter atributos para armazenar o nome do titular da conta, o número da conta e seu saldo e métodos
# para realizar as operações de depósito e saque.
# Escrever um programa para testar a classe.

class Cliente:
    def __init__(self):
        self.nome = ''
        self.numero_da_conta = 0
        self.saldo = 0
    
    def deposito(self):
        a = int(input("Digite o valor do deposito: R$ "))
        self.saldo += a
        print(f"Transação bem sucedida... Seu Saldo atual é de {self.saldo}")
        return self.saldo

    def saque(self):
        a = int(input("Digite o valor do saque: R$ "))
        while (self.saldo - a) < 0:
            print("Ocorreu um erro...")
            print("Saldo Insuficiente...")
            print(f"Seu saldo é de R$ {self.saldo}! ")
            a = int(input("Digite o novo valor válido do saque: R$ "))
        self.saldo -= a
        return self.saldo
    
    def extrato(self):
        print("----" * 15)
        print(f"Nome: {self.nome}")
        print("")
        print(f"Conta: {self.numero_da_conta}")
        print("")
        print("")
        print(f"Saldo Atual: R$ {self.saldo}")
        print("----" * 15)

        

_cliente = Cliente()
_cliente.nome = str(input("Digite o seu nome: "))
_cliente.numero_da_conta = int(input("Digite o número da sua conta (11 dígitos): "))
_cliente.saldo = int(input("Digite o seu Saldo: R$ "))
print("""
Digite 1 para realizar um Depóstio!
Digite 2 para realizar um Saque!
Digite 3 para ter acesso ao Extrato Bancário!
""")
operação = int(input("Digite o número de sua operação: "))

while True:
    if (operação == 1):
        _cliente.deposito()
    else:
        if (operação == 2):
            _cliente.saque()
        else:
            _cliente.extrato()


            
