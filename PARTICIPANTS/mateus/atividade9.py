#função para calcular o salário com aumento ou desconto
def calcularsalario(salario, percentual, operacao):
    if operacao == "aumento":
        novo_salario = salario + (salario * percentual / 100)
    elif operacao == "desconto":
        novo_salario = salario - (salario * percentual / 100)
    else:
        return "Operação inválida. Use 'aumento' ou 'desconto'."
    return novo_salario 

#solicitar ao usuário o salário atual, o percentual e a operação
salario_atual = float(input("Digite o salário atual: "))
percentual = float(input("Digite o percentual de aumento ou desconto: "))
operacao = input("Digite a operação (aumento ou desconto): ")
novo_salario = calcularsalario(salario_atual, percentual, operacao)
print("O novo salário é:", novo_salario)