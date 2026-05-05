import pygame, sys
pygame.init()

size = (500, 700)
#definir colores
#primero es rojo el segundo es verde y el tercero es azul
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
BLUE = (0, 0, 128)
TEAL = (0, 128, 128)
VERDEPASTO = (0, )

#CREAR VENTANA 
screen = pygame.display.set_mode(size)

#creacion bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() 
#color del fondo
    screen.fill(VERDEPASTO)
#----Zona de dibujo 
    pygame.draw.line(screen, BLUE, [0,100], [100,100], 10)
    pygame.draw.rect(screen, TEAL, (165, 320, 170, 50))




#Zona de dibujo----
    #actualizar pantalla
    pygame.display.flip()