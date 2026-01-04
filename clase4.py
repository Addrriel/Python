# 1. Declara una variable text con la frase "Aprendiendo Python" y luego imprime la longitud de la cadena usando len().
text = "Aprendiendo Python"
print(len(text))

#--------------------------------------------------------------------------------------------------------------------------------

# 2. Concatena dos cadenas: "Hola" y "Python", y muestra el resultado en una sola lí­nea.
print("Hola" + "Python")

#--------------------------------------------------------------------------------------------------------------------------------

# 3. Crea una cadena que incluya un salto de lí­nea, y luego imprí­mela para ver el resultado.
print("Hola papus \nadios, papus")


#--------------------------------------------------------------------------------------------------------------------------------

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
name = "Alejandro"
lastname= "Bedoya"
age= 23
print(f"Mi nombre es {name} {lastname} y tengo {age} años.")


#--------------------------------------------------------------------------------------------------------------------------------

# 5. Desempaqueta los caracteres de la palabra "Python" en variables separadas y luego imprí­melos uno por uno.
variableEjemplo = "Python"
a,b,c,d,e,f = variableEjemplo
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


#--------------------------------------------------------------------------------------------------------------------------------

# 6. Extrae un slice de la palabra "Programación" para obtener los caracteres desde la posición 3 hasta la 7.
lenguaje = "Programación"
lenguaje_deslice = lenguaje[3:7]
print(lenguaje_deslice) #gram


#--------------------------------------------------------------------------------------------------------------------------------

# 7. Invierte la cadena "Python" usando slicing y muestra el resultado.
programasao = "Python"
reverso = programasao[::-1]
print(reverso)

#--------------------------------------------------------------------------------------------------------------------------------

# 8. Convierte la cadena "aprendiendo python" en mayúsculas usando el método adecuado e imprí­mela.
cadenaLarga = "aprendiendo python"
print(cadenaLarga.upper())


#--------------------------------------------------------------------------------------------------------------------------------

# 9. Cuenta cuántas veces aparece la letra on en la cadena Programacion en Python.
cadenaMediana = "Programacion en Python"
print(cadenaMediana.count("on"))


#--------------------------------------------------------------------------------------------------------------------------------

# 10. Verifica si la cadena "12345" es numérica usando el método adecuado e imprime el resultado.
numericString = "12345"
print(numericString.isnumeric())


#--------------------------------------------------------------------------------------------------------------------------------