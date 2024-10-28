# 2. Uma Viagem
# Escrever a classe Viagem de acordo com o diagrama UML apresentado abaixo. A classe deve ter atributos para
# armazenar a distância em km e o tempo gasto em horas e minutos da viagem realizada. A classe deve possuir
# método para calcular a velocidade média atingida na viagem em km/h de acordo com a distância e o tempo gasto,
# além dos métodos de acesso para definir e recuperar os atributos.
# Escrever um programa para testar a classe.

class Viagem:
    def __init__(self):
        self.distancia = 0
        self.horas = 0
        self.minutos = 0
        
    def set_distancia(self,v):
        if (v >= 0): self.distancia = v
        else:
            raise ValueError("Uma distância não pode ser negativa!")
    
    def set_horas(self,v):
        if (v >= 0): self.horas = v
        else:
            raise ValueError("Um tempo não pode ser negativo!")
        
    def set_minutos(self,v):
        if (v >= 0): self.minutos = v
        else:
            raise ValueError("Um tempo não pode ser negativo!")
        
    def get_distancia(self):
        return self.distancia
    
    def get_horas(self):
        return self.horas
    
    def get_minutos(self):
        return self.minutos

    def velocidadeMedia(self):
        return self.distancia / (self.horas + (self.minutos / 60))

viagem = Viagem() 
viagem.set_distancia(float(input("Digite a distancia da viagem: Km"))) 
viagem.set_horas(float(input("Digite a quantidade de horas da viagem: ")))
viagem.set_minutos(float(input("Digite a quantidade de minutos da viagem: ")))

op = 0
while op != 5:
    print(""" 
***************************************
Digite a Operação que deseja realizar:
1 - Calcular Velocidade Média.
2 - Valor da distancia.
3 - Valor das horas.
4 - Valor dos minutos.
5 - Nova Distância.
6 - Novo tempo.
7 - Sair
***************************************

""")
    op = int(input("Digite a Operação que deseja: "))
    if (op == 1):
        print(f"A velocidade Média de sua viagem foi de {viagem.velocidadeMedia():.2f} km/h")
    elif (op == 2):
        print(f"A distancia da sua viagem é {viagem.get_distancia():.2f} km")
    elif (op == 3):
        print(f"{viagem.get_horas():.2f} horas.")
    elif (op == 4):
        print(f"{viagem.get_minutos():.2f} minutos.")

    elif (op == 5):
        viagem.set_distancia(float(input("Digite a distancia da viagem: Km"))) 
    
    elif (op == 6):
        viagem.set_horas(float(input("Digite a quantidade de horas da viagem: ")))
        viagem.set_minutos(float(input("Digite a quantidade de minutos da viagem: ")))
    
    elif (op == 7):
        break

    else:
            op = int(input("Valor inválido! Digite a Operação válida: "))


