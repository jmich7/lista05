n = int(input("Tamanho da matriz: "))

matriz = []

for i in range(n):
    linha = []

    for j in range(n):
        linha.append(int(input()))

    matriz.append(linha)

diag_principal = 0
diag_secundaria = 0

for i in range(n):
    diag_principal += matriz[i][i]
    diag_secundaria += matriz[i][n-1-i]

print(diag_principal)
print(diag_secundaria)