#função para converter segundos em dias, horas, minutos e segundos
def convertersegundos(tempo_em_segundos):
    dias = tempo_em_segundos // 86400
    horas = (tempo_em_segundos % 86400) // 3600
    minutos = (tempo_em_segundos % 3600) // 60   
    segundos = tempo_em_segundos % 60
    return dias, horas, minutos, segundos


#Usuário insere o número de segundos e o programa converte para dias, horas, minutos e segundos
segundos = int(input("Digite o número de segundos: "))
dias, horas, minutos, segundos = convertersegundos(segundos)
print(f"Isso dá {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos")