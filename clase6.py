# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e impí­mela.
primeraTupla = (10,20,30,40,50)
print(primeraTupla)

# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muéstralo.
segundaTupla = (100, 200, 300, 400, 500)
print(segundaTupla[1])

# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.
"""
No se puede modificar, las tuplas son inmutables

"""
# 4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3).
terceraTupla = (1, 2, 3, 3, 4, 5, 3)
print(terceraTupla.count(3))

# 5. Encuentra el í­ndice de la primera aparición de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").
cuartaTupla = ("Java", "Python", "JavaScript", "Python")
print(cuartaTupla.index("Python"))

# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
sumaTuplas = tupla1 + tupla2
print(sumaTuplas)

# 7. Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).
tuplaCompleta = (10, 20, 30, 40, 50)
subtupla = tuplaCompleta[1:3] #entre el 10 y el 40
print(subtupla) #20 y 30

# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista,
#  cambia el segundo elemento a "amarillo" y
#  vuelve a convertirla en una tupla.
#  Imprime la tupla resultante.

colores = ("rojo", "verde", "azul")

listaColores = list(colores)

listaColores[1] = "amarillo"

coloresTupla = tuple(listaColores)

print(listaColores)

# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.

my_tuple= ("aña")
del my_tuple
"""
La variable fue completamente borrada, no se podrá imprimir
"""

# 10. Crea una tupla con un solo elemento (el número 100) e imprí­mela.
#  Asegúrate de usar la sintaxis correcta para crear una tupla con un solo elemento.
tuplaSapa = (100,) #Se usa una coma al final para que haga referencia en una tupla
"""
Si se escribe sin la coma y vemos el type, marcará que es un entero (int)
"""
print(tuplaSapa)
