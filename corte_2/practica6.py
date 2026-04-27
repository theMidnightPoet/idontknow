#Lista vacia
numero = [] 
cantidad = int(input("Ingrese la cantidad: "))

#for
for i in range (cantidad):
    num = int(input("Ingrese el valor: ")) #Este nos permite ingresar cada valor a la lista
    numero.append(num) #adicione temporalmente en la variable numero lo q esta en num


#Recorrer con el for y sumar
suma = 0
for j in numero:
    suma = suma + j
print (f"Los valores que estan en el arreglo son: {numero}")


promedio = suma / cantidad #sobre "cantidad" pq es la q tiene el tamaño del arreglo
print (f"El promedio es {promedio}")
