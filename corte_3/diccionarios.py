#clase diccionarios
#en un diccionario no se puede repetir las claves pero si los valores
estudiante ={"nombre": "julian", "edad": 17, "carrera": "ing"} #se componen por una {clave: valor}
print(estudiante["nombre"]) #Acceso a un diccionario

#dict.keys(["nombres", "edades", "carrera"])
print(estudiante.keys()) #para conocer las claves
lista_llaves = list(estudiante.keys())
print(lista_llaves)
#valores()
print("")
print(estudiante.values())#para conocer los valores
lista_valores = list(estudiante.values())
print(lista_valores)
#modificar/agregar
print("")
estudiante ["nombre"] = "salvador" #aca se modifica 
estudiante ["genero"] = "Masculino" #aca se agrega
print(estudiante)
print("")
#ejercicio
#desarrollar un programa que contenga un diccionario con la siguiente estructura un 
#diccionario q se llame vehiculos q contenga 3 clave valor kia 25 mazda 30 y toyota 40
#devolver el valor de mazda
#agregar 3 nuevos elementos al diccionario
#retornar 2 listas primera claves y segundo los valores
#retornar un true si la clave kia existe y false si no existe
print("problema")
Vehiculos = {"kia": 25, "mazda": 30, "Toyota": 40 }
print(Vehiculos["mazda"])
print("")
Vehiculos ["subaru"] = 42
Vehiculos ["lexus"] = 12
Vehiculos ["BMW"] = 33
print(Vehiculos.keys())
print(Vehiculos.values())
print("¿kia existe en el diccionario?")
if "kia" in Vehiculos:
    print(True)
else:
    print(False)

#ejercicio 2
#desarrollar un programa que permita recivir un str atraves del teclado en seguida se debera crear un diccionario que almacene la cantidad
#de veces q aparece cada una de las letras q contega el str
#investigar la palabra from.kets()
print("")
print("ejercicio 1")
keys = input("ingrese una palabra: ").split()
for i in
valure = 1 
diccionario = dict.fromkeys(keys, valure)
print(diccionario)


