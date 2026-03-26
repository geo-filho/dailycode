def inverter_texto(texto):

    texto_invertido = texto[::-1]
    return texto_invertido


entrada_usuario = input("Digite uma palavra ou frase: ")

if entrada_usuario.strip():
    resultado = inverter_texto(entrada_usuario)
    
    print("-" * 30)
    print(f"Texto Original:  {entrada_usuario}")
    print(f"Texto Invertido: {resultado}")
    print("-" * 30)
else:
    print("Ops! Você não digitou nada.")