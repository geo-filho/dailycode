def fibonacci(n):
    sequencia = []

    a, b = 0, 1

    for i in range(n):
        sequencia.append(a)
        a, b = b, a + b

    return sequencia

while True:
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        if numero > 0:
            break
        else:
            print("Digite um número maior que 0.")
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")


resultado = fibonacci(numero)

print("Sequência de Fibonacci:")
print(resultado)