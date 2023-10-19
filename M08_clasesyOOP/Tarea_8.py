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