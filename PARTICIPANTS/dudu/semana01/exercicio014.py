def verificar_numero(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


try:
    numero = int(input("Digite um número inteiro: "))
    
    if verificar_numero(numero):
        print("True - É primo")
    else:
        print("False - Não é primo")

except ValueError:
    print("Entrada inválida! Digite um número inteiro.")