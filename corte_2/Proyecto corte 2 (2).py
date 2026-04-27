print("******REGISTRO******")
print("Por favor regístrese para iniciar.")

usuario_valido = False
password_valido = False

while not usuario_valido:
    nombre_usuario = input("Ingrese su nombre de usuario: ")   
    if nombre_usuario.isalnum():
        usuario_valido = True
        print("Usuario válido.")
    else:
        print("Error: el usuario debe ser alfanumérico (solo letras y números).")
while not password_valido:
    password_registro = input("Ingrese su contraseña (8 a 12 caracteres): ")
    largo = len(password_registro)
    if largo >= 8 and largo <= 12:
        password_valido = True
        print("Contraseña válida y registrada.")
    else:
        print(f"Error: Su contraseña tiene {largo} caracteres. Debe tener entre 8 y 12.")
Usuario = [nombre_usuario, password_registro]

Iniciar_Sesion = 0
while Iniciar_Sesion == 0:
    print("" "")
    print("Porfavor Inicie Sesion")
    print("" "")
    Inicio_Sesion = [input(), input()]
    if Inicio_Sesion[0] == Usuario[0] and Inicio_Sesion[1] == Usuario[1]:
        Iniciar_Sesion = 1
        print("Sus Credenciales son correctas")
    else:
        Iniciar_Sesion = 0
        print("Sus Credenciales son incorrectas, por favor inicie sesion nuevamente")

menu = 0
Laptops = 0
Tablets = 0
Proyectores = 0

while menu != "3":

    print("" "")

    print("""Que opción desea realizar
    1. Registrar Préstamo de equipos
    2. Estadísticas de préstamos
    3. Salir del programa""")
    
    print("" "")

    menu = input()

    if menu == "1":

        registro = "s"

        while registro != "d":
            print("" "")

            print("***********Registro**********")
            print("" "")

            print("""
        a. Prestar Laptops
        b. Prestar Tablets
        c. Prestar Proyectores
        d. Salir""")
            print("" "")
            registro = input()


            if registro == "a":
                print("Cantidad de laptops prestadas")
                print("" "")

                cantidad = int(input())
                Laptops += cantidad

                print("" "")
                print("Cantidad de laptops prestadas registrado correctamente")

            elif registro == "b":

                print("Cantidad de tablets prestadas")

                print("" "")
        
                Cantidad = int(input())
                Tablets += Cantidad
                print("" "")
                
                print("Cantidad de tablets prestadas registrado correctamente")

            elif registro == "c":

                print("Cantidad de proyectores prestados")

                print("" "")
                CAntidad = int(input())
                Proyectores += CAntidad

                print("" "")
                
                print("Cantidad de proyectores prestados registrado correctamente")
            elif registro != "a" and registro != "b" and registro != "c" and registro != "d":
                print("Porfavor Seleccione una de las opciones correspondientes")

    elif menu == "2":

        estadisticas = "s"

        while estadisticas != "d":

            print("" "")

            print("********Estadísticas**********")

            print("""
        a. Total laptops prestadas
        b. Total tablets prestadas
        c. Total proyectores prestados
        d. Salir
            """)

            print("" "")

            estadisticas = input()

            if estadisticas == "a":
                print(f"El total de laptops prestadas es de {Laptops} ")

            elif estadisticas == "b":
                print(f"El total de tablets prestadas es de {Tablets} ")

            elif estadisticas == "c":
                print(f"El total de proyectores prestados es de {Proyectores} ")

            elif estadisticas != "a" and estadisticas != "b" and estadisticas != "c" and estadisticas != "d":
                print("Porfavor Seleccione una de las opciones correspondientes")

    elif menu == "3":

        print("" "")

        print("Saliendo del programa......")





