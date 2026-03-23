def contar_vogais(texto):
    vogais = "aeiou"
    qtd_vogais = 0
    qtd_consoantes = 0
    vogais_encontradas = []

    for letra in texto.lower():
        if letra.isalpha():  
            if letra in vogais:
                qtd_vogais += 1
                if letra not in vogais_encontradas:
                    vogais_encontradas.append(letra)
            else:
                qtd_consoantes += 1

    return qtd_vogais, qtd_consoantes, vogais_encontradas

while True:
    texto = input("Digite uma palavra ou frase: ")

    if any(letra.isalpha() for letra in texto):
        break
    else:
        print("Entrada inválida! Digite pelo menos uma letra.")

qtd_vogais, qtd_consoantes, lista_vogais = contar_vogais(texto)

print(f"Quantidade de vogais: {qtd_vogais}")
print(f"Quantidade de consoantes: {qtd_consoantes}")
print(f"Vogais encontradas: {lista_vogais}")