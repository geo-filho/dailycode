def calcularSalario(salario, porcentagem, tipo):
    valor = salario * (porcentagem / 100)

    if tipo == "aumento":
        novo_salario = salario + valor
    elif tipo == "decremento":
        novo_salario = salario - valor
    else:
        return "Tipo inválido"

    return valor, novo_salario

salario = float(input("Digite o salário: "))
porcentagem = float(input("Digite a porcentagem: "))
tipo = input("Digite o tipo (aumento ou decremento): ").lower()

resultado = calcularSalario(salario, porcentagem, tipo)

if resultado != "Tipo inválido":
    valor, novo_salario = resultado
    print(f"Valor da alteração: R$ {valor:.2f}")
    print(f"Novo salário: R$ {novo_salario:.2f}")
else:
    print(resultado)