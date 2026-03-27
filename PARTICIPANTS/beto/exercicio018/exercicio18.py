def inverter_texto(texto):
    return texto[::-1]


texto = input("Digite uma palavra ou frase: ")

resultado = inverter_texto(texto)

print("Texto invertido:", resultado)