def converterTempo(dias, horas, minutos, segundos):
    total = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos
    return total

dias = int(input("Digite os dias: "))
horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

total_segundos = converterTempo(dias, horas, minutos, segundos)

print("Total em segundos:", total_segundos)