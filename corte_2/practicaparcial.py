#Problema: Una tienda tiene 5 productos. Pide al usuario el precio de cada uno de los 5 productos. Al finalizar, el programa debe mostrar:
#El total de la compra.
#Cuántos productos costaron más de $50,000
total_compra = 0
productos_caros = 0
for i in range(1, 6):
    precio = float(input(f"Ingrese el precio del producto {i}: "))
    total_compra += precio
    if precio > 50000:
        productos_caros += 1
print(f"la suma total es {total_compra}")
print(f"los productos que cuestas mas de 50000 son {productos_caros}")

#Problema: Un atleta corre durante 7 días. Pide al usuario cuántos kilómetros recorrió cada día. Al final, el programa debe calcular:
#El promedio de kilómetros recorridos en la semana.
#El día que más kilómetros recorrió (Pista: usa una variable maximo).

kilometros = []

for i in range (1,8):
    diarios = int(input(f"cuantos kilometros recorrio el dia {i}: "))
    kilometros.append(diarios)
promedio = sum(kilometros)/len(kilometros)
print (f"El promedio recorrido por el atleta es de {promedio}km por dia")
print(f"el dia que mas recorrio el atleta recorrio {max(kilometros)}km")

#Problema: Crea un programa que actúe como un login sencillo.
#La contraseña correcta es UAO2026.
#El programa debe pedir la contraseña al usuario.
# falla, debe decir "Contraseña incorrecta, intenta de nuevo".
#El ciclo solo termina cuando el usuario ingresa la clave correcta.

contraseña = "UAO2026"
intentos = 0
acceso = False
while intentos < 3 and acceso == False:
    clave = int(f"Intentos {intentos + 1} ingrese su clave ")
    
    if clave == contraseña:
        print("ingreso")
        acceso = True
    else:
        intentos +=1
        print(f"acceso denegado vuelva a intentar te quedan {3 - intentos}")
if not acceso:
    print("cuenta bloqueada por seguridad")

        
    