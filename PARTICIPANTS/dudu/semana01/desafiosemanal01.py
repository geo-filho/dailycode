def login():
    # Credenciais pré-definidas
    usuario_correto = "admin"
    senha_correta = "1234"
    
    tentativas = 0
    max_tentativas = 3

    while tentativas < max_tentativas:
        usuario = input("Digite o usuário: ")
        senha = input("Digite a senha: ")

        if usuario == usuario_correto and senha == senha_correta:
            print("Login realizado com sucesso")
            return
        else:
            tentativas += 1
            print("Usuário ou senha inválidos")

    print("Acesso bloqueado")


# Chamando a função
login()