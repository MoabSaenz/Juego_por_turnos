#Toda la logica para el juego por turnos, queremos que el jugador que gane los dados siempre ataque primero sin importar la velocidad
#para esto primero deberemos comprobar si los dos estan vivos
#Después queremos saber si alguien murio, por lo que acabara el combate, y el ganador subirá un nivel
def Inicio_combate(pj1, pj2, Primer_turno):
    if Primer_turno == 'Jugador 2':
        pj2, pj1 = pj1, pj2

    Primer_turno = True

    while pj1.Esta_vivo() and pj2.Esta_vivo():
        if Primer_turno:
            pj1.Atacar(pj2)
            Primer_turno = False

        else:
            if pj1.Velocidad >= pj2.Velocidad:
                Atacante, Defensor = pj1, pj2
                Atacante.Atacar(Defensor)
                if pj2.Esta_vivo():
                    pj2.Atacar(pj1)
            else:
                Atacante, Defensor = pj2, pj1
                Atacante.Atacar(Defensor)
                if pj1.Esta_vivo():
                    pj1.Atacar(pj2)
            


    if pj1.Esta_vivo():
        print(f"El ganador es: {pj1.Nombre}")
    else:
        print(f"El ganador es: {pj2.Nombre}")
    
    

