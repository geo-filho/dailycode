def saudacao(nome: str) -> str: # Função que recebe o nome do usuário como string
    return f"Olá, {nome}! Seja bem-vindo ao programa de cálculo de funções!\n"


def calcular(a, b): # Recebe dois parâmetros
    resultado = (2 * a) * (3 * b)
    return resultado # A função devolve o valor calculado


def main(): # Função principal
    nome = input("Olá! Para começar, digite o seu nome: ")
    print (saudacao(nome))

    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    
    resultado = calcular(a, b) # Chama a função 
    print(f"Resultado: {resultado:.2f}") # Determina a quantidade de casas decimais


main()