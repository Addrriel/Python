#VARIABLES

#Las variables solo deben ser en minúsculas o snake case
#snake_case


#ERROR DE VARIABLES
#first-name : No puede haber un -, esto daña el nombre
#first@name : No pueden haber caracteres especiales en la variable
#first$name : No pueden haber caracteres especiales en la variable 
#num-1 : No puede haber un -, esto daña el nombre
#1num : Tampoco se puede iniciar la variable con un número pero si puedes hacer "num1"

#Mío
firstName = "Alejandro Bedoya"
age = 23
is_student = True
hasMoney = True
hasPC = True
hasLaptop = False
money= 40.56
#Datos
num1 = 4
num2 = 12
num3= 3.12131415
num4= 2
texto = "texto"

#Funciones matemáticas

print(abs(money)) #Nos da el valor absoluto
print(divmod(num2 , num1)) #Dará el cociente y el residuo, basicamente es un // y %
print(pow(4,2)) #Es para usar potencia, el primer número es la base y el segundo número es la potencia 4 para 2 = 16
print(round(num3 , 2)) #Sirve para redondear, el primer valor es el número y el segundo con cuántos decimales debe estar
print(sum([num1,num2])) #Suma los elementos
print(max(num1, num2, num4)) #Saca el valor más alto = num2 que es 12
print(min(num1, num2, num4)) #Saca el valor menor = num4 que es 2
print(int("12")) #Transforma a entero
print(float(4)) #Transforma a decimal (le agrega el .0 si es entero, ejemplo el 4 será 4.0)

#Estructura de Datos
print(list((1,3,4,5))) #Crear lista
print(tuple([1,2,3,4])) #Crear tupla
print(set([1,1,2,2,3,4,5,5])) #Crear conjunto (set) = no se repiten valores
print(frozenset([1,2,2,3,4])) # Conjunto inmutable
print(dict(carrera = "Desarrollo de Software", semestre = 4)) #Crear diccionario

#Iteración y secuencias

print(list(range(4))) #Rango de números
print(list(enumerate(["primer valor", "segundo"]))) #Sirve para mostrar el índice (el índice es el puesto donde se ubica), y el valor
print(list(zip([1,2,5] , [3,4,6]))) #Une las listas mediante índices
print(list(reversed(["hola", "soy", "goku"]))) #Invierte el valor
print(list(sorted(["a", "b", "z", "c"]))) #Ordena los valores (cadenas, int o float)

#Lógica y Validaciones
print(all([hasMoney, hasPC, is_student])) #Devuelve True si todos son verdaderos, pero si hay uno false devolverá eso
print(any([hasMoney, hasPC, hasLaptop])) #Devuelve True si al menos uno es verdadero
print(bool(0)) #Transforma a booleano, solo funciona con 0 y 1 ; 0 es false y 1 es true
print(isinstance("soyString", str)) #Valida si el tipo es correcto, el primer valor es el dato que damos y el segundo el tipo de dato


#Texto y Caracteres
print(str(money)) #Transforma a string = "40,56"
print(ascii("niño")) #Convierte los caracteres raros en formato asci (como la ñ)


