#importamos las librerias necesarias
import pygame
import random

# definimos los colores que vamos a estar usando
CARAMELO = (236, 226, 224)
ROJO = (183, 50, 24)


#definimos los tamaños de la pantalla
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

#definimos el tamaño de nuestra bola
tamano_bola = 25


#funcion para ratrear la bola
class Bola:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0

#creamos una nueva bola
def make_bola():
    bola = Bola()
    # posicion inicial de la bola
    bola.x = random.randrange(tamano_bola, SCREEN_WIDTH - tamano_bola)
    bola.y = random.randrange(tamano_bola, SCREEN_HEIGHT - tamano_bola)

    # definimos la velocidad del rectangulo
    bola.change_x = random.randrange(-2, 3)
    bola.change_y = random.randrange(-2, 3)

    return bola

def main():
    pygame.init()

    # Creamos los tamaños de la pantalla ayudandonos de las constantes anteriores
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Lanzador de Bolas")

    # bucle hasta que se cierre la ventana
    done = False

    # procesamos los cambios en la pantalla
    clock = pygame.time.Clock()

    bola_list = []

    bola = make_bola()
    bola_list.append(bola)

    # --------Bucle principal -----------
    while not done:
        #procesamos los eventos del teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bola = make_bola()
                    bola_list.append(bola)

        # logica del juego
        for bola in bola_list:

            bola.x += bola.change_x
            bola.y += bola.change_y


            if bola.y > SCREEN_HEIGHT - tamano_bola or bola.y < tamano_bola:
                bola.change_y *= -1
            if bola.x > SCREEN_WIDTH - tamano_bola or bola.x < tamano_bola:
                bola.change_x *= -1

        #definimos el color de fondo
        screen.fill(CARAMELO)

        # dibujamos la bola
        for bola in bola_list:
            pygame.draw.circle(screen, ROJO, [bola.x, bola.y], tamano_bola)

        #definimos los cuadros por segundo
        clock.tick(60)

        # actualizar la pantalla
        pygame.display.flip()

    # cerrar el juego
    pygame.quit()


#definimos el punto de entrada de nuestro juego que aun no existe
if __name__ == "__main__":
    main()
