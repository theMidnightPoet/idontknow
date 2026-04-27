compras = []
compras.append("azucar")
compras.append("leche")
compras.append("sal")
compras.append("pan")
compras.append("tomate")
print(compras)
compras.remove ("leche")
print (min(compras))
print (max(compras))
print(f"cuenta con {len(compras)} elementos en su compra los cuales son {compras}")
#lista de notas2
notas = []
nota1 = int(input("Escriba su primera nota: "))
notas.append(nota1)
nota2 = int(input("EScriba su segunda nota: "))
notas.append(nota2)
nota3 = int(input("Escriba su tercer nota: "))
notas.append(nota3)
nota4 = int(input("Escriba su cuarta nota: "))
notas.append(nota4)
nota5 = int(input("Escriba su quinta nota: "))
notas.append(nota5)
if sum(notas) > 0:
    promedio = sum(notas)/len(notas)
else:
    promedio = 0
print (f"La nota mas alta es {max(notas)}")
print (f"La nota mas baja es {min(notas)}")
print (f"El promedio de sus notas es {promedio}")
print(f"Tus notas fueron {notas}")
notas.remove (min(notas))
print(f"Tus notas menos la nota mas baja {notas}")