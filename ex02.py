faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0

num = 0

while num >= 0:

    num = int(input("Digite um número: "))

    if 0 <= num <= 25:
        faixa1 += 1

    elif 26 <= num <= 50:
        faixa2 += 1

    elif 51 <= num <= 75:
        faixa3 += 1

    elif 76 <= num <= 100:
        faixa4 += 1

print("Quantidade entre 0 e 25:", faixa1)
print("Quantidade entre 26 e 50:", faixa2)
print("Quantidade entre 51 e 75:", faixa3)
print("Quantidade entre 76 e 100:", faixa4)