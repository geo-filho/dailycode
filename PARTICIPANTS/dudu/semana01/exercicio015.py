def fibonacci(n):
    sequencia = []
    
    a, b = 0, 1
    for _ in range(n):
        sequencia.append(a)
        a, b = b, a + b
    
    return sequencia


try:
    numero = int(input("Digite um número inteiro positivo: "))
    
    if numero <= 0:
        print("Digite um número maior que zero.")
    else:
        resultado = fibonacci(numero)
        print("Sequência de Fibonacci:", resultado)

except ValueError:
    print("Entrada inválida! Digite um número inteiro.")