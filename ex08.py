numero = input("Digite um número: ")

invertido = ""

for i in range(len(numero) - 1, -1, -1):
    invertido += numero[i]

print(invertido)