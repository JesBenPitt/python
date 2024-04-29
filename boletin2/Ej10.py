dia = int(input("Escribe el dia: "))
mes = int(input("Escribe el mes: "))
año = int(input("Escribe el año: "))

fecha = True

if mes >= 1 and mes <= 12:
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        fecha = dia >= 1 and dia <= 30
    else:
        if mes == 2:
            fecha = dia >= 1 and dia <= 28
        else:
            fecha = dia >= 1 and dia <= 31

if fecha:
    print("La fecha es correcta")
else:
    print("La fecha es incorrecta")
    