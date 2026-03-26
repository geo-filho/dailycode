def verificar_maior_menor(n1, n2, n3):
    maior = n1
    menor = n1

    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3

    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3

    return maior, menor

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior, menor = verificar_maior_menor(num1, num2, num3)

print("Maior número:", maior)
print("Menor número:", menor)