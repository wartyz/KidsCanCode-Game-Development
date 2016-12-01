# Pygame template - esqueleto para un nuevo proyecto de pygame

import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 30

# define colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Los sprites son objetos, estos son sus manejadores de su rect:
#      (x,y)       top      topright
#        o----------o----------o
#        |                     |
#        |                     |
#        |        center       |
#   left o          o          o right
#        |                     |
#        |                     |
#        |                     |
#        o----------o----------o
#    bottomleft  bottom    bottomright

class Player(pygame.sprite.Sprite):
    # Sprite del player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))  # Creamos como imagen un simple cuadrado
        self.image.fill(GREEN)  # Y lo rellenamos de color verde
        self.rect = self.image.get_rect()  # Obtenemos el rect del sprite
        self.rect.center = (WIDTH / 2, HEIGHT / 2)  # Ponemos el player en el centro de la pantalla

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:  # Si supera el lado derecho de la ventana
            self.rect.right = 0  # Moverlo a la izquierda

# inicializa pygame y crea ventana
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()  # Creamos un grupo de sprites
player = Player()  # Creamos objeto player
all_sprites.add(player)  # Añadimos el objeto player a la lista de sprites


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
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)  # Dibujamos todos los sprites
    # *despues* de dibujar, intercambiar la pantalla
    pygame.display.flip()

pygame.quit()