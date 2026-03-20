def calcularTotalSegundos(dias, horas, minutos, segundos):

    SEGUNDOS_POR_MINUTO = 60
    SEGUNDOS_POR_HORA = 3600
    SEGUNDOS_POR_DIA = 86400

    total = (dias * SEGUNDOS_POR_DIA) + (horas * SEGUNDOS_POR_HORA) + (minutos * SEGUNDOS_POR_MINUTO) + segundos

    return total

d = (int(input("Quantidade de Dias: ")))
h = (int(input("Quantidade de Horas: ")))
m = (int(input("Quantidade de Minutos: ")))
s = (int(input("Quantidade de Segundos: ")))

resultado_total = calcularTotalSegundos(d, h, m, s)

print(f"O total é {resultado_total } segundos. ")