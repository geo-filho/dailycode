def validar_login():
    usuario = "giba"
    senha =  "maro"

    tentativas_max = 3
    tentativas_att = 0

    print("---Sistema de Entrada---")

    while tentativas_att < tentativas_max:
       
        usuario_input = input("Digite o usuário: ").strip()
        senha_input = input("Digite a senha: ").strip()
        
        if usuario_input == usuario and senha_input == senha:
            return  "Acesso concluida! Bem-vindo ao sistema."
        else:
            tentativas_att += 1
            tentativas_restantes = tentativas_max - tentativas_att
            
            if tentativas_restantes > 0:
                print(f" Usuário ou senha incorretos! Você ainda tem {tentativas_restantes} tentativa(s).")
            else:
                return "Limite de tentativas excedido!!!"

resultado = validar_login()
print("\n" + "=")
print(resultado)
print("=")