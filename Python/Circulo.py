# 1. Um Círculo
# Escrever a classe Círculo de acordo com o diagrama UML apresentado abaixo. A classe deve ter um atributo raio
# para armazenar a dimensão da figura e métodos para calcular sua área e sua circunferência, além dos métodos de
# acesso para definir e recuperar o atributo raio.
# Escrever um programa para testar a classe.

class Circulo():
    def __init__(self):
        self.raio = 0
    
    def set_raio(self,v):
        if (v >= 0): self.raio = v
        else:
            raise ValueError("a base do triângulo não pode ser negativa")

    def get_raio(self):
        return self.raio

    def calcu_Area(self):
        return self.raio ** 2 * 3.14
    
    def calcu_Circuferencia(self):
        return 2 * 3.14 * self.raio
    
circulo = Circulo()

circulo.set_raio(float(input("Digite o raio do círculo: ")))


op = 0
while op != 5:
    print(""" 
***************************************
Digite a Operação que deseja realizar:
1 - Calcular Área.
2 - Calcular Circuferência.
3 - Valor do Raio.
4 - Novo valor do Raio.
5 - Sair
***************************************

""")
    op = int(input("Digite a Operação que deseja: "))
    if (op == 1):
        print(f"Área do Círculo = {circulo.calcu_Area():.2f}")
    elif (op == 2):
        print(f"Circuferência do Círculo = {circulo.calcu_Circuferencia():.2f}")
    elif (op == 3):
        print(f"Raio = {circulo.get_raio():.2f}")
    elif (op == 4):
        circulo.set_raio(float(input("Digite um novo raio do círculo: ")))
    else:
            op = int(input("Valor inválido! Digite a Operação válida: "))



        


