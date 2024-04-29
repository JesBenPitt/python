num = float(input("Escribe un número decimal: "))

if num == 0:
    print("No es casi cero")
elif -1 < num < 1:
    print("Es casi cero")
else:
    print("No es casi cero")