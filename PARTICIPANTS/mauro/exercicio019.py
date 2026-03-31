def verificar_senha(senha):
   
    senha = senha.strip()
    
   
    tem_tamanho = len(senha) >= 8
    tem_numero = any(char.isdigit() for char in senha)
    tem_maiuscula = any(char.isupper() for char in senha)

   
    if tem_tamanho and tem_numero and tem_maiuscula:
        return "Senha forte"
    else:
      
        faltantes = []
        if not tem_tamanho: faltantes.append("mínimo 8 caracteres")
        if not tem_numero: faltantes.append("pelo menos um número")
        if not tem_maiuscula: faltantes.append("pelo menos uma letra maiúscula")
        return f"Senha fraca (Falta: {', '.join(faltantes)})"


print(" Validador de Senha Segura ")
senha_usuario = input("Digite a senha para validação: ")


if not senha_usuario.strip():
    print("\n A senha não pode ser composta apenas por espaços ou estar vazia!")
else:
    resultado = verificar_senha(senha_usuario)
    print(f"\nResultado da análise: {resultado}")