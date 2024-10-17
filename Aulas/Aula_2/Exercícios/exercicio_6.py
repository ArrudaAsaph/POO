# O Maior
# Entrada
# O arquivo de entrada contém três valores inteiros.

# Saída
# Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

lista = list(map(int,input().split()))
print(f"{max(lista)} eh o maior")