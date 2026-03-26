def fibonacci(n):

    sequencia = []
    a, b = 0, 1
    
    for _ in range(n):
        sequencia.append(a)
        a, b = b, a + b
        
    return sequencia

def executar_programa():
    print("Mostrador de Sequência de Fibonacci")
    
    try:
        
        entrada = input("Digite um número inteiro positivo (posição do número escolhido): ")
        posicao = int(entrada)
        
       
        if posicao <= 0:
            print("  Por favor, Digite um número maior que zero.")
        else:
            
            resultado = fibonacci(posicao)
            print(f"\n Sequência até a posição {posicao}:")
            print(resultado)
            
    except ValueError:
       
        print(" Mensagem inválida. Você deve digitar um número inteiro.")

if __name__ == "__main__":
    executar_programa()