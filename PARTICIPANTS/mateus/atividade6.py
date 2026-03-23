#Função para calcular a média de três matérias.
def calcularmedia(materia1, materia2, materia3):
    media = (materia1 + materia2 + materia3) / 3
    return media

#Solicitar ao usuário as notas das três matérias, chamar a função calcularmedia e exibir a média.
materia1 = float(input("Digite a nota da matéria 1: "))
materia2 = float(input("Digite a nota da matéria 2: "))     
materia3 = float(input("Digite a nota da matéria 3: "))
media = calcularmedia(materia1, materia2, materia3)
print("A média das notas é:", media)

#Verificar se a média é maior ou igual a 7 para determinar se o aluno está aprovado ou reprovado.
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")