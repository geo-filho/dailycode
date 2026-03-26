def calcular_desconto(valor_compra):

    if valor_compra <= 100:
        percentual = 0
    elif valor_compra <= 500:
        percentual = 0.10
    else:
        percentual = 0.20
    

    valor_desconto = valor_compra * percentual
    valor_final = valor_compra - valor_desconto

    return valor_desconto, valor_final

try:

    entrada = input("Digite o valor da compra R$").replace(',','.')
    valor_da_compra = float(entrada)

    desconto,total_desconto = calcular_desconto(valor_da_compra)

    print(f"Valor original: R$ {valor_da_compra:.2f}")
    print(f"Desconto aplicado: R$ {desconto:.2f}")
    print(f"Valor final: R$ {total_desconto:.2f}")

except ValueError:
    print("Insira um Valor númerico")