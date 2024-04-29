num=int(input("dame un numero: "))
while ( num != 0):

    cuadrado=num**2

    p=num%2

    if (p==0):
        print("es par")
    else:
        print("es impar")

    print( f"su cuadrado es {cuadrado}")

    if (num>0):
        print("es positivo")
    else:
        print("es negativo")
    num=int(input("dame un numero: "))




