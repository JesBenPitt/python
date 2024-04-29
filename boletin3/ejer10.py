numero = int(input("Ingrese un número entre 1 y 10: "))

while numero < 1 or numero > 10:
    numero = int(input("Número fuera de rango. Ingrese un número entre 1 y 10: "))

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
