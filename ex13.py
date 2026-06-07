matriz = [
    [1,2,3],
    [2,4,2],
    [5,2,1]
]

valor = int(input("Valor: "))

cont = 0

for linha in matriz:
    for item in linha:
        if item == valor:
            cont += 1

print(cont)