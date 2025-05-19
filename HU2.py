def sumar_numeros():
    suma = 0
    numero = int(input("Ingrese un número (0 para salir): "))

    if numero != 0:
        suma += numero
        
    while numero != 0:
        numero = int(input("Ingrese un número (0 para salir): "))
        #numero=9
        suma += numero
        #suima dice: voy a sumar 0+9

    return suma

resultado = sumar_numeros()
print(f"La suma total es {resultado}.")