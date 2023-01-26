#Ejercicio de clases con herencia en Python

# Punto 1:
# Escribe una clase llamada Poligono() que genera objetos de polígono de 3 o más lados.  
# Al crear un objeto, en el constructor __init__ ( ), se indica el número de lados que va a tener y 
# se crea una lista que va a tener ese número de elementos cuyos valores iniciales serán 0. 

# Punto 2:
# La clase Poligono() tendrá un método llamado darlados( ) que le pedirá al usuario que 
# introduzca uno a uno los valores de todos los lados. 

class Poligono:
    def __init__(self, num_lados):
        if num_lados < 3:
            print("Error: el polígono debe tener al menos 3 lados.")
        else:
            self.num_lados = num_lados
            for i in range(num_lados):
                self.lados = [0] * num_lados

    def darLados(valLado, pol):
        for i in range(pol.num_lados):
            valLado = int(input("Introduce el valor del lado: "))
            pol.lados[i] = valLado
        
    

print("Punto 1: \n")
pol = int(input("Introduce el número de lados del polígono: "))
pol = Poligono(pol)
print(pol.lados)

print("Punto 2: \n")
valLado = 0
Poligono.darLados(valLado, pol)
print(pol.lados)





