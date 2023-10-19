## Clases y Programación Orientada a Objetos

'''1) Crear la clase vehículo que contenga los atributos:<br>
Color<br>
Si es moto, auto, camioneta ó camión<br>
Cilindrada del motor'''
class Vehiculo: # definición de la clase Vehiculo
    def __init__(self, tipo,color,cilindraje): # definición de los parámetros de la clase
        self.tipo = tipo # Asignación de los parámetros de la clase
        self.color = color
        self.cilindraje = cilindraje

'''2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
Acelerar<br>
Frenar<br>
Doblar<br>'''
class Vehiculo: # definición de la clase Vehiculo
    def __init__(self, tipo,color,cilindraje): # definición de los parámetros de la clase
        self.tipo = tipo # Asignación de los parámetros de la clase
        self.color = color
        self.cilindraje = cilindraje
        self.vel_a = 0
        self.sentido = "recto"

    def Acelerar(self):
        vel = input(int('Ingrese la velocidad a alcanzar: '))
        if vel > vel_a:
            vel_a = vel
            print('Aceleración realizada. La nueva velocidad es de:',vel_a,'km/h')
        elif vel == vel_a:
            print('Actualmente el vehículo tiene esa velocidad')
        else:
            print('La velocidad ingresada requiere un frenado. Actualmente la velocidad es de:',vel_a,'km/h')
   
    def Frenar(self):
        vel = input(int('Ingrese la velocidad después de frenado: '))
        if vel < vel_a:
            vel_a = vel
            print('Frenado realizado. La nueva velocidad es de:',vel_a,'km/h')
        elif vel == vel_a:
            print('Actualmente el vehículo tiene esa velocidad')
        else:
            print('La velocidad ingresada requiere una aceleración. Actualmente la velocidad es de:',vel_a,'km/h')

    def Doblar(self):
        giro = input('Ingrese la dirección a tomar: (recto, izquierda o derecha)')
        if giro != 'recto' or giro != 'izquierda' or giro != 'derecha':
            print('La dirección ingresada no se reconoce. Ingrese: recto, izquierda o derecha')
        elif giro == sentido:
            print('No es posible el cambio de dirección, el vehículo actualmente lleva esa dirección')
        else:
            sentido = giro
            print('Dirección modificada, el vehículo acaba ahora va en dirección', sentido)
        

'''3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado'''
Vehiculo1 = Vehiculo("Moto","Roja","125cc")
Vehiculo2 = Vehiculo("Auto", "Azul", "1200cc")
Vehiculo3 = Vehiculo("Camioneta","Gris","2500cc")
Vehiculo1.cilindraje
Vehiculo3.vel_a

'''4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada'''

class Vehiculo: # definición de la clase Vehiculo
    def __init__(self, tipo,color,cilindraje): # definición de los parámetros de la clase
        self.tipo = tipo # Asignación de los parámetros de la clase
        self.color = color
        self.cilindraje = cilindraje
        self.vel_a = 0
        self.sentido = "recto"

    def Acelerar(self,vel):
        '''
        Ingrese la velocidad a alcanzar
        '''
        if vel > self.vel_a:
            self.vel_a = vel
            print('Aceleración realizada. La nueva velocidad es de:',self.vel_a,'km/h')
        elif vel == self.vel_a:
            print('Actualmente el vehículo tiene esa velocidad')
        else:
            print('La velocidad ingresada requiere un frenado. Actualmente la velocidad es de:',self.vel_a,'km/h')
   
    def Frenar(self,vel):
        '''
        Ingrese la velocidad después de frenado
        '''
        if vel < self.vel_a:
            self.vel_a = vel
            print('Frenado realizado. La nueva velocidad es de:',self.vel_a,'km/h')
        elif vel == self.vel_a:
            print('Actualmente el vehículo tiene esa velocidad')
        else:
            print('La velocidad ingresada requiere una aceleración. Actualmente la velocidad es de:',self.vel_a,'km/h')

    def Doblar(self,giro):
        '''
        Ingrese la dirección a tomar: (recto, izquierda o derecha)
        '''
        if giro != 'recto' or giro != 'izquierda' or giro != 'derecha':
            print('La dirección ingresada no se reconoce. Ingrese: recto, izquierda o derecha')
        elif giro == self.sentido:
            print('No es posible el cambio de dirección, el vehículo actualmente lleva esa dirección')
        else:
            self.sentido = giro
            print('Dirección modificada, el vehículo acaba ahora va en dirección', self.sentido)

    def Estado(self):
        print('Actualmente el vehículo tiene una velocidad de:',self.vel_a,'km/h, y va en dirección:',self.sentido)
    
    def Descripcion(self):
        print('El vehículo es tipo', self.tipo, 'de color', self.color, 'y con un cilindraje de', self.cilindraje)

