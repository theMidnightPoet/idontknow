libros = {}
usuarios = {}
menu = 0

while menu != 7:
    print("------Bienvenido al Menu------")
    print("1. Registrar Libro")
    print("2. Registrar Usuario")
    print("3. Prestar Libro")
    print("4. Devolver Libro")
    print("5. Consultar Libros por Categoría")
    print("6. Consultar Libros de Usuario")
    print("7. Salir")
    
    menu = input("Elige una opción: ")
    
    if menu == "1":
        
        id_libro = input("ID libro: ")
        
        if id_libro in libros:
            print("El Libro ya existe")
            
        
        else:
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            copias = int(input("Copias Disponibles: "))
            
            libros [id_libro] = {"titulo" : titulo, "autor" : autor, "categora": categoria, "copias_disponibles" : copias}
            
            print(libros)
            ("Libro Registrado")
            
    
    elif menu == "2":
        
        id_usuario = input("ID usuario: ")
        
        if id_usuario in usuarios:
            
            print("El usuario ya existe")
            
        else:
            nombre = input("Nombre: ")
            
            usuarios[id_usuario] = {"nombre": nombre, "libros_prestados": []}
            
            print("usuario registrado")
			


