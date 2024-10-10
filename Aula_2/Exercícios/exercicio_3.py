# 3. Calcular a média parcial de uma disciplina semestral, dadas as notas dos 1o e 2o bimestres (pesos 2 e 3).
# Considerar as notas com valores inteiros entre zero e cem.
# Digite a nota do primeiro bimestre da disciplina:
# 50
# Digite a nota do segundo bimestre da disciplina:
# 70
# Média parcial = 62

nota_1 = int(input("Digite a nota do primeiro bimestre da disciplina: "))
nota_2 = int(input("Digite a nota do segundo bimestre da disciplina: "))

media =int(( nota_1* 2 + nota_2 * 3) / 5)
print(f"Média parcial = {media}")