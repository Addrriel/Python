#DICCIONARIOS

#Formas de hacer un diccionario
diccionario = dict()
print(type(diccionario))

#Es clave - valor
#clave es para strings
#Valor para números

#Ejemplo Clave
diccionarioDatos = {"Nombre": "Alejandro Bedoya",
                    "Edad": 23,
                    "Ciudad": "Quito",
                    "Dinero": 20.15}
print(len(diccionarioDatos))
#Ejemplo Valor
diccionarioValor = {1:"Adriel", 2: "Suárez"}
print(len(diccionarioValor))

#Se pueden mezclar
diccionarioMezclado = {"Pais": "Ecuador", 1: "Quito", 2: "La Carolina", "Residencia": "Casa"}
print(diccionarioMezclado)

#Se pueden hacer tipos de datos embebidos
diccionarioInterno = {
    "información": {"nombre", "apellido", "no sé que poner xd"} #set dentro de diccionario
}

print(len(diccionarioInterno))

#Para buscar por clave o valor
print(diccionarioMezclado["Pais"])#clave
print(diccionarioMezclado[2])#valor

#Cambiar el resultado
diccionarioMezclado["Pais"] = "Brazuca"
print(diccionarioMezclado) #ahora es brazuca y no Ecuador

#Para visualizar por clave (ojo, si pones el valor no funcionará; solo es la clave)
print("Quito" in diccionarioMezclado)#sale error porque es un valor
print("Pais" in  diccionarioMezclado)#sale true porque esa clave si existe

#Listado de los items
print(diccionarioMezclado.items()) #(clave: valor)

#Mostrar solo las claves
print(diccionarioMezclado.keys())

#Mostrar solo los valores
print(diccionarioMezclado.values())

#Crear un diccionario nuevo pero que no tiene valores
nuevoDiccionario = diccionarioMezclado.fromkeys(("Nombre", "Apellido", "edad", "esSapo?"))
print(nuevoDiccionario)
