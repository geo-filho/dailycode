def verificar_numero(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

resultado = verificar_numero(numero)

if resultado:
    print("O número é primo")
else:
    print("O número não é primo")