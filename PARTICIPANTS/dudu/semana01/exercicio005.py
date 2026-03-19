def saudacao(nome: str) -> str: # Função que recebe o nome do usuário como string
    return f"Olá, {nome}! Seja bem-vindo ao cálculo de imposto!\n"


def calcularImposto(salario):
    if salario > 1200:
        return "Você deve pagar imposto!"
    else:
        return "Você não precisa pagar imposto!"


def main():
    nome = input("Olá! Para começar, digite o seu nome: ")
    print(saudacao(nome))

    salario = float(input("Digite o valor do seu salário mensal: "))

    resultado = calcularImposto(salario)
    print(resultado)


main()