gabarito = ["A", "B", "C", "D", "E", "E", "D", "C", "B", "A"]

maior = 0
menor = 10
total_alunos = 0
soma_notas = 0

continuar = "S"

while continuar == "S":

    acertos = 0

    for i in range(10):

        resposta = input("Questão " + str(i + 1) + ": ").upper()

        if resposta == gabarito[i]:
            acertos += 1

    print("Nota:", acertos)

    total_alunos += 1
    soma_notas += acertos

    if acertos > maior:
        maior = acertos

    if acertos < menor:
        menor = acertos

    continuar = input("Outro aluno? (S/N): ").upper()

print("Maior acerto:", maior)
print("Menor acerto:", menor)
print("Total de alunos:", total_alunos)
print("Média da turma:", soma_notas / total_alunos)