Vehiculo1 = Vehiculo("Moto","Roja","125cc")
Vehiculo2 = Vehiculo("Auto", "Azul", "1200cc")
Vehiculo3 = Vehiculo("Camioneta","Gris","2500cc")

Vehiculo1.Estado()
Vehiculo1.Descripcion()

Vehiculo2.Acelerar(50)
Vehiculo2.Descripcion()
Vehiculo2.Estado()

'''5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 6<br>'''
class Tarea:
    def __init__(self) -> None:
        pass
    
    '''Verificar Primo: USA NÚMERO'''
    def Primo(self,n):
        '''Verifica si un número "n" es primo'''
        if n <= 1:
            print("El número ingresado debe ser mayor de 1")
        else:
            Primo = True
            Div = 2
            while Div < n:
                if n % Div == 0:
                    Primo = False
                    break
                Div +=1
        return(Primo)
    
    '''Valor modal: : USA LISTA'''
    def CuentaRep(self,Lista):
        Cuenta = []
        Rep = []
        for dato in Lista:
            Cuenta.append(Lista.count(dato))
        for i in range(len(Cuenta)):
            if Cuenta[i] == max(Cuenta):
                Rep.append(Lista[i])
        R = input("¿Requiere el menor(min) o valor mayor(max) de los repetidos?: ")
        if R == "min":
            print("El número menor de los más repetidos es",min(Rep))
        elif R == "max":
            print("El número mayor de los más repetidos es",max(Rep))
        else:
            print("No entendí la respuesta, solo entiendo 'min' o 'max'")
    
    '''Conversión grados: USA NÚMERO'''
    def Grados(self,V,O,D): 
        '''Valor(V), Origen(O), Destino(D).
        El valor es la cantidad de grados en la medida de origen;
        O y D deden ser "F": Farenheit, "C": Centígrados o "K": Kelvin.
        El destino no puede ser el mismo del origen'''
        if O == "K" and D == "F":
            R = 32 + ((9/5)*(V-273.15)) 
        elif O == "K" and D == "C":
            R = V - 273.15
        elif O == "F" and D == "K":
            R = ((5/9)*(V-32))+273.15
        elif O == "F" and D == "C":
            R = (5/9)*(V-32)
        elif O == "C" and D == "F":
            R = 32 + ((5/9)*V)
        elif O == "C" and D == "K":
            R = V + 273.15
        else:
            print('Error en la definición de orígen o destino')
        print(V,"°",O,"Equivalen a",round(R,2),"°",D)

    '''Factorial: USA NÚMERO'''
    def Factorial(self,n):
        if type(n) != int:
            print("El dato ingresado no es un número entero, la función aplica únicamente para números enteros mayores a cero")
        elif n < 0:
            print("El número ingresado es negativo, la función aplica únicamente para número enteros mayores a cero")
        else:
            x = n-1
            while x > 1:
                n = n * x
                x -= 1
            return(n)

'''6) Probar las funciones incorporadas en la clase del punto 5'''

