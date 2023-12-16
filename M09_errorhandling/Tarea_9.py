class Tarea:
    def __init__(self,Lista):
        assert type(Lista) == list, "Se esperaba una lista como objeto de ingreso"
        assert len(Lista) > 0, "Se esperaba una lista no vacía"
        self.Lista = Lista
    
    def Factorial(self):
        for n in self.Lista:
            print('El factorial de',n,'es',self.__Factorial(n))
        
    def Grados(self,O,D):
        for n in self.Lista:
            assert type(n) == int or type(n) == float, 'Solo aplica para elementos numéricos positivos'
            self.__Grados(n,O,D)
    
    def Primo(self):
        for n in self.Lista:
            self.__Primo(n)
                
    '''Verificar Primo: USA NÚMERO'''
    def __Primo(self,n):
        '''Verifica si un número "n" es primo'''
        assert n >= 2, 'El número debe ser superior a uno'
        assert type(n) != 'str', 'Solo aplica para elementos numéricos positivos'
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
        R = input("¿Requiere el menor(min) o mayor(max) datos de los repetidos?: ")
        assert R == 'min' or R == 'max', "No entendí la respuesta, solo entiendo 'min' o 'max'"
        if R == "min":
            print("El número menor de los más repetidos es",min(Rep))
        else:
            print("El número mayor de los más repetidos es",max(Rep))
    
    '''Conversión grados: USA NÚMERO'''
    def __Grados(self,V,O,D): 
        '''Valor(V), Origen(O), Destino(D).
        El valor es la cantidad de grados en la medida de origen;
        O y D deden ser "F": Farenheit, "C": Centígrados o "K": Kelvin.
        El destino no puede ser el mismo del origen'''
        assert O == "K" or O == "F" or O == "C", "El origen debe ser deden ser 'F': Farenheit, 'C': Centígrados o 'K': Kelvin"
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
        assert n > 0, 'Solo aplica para elementos numéricos positivos'
        assert type(n) == 'int', 'Solo aplica para elementos numéricos positivos'
        x = n-1
        while x > 1:
            n = n * x
            x -= 1
        return(n)