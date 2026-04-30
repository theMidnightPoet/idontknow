import pygame, sys
pygame.init()

size = (800, 500)

#CREAR VENTANA 
screen = pygame.display.set_mode(size)

#creacion bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            sys.exit() 