def calcular_desconto(valor):
    if valor <= 100:
        desconto = 0
    elif valor <= 500:
        desconto = valor * 0.10
    else:
        desconto = valor * 0.20

    valor_final = valor - desconto

    return desconto, valor_final

valor = float(input("Digite o valor da compra: "))

desconto, valor_final = calcular_desconto(valor)

print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")