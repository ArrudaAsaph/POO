# 4. Calcular área, perímetro e diagonal de um retângulo, dados sua base e sua altura. Considerar que os valores
# podem ser números reais. Mostrar o resultado com duas casas decimais.
# Digite a base e a altura do retângulo
# 3
# 4
# Área = 12.00 - Perímetro = 14.00 - Diagonal = 5.00'
import math 
base = int(input("Digite a base do retângulo: "))
altura = int(input("Digite a altura do retângulo: ")) 

area = base * altura
perimetro = base * 2 + altura * 2
diagonal = math.sqrt((base * base ) + (altura * altura))
print(f"Área = {area:.2f} - Perímetro = {perimetro:.2f}- Diagonal = {diagonal:.2f}")