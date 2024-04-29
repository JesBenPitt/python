notas = [float(input(f"Ingrese la nota del alumno {i + 1}: ")) for i in range(6)]

aprobados = sum(nota >= 5 for nota in notas)
condicionados = sum(4 <= nota < 5 for nota in notas)
suspendidos = sum(nota < 4 for nota in notas)

print(f"Aprobados: {aprobados}\nCondicionados: {condicionados}\nSuspendidos: {suspendidos}")
