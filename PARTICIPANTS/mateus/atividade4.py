#Função para calcular a soma de A e B, onde A é multiplicado por 2 e B é multiplicado por 3.
def calcular (A, B):
    resultado = (A*2) + (B*3)
    return resultado

#Solicitar ao usuário os valores de A e B, chamar a função calcular e exibir o resultado.
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

#Chamar a função calcular e exibir o resultado.
soma = calcular(A, B)
print("A soma de A e B é:", soma)