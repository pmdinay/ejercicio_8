"""" Ejercicio 8"""

import Persistencia_json as Pj

coches = list()
nombre_arch = input("¿Como quieres que se llame el archhivo creado?: ")

while True:
    marca_coche = input("De que marca es el coche?: ")
    if marca_coche == "fin":
        break
    modelo = input("Cual es el modelo?: ")
    combustible = input("Tipo de combustible: ")
    cilindrada = input("Cual es la cilindrada del vehículo?: ")
#crear diccionario vacío.
    linea = {}
#Añadimos cada apartado del diccionario.
    linea["Marca coche"] = marca_coche
    linea["Modelo del coche"] = modelo
    linea["Combustible"] = combustible
    linea["Cilindrada"] = cilindrada

#Añadimos el diccionario a la lista.
    coches.append(linea)

Pj.store(coches, nombre_arch)
coches = [] #vaciamos la lista
print("\ncoches:\n", coches)
coches = Pj.retrieve(nombre_arch)
print("Coches de la lista: ", coches) #Hacemos print de la lista