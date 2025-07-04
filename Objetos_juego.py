#Creación de clases para un mini juego por turnos
class Personaje:
    #Crear los atributos
    def __init__(self, Nombre ):
        self.Nombre = Nombre
        self.Fuerza = 0
        self.Inteligencia = 0
        self.Resistencia = 0
        self.Vida = 100
        self.Velocidad = 0
    def Atributos(self):#Metodo para mostrar las estadisticas del personaje en pantalla
        print("\nAtributos ", self.Nombre, ":", sep="")
        print("-Fuerza:", self.Fuerza)
        print("-Inteligencia:", self.Inteligencia)
        print("-Resistencia:", self.Resistencia)
        print("-Vida:", self.Vida)
        print("-Velocidad:", self.Velocidad )

    def Subir_nivel(self, Fuerza, Inteligencia, Resistencia, Vida, Velocidad):#Metodo para subir de nivel las estadisticas de personaje
        print("Subida de nivel")
        self.Fuerza = self.Fuerza + Fuerza
        self.Inteligencia = self.Inteligencia + Inteligencia
        self.Resistencia = self.Resistencia + Resistencia
        self.Vida = self.Vida + Vida
        self.Velocidad = self.Velocidad + Velocidad
    
    def Esta_vivo(self):
        return self.Vida > 0 #Si la vida es mayora  0, nos regresara True, en caso contrario False
    
    def Morir(self):
        self.Vida = 0
        print(self.Nombre, "Ha muerto")
        
    def Daño(self, enemigo):#Agregamos la variable enemigo, donde encapsularemos al otro personaje contra quien nos enfrentamos
        return self.Fuerza - enemigo.Resistencia 
    

    def Atacar(self, Enemigo):#Este metodo es para calcular el dmg que le haremos a nuestro rival usando la formula del metodo Daño
        Daño = self.Daño(Enemigo)
        Enemigo.Vida = Enemigo.Vida - Daño
        print(self.Nombre, "Ha realizado", self.Daño(Enemigo), "puntos de daño a:", Enemigo.Nombre)
        if Enemigo.Esta_vivo():
            print("La vida de", Enemigo.Nombre, "es de:", Enemigo.Vida )
        else:
            Enemigo.Morir()

#----------------------------------------------------------Subclase Guerrero----------------------------------------------------
    
class Guerrero(Personaje):
    def __init__(self, Nombre):
        super().__init__(Nombre)
        self.Espada = 0
        self.Nombres_espadas = { #Creamos un diccionario para asignarles los nombres a cada numero, y luego poder imprimirlos
            8:"(Lanza de shojin)",
            10:"(Espada del rey arruinado)"
        } 
        
    def Elegir_arma(self):
        opcion = input("Elige un arma: (1)Espada del rey arruinado (2)Lanza de shojin\n").strip() #Le damos la opcion al usuario 
        if opcion == "1":
            self.Espada = 10
        elif opcion == "2":
            self.Espada = 8
        else:
            print("Elegiste un numero incorrecto, elige otra vez")
        
    def Atributos(self):
        stats = super().Atributos() #Toma del metodo atributos de la clase super(Personaje, lo hacemos una variable para que podamos
        #imprimir despues el nuevo atributo que queremos (Nombre_espada)
        Nombre_espada = self.Nombres_espadas.get(self.Espada, 'Sin arma.')
        print(f"-Espada:{self.Espada} {Nombre_espada}" )
        return stats#nos regresamos a la variable stats, y asi podemos imprimir nombre espadas, y hacerlo otro atributo
        
    def Daño(self, enemigo): #Usaremos el metodo Daño del objeto personaje
        return (self.Espada * self.Fuerza) - enemigo.Resistencia

    def Atacar(self, Enemigo):
        return super().Atacar(Enemigo)

#-----------------------------------------------Subclase Mago------------------------------------------------------------------#

class Mago(Personaje):
    def __init__(self, Nombre):
        super().__init__(Nombre)
        self.Baculo = 0
        self.Nombres_baculos= { #Creamos un diccionario para asignarles los nombres a cada numero, y luego poder imprimirlos
            8:"(Báculo del árcangel)",
            10:"(Báculo del vacío)"
        } 
        
    def Elegir_arma(self):
        opcion = input("Elige un arma: (1)Báculo del árcangel (2)Báculo del vacío\n").strip() #Le damos la opcion al usuario 
        if opcion == "1":
            self.Baculo = 8
        elif opcion == "2":
            self.Baculo = 10
        else:
            print("Elegiste un numero incorrecto, elige otra vez")
        
    def Atributos(self):
        stats = super().Atributos() 
        Nombre_baculo = self.Nombres_baculos.get(self.Baculo, 'Sin arma.')
        print(f"-Báculo:{self.Baculo} {Nombre_baculo}" )
        return stats#nos regresamos a la variable stats, y asi podemos imprimir nombre baculo, y hacerlo otro atributo
        
    def Daño(self, enemigo): #Usaremos el metodo Daño del objeto personaje
        return (self.Baculo * self.Inteligencia) - enemigo.Resistencia

    def Atacar(self, Enemigo):
        return super().Atacar(Enemigo)
        

