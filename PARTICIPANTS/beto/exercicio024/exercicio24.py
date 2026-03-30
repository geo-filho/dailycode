import random

def buscar_numero(lista, numero):
    if numero in lista:
        return lista.index(numero)
    else:
        return -1


numeros = []

for i in range(10):
    numeros.append(random.randint(1, 100))

print("Lista gerada:", numeros)

numero = int(input("Digite um número: "))

posicao = buscar_numero(numeros, numero)

if posicao != -1:
    print("Número encontrado na posição:", posicao)
else:
    print("Número não encontrado")