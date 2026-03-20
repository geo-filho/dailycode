def converterMilimetros(metros):
    milimetros = metros * 1000
    return milimetros

entrada = input("Digite o valor em metros: ")

valor_metros = float(entrada)

resultado = converterMilimetros(valor_metros)

print(f"Esse valor em metros {valor_metros}M equivale a {resultado}MM")
