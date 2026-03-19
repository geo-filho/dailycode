def calcularImposto(salario):

    if salario > 1200:
        return "Você deve pagar imposto"
    else:
        return "Isento, você não precisa pagar imposto"
    

try: 
    valor_salario = float(input("Digite seu salário: R$"))
    status = calcularImposto(valor_salario)
    print(f"Status fiscal: {status}")

except ValueError:
    print("Insira apenas números")
