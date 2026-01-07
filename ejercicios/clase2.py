"""
# 1. Declara y asigna valores a las siguientes variables:
# name: una cadena que contenga tu nombre.
# age: un número entero que represente tu edad.
# height: un número flotante que represente tu altura.
# Imprime cada variable en una línea separada.

# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuántos aÃ±os tienes.

# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False según corresponda e imprímela.

# 4. Usa la función len() para calcular cuántos caracteres tiene tu nombre completo, almacenado en una variable.

# 5. Declara tres variables en una sola línea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.

# 6. Usa la función input() para solicitar al usuario su color favorito y almacÃ©nalo en una variable color. Luego, imprime el valor ingresado.

# 7. Declara una variable fruit e inicialízala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.

# 8. Convierte un número decimal, almacenado en la variable price, a un número entero y luego imprímelo.

# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una direcciÃ³n usando la funciÃ³n len(). Imprime el resultado.

# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurándote de que siempre será un número. Luego, cambia su valor a un número diferente y verifica el tipo de la variable con type().
"""


# 1. Declara y asigna valores a las siguientes variables:
# name: una cadena que contenga tu nombre.
# age: un número entero que represente tu edad.
# height: un número flotante que represente tu altura.
# Imprime cada variable en una línea separada.

name = "Alejandro"
age = 23
height = 1.82
print("Mi nombre es", name)
print("Mi edad es", age)
print("Mi estatura es", height, "metros")

#---------------------------------------------------------------------------------------------------
# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuántos años tienes.
edadCadena = str(age)
print("Tengo la edad de" , age , "años")

#---------------------------------------------------------------------------------------------------
# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False según corresponda e imprímela.
is_student = True
print("¿Alejandro Bedoya es un estudiante?", is_student)

#---------------------------------------------------------------------------------------------------
# 4. Usa la función len() para calcular cuántos caracteres tiene tu nombre completo, almacenado en una variable.
print(len(name)) #Tiene un total de 9 caracteres

#---------------------------------------------------------------------------------------------------
# 5. Declara tres variables en una sola línea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.
name5= "Alejandro" ; lastname5 = "Bedoya" ; city = "Quito"
print(name5, lastname5, city)

#---------------------------------------------------------------------------------------------------
# 6. Usa la función input() para solicitar al usuario su color favorito y almacénalo en una variable color. Luego, imprime el valor ingresado.
#color = input("Escribe tu color favorito: ")
#print(color) le pongo comentario para poder ver lo demás sin poner todo el rato el color

#---------------------------------------------------------------------------------------------------
# 7. Declara una variable fruit e inicialízala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.
fruit = "Mandarina"
fruit = "Manzana"
print(fruit)
#---------------------------------------------------------------------------------------------------
# 8. Convierte un número decimal, almacenado en la variable price, a un número entero y luego imprímelo.
price = 4.15
priceInt = int(price)
print(priceInt) #No devuelve decimales, solo el valor entero
#---------------------------------------------------------------------------------------------------
# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una dirección usando la función len(). Imprime el resultado.
address_len = "Carolina y Tijuana"
print("Esta dirección tiene en total",len(address_len), "caracteres")
#---------------------------------------------------------------------------------------------------
# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurándote de que siempre será un número.
# Luego, cambia su valor a un número diferente y verifica el tipo de la variable con type().
phone = float(3.14)
phone = int(12)
print(phone , type(phone))
#---------------------------------------------------------------------------------------------------


