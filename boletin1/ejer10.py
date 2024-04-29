num = int(input("Escribe un número: "))
num2 = int(input("Escribe otro número: "))
resto = num % num2
mult = num2 - resto
print(f'Le faltan {mult} números para que {num} sea múltiplo de {num2}.')