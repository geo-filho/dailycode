def calcular_desconto(valor_compra):
    if valor_compra <= 100:
        desconto = 0
    elif valor_compra <= 500:
        desconto = valor_compra * 0.10
    else:
        desconto = valor_compra * 0.20

    valor_final = valor_compra - desconto

    return desconto, valor_final


valor = float(input("Digite o valor da compra: R$ "))

desconto, total = calcular_desconto(valor)

print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {total:.2f}")