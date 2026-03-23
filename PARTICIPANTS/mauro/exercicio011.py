def contar_vogais(texto):
    vogais_base = "aeiou"
    texto_clear = texto.lower()

    vogais_encontradas = set()
    qtd_vogais = 0
    qtd_consoantes = 0

    for char in texto_clear:
        if char.isalpha():
            if char in vogais_base: 
                qtd_vogais += 1
                vogais_encontradas.add(char)
            else: 
                qtd_consoantes += 1
    
   
    return qtd_vogais, qtd_consoantes, sorted(list(vogais_encontradas))
    
def iniciar_programa():
    print("-- Contador de vogais e consoantes --")

    while True: 
        entrada = input("\nInforme uma Palavra ou uma frase: ").strip()

      
        if any(c.isalpha() for c in entrada):   
            break
        else:
            print(" Palavra inválida! O texto deve conter pelo menos uma letra.")


    v_total, c_total, lista_v = contar_vogais(entrada)
    
    print("\n" + "=")
    print(f"Texto analisado: '{entrada}'")
    print(f"Total de Vogais: {v_total}")
    print(f"Total de Consoantes: {c_total}")
    print(f"Vogais encontradas: {', '.join(lista_v) if lista_v else 'Nenhuma'}")
    print("=")

if __name__ == "__main__":
    iniciar_programa()