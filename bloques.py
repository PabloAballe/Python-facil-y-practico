
#importamos las librerias
import pygame
import random

# definimos los colores que vamos a usar
AZULADO = (  24,   166,   183)
BLANCO = (255, 255, 255)
AMARILLO   = (255,   247,   29)





#representamos los bloques de nuestro juego
class Block(pygame.sprite.Sprite):
     def __init__(self, color, width, height):
#llamamos al metodo contrsuctor
        super().__init__()

    #creamos las imagenes de los bloques
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

#tomamos los parametros de los rectangulos
        self.rect = self.image.get_rect()

# iniciamos PyGame
pygame.init()

# definimos el alto y el ancho de la pantalla
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

#definimos el grupo de objetos que serian los bloques
block_list = pygame.sprite.Group()

#aqui estan todos los objetos incluidos el de nuestro raton
all_sprites_list = pygame.sprite.Group()

for i in range(30):
    # representamos nuestros bloques
    block = Block(AZULADO, 20, 15)

    # definimos la posicion de los rectangulos
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    # Añadimos los bloques a la lista de objetos
    block_list.add(block)
    all_sprites_list.add(block)

# Creamos el bloque del jugador
player = Block(AMARILLO, 20, 15)
all_sprites_list.add(player)

#definimos el bucle hasta que el usuario cierre la ventana
done = False

# definimos cada cuanto queremos que se actualice la ventana
clock = pygame.time.Clock()

score = 0

# -------- funcion principal del juego -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # limpiamos la pantalla
    screen.fill(BLANCO)

#tomamos la posicion actual del raton
    pos = pygame.mouse.get_pos()

    player.rect.x = pos[0]
    player.rect.y = pos[1]

    # vemos si el bloque del jugador a colisionado con algo.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    # chckeamos las coaliciones.
    for block in blocks_hit_list:
        score += 1
        print(score)

    # dibujamos los rectangulos
    all_sprites_list.draw(screen)

    # actualizamos la pantalla
    pygame.display.flip()

    # liemite de cuadros por segundo
    clock.tick(60)


    #fin del juego
pygame.quit()
