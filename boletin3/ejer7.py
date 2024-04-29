num = 1

for i in range(1, 20, 1):
    resto = i % 2
    if resto != 0:
        num *= i
        print(i)
    
print(f'El producto de los 10 primeros números impares es: {num}')