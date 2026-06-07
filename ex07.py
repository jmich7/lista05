nome = input("Nome do atleta: ")

notas = []

for i in range(7):
    nota = float(input("Nota: "))
    notas.append(nota)

maior = notas[0]
menor = notas[0]

for nota in notas:
    if nota > maior:
        maior = nota

    if nota < menor:
        menor = nota

soma = 0

for nota in notas:
    if nota != maior and nota != menor:
        soma += nota

media = soma / 5

print("Melhor nota:", maior)
print("Pior nota:", menor)
print("Média:", media)