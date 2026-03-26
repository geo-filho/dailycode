def login(usuario_correto, senha_correta):
    tentativas = 0

    while tentativas < 3:
        usuario = input("Digite o usuário: ")
        senha = input("Digite a senha: ")

        if usuario == usuario_correto and senha == senha_correta:
            return "Login realizado com sucesso"
        else:
            tentativas += 1
            print("Usuário ou senha inválidos")

    return "Acesso bloqueado"


usuario_correto = input("Crie um usuário: ")
senha_correta = input("Crie uma senha: ")

resultado = login(usuario_correto, senha_correta)

print(resultado)