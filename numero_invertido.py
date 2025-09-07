num = int(input("Ingresa un número: "))
invertir = 0

while num > 0:
    digitos = num % 10 #Para obtener el ultimo digito
    invertir = invertir * 10 + digitos 
    num //= 10

print("El número invertido es: ",invertir)