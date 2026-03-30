def verificar_senha(senha):
    tem_numero = False
    tem_maiuscula = False

    
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
        if caractere.isupper():
            tem_maiuscula = True

   
    if len(senha) >= 8 and tem_numero and tem_maiuscula:
        return "Senha forte"
    else:
        return "Senha fraca"



senha = input("Digite uma senha: ")
resultado = verificar_senha(senha)

print(resultado)