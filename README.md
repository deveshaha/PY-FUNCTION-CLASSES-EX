# PY-FUNCTION-CLASSES-EX

# Ejercicio de Funciones (1)

## 1. generar_n_caracteres(n, caracter)

This function takes in an integer "n" and a character "caracter" and returns the "caracter" multiplied by "n".

Example:

    generar_n_caracteres(5, "x") 

would return "xxxxx".

## 2. histograma(lista_números)

This function takes in a list of integers and displays a histogram with columns measuring the value of the numbers.

Example:

    histograma([4, 9, 2,7]) 

would display:

    **** 
    ********* 
    ** 
    ******* 

## 3. funcionLista(función, lista)

This function takes in another previously created function and a list, and returns another list with the result of applying the given function to each element of the list.

Example:

    lista = [1,2,3,4,5]
    def cubo(x):
	    return x**3
    funcionLista(cubo, lista)

would return 
`[1,8,27,64,125]`

## 4. palabrasLongitud(frase)

This function takes in a sentence and returns a dictionary with the words in the sentence and their length.

Example:

    palabrasLongitud("Hola y adiós") 

would return:

    {'Hola':4, 'y':1, 'adiós':5}

## 5. calificaPalabras(diccAsignaturas)

This function receives a dictionary with the subjects and numerical grades of a student and returns another dictionary with the subjects in uppercase and the corresponding grades in words.

The criteria for the grading will be as follows:

-   note <5 → Suspenso (Fail)
-   5 <= note < 7 → Aprobado (Pass)
-   7 <= note < 9 → Notable (Good)
-   9 <= note <=10 → Sobresaliente (Excellent)

Note: The grade cannot exceed 10.

Example: The function receives the dictionary {'Android':8.2, 'Hilos':5, 'Python':9.3, 'Interfaces':4.4} and returns the dictionary {'ANDROID':'Notable', 'HILOS':'Aprobado', 'PYTHON':'Sobresaliente', 'INTERFACES':'Suspenso' }
