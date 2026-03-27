def inverter_texto(texto):
    return texto[::-1]


entrada = input("Digite uma palavra ou frase: ")

resultado = inverter_texto(entrada)

print("Texto invertido:", resultado)