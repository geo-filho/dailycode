def verificar_produto(produtos, nome):
    return nome in produtos

produtos = []

while True:
    print("\n1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Listar produtos")
    print("4 - Verificar produto")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do produto: ")
        produtos.append(nome)

    elif opcao == "2":
        nome = input("Digite o nome do produto: ")
        if nome in produtos:
            produtos.remove(nome)
        else:
            print("Produto não encontrado")

    elif opcao == "3":
        if produtos:
            for p in produtos:
                print(p)
        else:
            print("Estoque vazio")

    elif opcao == "4":
        nome = input("Digite o nome do produto: ")
        if verificar_produto(produtos, nome):
            print("Produto existe")
        else:
            print("Produto não existe")

    elif opcao == "0":
        break

    else:
        print("Opção inválida")