#Nombre, Fuerza, Inteligencia, Resistencia, Vida, Velocidad)

from Objetos_juego import Personaje, Guerrero, Mago
from Seleccion_rasgos import menu_seleccion_clase
#----------------------------------------Distribución de puntos del personaje-----------------------------------------------------#--#
def Creador_personaje():
    print("Bienvenido al creador de personajes")
    Puntos = 8
    clase_elegida = menu_seleccion_clase()
    print(f"Clase elegida:{clase_elegida}")

    
    nombre = input('Ingrese el nombre de su personaje:\n')
    Pj = Personaje(nombre)


    if clase_elegida == "Guerrero":
        Pj = Guerrero(nombre)
        Arma = Guerrero.Elegir_arma(Pj)
    else:
        Pj = Mago(nombre)
        Arma = Mago.Elegir_arma(Pj)

    


    print(f"\nTienes {Puntos} puntos para repartir entre tus habilidades")
    Opcion = input("¿Deseas repartirlos(si/no)? ").upper().strip()

    if Opcion != "SI":
        print('Podrá usar sus puntos siempre que quiera')
    else:
        while Puntos > 0:
            print(f"Puntos restantes: {Puntos}")
            print("\n 1-Fuerza.\n 2-Inteligencia.\n 3-Resistencia.\n 4-Velocidad.")
            Opcion = input("¿Dónde quiere añadir un punto?\n")

            if Opcion == "1":
                Pj.Fuerza += 1
            elif Opcion == "2":
                Pj.Inteligencia += 1
            elif Opcion == "3":
                Pj.Resistencia += 1
            elif Opcion == "4":
                Pj.Velocidad += 1
            else:
                print("Opcion inválida, intente otra vez")

            Puntos -= 1
        
        Pj.Atributos()
        return Pj
    
            
                
        

