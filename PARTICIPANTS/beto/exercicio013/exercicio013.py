def simular_poupanca(deposito, taxa):
    saldo = deposito
    juros_total = 0

    for mes in range(1, 25):  
        juros = saldo * (taxa / 100)
        saldo += juros
        juros_total += juros

        print(f"Mês {mes}: R$ {saldo:.2f}")

    return saldo, juros_total


deposito = float(input("Digite o valor do depósito inicial: "))
taxa = float(input("Digite a taxa de juros mensal (%): "))

saldo_final, total_juros = simular_poupanca(deposito, taxa)

print("\n--- Resultado Final ---")
print(f"Saldo final: R$ {saldo_final:.2f}")
print(f"Total ganho em juros: R$ {total_juros:.2f}")