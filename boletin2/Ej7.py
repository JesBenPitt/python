num1 = float(input("Escribe la número 1: "))
num2 = float(input("Escribe la número 2: "))
num3 = float(input("Escribe la número 3: "))

if num1 > num2:
    if num2 > num3:
        print(f"{num1} {num2} {num3}")
    else:
        if num1 > num3:
            print(f"{num1} {num3} {num2}")
        else:
            print(f"{num3} {num1} {num2}")
else:
    if num1 > num3:
        print(f"{num2} {num1} {num3}")
    else:
        if num2 > num3:
            print(f"{num2} {num3} {num1}")
        else:
            print(f"{num3} {num2} {num1}")