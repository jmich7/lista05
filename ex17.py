matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

quadrada = True

for linha in matriz:
    if len(linha) != len(matriz):
        quadrada = False

print(quadrada)