#função para converter metros para milímetros
def convertermilimetros(metros):
    milimetros = metros * 1000
    return milimetros

#Usuário insere a quantidade de metros e o programa converte para milímetros
metros = float(input("Digite a quantidade de metros: "))
milimetros = convertermilimetros(metros)
print(f"{metros} metros equivalem a {milimetros} milímetros.")