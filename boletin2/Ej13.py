semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
num = (int(input("Escribe un número del 1 al 7: ")))
if 1 <= num <= 7:
    print(semana[num - 1])