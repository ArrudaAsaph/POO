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
        

    def velocidadeMedia(self):
        if self.minutos != 0:
            self.horas += self.minutos / 60
        veloMedia = self.distancia / self.horas

        return veloMedia

viagem = Viagem()
viagem.distancia = float(input("Digite a distancia da sua Viagem: "))
viagem.horas = int(input("Digite a quantidade de horas da sua Viagem: "))
viagem.minutos = int(input("Digite a quantidade de minutos da sua Viagem: "))


print(f"Você fez {viagem.distancia} km em {viagem.horas} horas e {viagem.minutos} lgo sua velocidade média é {viagem.velocidadeMedia():.2f} Km/h.")
# print(f"A circuferencia do seu círculo é: {circuferencia:.2f}")
