nota = float(input("Escribe una nota: "))

if nota<11 and nota >= 0:
    if nota<5: 
        print("Insuficiente")
    else:
        if nota == 5:
            print("Suficiente")
        else:
            if nota == 6:
                print("Bien")
            else:
                if nota == 7 or nota == 8:
                    print("Notable")
                else:
                    if nota > 8:
                        print("Sobresaliente")
else:
    print("La nota no es valida")