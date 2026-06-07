matriz = [
    [1, 8, 3],
    [9, 2, 4]
]

maior = matriz[0][0]
menor = matriz[0][0]

for linha in matriz:
    for numero in linha:

        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

print("Maior:", maior)
print("Menor:", menor)