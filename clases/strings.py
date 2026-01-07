#STRINGS

unString = "Soy un string"
otroString = "Soy otro string"

#Ver la cantidad de letras
print(len(unString))

#el %s sirve para meterlo

name= "Alejandro"
surname = "Bedoya"
age = 23
#Formas de hacer print en string
print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age)) #Podemos aplicar un formato
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age)) #Podemos hacer acotaciones el %s sirve para texto y el %d sirve para números
print("Mi nombre es", name , "", surname, "y tengo", age, "años")# Print normal
print(f"Mi nombre es {name}, {surname}, y tengo {age} años") #Con esto podemos hacer un print más recomendable y fácil

#Desempaquetando paquetes
language = "Python"
a,b,c,d,e,f = language
print(a)#Saldrá por índice
print(b)#Saldrá por índice
print(c)#Saldrá por índice
print(d)#Saldrá por índice
print(e)#Saldrá por índice
print(f)#Saldrá por índice

#Salto de Línea
cadena = "Hola, este es el primer mensaje.\nY esta es la segunda línea."
print(cadena)

#División
language_slice = language[0:5] #Indice inicial que queramos : indice final que queramos
print(language_slice)

#Reverso
reversed_language = language[::-1] #Sirve para hacer el reverso
print(reversed_language)

# Funciones
print(language.capitalize()) #Sirve para hacer mayúscula en cada palabra tipo "SoyUnaPalabra"
print(language.upper()) # Sirve para poner todo en mayúsculas
print(language.count("t")) #Sirve para contar algo en específico, en este caso será la letra "t"
print(language.isnumeric()) #Sirve para decirnos si es numérico
print("23".isnumeric()) #Sirve para decirnos si es numérico
print(language.lower()) #Se pasa todo a minúsculas
print(language.startswith("Py"))#Es para ver si inicia con algo o no
#recordemos que "py" no es lo mismo que "Py", si pones py en minúsculas dará false 
print("py" == "Py")
