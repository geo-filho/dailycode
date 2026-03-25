def calcularmedia(materia1, materia2, materia3):
    media = (materia1 + materia2 + materia3) /3
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"
    
materia1 = int(input("Digite a media 1:"))
materia2 = int(input("Digite a media 2:"))
materia3 = int(input("Digite a media 3:"))

print(calcularmedia(materia1, materia2,materia3))