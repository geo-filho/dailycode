import time

def contagem_regressiva(segundos):
    for i in range(segundos, -1, -1):
        print(i)
        time.sleep(1)


while True:
    try:
        tempo = int(input("Digite o tempo em segundos: "))
        if tempo >= 0:
            break
        else:
            print("Digite um número inteiro positivo.")
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")


contagem_regressiva(tempo)