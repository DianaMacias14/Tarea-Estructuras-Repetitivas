n = int(input("Ingrese un número: "))

suma_pares = 0
suma_impares = 0
pares = []
impares = []

for i in range(1, n + 1): 
    if i % 2 == 0:
        suma_pares = suma_pares + i 
        
    else:
        suma_impares = suma_impares + i 
        
print("Suma de pares:", suma_pares) 
print ("Suma de impares:", suma_impares)