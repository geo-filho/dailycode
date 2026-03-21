def encontrarMaiorEMenor(n1, n2, n3):
    maior = max(n1, n2, n3)
    menor = min(n1, n2, n3)
    return maior, menor


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior, menor = encontrarMaiorEMenor(num1, num2, num3)

print("Maior número:", maior)
print("Menor número:", menor)