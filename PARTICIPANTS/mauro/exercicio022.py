def analisar_avaliacoes(lista_notas):
    if not lista_notas:
        return 0, 0, 0
    
    quantidade = len(lista_notas)
    media = sum(lista_notas) / quantidade
    

    acima_da_media = len([nota for nota in lista_notas if nota > media])
    
    return media, quantidade, acima_da_media

def sistema_filmes():
    notas = []
    print(" Avaliador de Filmes ")
    print("Insira as notas de 0 a 10 (ou digite -1 para encerrar)")

    while True:
        try:
            entrada = float(input("Nota do filme: "))
            
            if entrada == -1:
                break
            
            if 0 <= entrada <= 10:
                notas.append(entrada)
            else:
                print(" insira uma nota entre 0 e 10.")
        except ValueError:
            print(" Digite apenas números.")

   
    if notas:
        media, total, acima = analisar_avaliacoes(notas)
        
        print("\nResultado da Análise ")
        print(f"Total de filmes avaliados: {total}")
        print(f"Média das notas: {media:.2f}")
        print(f"Filmes com nota acima da média: {acima}")
    else:
        print("\nNenhuma nota foi registrada.")

if __name__ == "__main__":
    sistema_filmes()