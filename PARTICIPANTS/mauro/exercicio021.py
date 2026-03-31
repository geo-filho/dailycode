
jogadores = []

def cadastrar_jogador():
    nome = input("Nome do jogador: ").strip()
    try:
        pontuacao = int(input(f"Pontuação de {nome}: "))
       
        jogadores.append({"nome": nome, "pontos": pontuacao})
        print(f" {nome} cadastrado com sucesso!")
    except ValueError:
        print("A pontuação deve ser um número inteiro.")

def gerar_ranking():
    if not jogadores:
        print("\nNenhum jogador cadastrado para gerar o ranking.")
        return

   
    ranking = sorted(jogadores, key=lambda j: j["pontos"], reverse=True)

    print("\n RANKING ATUALIZADO ")
    for indice, jogador in enumerate(ranking, 1):
        print(f"{indice}º Lugar: {jogador['nome']} - {jogador['pontos']} pts")
    print("----------------------------\n")

def menu():
    while True:
        print(" SISTEMA DE TORNEIO")
        print("1. Cadastrar Jogador")
        print("2. Exibir Ranking")
        print("3. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_jogador()
        elif opcao == "2":
            gerar_ranking()
        elif opcao == "3":
            print("Encerrando o sistema de jogo. Até a próxima!")
            break
        else:
            print(" Opção inválida!")

if __name__ == "__main__":
    menu()