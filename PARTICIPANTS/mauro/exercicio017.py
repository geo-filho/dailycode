import time

def contagem_regressiva(segundos):

    for i in range(segundos, -1, -1):
        print(f"Contagem:{i}", end='\r', flush=True)

        time.sleep(1)

    print("\n A contagem terminou. ")

try:
    valor = int(input("Digite o tempo da contagem (segundos): "))
    if valor < 0:
        print("Digite um número positivo!")
    else:
        contagem_regressiva(valor)
except ValueError:
    print("Digite um número válido. ")