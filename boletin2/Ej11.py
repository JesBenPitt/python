hora = int(input("Escribe la hora: "))
minu = int(input("Escribe los minutos: "))
seg = int(input("Escribe los segundos: "))

seg = seg + 1

if seg >= 60: 
    seg = 0
    minu = minu + 1

if minu >= 60:
    minu = 0
    hora = hora + 1

if hora >= 24:
    hora = 0

print(f"{hora}:{minu}:{seg}")
