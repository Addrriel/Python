# 1. Crea una lista con los números del 1 al 5 e imprí­mela.
primeraLista = [1,2,3,4,5]
print(primeraLista)

# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].
listaEjercicio = [10, 20, 30, 40, 50]
print(listaEjercicio[2])

# 3. Agrega el número 6 al final de la lista [1, 2, 3, 4, 5] e imprí­mela.
listaEjercicio2 = [1, 2, 3, 4, 5]
listaEjercicio2.append(6)
print(listaEjercicio2)

# 4. Inserta el número 15 en la posición 2 de la lista [10, 20, 30, 40, 50].
listaEjercicio3 = [10, 20, 30, 40, 50]
listaEjercicio3.insert(1, 15)
print(listaEjercicio3)

# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].
listaEjercicio4 = [10, 20, 30, 30, 40, 50]
listaEjercicio4.remove(30)
print(listaEjercicio4)

# 6. Usa la función pop() para eliminar el último elemento de la lista [1, 2, 3, 4, 5] y almacénalo en una variable.
#  Imprime la variable y la lista.
listaEjercicio5 = [1, 2, 3, 4, 5]
listaEliminaPOP = listaEjercicio5.pop()
print("Lista 1:", listaEjercicio5, "; lo que borró el pop: ", listaEliminaPOP)

# 7. Invierte la lista [100, 200, 300, 400, 500] e imprí­mela.
listaEjercicio6 = [100, 200, 300, 400, 500]
listaEjercicio6.reverse()
print(listaEjercicio6)

# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprí­mela.
listaEjercicio7 = [3, 1, 4, 2, 5]
listaEjercicio7.sort() #por default es ascendente
"""
listaEjercicio7.sort(reverse=True) así sería de forma descendente
"""
print(listaEjercicio7)

# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.
lista1 = [1,2,3]
lista2 = [4,5,6]
listaJunta = lista1 + lista2
print(listaJunta)

# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50]
# que van desde la posición 1 hasta la 3 (sin incluir la posición 3).
listaCompleta = [10, 20, 30, 40, 50]
sublista = listaCompleta[1:3]
print(sublista)