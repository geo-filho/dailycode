import math

def verificar_numero(n):

    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
        
    
    limite = int(math.sqrt(n)) + 1
    for i in range(3, limite, 2):
        if n % i == 0:
            return False
            
    return True

def executar_programa():
    print(" Verificar Números Primos ")
    
    try:
        
        entrada = input("Digite um número inteiro: ")
        numero = int(entrada)
        
        
        primo = verificar_numero(numero)
        
        if primo:
            print(f"O número {numero} é PRIMO.")
        else:
            print(f"O número {numero} NÃO é primo.")
            
    except ValueError:
        print("Erro: Por favor, insira apenas números inteiros válidos.")

if __name__ == "__main__":
    executar_programa()