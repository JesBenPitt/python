num = int(input("Escribe un número: "))

if 0 <= num <= 9999:
    if num<10:
        print("Es capicua")
    else:
        if num<100:
            num2 = num % 10
            numalt = int(num/10)
            if numalt == num2: 
                print("Es capicua")
            else:
                print("No es capicua")
        else:
            if num<1000:
                num3 = (num % 10)
                num4 = int(num/100)
                if num3 == num4:
                    print("Es capicua")
                else:
                    print("No es capicua")
            else:
                if num<10000:
                    num5 = (num%10)
                    num6 = int(num/1000)
                    num7 = int(num/10)
                    num8 = (num7 % 10)
                    num9 = int(num/100)
                    num10 = (num9%10)
                    if num5 == num6 and num8 == num10:
                        print("Es capicua")
                    else:
                        print("No es capicua")
else:
    print("No es valido")
    