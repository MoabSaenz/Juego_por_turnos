import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar pantalla
ANCHO, ALTO = 600, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Selecciona tu clase")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 120, 255)
GRIS = (200, 200, 200)

# Fuente
fuente = pygame.font.SysFont(None, 40)

# Opciones
opciones = ["Guerrero", "Mago"]
indice_seleccionado = 0

def dibujar_menu():
    pantalla.fill(BLANCO)
    for i, opcion in enumerate(opciones):
        color = AZUL if i == indice_seleccionado else NEGRO
        texto = fuente.render(opcion, True, color)
        rect = texto.get_rect(center=(ANCHO // 2, 150 + i * 60))
        pantalla.blit(texto, rect)
    pygame.display.flip()

def obtener_opcion_por_click(pos):
    for i, opcion in enumerate(opciones):
        rect = pygame.Rect(200, 130 + i * 60, 200, 50)
        if rect.collidepoint(pos):
            return i
    return None

def menu_seleccion_clase():
    print("Seleccione su clase(Ventana abierta)")
    global indice_seleccionado
    corriendo = True
    while corriendo:
        dibujar_menu()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    indice_seleccionado = (indice_seleccionado - 1) % len(opciones)
                elif evento.key == pygame.K_DOWN:
                    indice_seleccionado = (indice_seleccionado + 1) % len(opciones)
                elif evento.key == pygame.K_RETURN:
                    corriendo = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                indice = obtener_opcion_por_click(evento.pos)
                if indice is not None:
                    indice_seleccionado = indice
                    corriendo = False
    return opciones[indice_seleccionado]


