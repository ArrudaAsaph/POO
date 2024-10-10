# 2. Ler o nome completo de uma pessoa e mostrar a mensagem: “Bem-vindo ao Python, <xxx>”, onde <xxx> é o
# primeiro nome da pessoa.
# Digite seu nome completo:
# Gilbert Azevedo da Silva
# Bem-vindo ao Python, Gilbert

nome = input("Digite seu primeiro nome: ").split()
print(f"Bem-vindo ao Python, {nome[0]}")