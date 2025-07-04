#Creación del inicio del juego, donde tiraremos dados para ver quien comienza primero
import random
from Objetos_juego import Personaje


def Dado():
    Dado =  random.randint(1, 6)
    print(Dado)
    return Dado

def Turno(Pj1, Pj2):
    input(f"Jugador 1({Pj1.Nombre}) - Presione Enter para tirar su primer dado")
    Dado1 = Dado()
    input(f"Jugador 1({Pj1.Nombre}) - Presione Enter para tirar su segundo dado")
    Dado2 = Dado()
    Total_j1 = Dado1 + Dado2
    print(f"Total de puntos jugador 1({Pj1.Nombre}):", Total_j1)

    input(f"Jugador 2({Pj2.Nombre}) - Presione Enter para tirar su primer dado")
    Dado1R = Dado()
    input(f"Jugador 2({Pj2.Nombre}) - Presione Enter para tirar su segundo dado")
    Dado2R = Dado()
    Total_j2 = Dado1R + Dado2R
    print(f"Total de puntos jugador 2:({Pj2.Nombre})", Total_j2)

    

    print(f"Jugador 1({Pj1.Nombre}) sacó: {Dado1} y {Dado2}")
    print(f"Jugador 2 sacó({Pj2.Nombre}): {Dado1R} y {Dado2R}")

    if Total_j1 == Total_j2:
        print("Empate, vuelvan a tirar dados")
    else:
        Ganador = str("Jugador 1" if Total_j1 > Total_j2 else "Jugador 2")
        print("El puntaje mayor fue del", Ganador, "por lo que jugará el primer turno.")
        return Ganador

