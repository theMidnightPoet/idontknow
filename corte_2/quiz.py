#1.	Lista de edades 
#Crea un programa que:
#a.	Pida al usuario cuantas edades desea ingresar
#b.	Guarde las edades en una lista 
#c.	Recorra la lista con un  for
#d.	Muestre cada edad 
#e.	Indique cuantas personas son mayores de 18 años

Edades = []
cantidad = int(input("Ingrese la cantidad de las edades: "))

for i in range (cantidad):
    num = int(input("Ingrese el valor: "))
    Edades.append(num)
print (f"Las edades registradas son: {Edades}")

mayor = 0
for e in Edades:
    if e >= 18:
        mayor = mayor + 1
print (f"las cantidad de personas mayores de edad son {mayor}")


#2.	Lista de compras
#Crea un programa que:
#a.	Pida al usuario cuantos productos desea ingresar
#b.	Solicite el nombre de cada producto y lo guarde en una lista
#c.	Recorra la lista con un for
#d.	Muestre todos los productos ingresados
#e.	Muestre el total de los productos

compras = []
cantidad = int(input("Ingrese la cantidad de productos: "))

for i in range (cantidad):
    cosas = str(input("Ingrese los productos que desea comprar: "))
    compras.append(cosas)
print (f"Los productos resistrados son: {compras}")
print (f"La cantidad de productos ingresados son {len(compras)}")
 
 
#3.	Números positivos y negativos
#Crea un programa que:
#a.	Pida al usuario cuantos números desea ingresar
#b.	Guarde los números en una lista
#c.	Recorra la lista con un for
#d.	Cuente cuantos números son positivos y cuantos son negativos
#e.	Muestre el resultado final

numeros = []
cantidad = int(input("Ingrese la cantidad de numeros que desea ingresar: "))

for i in range (cantidad):
    num = int(input("Ingrese los valores: "))
    numeros.append(num)
print (f"Los numeros registrados son {numeros}")

Positivos = 0
for p in numeros:
    if p > -1:
        Positivos = Positivos + 1

negativos = 0
for n in numeros:
    if n < 0:
        negativos = negativos + 1
print (f"Hay {Positivos} numeros positivos")
print (f"Hay {negativos} numeros negativos")
