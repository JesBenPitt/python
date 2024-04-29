import random

oculto=random.randrange(1,100)

salir=int((-1))

num=0

while (num >= salir or num==oculto):
    num=int(input("dame un numero: "))

    if(num > oculto):
        print(f"{num} es mayor")
    elif(num == oculto):
        print("ganaste")
        break
    else:
        print(f"{num} es menor")
