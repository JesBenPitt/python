dia = int(input("Escribe el dia: "))
mes = int(input("Escribe el mes: "))
año = int(input("Escribe el año: "))

if dia >= 1 and dia <= 31 and mes >= 1 and mes <= 12:
    if mes == 12 and dia == 31:
        dia = 1
        mes = 1
        año = año + 1
    else:
        if dia == 31 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10):
            dia = 1
            mes = mes + 1
        else:
            if dia == 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
                dia = 1
                mes = mes + 1
            else:
                if (dia == 28 and mes == 2 and (año % 4 != 0 or (año % 100 == 0 and año % 400 != 0))) or (dia == 29 and mes == 2):
                    dia = 1
                    mes = mes + 1
                else:
                    dia = dia + 1
                if dia > 31:
                    dia = 1
                    mes = mes + 1

    print("La fecha del día siguiente es:", dia, "/", mes, "/", año)
else:
    print("La fecha no es válida.")