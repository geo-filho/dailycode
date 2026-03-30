def analisar_tempos(tempos):
    melhor = min(tempos)
    pior = max(tempos)
    media = sum(tempos) / len(tempos)

    return melhor, pior, media


tempos = []

while True:
    tempo = float(input("Digite o tempo (ou 0 para parar): "))
    
    if tempo == 0:
        break
    
    tempos.append(tempo)

if len(tempos) > 0:
    melhor, pior, media = analisar_tempos(tempos)

    print("Melhor tempo:", melhor)
    print("Pior tempo:", pior)
    print("Média dos tempos:", media)
else:
    print("Nenhum tempo foi registrado")