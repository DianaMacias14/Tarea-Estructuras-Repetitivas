contador = 0
num = int(input("Ingresa un número: "))
cadena_num = str(num)

for digito in cadena_num:
    contador = contador + 1
    
print("El número ", num,"tiene", contador,"digito(s)")