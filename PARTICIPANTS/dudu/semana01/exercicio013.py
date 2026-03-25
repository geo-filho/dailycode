def simular_poupanca():
    # Entrada de dados
    deposito_inicial = float(input("Digite o valor do depósito inicial: "))
    taxa_juros = float(input("Digite a taxa de juros mensal (%): ")) / 100

    saldo = deposito_inicial
    total_juros = 0

    # Simulação de 24 meses
    for mes in range(1, 25):
        juros = saldo * taxa_juros
        saldo += juros
        total_juros += juros

        print(f"Mês {mes}: R$ {saldo:.2f}")

    return saldo, total_juros


# Chamando a função
saldo_final, total_juros = simular_poupanca()

print("\nResultado final:")
print(f"Saldo final: R$ {saldo_final:.2f}")
print(f"Total ganho em juros: R$ {total_juros:.2f}")