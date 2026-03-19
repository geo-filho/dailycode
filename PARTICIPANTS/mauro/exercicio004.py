def calcular (a,b):
    
    return ( 2 * a) * ( 3 * b)

print("Calculadora de 2a x 3b")

try:

    num_a = float(input("Digite o valor a: "))
    num_b = float(input("Digite o valor a: "))

    resultado_final = calcular (num_a, num_b)

    print(f"\n O resultado da conta (2 * {num_a}) * (3 * {num_b}) é: {resultado_final}")

#-----Bloqueio para que seja colocado apenas números
except ValueError:

    print("Digite apenas números")
