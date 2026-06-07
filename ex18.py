matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

nova = []

for i in range(len(matriz) - 1, -1, -1):
    nova.append(matriz[i])

for linha in nova:
    print(linha)