def calcularMedia(materia1, materia2, materia3):
    media_final = (materia1 + materia2 + materia3) / 3

    print(f" A sua média final foi: {media_final:.2f}")

    if media_final > 7:
        return "Aluno Foi aprovado!!!!!"
    else:
        return "Aluno foi Reprovado!!!!!"
    
try:

    materia1 = float(input("Digite a sua nota da materia 1: "))
    materia2 = float(input("Digite a sua nota da materia 2: "))
    materia3 = float(input("Digite a sua nota da materia 3: "))

    resultado = calcularMedia(materia1, materia2, materia3)

    print(f"Seu resultado foi: {resultado}")

except ValueError:
    print("Erro: use ponto para casas decimais")