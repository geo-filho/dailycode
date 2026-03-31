
estoque = []

def adicionar_produto():
    nome = input("Digite o nome do produto para adicionar: ").strip()
    if nome:
        estoque.append(nome)
        print(f"Produto '{nome}' adicionado com sucesso!")
    else:
        print(" O nome do produto não pode estar vazio.")

def remover_produto():
    nome = input("Digite o nome do produto para remover: ").strip()
    if nome in estoque:
        estoque.remove(nome)
        print(f"Produto '{nome}' removido do estoque.")
    else:
        print(" Produto não encontrado.")

def listar_produtos():
    if not estoque:
        print("\n  O estoque está vazio.")
    else:
        print("\n Produtos em Estoque ")
        for i, produto in enumerate(estoque, 1):
            print(f"{i}. {produto}")

def buscar_produto():
    nome = input("Digite o nome do produto que deseja buscar: ").strip()
   
    if nome in estoque:
        print(f" O produto '{nome}' ESTÁ disponível no estoque.")
    else:
        print(f"  O produto '{nome}' NÃO foi encontrado.")

def menu():
    while True:
        print("\n GERENCIADOR DE ESTOQUE ")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Listar Produtos")
        print("4. Buscar Produto")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            remover_produto()
        elif opcao == "3":
            listar_produtos()
        elif opcao == "4":
            buscar_produto()
        elif opcao == "5":
            print("Saindo do sistema")
            break
        else:
            print(" Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()