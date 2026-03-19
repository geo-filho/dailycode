def calcularImposto(salario):
    if salario > 1200:
        return "Deve pagar imposto"
    else:
        return "Não precisa pagar imposto"

salario = float(input("Digite o salário: "))
print(calcularImposto(salario))