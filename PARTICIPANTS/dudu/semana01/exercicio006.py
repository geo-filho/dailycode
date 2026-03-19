def ler_nota(mensagem): 
    while True: # Esse loop continua pedindo a nota até ser digitada
        try: # Tratamento de erro
            return float(input(mensagem))
        except ValueError:
            print("Por favor, digite um número válido!")


def calcularMedia(materia1, materia2, materia3):
    resultadoMedia = round(materia1 + materia2 + materia3) / 3
    
    if resultadoMedia >= 7:
        return "O aluno foi APROVADO!"
    else:
        return "O aluno foi REPROVADO!"


def main():
    nome = input("Olá, Professor(a)! Para começar, digite o seu nome: ") # Saudação realizada sem a função "def saudacao(nome: str) -> str:"
    print(f"Olá, {nome}! Seja bem-vindo ao sistema de notas!\n")

    materia1 = ler_nota("Digite a nota da primeira matéria: ")
    materia2 = ler_nota("Digite a nota da segunda matéria: ")
    materia3 = ler_nota("Digite a nota da terceira matéria: ")

    resultado = calcularMedia(materia1, materia2, materia3)
    print(resultado)


main()