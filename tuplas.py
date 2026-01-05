#TUPLAS

#Se hace con los ()
#Una tupla es un conjunto de valores

primeraTupla = ()
segundaTupla = tuple()

#Ejemplo
informacionTuple = ("Alejandro", "Bedoya", 23, 23, "blanco")
print(informacionTuple)
print(type(informacionTuple))

#Buscar por índice
print(informacionTuple[0]) #Alejandro
print(informacionTuple[-1])# 23

#Conteo de veces count()
print(informacionTuple.count(23))

#Podemos ver en qué índice está
print(informacionTuple.index("blanco"))


#Una tupla es inmutable, es decir, no se podrá cambiar el valor posteriormente
edades = (23,40,11,68)
print("edades:", edades)

#Se puede concatenar las tuplas (ojo, es una nueva tupla la que se crea, no se puede modificar las anteriores en el code)
tuplaMezclada = informacionTuple + edades
print(tuplaMezclada)

#Buscar entre atributos
print(tuplaMezclada[3:6]) #23 blanco 23

#Se puede modificar el tipo
transformacionLista = list(tuplaMezclada)
print(transformacionLista)
print(type(transformacionLista))
#recordemos que una lista si se puede modificar
transformacionLista[2] = "Cambie el 23"
print(transformacionLista)

#Si queremos volver hacerle una tupla, entonces
print(tuple(transformacionLista))


