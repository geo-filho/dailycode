def calcularAlteracaoSalarial(salario, porcentagem, operacao):
    valor_variacao = salario * (porcentagem / 100)

    if operacao == '+':
        novo_salario = salario + valor_variacao
    elif operacao == '-':
        novo_salario = salario - valor_variacao
    else:
        return None , None
    return valor_variacao, novo_salario

salario_atual = float(input("Digite o seu sálario: "))
porcentagem = float(input("Digite a porcentagem: "))
tipo = input("Digite a operação: ")

variacao, salario_final = calcularAlteracaoSalarial(salario_atual, porcentagem, tipo)

if variacao is not None:
    print(f"Valor alterado: R$ {variacao:.2f}")
    print(f"Novo Sálario: R$ {salario_final: .2f}")
else: print("Operação inválida")

