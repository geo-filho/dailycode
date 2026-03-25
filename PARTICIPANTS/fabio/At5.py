def calcularimposto(salario):
    if salario >= 1200: 
        return("Você terá que pagar imposto.")
    else:
       return("Você não precisa pagar imposto.")

salario = int(input("Digite seu salario: "))

print (calcularimposto(salario))

