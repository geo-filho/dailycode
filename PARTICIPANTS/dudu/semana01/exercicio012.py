def avaliar_emprestimo():
    # Entrada de dados
    valor_casa = float(input("Digite o valor da casa: "))
    salario = float(input("Digite seu salário mensal: "))
    anos = int(input("Digite em quantos anos deseja pagar: "))
    
    # Cálculo do número de meses
    meses = anos * 12
    
    # Cálculo da prestação mensal
    prestacao = valor_casa / meses
    
    # Verificação (30% do salário)
    limite = salario * 0.30
    
    if prestacao > limite:
        resultado = "Empréstimo negado"
    else:
        resultado = "Empréstimo aprovado"
    
    # Retorno dos valores
    return prestacao, resultado


# Chamando a função
prestacao, resultado = avaliar_emprestimo()

print(f"Prestação mensal: R$ {prestacao:.2f}")
print(resultado)