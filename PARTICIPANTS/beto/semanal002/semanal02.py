alunos = []


def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")

    while True:
        try:
            nota1 = float(input("Digite a nota 1: "))
            nota2 = float(input("Digite a nota 2: "))
            break
        except ValueError:
            print("Digite apenas números para as notas.")

    aluno = {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2
    }

    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!\n")


def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.\n")
        return

    print("\n--- Lista de Alunos ---")

    for aluno in alunos:
        media = calcular_media(aluno["nota1"], aluno["nota2"])
        situacao = verificar_situacao(media)

        print(f"Nome: {aluno['nome']}")
        print(f"Média: {media:.2f}")
        print(f"Situação: {situacao}")
        print("----------------------")

    print()

while True:
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!\n")