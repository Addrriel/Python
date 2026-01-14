"""
1. Usa un bucle for para imprimir todos los números impares entre 1 y 25.

2. Dada la lista ["manzana", "banana", "cereza", "pera"], usa un bucle for para imprimir cada fruta junto con su longitud (número de caracteres).

3. Escribe un programa que use un bucle while para calcular el factorial de un número n ingresado por el usuario.

4. Dada la cadena "abracadabra", usa un bucle for para contar cuántas veces aparece la letra "a".

5. Usa un bucle while para encontrar el primer número mayor que 50 que sea divisible tanto por 3 como por 5.

6. Dado el diccionario {"Juan": 15, "Ana": 22, "Luis": 19}, usa un bucle for para imprimir solo los nombres de las personas que tienen edad mayor o igual a 18.

7. Escribe un programa que use un bucle for para imprimir la tabla de multiplicar del 7 (del 1 al 10).

8. Usa un bucle while para invertir una cadena ingresada por el usuario sin usar la función [::-1].

9. Dada la lista [5, 8, 12, 3, 10], usa un bucle for para calcular la suma de los números que sean mayores a 5.

10. Escribe un programa que use un bucle for para generar y mostrar la serie de Fibonacci hasta el décimo término.
"""

#Usa un bucle for para imprimir todos los números impares entre 1 y 25.
contador = 1

#Mientras que contador sea menor o igual a 25 entonces
while contador <= 25:
    #Veremos cual número es impar 
    if contador % 2 != 0:
        #imprimimos ese número
        print(contador)
    #Fuera del if, vamos aumentando los números de uno en uno para ver los impares
    contador += 1

#2. Dada la lista ["manzana", "banana", "cereza", "pera"],
# usa un bucle for para imprimir cada fruta junto con su longitud (número de caracteres).       

frutas = ["manzana", "banana", "cereza", "pera"]
for elemento_frutas in frutas:
    print(elemento_frutas)
    print(len(elemento_frutas))
    
#3. Escribe un programa que use un bucle while para calcular el factorial de un número n ingresado por el usuario.
#1*2*3*4*5*6*7*n
# Factorial usando while

numero_usuario = int(input("Coloca un número entero para calcular su factorial: "))

factorial = 1
contador = 1

while contador <= numero_usuario:
    factorial *= contador  # multiplicamos el acumulador por el contador
    contador += 1  # avanzamos al siguiente número

print("El factorial de", numero_usuario, "es:", factorial)


