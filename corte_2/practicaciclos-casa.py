#Imagina que estás en tu clase de Diseño Conceptual y necesitas evaluar la resistencia de un material. Para ello, debes simular un conteo de pruebas de presión.
#Instrucciones del ejercicio:
#Crea un ciclo que cuente del 1 al 12 (simulando 12 pruebas).
#Para cada número, el programa debe imprimir: "Realizando prueba de presión #...".
#Al finalizar el ciclo (fuera de él), debe imprimir un mensaje de cierre que diga: "Proceso de testeo finalizado con éxito".
prueba = 0
while prueba <12:
    prueba = prueba + 1
    print (f"Realizando prueba de presion # {prueba}")

print ("Proseso de testeo final realizado con exito")

