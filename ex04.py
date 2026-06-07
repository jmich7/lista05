cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
nulos = 0
brancos = 0

voto = 1

while voto != 0:

    voto = int(input("Digite o voto (0 encerra): "))

    if voto == 1:
        cand1 += 1

    elif voto == 2:
        cand2 += 1

    elif voto == 3:
        cand3 += 1

    elif voto == 4:
        cand4 += 1

    elif voto == 5:
        nulos += 1

    elif voto == 6:
        brancos += 1

total = cand1 + cand2 + cand3 + cand4 + nulos + brancos

print("Candidato 1:", cand1)
print("Candidato 2:", cand2)
print("Candidato 3:", cand3)
print("Candidato 4:", cand4)
print("Nulos:", nulos)
print("Brancos:", brancos)

print("Percentual de nulos:", (nulos * 100) / total)
print("Percentual de brancos:", (brancos * 100) / total)