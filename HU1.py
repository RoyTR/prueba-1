#Escribe un programa que pida al usuario una palabra e imprima cuántas vocales contiene.
#Requisitos:
#Usar un ciclo for para recorrer la palabra.
#Usar if para verificar si cada letra es una vocal.
#Ejemplo:
#Entrada: "computadora"
#Salida: "La palabra tiene 5 vocales."

def contar_vocales(palabra):
    vocales = "aeiouAEIOU"
    contador = 0

    #palabra=gonzalo
    for letra in palabra:
        #letra=o
        if letra in vocales:
          #buscar o, si es que esta dentro del arreglo vocales
            contador += 1

    return contador

palabra_ingresada = input("Ingrese una palabra: ")
cantidad_vocales = contar_vocales(palabra_ingresada)
print(f"La palabra tiene {cantidad_vocales} vocales.")
