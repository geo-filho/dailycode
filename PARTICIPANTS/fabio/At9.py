def ajusteSalarial (salario, porcetagem, aumentoOUdesconto):
    valor = salario * (porcetagem/100)
    if aumentoOUdesconto == "aumento":
        novo_salario = salario + valor
    else:
        novo_salario = salario - valor
    return valor, novo_salario

salario = float(input("Digite seu salario:R$"))
porcetagem = float (input("Digite o valor da porcetagem:"))
aumentoOUdesconto = str(input("Digite se foi 'Aumento' ou 'Desconto':"))

diferença, final = ajusteSalarial (salario, porcetagem, aumentoOUdesconto)

print(f"O valor da diferença foi:R${diferença}")
print(f"O valor final foi:R${final}")



