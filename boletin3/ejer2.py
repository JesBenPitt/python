edades = []
total_alumnos = 0

edad = int(input("Ingresa la edad del alumno (ingresa un número negativo para salir): "))

while edad >= 0:
    edades.append(edad)
    total_alumnos += 1
    edad = int(input("Ingresa la edad del alumno (ingresa un número negativo para salir): "))

if total_alumnos > 0:
    suma_edades = sum(edades)
    media_edades = suma_edades / total_alumnos

    print("\nResumen:")
    print(f"Número total de alumnos: {total_alumnos}")
    print(f"Suma de edades: {suma_edades}")
    print(f"Media de edades: {media_edades}")
else:
    print("No se ingresaron edades.")
 
