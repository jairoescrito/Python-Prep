## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

def Primo(n):
    if n <= 1:
        print("El número ingresado debe ser mayor de 1")
    elif n in [2,3,5,7]:
        print(True)
    else:
        Div = 2
        P = 0
        while Div < n:
            if n % Div == 0:
                P = 1
                print(False)
                break
            Div +=1
        if P == 0:
            print(True)
Primo(7)

# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

def Primos(L):
    Lista = []
    for n in L:
        if n == 2:
            Lista.append(n)
        elif n <= 1:
            continue
        else:
            Div = 2
            P = 0
            while Div < n:
                if n % Div == 0:
                    P = 1
                    break
                Div +=1
            if P == 0:
                Lista.append(n)
    return(Lista)

L = list(range(501))
L
Primos(L)

# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

def ContarRep(Lista):
    Max = 0
    Num = []
    Cuenta = 0
    for dato in Lista:
        if Lista.count(dato) > Max:
            Num = dato
            Max = Lista.count(dato)
    print("El número que más se repite es",Num,", aparece",Max,"veces")

L = [1,1,1,1,2,2,2,3,3,4]
ContarRep(L)

# 4) A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor o el mayor de los mas repetidos.

def CuentaRep(Lista):
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

L = [1,1,1,1,1,1,2,2,2,2,2,3,3,4,4,4,4,4,4]
CuentaRep(L)

# 5) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino

def Grados(V,O,D): # Valor(V), Origen(O), Destino(D)
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
    else:
        R = V + 273.15
    print(V,"°",O,"Equivalen a",round(R,2),"°",D)

Grados(100,"K","F")
Grados(14,"C","F")

# 6) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:
Temp = [(100,"K","F"),(100,"K","C"),(14,"C","F"), (35,"C","K"),(50,"F","K"), (50,"F","C")]
for t in Temp:
    Grados(t[0],t[1],t[2])


# 7) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo
def Factorial(n):
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

Factorial(-100)