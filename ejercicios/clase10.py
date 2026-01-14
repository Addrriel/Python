"""
# 1. Usa un bucle while para imprimir los números del 1 al 10.

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada nÃºmero.

# 3. Escribe un programa que use un bucle while para sumar los números del 1 al 100 e imprime el resultado.

# 4. Escribe un bucle for que imprima cada carÃ¡cter de la cadena "Python".

# 5. Usa un bucle while para encontrar el primer número divisible por 7 entre 1 y 50.

# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.

# 7. Escribe un programa que use un bucle while para imprimir los números pares entre 1 y 20.

# 8. Usa un bucle for con la funciÃ³n range() para imprimir los números del 1 al 10 en orden inverso.

# 9. Escribe un programa que use un bucle for para contar cuÃ¡ntas veces aparece el número 30 en la lista[30, 10, 30, 20, 30, 40].

# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".
"""

#1) Usa un bucle while para imprimir los números del 1 al 10.

contador = 0

while contador < 10:
    contador += 1
    print(contador)

print("----------------------------------")

#2) Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada número.
lista_preciosa = [10, 20, 30, 40, 50]

for lista in lista_preciosa:
    print(lista)
print("-------------------------------------------------------------------")

#3) Escribe un programa que use un bucle while para sumar los números del 1 al 100 e imprime el resultado.

acumulador = 0
num = 1

while num <= 100:
    acumulador += num
    num += 1

print(acumulador)
print("-------------------------------------------------------------------")

#4) Escribe un bucle for que imprima cada caracter de la cadena "Python".

frase = "Python"

for letras in frase:
    print(letras)

print("-------------------------------------------------------------------")

# 5) Usa un bucle while para encontrar el primer número divisible por 7 entre 1 y 50.

num= 1

while num <= 50:
    if num % 7 == 0:
        print(num)
        break
    num+= 1 

print("-------------------------------------------------------------------")

#6) Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.

diccionario = {"name": "Brais", "age": 37, "country": "Galicia"}

for palabras in diccionario:
    print(palabras)
print("-------------------------------------------------------------------")

#8) Usa un bucle for con la función range() para imprimir los números del 1 al 10 en orden inverso.

#Empieza en 10, termina en 0 y va restando de uno en uno
for numeros in range(10 , 0 , -1 ):
    print(numeros)
print("-------------------------------------------------------------------")
#9) Escribe un programa que use un bucle for para contar cuántas veces aparece el número 30 en la lista[30, 10, 30, 20, 30, 40].

lista_ver = [30, 10, 30, 20, 30, 40]
num_ver = 30
contador = 0
for contar in lista_ver:
    if contar == 30:
        contador += 1        
print(contador , "veces")    
print("-------------------------------------------------------------------")

#10) Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".

lista_nombres = ["Alejandro", "Adriel", "Martín", "Brais", "Maiccol"]

for nombres in lista_nombres:
    if nombres == "Brais":
        print ("Se encontró")
