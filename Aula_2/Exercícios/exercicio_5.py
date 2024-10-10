# Salário com Bônus
# Entrada
# O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e montante total das vendas efetuadas por este vendedor, respectivamente.

# Saída
# Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.a

nome = str(input())
salario = float(input())
comissao = float(input()) * 0.15

print(f"TOTAL = R$ {(salario + comissao):.2f}")