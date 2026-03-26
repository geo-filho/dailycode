def compararNumeros(numero1, numero2, numero3):
    maior = numero1
    if numero2 > maior:
        maior = numero2
    if numero3 > maior:
        maior = numero3
    menor = numero1
    if numero2 < menor:
        menor = numero2
    if numero3 < menor:
        menor = numero3
    return maior, menor

numero1 = float(input("Digite o primeiro numero:"))
numero2 = float(input("Digite o segundo numero:"))
numero3 = float(input("Digite o terceiro numero:"))

o_maior, o_menor = compararNumeros (numero1, numero2, numero3)

print(f"O numero maior foi:{o_maior}")
print(f"O numero menor foi:{o_menor}")