n = int(input("Ingrese un número: "))
conteo_primos = 0

print(f"Números primos hasta {n}:")
for num in range(1, n + 1):
    es_primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"{num} (primo)")
        conteo_primos += 1
    else:
        print(f"{num} (no primo)")

print(f"\nHay {conteo_primos} números primos y {n - conteo_primos} números no primos hasta {n}.")