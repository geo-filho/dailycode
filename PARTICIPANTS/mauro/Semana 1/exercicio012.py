def avaliar_emprestimo(valor_casa, salario, anos): 
    meses = anos * 12
    prestacao = valor_casa / meses
    limite = salario * 0.30

    if prestacao > limite:
        aprovado = False  
    else: 
        aprovado = True    
        
    return prestacao, aprovado

print("=== Sistema de Aprovação de Empréstimo Imobiliário ===")

casa = float(input("Qual o valor da casa? R$ "))
salario_mensal = float(input("Qual o seu salário mensal? R$ "))
tempo_anos = int(input("Em quantos anos pretende pagar? "))

valor_mensal, resultado = avaliar_emprestimo(casa, salario_mensal, tempo_anos)

print("-" * 30)
print(f"Valor da Prestação: R$ {valor_mensal:.2f}")

if resultado:
    print("Situação: Empréstimo APROVADO! ")
else:
    print("Situação: Empréstimo NEGADO. ")
    print(f"Motivo: A parcela excede 30% do seu salário (R$ {salario_mensal * 0.3:.2f}).")