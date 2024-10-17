# 2. Uma Viagem
# A classe deve ter atributos para armazenar a distância em km e o tempo gasto em horas e minutos da viagem
# realizada. A classe deve possuir método para calcular a velocidade média atingida na viagem em km/h de acordo
# com a distância e o tempo gasto.
# Escrever um programa para testar a classe.

class Viagem:
    def __init__(self):
        self.distancia = 0
        self.horas = 0
        self.minutos = 0
        self.tempo = (self.minutos / 60) + self.horas

    def velocidadeMedia(self):
        veloMedia = self.distancia / self.tempo
        return veloMedia

circulo = Viagem()
circulo.distancia = float(input("Digite a distancia da sua Viagem: "))
circulo.horas = float(input("Digite a quantidade de horas da sua Viagem: "))
circulo.minutos = float(input("Digite a quantidade de minutos da sua Viagem: "))


print(f"A area do seu círculo é: {area}")
print(f"A circuferencia do seu círculo é: {circuferencia:.2f}")
