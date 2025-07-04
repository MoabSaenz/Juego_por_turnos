#-------------------------------------Creacion de personajes--------------------------------------------------------------------#
from Creador_personaje import Creador_personaje
from Random_juego import Turno
from Logica_turnos import Inicio_combate

print("Jugador 1, cree su personaje")

Pj1 = Creador_personaje()


print("Jugador 2, cree su personaje")

Pj2 = Creador_personaje()

print("\n¡Listos para pelear!")
Pj1.Atributos()
Pj2.Atributos()

inicio_juego = Turno(Pj1, Pj2)
Inicio_combate(Pj1, Pj2, inicio_juego)
