divida = float(input("Valor da dívida: "))

parcelas = [1, 3, 6, 9, 12]
juros = [0, 10, 15, 20, 25]

print("\nValor da Dívida | Juros | Parcelas | Valor da Parcela")

for i in range(len(parcelas)):
    valor_juros = divida * juros[i] / 100
    total = divida + valor_juros
    valor_parcela = total / parcelas[i]

    print(f"R${total:.2f} | R${valor_juros:.2f} | {parcelas[i]} | R${valor_parcela:.2f}")