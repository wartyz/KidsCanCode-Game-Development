# Game Development 1- 1,2,3: Sprites

import pygame
import random
import os

WIDTH = 800
HEIGHT = 600
FPS = 30

# define colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Activa assets
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img")

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
        # Cargamos la imagen (obtenemos una surface) y la convertimos a un nuevo formato de píxeles
        self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
        self.image.set_colorkey(BLACK) # Color transparente para sprite
        self.rect = self.image.get_rect()  # Obtenemos el rect del sprite
        self.rect.center = (WIDTH / 2, HEIGHT / 2)  # Ponemos el player en el centro de la pantalla
        self.y_speed = 5

    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        if self.rect.bottom > HEIGHT - 200:  # Si baja mucho ---> subir
            self.y_speed = -5
        if self.rect.top < 200:  # Si sube mucho --> bajar
            self.y_speed = 5
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
    screen.fill(BLUE)
    all_sprites.draw(screen)  # Dibujamos todos los sprites
    # *despues* de dibujar, intercambiar la pantalla
    pygame.display.flip()

pygame.quit()