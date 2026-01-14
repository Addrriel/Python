#CONDICIONALES

#Sirve para los flujos de ejecución de nuestro código

#Primer condicional = If

primeraCondicion = 5
#if + condicional :
    #resultado
#else:
    #el otro resultado
if primeraCondicion == 6:
    print("Esta condición se cumple")
else :
    print("Esta condición no se cumple")


#En caso de querer hacer más de uno, usamos otro if
alumno = "Carlos"
esEstudiante = True

if (alumno == "Carlos"):
    print("Se llama Carlos")

if (alumno == "Carlos" and esEstudiante == True):
    print("Es un alumno y se llama Carlos")

#En caso de querer hacer en el mismo condicional, podemos usar el elif

promedioCurso = 7

if(promedioCurso >= 7):
    print("Su curso supero lo mínimo")
elif (promedioCurso >= 9): #dándome cuenta, siempre se debe empezar desde lo más alto pero me olvidé xd
    print("Su curso supero la media estudiantil")
else: 
    print("Tiene curso de vagos")

    









