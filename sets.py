#SET
#Es un conjunto de datos
#Se diferencian porque no es una estructura ordenada y tampoco se pueden repetir los datos
#Se usa cuando necesites una colección sin orden, sin duplicados y para hacer operaciones de conjuntos (unión, intersección, etc.).

primerSet = set()
segundoSet = {"Primer Dato", "Segundo dato"} #El diccionario no tiene los datos seguidos, es un conjunto de datos
tercerSet = {} #Diccionario
print(type(primerSet))
print(type(segundoSet))
print(type(tercerSet))

#Length par alos elementos dentro
print(len(segundoSet))

#Añadir un elemento al inicio
primerSet.add("Primer Dato")
print(primerSet)

#Verificar que el dato existe
print("Primer Dato" in segundoSet)#Verdadero porque si hay eso
print("Tercer Dato" in segundoSet)#Falso porque nunca se añadió ni escribió eso

#Eliminar un dato
primerSet.remove("Primer Dato")
print(primerSet)

#Borrar todos los elementos del set
cuartoSet = {1,2,3,4,5,6,7}
cuartoSet.clear() #Borramos los datos dentro del set
print(cuartoSet)
print(len(cuartoSet)) #Saldrá 0 porque no tiene valores dentro

#Unir dos sets
setPrueba = {"tu", "ñaña"}
setPrueba2 = {"calla", "sapo"}
unionSets = setPrueba.union(setPrueba2)
print(unionSets)

#Quitamos los elementos
print(unionSets.difference(setPrueba2))