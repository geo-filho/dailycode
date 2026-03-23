import re

def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    
    lista_vogais = [letra for letra in texto if letra in vogais]
    qtd_vogais = len(lista_vogais)
    
    # Considera apenas letras para contar consoantes
    letras = re.findall(r"[a-zA-Z]", texto)
    qtd_consoantes = len([l for l in letras if l not in vogais])
    
    return qtd_vogais, qtd_consoantes, lista_vogais


def entrada_valida(texto):
    # Verifica se há pelo menos uma letra
    return bool(re.search(r"[a-zA-Z]", texto))


def main():
    while True:
        texto = input("Digite uma palavra ou frase: ").strip()
        
        if not entrada_valida(texto):
            print("Entrada inválida! Digite um texto que contenha letras.")
            continue
        
        qtd_vogais, qtd_consoantes, lista_vogais = contar_vogais(texto)
        
        print("\nResultados:")
        print(f"Quantidade de vogais: {qtd_vogais}")
        print(f"Quantidade de consoantes: {qtd_consoantes}")
        print(f"Vogais encontradas: {lista_vogais}")
        break


if __name__ == "__main__":
    main()