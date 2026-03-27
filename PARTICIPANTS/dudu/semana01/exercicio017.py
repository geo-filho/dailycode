import time

def contagem_regressiva(segundos):
    for i in range(segundos, -1, -1):
        print(i)
        time.sleep(1)  # delay de 1 segundo


tempo = int(input("Digite o tempo em segundos: "))

contagem_regressiva(tempo)