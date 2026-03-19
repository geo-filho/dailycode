def saudacao(nome: str) -> str:
    return f"Olá, {nome}! Seja bem-vindo!"


def main():
    nome = input("Digite seu nome: ")
    print(saudacao(nome))


if __name__ == "__main__":
    main()