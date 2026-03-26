def avaliar_emprestimo(valor_casa, salario, anos):
    meses = anos * 12
    prestacao = valor_casa / meses

    limite = salario * 0.3

    if prestacao > limite:
        resultado = "Empréstimo negado"
    else:
        resultado = "Empréstimo aprovado"

    return prestacao, resultado


valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite seu salário mensal: "))
anos = int(input("Digite em quantos anos deseja pagar: "))

prestacao, resultado = avaliar_emprestimo(valor_casa, salario, anos)

print(f"Prestação mensal: R$ {prestacao:.2f}")
print(resultado)