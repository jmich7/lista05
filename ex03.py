total = 0
codigo = 1

while codigo != 0:

    codigo = int(input("Código (0 encerra): "))

    if codigo != 0:

        qtd = int(input("Quantidade: "))

        if codigo == 100:
            preco = 1.20

        elif codigo == 101:
            preco = 1.30

        elif codigo == 102:
            preco = 1.50

        elif codigo == 103:
            preco = 1.20

        elif codigo == 104:
            preco = 1.30

        elif codigo == 105:
            preco = 1.00

        valor = preco * qtd

        total += valor

        print("Valor do item: R$", valor)

print("Total geral: R$", total)