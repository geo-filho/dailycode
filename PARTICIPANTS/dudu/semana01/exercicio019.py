def verificar_senha(senha):
    tem_tamanho = len(senha) >= 8
    tem_numero = any(char.isdigit() for char in senha)
    tem_maiuscula = any(char.isupper() for char in senha)

    if tem_tamanho and tem_numero and tem_maiuscula:
        return "Senha forte"
    else:
        return "Senha fraca"


# Programa principal
senha_usuario = input("Digite sua senha: ")
resultado = verificar_senha(senha_usuario)
print(resultado)