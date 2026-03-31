def analisar_tempos(lista_tempos):
    if not lista_tempos:
        return 0, 0, 0
    return min(lista_tempos), max(lista_tempos), sum(lista_tempos) / len(lista_tempos)

def registrar_corrida():
    tempos = []
    print("  Analisador de Desempenho ")
    print("Instira os tempos (ou 0 para parar)")


    while True:
        try:
           
            entrada = input("Tempo (seg): ").strip()
            
           
            if not entrada:
                continue 
                
            tempo = float(entrada)

           
            if tempo == 0:
                print("Finalizando inserção")
                break 

            if tempo > 0:
                tempos.append(tempo)
            else:
                print("Digite um valor maior que zero.")

        except ValueError:
            print("Digite apenas números válidos.")

    if tempos:
        melhor, pior, media = analisar_tempos(tempos)
        print(f"\nResultados:\nMelhor: {melhor}s | Pior: {pior}s | Média: {media:.2f}s")
    else:
        print("\nNenhum tempo foi registrado.")

registrar_corrida()