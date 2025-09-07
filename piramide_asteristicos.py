num = int(input("Ingresa la altura:"))

for i in range(1, num + 1):
    espacios = " " * (num - i) #epacios a la izquierda
    asteriscos = "*" * (2 * i - 1) #Cantidad asteriscos
    print(espacios + asteriscos)
    