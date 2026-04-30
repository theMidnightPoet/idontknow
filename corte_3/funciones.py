#funciones en pythone
#la palabra reservada es def 
#tiene la siguiente sintax 
def nombredelafuncion ():
##instrucciones
    pass
#nombredelafuncion() #aca se esta llamando la funcion para que se ejecute
#van a consultar sobre las funciones sin parametros y con parametros, con 3 parametros.
#tambien utilizando return
# función sin parámetros o retorno de valores
def diHola():
  print("Hello!")

diHola()  # llamada a la función, 'Hello!' se muestra en la consola

# función con un parámetro
def holaConNombre(name):
  print("Hello " + name + "!")

# esta es una función básica de suma
def suma(a, b):
  return a + b

result = suma(1, 2)
# result = 3