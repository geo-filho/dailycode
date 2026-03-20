def identificarMaiorMenor(n1,n2,n3):
    
    numeros = [n1, n2, n3]

    maior = max(numeros)
    menor = min(numeros)
    return maior, menor

num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
num3 = float(input("Digite um número: "))

resultado_maior, resultado_menor = identificarMaiorMenor(num1, num2, num3)

print(f"O maior número é: {resultado_maior:.2f}")
print(f"O menor número é: {resultado_menor: .2f}")
