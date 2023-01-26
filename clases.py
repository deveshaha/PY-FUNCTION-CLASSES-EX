#Ejercicio de clases con herencia en Python

# Punto 1:
# Escribe una clase llamada Poligono() que genera objetos de polígono de 3 o más lados.  
# Al crear un objeto, en el constructor __init__ ( ), se indica el número de lados que va a tener y 
# se crea una lista que va a tener ese número de elementos cuyos valores iniciales serán 0. 

# Punto 2:
# La clase Poligono() tendrá un método llamado darlados( ) que le pedirá al usuario que 
# introduzca uno a uno los valores de todos los lados. 

# Punto 3:
# La clase Polígono() tendrá otro método llamado verlados( ) que mostrará uno a uno los 
# valores introducidos de todos los lados. 

# Punto 4:
# Se va a crear una clase llamada Triangulo() que hereda de la clase  Poligono().  
# Al crear un objeto triangulo, se invoca al constructor de la clase Poligono() al que se indica el 
# número de lados = 3. 
 

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
            valLado = int (input(f'Introduce el valor del lado {i+1}: '))
            pol.lados[i] = valLado

    def verLados(pol):
        for i in range(pol.num_lados):
            print(f'El valor del lado {i+1} es {pol.lados[i]}')


class Triangulo(Poligono):
    def __init__(self):
        super().__init__(3)
        
    

print("Punto 1: \n")
pol = int(input("Introduce el número de lados del polígono: "))
pol = Poligono(pol)
print(pol.lados)

print("\nPunto 2: \n")
valLado = 0
Poligono.darLados(valLado, pol)
print(pol.lados)

print("\nPunto 3: \n")
Poligono.verLados(pol)

print("\nPunto 4: \n")
tri = Triangulo()
print(tri.lados)








