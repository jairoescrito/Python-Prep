# Definición de clases para crear objetos

class Gato: # definición de la clase y su nombre
    def __init__(self, nombre, edad,raza, sexo): # definición de los parámetros de la clase
        self.nombre = nombre # Asignación de los parámetros de la clase
        self.edad = edad
        self.raza = raza
        self.sexo = sexo
   #Creamos el método presentar
    def presentar(self): #definición del método de la clase
        print("Mi Nombre: ", self.nombre) # Acciones que ejecuta el método
        print("Edad: ", self.edad,"años")
        print("Raza: ", self.raza)
        print("Sexo: ", self.sexo)


Lucy = Gato("Lucy",1,"Criolla","Hembra")
Lucy.presentar()

# Pilares de la programación orientada a objetos

# Abstracción: ing inversa, a partir de un objeto (aún no definido como clase) se identifican sus atributos y 
# sus posibles métodos y con esto se crea la clase modelo (el molde del objeto)

# Encapsulamiento: "encerrar" atributos de una clase para cuando se asignen a un objeto creado a una clase estos
# no puedan ser consultados ni moficicados 

# Herencia: se crean nuevas clases (hijos: subclases) a partir de una clase previa o ya existente (padre: superclase) las cuales 
# las subclases heredan métodos y atributos de la superclase. Las clases hijas pueden tener métodos particulares que se definen
# al definir la clase hija. Si la clase hija requiere atributos adicionales  se deben llamar los atributos de la superclase
# haciendo uso de la función super()

# Polimorfismo: Crear métodos a partir de los atributos de la clase

# Ejemplo de una clase con encapsulamiento
class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # el atributo saldo está encapsulado con __
        # el atribuuto saldo se hace oculto, es decir, no se puede modificar
        # directamente usando el atributo saldo, se debe hacer a partir de otros
        # atributos y a partir de unos métodos definidos para tal
    def depositar(self, monto):
        self.__saldo += monto

    def retirar(self, monto):
        if self.__saldo >= monto:
            self.__saldo -= monto
        else:
            print("Saldo insuficiente")

    def obtener_saldo(self):
        return self.__saldo

# Ejemplo de una superclase y subclases

# Definición de la superclase
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    # Método genérico pero con implementación particular
    def hablar(self):
        # Método vacío
        pass # pass se usa para dejar el método creado pero sin ninguna acción
    # Método genérico pero con implementación particular
    def moverse(self):
        # Método vacío
        pass
    # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__) #type(self).__name__ entrega el nombre de la subclase que 
        # usa la ésta superclase

# Definición de las superclases
class Perro(Animal):
    def hablar(self): # en los métodos vacíos se crean las acciones
        print("Guau!")
    def moverse(self):
        print("Caminando con 4 patas")

class Vaca(Animal):
    def hablar(self):
        print("Muuu!")
    def moverse(self):
        print("Caminando con 4 patas")

class Abeja(Animal):
    def hablar(self):
        print("Bzzzz!")
    def moverse(self):
        print("Volando")
    # Nuevo método
    def picar(self): # En esta subclase se crea un método que no hace parte de la superclase
        print("Picar!")