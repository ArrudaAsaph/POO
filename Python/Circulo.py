# 1. Um Círculo
# A classe deve ter um atributo raio para armazenar a dimensão da figura e métodos para calcular sua área e sua
# circunferência.
# Escrever um programa para testar a classe.
class Circulo:
    def __init__(self):
        self.raio = 0

    def calculaArea(self):
        area =  (self.raio ** 2) * 3.14
        return area

    def calculaCircunferencia(self):
        circunferencia =( 3.14 * 2 )* self.raio
        return circunferencia

circulo = Circulo()
circulo.raio = float(input("Digite o Raio do seu Círculo: "))

area = circulo.calculaArea()
circuferencia = circulo.calculaCircunferencia()

print(f"A area do seu círculo é: {area}")
print(f"A circuferencia do seu círculo é: {circuferencia:.2f}")
