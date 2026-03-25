def simulador_poupanca(deposito, juros_mensal):
    saldo_atual = deposito
    total_juros = 0
    
    taxa_decimal = juros_mensal / 100

    print(f"\n -- Saldo durante (24 meses) -- ")

    for mes in range (1,25):
        juros_mensal = saldo_atual * taxa_decimal
        saldo_atual += juros_mensal
        total_juros += juros_mensal
        
        print(f"Mês {mes:02d}: R$ {saldo_atual:,.2f}")

    return saldo_atual , total_juros

try:
    valor_deposito = float(input("Digite o valor do deposito: R$"))
    taxa = float(input("Digite a taxa de juros mensal (%): "))
    resultado_final, juros_acumulados = simulador_poupanca(valor_deposito, taxa)

    print("-" * 36)
    print(f"✅ Saldo final após 24 meses: R$ {resultado_final:,.2f}")
    print(f"📈 Total ganho em juros: R$ {juros_acumulados:,.2f}")
    print("-" * 36)

except ValueError:
    print("Por favor, insira valores numéricos válidos.")

