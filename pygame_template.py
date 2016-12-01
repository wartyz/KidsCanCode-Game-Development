# Pygame template - esqueleto para un nuevo proyecto de pygame
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

# define colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# inicializa pygame y crea ventana
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Game Loop
running = True
while running:
    # Mantener el bucle con la velocidad adecuada
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # prueba de cerrar ventana
        if event.type == pygame.QUIT:
            running = False
    # Update

    # Draw / render
    screen.fill(BLACK)
    # *despues* de dibujar, intercambiar la pantalla
    pygame.display.flip()

pygame.quit()