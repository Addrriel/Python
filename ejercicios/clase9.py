# 1. Escribe un programa que verifique si un número es positivo, negativo o cero.
numeroUsuario = int(input("Ingrese un número entero: "))
if (numeroUsuario > 0):
    print("Es un número positivo")
elif (numeroUsuario < 0):
    print("Es un número negativo")
elif (numeroUsuario == 0):
    print("Es el número cero")
else:
    print("Su valor no es admitido")

# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 años o más) o menor de edad.
edadUsuario = int(input("Ingrese su edad por favor : "))
if(edadUsuario >= 18):
    print("Usted ya es mayor de edad")
elif (edadUsuario < 18):
    print("Aún es menor de edad")
else: 
    print("Error al ejecutar la condicional")

# 3. Escribe un programa que verifique si una cadena de texto está vací­a y muestre un mensaje en consecuencia.
cadenaVacia = ""
if (cadenaVacia == ""):
    print("la cadena está vacía")
else:
    print(cadenaVacia)

# 4. Crea un programa que solicite dos números al usuario y compare cuál es mayor. Si son iguales,
#  muestra un mensaje indicando la igualdad.
num1 = float(input("Ingrese el primer número para la comparación: "))
num2 = float(input("Ingrese el segundo número para la comparación: "))

if(num1 == num2):
    print("Los números son iguales")
elif(num1 > num2):
    print("El primer número es mayor")
elif(num1 < num2):
    print("el segundo número es mayor")
else:
    print("Error al ejecutar la condicional")

# 5. Escribe un programa que verifique si un número es divisible por 3 y por 5 al mismo tiempo.
numeroDivisible = int(input("Ingrese un número para verificar si es divisible: "))
if(numeroDivisible % 3 == 0 and numeroDivisible % 5 == 0):
    print("Es divisible para 5 y para 3")
else: 
    print("No es divisible para los dos al mismo tiempo")

# 6. Solicita al usuario que ingrese un número y verifica si es par o impar.
comprobacionNumero = int(input("Ingrese un número para verificar si es par o no es par: "))
if(comprobacionNumero % 2 == 0): #El residuo será 0, eso quiere decir que es divisible y que es par
    print("Es un número par")
elif (comprobacionNumero % 3 == 1): #Por otro lado, aquí el residuo será 1 debido a que no es número par y por ende será en decimales
    print("es impar")
else: 
    print("No es número válido")

# 7. Escribe un programa que determine si una persona puede votar en función de su edad(mayor o igual a 18).
#  Si tiene 16 o 17 años, indica que puede votar con permiso especial.
permisoVotacion = int(input("Ingrese su edad para ver si puede votar o no: "))
if(permisoVotacion >= 18):
    print("Es apto para poder votar legalmente")
elif (permisoVotacion == 17 or permisoVotacion == 16):
    print("Tienen un permiso especial para poder votar")
else: 
    print("No tienen la edad suficiente para poder votar")

# 8. Crea un programa que solicite una contraseña al usuario y verifique si coincide con una contraseña predefinida.
#  Si no coincide, muestra un mensaje de error.
user_password = input("Ingrese su contraseña: ")
contraseniaRealUser = "AlejandroBedoya"

if(user_password == contraseniaRealUser):
    print("Ingreso exitoso, disfrute su estadía")
else: 
    print("Contraseña incorrecta, intentalo nuevamente")


# 9. Escribe un programa que determine si un número está entre 10 y 20 (ambos incluidos).
numeroFuera = 9
numeroRango = 12

#Este estará fuera del rango
if(numeroFuera >= 10 and numeroFuera <= 20 ):
    print("Este número está dentro del rango")
else:
    print("Este número está fuera del rango")

#Este estará dentro del rango
if(numeroRango >= 10 and numeroRango <= 20 ):
    print("Este número está dentro del rango")
else:
    print("Este número está fuera del rango")

# 10. Escribe un programa que simule un semáforo:
#  solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse,
#  estar alerta o avanzar.

semaforoUser = input("Escribe uno de estos 3 colores para saber el color real del semáforo: ")

if (semaforoUser == "verde"):
    print("El semáforo está de color rojo, debes detenerte")
elif (semaforoUser == "amarillo"):
    print("El semáforo está a punto de cambiar a verde, ten cuidado")
elif (semaforoUser == "rojo"):
    print("Puedes pasar, los carros están detenidos")
else: #el usuario puede escribir cualquier cosa y es mejor tener un manejo de errores siempre
    print("No son las palabras solicitadas, recuerda que es 'verde', 'amarillo' o 'rojo' ")