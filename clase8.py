# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.
diccionario = {
    "name": "Alejandro Bedoya",
    "age": 23,
    "country": "Ecuador"
}

print(diccionario)

# 2. Accede al valor de la clave name en el diccionario.
print(diccionario["name"])

# 3. Añade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.
diccionario["job"] = "Programador"
print(diccionario)

# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.
diccionario["age"] = 38
print(diccionario)

# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.
del diccionario ["country"]
print(diccionario)

# 6. Crea un diccionario donde las claves sean números del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).
diccionarioNuevo = {1:1 , 2:4 , 3:9 , 4:16 , 5:25}

# 7. Verifica si la clave age estÃ¡ presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.
diccionarioEjemplo = {"name": "Brais", "age": 37, "country": "Galicia"}
print("age" in diccionarioEjemplo) #true

# 8. Imprime solo las claves del diccionario.
print(diccionarioEjemplo.keys())

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.
print(list(diccionarioEjemplo.keys()))
print(diccionarioEjemplo)

# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(),
#  asignando a todas las claves el valor "Desconocido".
diccionario10 = {"name", "age", "job"}
nuevoDiccionariox = dict.fromkeys(diccionario10, "Desconocido")
print(nuevoDiccionariox)

#Investigue que también a la primera forma de hacer un diccionario se pueden aplicar las funciones como en la linea 42
#Creamos una variable para almacenar el futuro diccionario, transformamos el set en diccionario y asiganmos a cada variable el valor 
#"Desconocido"