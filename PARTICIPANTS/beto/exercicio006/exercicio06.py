def calcularMedia(materia1, materia2, materia3):
    media = (materia1 + materia2 + materia3) / 3
    
    if media > 7:
        return "Aluno aprovado"
    else:
        return "Aluno reprovado"

materia1 = float(input("Digite a nota da matéria 1: "))
materia2 = float(input("Digite a nota da matéria 2: "))
materia3 = float(input("Digite a nota da matéria 3: "))

print(calcularMedia(materia1, materia2, materia3))