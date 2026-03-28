# Array (lista) de produtos
produtos = []

# Funções
def adicionar(nome):
    produtos.append(nome)
    print(f"'{nome}' foi adicionado.")

def remover(nome):
    if nome in produtos:
        produtos.remove(nome)
        print(f"'{nome}' foi removido.")
    else:
        print("Produto não encontrado.")

def listar():
    if len(produtos) == 0:
        print("Estoque vazio.")
    else:
        print("\nLista de produtos:")
        for p in produtos:
            print("-", p)

def buscar(nome):
    if nome in produtos:
        print("Produto está no estoque.")
    else:
        print("Produto NÃO está no estoque.")

# Menu
while True:
    print("\n=== MENU ===")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Listar produtos")
    print("4 - Buscar produto")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        adicionar(nome)

    elif opcao == "2":
        nome = input("Nome do produto: ")
        remover(nome)

    elif opcao == "3":
        listar()

    elif opcao == "4":
        nome = input("Nome do produto: ")
        buscar(nome)

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")