venta = [32, 25, 7, 421, 24, 48, 60, 95, 300, 91]
print (venta) 

suma = sum (venta)
maximo = max (venta)
minimo = min (venta)
promedio = suma/len(venta)
print (f"La suma es: {suma}, la mayor venta es: {maximo}, la menor venta es: {minimo}")
print(f"El promedio es: {promedio}")
venta.insert(2, 29)
venta.append(121)
venta.remove(7)
print(venta)