import pygame, sys
pygame.init()

size = (475, 700)
#definir colores
#primero es rojo el segundo es verde y el tercero es azul
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
SEA_GREEN = (60, 179, 113)
TOMATO = (255, 99, 71)
BLUE = (0, 0, 128)
TEAL = (0, 128, 128)
GRAY = (128, 128, 128)
DODGER_BLUE = (30, 144, 255)
GOLD = (255, 215, 0)
INDIGO = (75, 0, 130)

#CREAR VENTANA 
screen = pygame.display.set_mode(size)

#creacion bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() 
#color del fondo
    screen.fill(INDIGO)
#----Zona de dibujo 
    pygame.draw.rect(screen, GOLD, (52, 15, 170, 330))
    pygame.draw.rect(screen, DODGER_BLUE, (52, 360, 170, 330))
    pygame.draw.rect(screen, SEA_GREEN, (250, 15, 170, 330))
    pygame.draw.rect(screen, TOMATO, (250, 360, 170, 330))





#Zona de dibujo----
    #actualizar pantalla
    pygame.display.flip()