calificaciones = []

for _ in range(5):
    calificacion = float(input("Ingrese la calificación del alumno: "))
    calificaciones.append(calificacion)

if any(calificacion < 5 for calificacion in calificaciones):
    print("Hay al menos un suspenso.")
else:
    print("No hay suspensos.")
