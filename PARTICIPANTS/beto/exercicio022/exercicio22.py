def analisar_avaliacoes(notas):
    quantidade = len(notas)
    soma = sum(notas)
    media = soma / quantidade

    acima_media = 0
    for nota in notas:
        if nota > media:
            acima_media += 1

    return media, quantidade, acima_media


notas = []

while True:
    nota = float(input("Digite uma nota (ou -1 para parar): "))
    
    if nota == -1:
        break
    
    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        print("Nota inválida")

if len(notas) > 0:
    media, quantidade, acima_media = analisar_avaliacoes(notas)

    print("Média:", media)
    print("Quantidade de avaliações:", quantidade)
    print("Notas acima da média:", acima_media)
else:
    print("Nenhuma nota foi informada")