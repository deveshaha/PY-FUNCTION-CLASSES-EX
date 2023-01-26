
usr = int(input("Indica el numero de ejercicio que deseas ejecutar: (1 - 5) "))

match usr:
    case 1:
        ## Ejercicio 1

        # Escribe una función generar_n_caracteres(n, carácter) a la que se le pasa un número entero n y un carácter. 
        # Devolverá el carácter multiplicado por n. 
        # Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx". Tantas x como indique el número.

        print("Ejercicio 1: \n")

        def generar_n_caracteres(n, caracter):
            return n * caracter

        numCar = int(input("Introduce un número: "))
        caracter = input("Introduce un carácter: ")

        print(generar_n_caracteres(numCar, caracter))

    case 2:
        ## Ejercicio 2
        ## Crea una función llamada histograma(lista_números) a la que se le pasa una lista de números enteros. 
        # Se mostrará un histograma cuyas columnas midan el valor de los números. 
        # Por ejemplo: histograma([4, 9, 2,7]) debería imprimir lo siguiente:

        print("Ejercicio 2: \n")
        
        def histograma(lista_numeros):
            for i in lista_numeros:
                print(i * "*")

        print("Introduce 4 números enteros: ")
        lista_numeros = []
        for i in range(4):
            lista_numeros.append(int(input()))

        histograma(lista_numeros)

    case 3:
        print("Ejercicio 3: \n")

        # Escribe una función funcionLista(función, lista) que reciba otra función creada 
        # anteriormente y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada 
        # uno de los elementos de la lista.  

        # Por ejemplo, la función que se le pasa calcula el cubo de un número.  
        # La lista que se pasa es una lista de números enteros. A cada número de la lista se le aplica la 
        # función y se calculará el cubo de todos ellos, mostrándolos en otra lista nueva.  
        # Si la lista que se pasara fuera [1,2,3,4,5] la función devolvería [1,8,27,64,125]

        def funcionLista(funcion, lista):
            listaNueva = []
            for i in lista:
                listaNueva.append(funcion(i))
            return listaNueva

        def cubo(num):
            return num ** 3

        lista = [1,2,3,4,5]
        print(funcionLista(cubo, lista))

    case 4:
        print("Ejercicio 4: \n")

        # Escribe una función palabrasLongitud(frase) que reciba una frase y devuelva un diccionario 
        # con las palabras que contiene y su longitud.  
        # Por ejemplo, la función recibe la frase 'Hola y adiós' y devuelve un diccionario de la forma 
        # {'Hola':4, 'y':1, 'adiós':5} 

        def palabrasLongitud(frase):
            palabras = frase.split()
            dicPalLong = {}

            for i in palabras:
                dicPalLong[i] = len(i)
            print(dicPalLong)

        frase = input("Introduce una frase: ")
        palabrasLongitud(frase)

    case 5:
        print("Ejercicio 5: \n")

        # Escribe una función calificaPalabras(diccionario) que reciba un diccionario con las 
        # asignaturas y las notas numéricas de un alumno y devuelva otro diccionario con las asignaturas en 
        # mayúsculas y las calificaciones correspondientes a las notas con palabras.  
        
        # El criterio será el siguiente:  nota <5 → Suspenso;  5 <= nota < 7 → Aprobado;   
        # 7 <= nota < 9 → Notable; 9 <= nota <=10 → Sobresaliente. La nota no puede sobrepasar 10. 
        
        # Por ejemplo, la función recibe el diccionario {'Android':8.2, 'Hilos':5, 'Python':9.3, 'Interfaces':4.4} 
        # y devuelve el diccionario {'ANDROID’:’Notable’,  ‘HILOS’:’Aprobado’, ‘PYTHON’:’Sobresaliente’, 
        # ‘INTERFACES’:’Suspenso’ } 

        def calificaPalabras(diccAsignaturas):
            for i in diccAsignaturas:
                if diccAsignaturas[i] < 5:
                    diccAsignaturas[i] = "Suspenso"
                elif diccAsignaturas [i] <= 5 or diccAsignaturas[i] < 7:
                    diccAsignaturas[i] = "Aprobado"
                elif diccAsignaturas [i] <= 7 or diccAsignaturas[i] < 9:
                    diccAsignaturas[i] = "Notable"
                elif diccAsignaturas [i] >= 9 or diccAsignaturas[i] <= 10:
                    diccAsignaturas[i] = "Sobresaliente"
            print(diccAsignaturas)
        
        diccAsignaturas = {'Android' : 8.2, 'Hilos' : 5, 'Python' : 9.3, 'Interfaces' : 4.4}
        calificaPalabras(diccAsignaturas)
    case _:
        print("El número introducido no es válido")
