max_rango = int(input('Introduce el número máximo del rango: '))
min_rango = int(input('Introduce el número mínimo del rango: '))

num = int(input('Introduce un número que esté dentro del rango: '))
while num < min_rango or num > max_rango:
    num = int(input('Introduce un número que esté dentro del rango: '))
