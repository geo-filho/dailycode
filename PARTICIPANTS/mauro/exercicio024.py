import random

def buscar_numero(lista, alvo):
 
    if alvo in lista:
        return lista.index(alvo)
    return -1

def sistema_busca_aleatoria():
    print(" Desafio de Busca Aleatória ")
    
    numeros = random.sample(range(1, 101), 10)
    
   
    print(f"\nLista gerada: {numeros}")
    
    
    try:
        palpite = int(input("\nDigite um número para buscar na lista: "))
        
        
        posicao = buscar_numero(numeros, palpite)
        
        if posicao != -1:
            print(f" O número {palpite} foi encontrado na posição {posicao}.")
        else:
            print(f" O número {palpite} não está na lista.")
            
    except ValueError:
        print(" Por favor, digite números inteiros.")

if __name__ == "__main__":
    sistema_busca_aleatoria()