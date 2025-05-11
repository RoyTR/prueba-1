def nombreDelMetodo(argumentos <opcionales>):
    mklfas
    fadf
    
    asdf
    
    asdfa
    asdfasdf
    
    adfsdfdaf
    
aca ya estoy fuera del metodo



def evaluarSiSonNumerosIguales(numero1, numero2, numero3):
    if (numero1==numero2 and numero1==numero3):
        print(f"AL buscar el mayor: los 3 son iguales")
    elif (numero1 == numero2 and numero1 != numero3):
        print(f"El primer y 2do numero son iguales")
    elif (numero1 == numero3 and numero1 != numero2):
        print(f"El primer y 3er numero son iguales")
    elif (numero2 == numero3 and numero2 != numero1):
        print(f"El 2do y 3er numero son iguales")
    
def encontrar_nro_mayor(numero1, numero2, numero3):
    if (numero1 >= numero2 and numero1 >= numero3):
        print(f"El numero mayor es: {numero1}")
    elif (numero2 >= numero1 and numero2 >= numero3):
        print(f"El numero mayor es: {numero2}")
    elif (numero3 >= numero1 and numero3 >= numero2):
        print(f"El numero mayor es: {numero3}")
    
def encontrar_nro_menor(numero1, numero2, numero3):
    if (numero1<=numero2 and numero1<=numero3):
        numeroMenor = numero1
    elif (numero2<=numero1 and numero2<=numero3):
        numeroMenor = numero2
    elif (numero3<=numero1 and numero3<=numero2):
        numeroMenor = numero3
        
    print(f"El numero menor es: {numeroMenor}")
    

nro1 = float(input("Ingrese el primer numero: "))
nro2 = float(input("Ingrese el seugndo numero: "))
nro3 = float(input("Ingrese el tercer numero: "))

evaluarSiSonNumerosIguales(nro1, nro2, nro3)
encontrar_nro_mayor(nro1, nro2, nro3)
encontrar_nro_menor(nro1, nro2, nro3)

