#Função para calcular o imposto de renda com base no salário, nesse exemplo o imposto é de 10%.
def calcularimposto(salario):
    if salario <= 1200:
        imposto = 0
    else:
        imposto = salario * 0.10
    return imposto

#Solicitar ao usuário o valor do salário, chamar a função calcularimposto e exibir o resultado.
salario = float(input("Digite o valor do salário: "))
imposto = calcularimposto(salario)
print("O imposto a ser pago é:", imposto)