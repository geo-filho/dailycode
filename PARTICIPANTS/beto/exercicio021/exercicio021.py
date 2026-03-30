def gerar_ranking(jogadores):
    jogadores_ordenados = jogadores.copy()
    jogadores_ordenados.sort(reverse=True)
    return jogadores_ordenados

jogadores = []

while True:
    print("\n1 - Cadastrar jogador")
    print("2 - Ver ranking")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome do jogador: ")
        pontuacao = int(input("Pontuação: "))
        jogadores.append([nome, pontuacao])

    elif opcao == "2":
        ranking = gerar_ranking(jogadores)
        posicao = 1
        for jogador in ranking:
            print(f"{posicao}º - {jogador[0]} ({jogador[1]})")
            posicao += 1

    elif opcao == "0":
        break

    else:
        print("Opção inválida")