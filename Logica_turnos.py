#Toda la logica para el juego por turnos, queremos que el jugador que gane los dados siempre ataque primero sin importar la velocidad
#para esto primero deberemos comprobar si los dos estan vivos
#Después queremos saber si alguien murio, por lo que acabara el combate, y el ganador subirá un nivel
def Inicio_combate(pj1, pj2, Primer_turno):
    if Primer_turno == 'Jugador 2':
        pj2, pj1 = pj1, pj2
    while pj1.Esta_vivo() and pj2.Esta_vivo():
        if pj1.Velocidad >= pj2.Velocidad:
            Atacante, Defensor = pj1, pj2 
        else:
            Atacante, Defensor = pj2, pj1
        Atacante.Atacar(Defensor)

        if Defensor.Esta_vivo():
            Atacante, Defensor = Defensor, Atacante
            Atacante.Atacar(Defensor)

    if pj1.Esta_vivo():
        print(f"El ganador es: {pj1.Nombre}")
    else:
        print(f"El ganador es: {pj2.Nombre}")
    
    

