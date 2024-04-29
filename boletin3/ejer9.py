altura_arbol = int(input("Ingrese la altura del árbol en centímetros (ingrese -1 para finalizar): "))
arboles = []

while altura_arbol != -1:
    arboles.append(altura_arbol)
    altura_arbol = int(input("Ingrese la altura del árbol en centímetros (ingrese -1 para finalizar): "))

arbol_mas_alto = max(arboles)
print(f"El árbol más alto tiene {arbol_mas_alto} centímetros.")
