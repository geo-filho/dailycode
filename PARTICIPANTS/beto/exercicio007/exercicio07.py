def converterMilimetros(metros):
    return metros * 1000

metros = float(input("Digite o valor em metros: "))

resultado = converterMilimetros(metros)

print(f"{metros} metros = {resultado} milímetros")