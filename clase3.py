
"""
1. Realiza las siguientes operaciones aritméticas:
1.1 Suma: 15 + 25
1.2 Resta: 50 - 22
1.3 Multiplicación: 8 * 7
1.4 Divisiónn: 100 / 20

"""
print()
print("EJERCICIO 1:")
print("Suma: " , 15+25)
print("Resta: ", 50-22)
print("Multiplicación", 8*7)
print("División: ", 100/20)


"""
2. Calcula el resto de la división de 37 entre 5 y almacénalo en una variable remainder. Luego imprímelo.

"""
remainder = 37%5
print()
print("EJERCICIO 2")
print(remainder)

"""
3. Convierte el número 7 en una cadena de texto y concaténalo con la frase es mi número favorito. Imprime el resultado.

"""
print()
print("EJERCICIO 3")
print(str(7), "es mi número favorito")


"""
4. Repite la palabra "Python" 10 veces usando el operador de multiplicación para cadenas y luego imprímela.

"""
print()
print("EJERCICIO 4")
print("Python" * 8)

"""
5. Crea dos variables: a y b con los valores 12 y 8 respectivamente. Compara si a es mayor que b y almacena el resultado en una variable booleana resultado. Imprime el valor de resultado.

"""
print()
a = 12
b= 8
resultado = a > b
print("EJERCICIO 5")
print(resultado)


"""
6. Compara dos cadenas de texto (apple y banana) usando los operadores > y < y explica cuál tiene mayor orden alfabético.

"""
print()
print("EJERCICIO 6")
print("apple" > "banana") #false  
print("apple" < "banana") #true 

"""
7. Realiza una comparación lógica usando and para verificar si el número 10 es mayor que 5 y menor que 20. Imprime el resultado.

"""
print()
print("EJERCICIO 7")
print(10>5 and 10<20) #si o si deben ser los dos

"""
8. Usa el operador or para verificar si el número 7 es menor que 3 o mayor que 5. Imprime el resultado.

"""
print()
print("EJERCICIO 8")
print(7<3 or 7>5) #al menos uno de los dos debe ser verdadero

"""
9. Aplica el operador not para invertir el resultado de la comparación 15 > 20. ¿Cuál es el resultado?

"""
print()
print("EJERCICIO 9")
print(not 15>20)

"""
10. Combina operadores aritméticos y lógicos: Verifica si el número resultante de la expresión (5 * 3) + 2 es mayor que 10 y menor que 20. Imprime el resultado.

"""
print()
print("Ejercicio 10")
print((5*3)+2>10 and (5*3)+2 < 20) #17 es mayor que 10 = true; 17 es menor que 20 = true; resultado = true

