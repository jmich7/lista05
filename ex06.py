nome = input("Nome do atleta: ")

saltos = []

for i in range(5):
    salto = float(input("Salto: "))
    saltos.append(salto)

maior = saltos[0]
menor = saltos[0]

for salto in saltos:
    if salto > maior:
        maior = salto

    if salto < menor:
        menor = salto

soma = 0

for salto in saltos:
    if salto != maior and salto != menor:
        soma += salto

media = soma / 3

print("Melhor salto:", maior)
print("Pior salto:", menor)
print("Média:", media)