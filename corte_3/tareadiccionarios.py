libros = {}
usuarios = {}
menu = 0    

while menu !=7:
    print("------Bienvenido al Menu------")
    print("1. Registrar Libro")
    print("2. Registrar Usuario")
    print("3. Prestar Libro")
    print("4. Devolver Libro")
    print("5. Consultar...")
    print("7. Salir")
    
    menu = input("Elige una opción: ")
    
    if menu == 1:
        id_libro = input("ID libro: ")
        if id_libro in libros:
            print("El Libro ya existe")
        else:
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            copias = int(input("Copias Disponibles: "))
            # Corregido "categoria" aquí:
            libros[id_libro] = {"titulo": titulo, "autor": autor, "categoria": categoria, "copias_disponibles": copias}
            print("Libro Registrado")
            
    elif menu == 2:
        id_usuario = input("ID usuario: ")
        if id_usuario in usuarios:
            print("El usuario ya existe")
        else:
            nombre = input("Nombre: ")
            usuarios[id_usuario] = {"nombre": nombre, "libros_prestados": []}
            print("usuario registrado")
            
    elif menu == 3:
        id_usuario = input("ID usuario: ")
        id_libro = input("ID Libro: ")
        
        if id_usuario not in usuarios:
            print("Usuario No Existe")
        elif id_libro not in libros:
            print("Libro no existe")
        else: 
            if libros[id_libro]["copias_disponibles"] > 0: 
                usuarios[id_usuario]["libros_prestados"].append(id_libro)
                libros[id_libro]["copias_disponibles"] -= 1 
                print("Libro prestado")
            else:
                print("no hay copias disponibles")

    elif menu == "4":
        id_usuario = input("ID usuario: ")
        id_libro = input("ID Libro: ")
        if id_usuario not in usuarios:
            print("Usuario No Existe")
        elif id_libro not in libros:
            print("Libro no existe")
        else:
            if id_libro in usuarios[id_usuario]["libros_prestados"]:
                usuarios[id_usuario]["libros_prestados"].remove(id_libro)
                libros[id_libro]["copias_disponibles"] += 1
                print("Libro devuelto correctamente")
            else:
                print("El usuario no tiene este libro en prestamo")
   


