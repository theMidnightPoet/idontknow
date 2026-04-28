libros = {}
usuarios = {}
menu = 0

while menu != "6":
    print("----- BIBLIOTECA DIGITAL -----")
    print("1. Registrar Libro")
    print("2. Registrar Usuario")
    print("3. Prestar Libro")
    print("4. Devolver Libro")
    print("5. Consultar")
    print("6. Salir")

    menu = input("Elige una opción: ")

    if menu == "1":

        id_libro = input("ID libro: ")

        if id_libro in libros:

            print("El libro ya existe.")

        else:

            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            copias = int(input("Copias disponibles: "))

            libros[id_libro] = {
                "titulo": titulo,
                "autor": autor,
                "categoria": categoria,
                "copias_disponibles": copias
            }

            print("Libro registrado correctamente.")

    elif menu == "2":

        id_usuario = input("ID usuario: ")

        if id_usuario in usuarios:

            print("El usuario ya existe.")

        else:

            nombre = input("Nombre: ")

            usuarios[id_usuario] = {
                "nombre": nombre,
                "libros_prestados": []
            }

            print("Usuario registrado correctamente.")


    elif menu == "3":

        id_usuario = input("ID usuario: ")
        id_libro = input("ID libro: ")

        if id_usuario not in usuarios:
            print("Usuario no existe.")

        elif id_libro not in libros:
            print("Libro no existe.")

        else:

            if libros[id_libro]["copias_disponibles"] > 0:

                # Duplicados pedorros
                if id_libro not in usuarios[id_usuario]["libros_prestados"]:

                    usuarios[id_usuario]["libros_prestados"].append(id_libro)
                    libros[id_libro]["copias_disponibles"] -= 1
                    print("Libro prestado correctamente.")

                else:
                    print(" El usuario ya tiene este libro.")

            else:
                print(" No hay copias disponibles.")

    elif menu == "4":

        id_usuario = input("ID usuario: ")
        id_libro = input("ID libro: ")

        if id_usuario not in usuarios:

            print("Usuario no existe.")

        elif id_libro not in libros:

            print("Libro no existe.")

        else:
            if id_libro in usuarios[id_usuario]["libros_prestados"]:

                usuarios[id_usuario]["libros_prestados"].remove(id_libro)
                libros[id_libro]["copias_disponibles"] += 1
                print("Libro devuelto correctamente.")

            else:

                print("El usuario no tiene ese libro.")


    elif menu == "5":

        sub = 0

        while sub != "3":

            print("--- CONSULTAS ---")
            print("1. Libros por categoría")
            print("2. Libros de usuario")
            print("3. Volver")

            sub = input("Elige una opción: ")


            if sub == "1":

                categoria = input("Categoría: ")

                print("Libros encontrados:")
                encontrado = False

                for libro in libros.values():

                    if libro["categoria"].lower() == categoria.lower():

                        print(f"- {libro['titulo']} (Disponibles: {libro['copias_disponibles']})")
                        encontrado = True

                if not encontrado:

                    print("No hay libros en esa categoría.")


            elif sub == "2":

                id_usuario = input("ID usuario: ")

                if id_usuario not in usuarios:

                    print("Usuario no existe.")

                else:
                    print(f" Libros de {usuarios[id_usuario]['nombre']}:")

                    if len(usuarios[id_usuario]["libros_prestados"]) == 0:
                        print("No tiene libros prestados.")

                    else:
                        for id_libro in usuarios[id_usuario]["libros_prestados"]:
                            print("-", libros[id_libro]["titulo"])

            elif sub == "3":
                print("Volviendo al menú principal...")

            else:
                print("Opción inválida.")


    elif menu == "6":
        print("Saliendo del sistema...")

    else:
        print("Opción inválida.")