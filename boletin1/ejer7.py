import math
diametro = float(input("Escribe el diámetro del circulo: "))
radio = diametro/2
per = (2*math.pi)*radio
area = math.pi*(radio**2)
print(f'El perímetro del circulo es: {per}')
print(f'El área del circulo es: {area}')