def converterSegundos (dias, horas , minutos, segundos):
    segundos1 = dias * 86400
    segundos2 = horas * 3600
    segundos3 = minutos * 60
    segundos4 = segundos * 1

    print("Dias em segundos:", segundos1 )
    print("Horas em segundos:", segundos2 )
    print("Minutos em segundos:", segundos3 )
    print("Segundos:", segundos4 )

    total = segundos1 + segundos2 + segundos3 + segundos4
    return total

dias = int(input("Digite os Dias: "))
horas = int (input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os Segundos: "))

total = converterSegundos(dias, horas, minutos, segundos)

print("Total em segundos: ", total)