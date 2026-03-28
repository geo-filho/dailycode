# Lista de jogadores
jogadores = []

# Função para cadastrar jogador
def cadastrar():
    nome = input("Nome do jogador: ")
    pontuacao = int(input("Pontuação: "))

    jogador = {
        "nome": nome,
        "pontuacao": pontuacao
    }

    jogadores.append(jogador)
    print("Jogador cadastrado com sucesso!")

# Função para gerar ranking
def gerar_ranking():
    if not jogadores:
        print("Nenhum jogador cadastrado.")
        return

    # Ordena do maior para o menor
    ranking = sorted(jogadores, key=lambda j: j["pontuacao"], reverse=True)

    print("\n=== RANKING ===")
    for i, jogador in enumerate(ranking, start=1):
        print(f"{i}º - {jogador['nome']} ({jogador['pontuacao']} pontos)")

# Menu
while True:
    print("\n=== MENU ===")
    print("1 - Cadastrar jogador")
    print("2 - Ver ranking")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar()

    elif opcao == "2":
        gerar_ranking()

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")