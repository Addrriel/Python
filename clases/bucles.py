# BUCLES - LOOPS

#Es un mecanimos que nos permite repetir algo

#BUCLE WHILE

condicion1 = 0

#Mientras condicion1 sea menor a 10
while condicion1 < 10: #entonces
    #Se suma 1
    condicion1+=1 #se autoincrementa
    #se imprime el resultado 
    print(condicion1)

print("Ya se detuvo el bucle y el código continua ")

#a un bucle while se le puede meter un else
while condicion1 < 10: #entonces
    #Se suma 1
    condicion1+=1 #se autoincrementa
    #se imprime el resultado 
    print(condicion1)
else:
    print("Mi condición es igual o mayor que 10")

print()

#BUCLE FOR
#se repite tantas veces como elementos tengamos iterables
lista_ejemplo = [1,2,3,4,5,6,7,8]

#for variable in variable o cosa que queramos recorrer
for element in lista_ejemplo:
    print(element) #Estamos recorriendo toda la lista

tupla_ejemplo = ("hola", "soy", "Goku")
set_ejemplo = {"Hola", "soy", "vegeta"}
diccionario_ejemplo = {"nombre": "Goku", "apellido": "Son", "edad": 43}

#recorremos toda la tupla
for elementTuple in tupla_ejemplo:
    print(elementTuple)
#recorremos todo el set
for elementSet in set_ejemplo:
    print(elementSet)
#En este diccionario por default se escriben las claves
for elementDict in diccionario_ejemplo:
    print(elementDict)
#Si añadimos el método "values()" podremos mostrar los valores
for elementDictValores in diccionario_ejemplo.values():
    print(elementDictValores)


