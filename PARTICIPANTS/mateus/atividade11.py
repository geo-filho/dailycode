def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    contagem_vogais = 0
    contagem_consoantes = 0
    for letra in frase:
        if letra in vogais:
            contagem_vogais += 1
        elif letra in consoantes:
            contagem_consoantes += 1
    return contagem_vogais, contagem_consoantes


frase = input("Digite uma frase: ")
vogais, consoantes = contar_vogais(frase)
print(f"A frase contém {vogais} vogais e {consoantes} consoantes.")