import pygame

#pip install pygame

ANCHO = 800
ALTO = 600
VENTANA = pygame.display.set_mode([ANCHO,ALTO])

jugando = True

while jugando:
    eventos = pygame.event.get()

    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False

    pygame.display.update()

quit()