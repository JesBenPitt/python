num = int(input("Escribe un número: "))

if 0 <= num <= 99:
    if num == 11:
        print('once')
    elif num == 12:
        print('doce')
    elif num == 13:
        print('trece')
    elif num == 14:
        print('catorce')
    elif num == 15:
        print('quince')
    else:
        num2 = num % 10
        num1 = int(num / 10)
        if num1 == 1:
            num1 = "Diez"
        elif num1 == 2:
            num1 = "Veinte"
        elif num1 == 3:
            num1 = "Treinta"
        elif num1 == 4:
            num1 = "Cuarenta"
        elif num1 == 5:
            num1 = "Cincuenta"
        elif num1 == 6:
            num1 = "Sesenta"
        elif num1 == 7:
            num1 = "Setenta"
        elif num1 == 8:
            num1 = "Ochenta"
        elif num1 == 9:
            num1 = "Noventa"
        else:
            num1 = None

        if num2 == 1:
            num2 = "uno"
        elif num2 == 2:
            num2 = "dos"
        elif num2 == 3:
            num2 = "tres"
        elif num2 == 4:
            num2 = "cuatro"
        elif num2 == 5:
            num2 = "cinco"
        elif num2 == 6:
            num2 = "seis"
        elif num2 == 7:
            num2 = "siete"
        elif num2 == 8:
            num2 = "ocho"
        elif num2 == 9:
            num2 = "nueve"


        if num1 is not None and num2 != 0:
            print(f"{num1} y {num2}")
        elif num1 is not None and num2 == 0:
            print(f"{num1}")
        else:
            print(f"{num2}")
