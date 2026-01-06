# 1. Crea un set con los números del 1 al 5 e imprí­melo.
numeros = {1,2,3,4,5}
print(numeros)

# 2. Añade el número 6 al set {1, 2, 3, 4, 5} e imprí­melo.
numeros.add(6)
print(numeros)

# 3. Intenta añadir el número 5 al set {1, 2, 3, 4, 5} nuevamente. ¿Qué sucede?
"""
No sucede nada, los sets no se pueden repetir así que todo quedaría igual
"""

# 4. Verifica si el número 3 está¡ en el set {1, 2, 3, 4, 5} e imprime el resultado.
print(3 in numeros) #Verdadero

# 5. Elimina el número 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.
numeros.remove(4)
print(numeros)

# 6. Usa el método clear() para vaciar un set y luego imprime su longitud.
numeros.clear()
print(len(numeros))

# 7. Convierte el set {"manzana", "naranja", "plátano"} en una lista e imprime el primer elemento de la lista.
frutas = {"manzana", "naranja", "plátano"}
frutasList = list(frutas)
print(frutasList[0])

# 8. Realiza la uniónn de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.
num1 = {1, 2, 3}
num2 = {4, 5, 6}

numUnidos = num1.union(num2)
print(numUnidos)

# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.
set1= {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.difference(set2)) #1 y 2

# 10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.
my_set = {"Me voy a borrar"}
print(my_set)
del my_set
print(my_set) #error porque no hay la variable