x = Tarea()
x.Primo(13)
x.CuentaRep([1,1,1,1,1,1,2,2,2,2,2,3,3,4,4,4,4,4,4])
x.Factorial(6)
x.Grados(30,"C","F")

'''7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas'''

class Tarea:
    def __init__(self,Lista):
        self.Lista = Lista
    
    def Factorial(self):
        for n in self.Lista:
            print('El factorial de',n,'es',self.__Factorial(n))
        
    def Grados(self,O,D):
        for n in self.Lista:
            self.__Grados(n,O,D)
    
    def Primo(self):
        for n in self.Lista:
            self.__Primo(n)
                
    '''Verificar Primo: USA NÚMERO'''
    def __Primo(self,n):
        '''Verifica si un número "n" es primo'''
        if n <= 1:
            print("El número ingresado debe ser mayor de 1")
        else:
            Primo = True
            Div = 2
            while Div < n:
                if n % Div == 0:
                    Primo = False
                    break
                Div +=1
            if Primo == True:
                print(n,'es un número primo')
            else:
                print(n,'no es un número primo')
    
    '''Valor modal: : USA LISTA'''
    def CuentaRep(self):
        Cuenta = []
        Rep = []
        for dato in self.Lista:
            Cuenta.append(self.Lista.count(dato))
        for i in range(len(Cuenta)):
            if Cuenta[i] == max(Cuenta):
                Rep.append(self.Lista[i])
        R = input("¿Requiere el menor(min) o valor mayor(max) de los repetidos?: ")
        if R == "min":
            print("El número menor de los más repetidos es",min(Rep))
        elif R == "max":
            print("El número mayor de los más repetidos es",max(Rep))
        else:
            print("No entendí la respuesta, solo entiendo 'min' o 'max'")
    
    '''Conversión grados: USA NÚMERO'''
    def __Grados(self,V,O,D): 
        '''Valor(V), Origen(O), Destino(D).
        El valor es la cantidad de grados en la medida de origen;
        O y D deden ser "F": Farenheit, "C": Centígrados o "K": Kelvin.
        El destino no puede ser el mismo del origen'''
        if O == "K" and D == "F":
            R = 32 + ((9/5)*(V-273.15)) 
        elif O == "K" and D == "C":
            R = V - 273.15
        elif O == "F" and D == "K":
            R = ((5/9)*(V-32))+273.15
        elif O == "F" and D == "C":
            R = (5/9)*(V-32)
        elif O == "C" and D == "F":
            R = 32 + ((5/9)*V)
        elif O == "C" and D == "K":
            R = V + 273.15
        else:
            print('Error en la definición de orígen o destino')
        print(V,"°",O,"Equivalen a",round(R,2),"°",D)

    '''Factorial: USA NÚMERO'''
    def __Factorial(self,n):
        if type(n) != int:
            print("El dato ingresado no es un número entero, la función aplica únicamente para números enteros mayores a cero")
        elif n < 0:
            print("El número ingresado es negativo, la función aplica únicamente para número enteros mayores a cero")
        else:
            x = n-1
            while x > 1:
                n = n * x
                x -= 1
            return(n)

Lista = [1,1,1,1,1,1,2,2,2,2,2,3,3,4,4,4,4,4,4]
x = Tarea(Lista)
x.Primo()
x.CuentaRep()
x.Factorial()
x.Grados("C","F")


'''8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones'''

import sys
sys.path
sys.path.append(r'/home/jairoescrito/OneDrive/Documentos/Henry/RepoGit_old/PrepCourse/Python-Prep/07 - Clases & OOP')

from Tarea_7 import *
L = [1,1,1,1,1,1,2,2,2,2,2,3,3,4,4,4,4,4,4]
Reto = Tarea(L)
Reto.Primo()
Reto.CuentaRep()
Reto.Factorial()
Reto.Grados("C","F")