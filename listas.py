#LISTAS

#1) Formas de hacer lista
#Una lista es un conjunto de datos
listaUno = list()
listaDos = []

print(len(listaDos))

edades = [23,22,52,56,64,60,69]
print(len(edades))

#También se pueden mezclar los tipos de datos
informacion = ["Alejandro", "Bedoya", 23, 45.32, 25, 25]
print(informacion)
print(type(informacion))

#Se puede buscar por posición
print(informacion[0]) #Alejandro
print(informacion[1]) #Bedoya
print(informacion[-1]) #45.32 ---- este sirve para buscar el final

#Se puede contar el número de veces que hay algo
print(informacion.count(25))#El 25 se repite 2 veces

#También podemos asignar variables a los valores de la tabla
nombre,apellido,edad,dinero,num1,num2 = informacion
print(nombre) #Alejandro
print(apellido) #Bedoya
print(edad) #23
print(dinero) #45.32
print(num1) #25
print(num2) #25

#Añadir nuevo elemento, siempre irá al final
informacion.append("verdura")
print(informacion)

#Para poder especificar en dónde queremos añadir
informacion.insert(2, "añadirIndice") #posición , dato
informacion.insert(3, "añadirIndice2") #posición , dato
print(informacion)

#Remover el item
informacion.remove("añadirIndice")
print(informacion)

#Remover el último valor
informacion.pop()
print(informacion)

#también se puede especificar cual quieres hacer
informacion.pop(1)
print(informacion)

#Otra manera de eliminar
del informacion[0]
print(informacion)

#Limpiar los datos de la lista
informacion.clear()
print(informacion)

#Podemos ordenar al revés
informacion = ["Alejandro", "Bedoya", 23, 45.32, 25, 25]
informacion.reverse()
print(informacion)

#otro orden
edades.sort()
print(edades)

