def calcularSalario(salario, porcentagem, operacao):
    alteracao = salario * (porcentagem / 100)

    if operacao == "aumento":
        novo_salario = salario + alteracao
    elif operacao == "desconto":
        novo_salario = salario - alteracao
    else:
        return None, None

    return alteracao, novo_salario


salario = float(input("Digite o salário: "))
porcentagem = float(input("Digite a porcentagem (%): "))
operacao = input("Digite o tipo (aumento/desconto): ").lower()

alteracao, novo_salario = calcularSalario(salario, porcentagem, operacao)

if alteracao is not None:
    print("Valor da alteração:", alteracao)
    print("Novo salário:", novo_salario)
else:
    print("Operação inválida!")