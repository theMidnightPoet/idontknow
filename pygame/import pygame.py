import pygame
import sys
import random
import time

pygame.init()

# Configuración de pantalla
size = (475, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Juego de Reacción")

# Colores Originales y sus versiones claras (Light)
INDIGO = (75, 0, 130)
GOLD = (255, 215, 0); L_GOLD = (255, 240, 150)
DODGER_BLUE = (30, 144, 255); L_DODGER_BLUE = (150, 200, 255)
SEA_GREEN = (60, 179, 113); L_SEA_GREEN = (150, 230, 180)
TOMATO = (255, 99, 71); L_TOMATO = (255, 180, 160)
WHITE = (255, 255, 255)

# Definición de los rectángulos (x, y, ancho, alto)
rects = [
    {"id": 0, "color": GOLD, "bright": L_GOLD, "rect": pygame.Rect(52, 15, 170, 330)},
    {"id": 1, "color": DODGER_BLUE, "bright": L_DODGER_BLUE, "rect": pygame.Rect(52, 360, 170, 330)},
    {"id": 2, "color": SEA_GREEN, "bright": L_SEA_GREEN, "rect": pygame.Rect(250, 15, 170, 330)},
    {"id": 3, "color": TOMATO, "bright": L_TOMATO, "rect": pygame.Rect(250, 360, 170, 330)}
]

# Variables de control de juego
font = pygame.font.SysFont("Arial", 24)
clock = pygame.time.Clock()

opciones_rondas = [1, 3, 5, 10]
rondas_totales = 0
ronda_actual = 0
tiempos_reaccion = []
estado = "MENU" # MENU, ESPERANDO, ILUMINADO, FINALIZADO

target_rect = None
tiempo_inicio_luz = 0
tiempo_aparicion = 0

def mostrar_texto(txt, y_off):
    text_surf = font.render(txt, True, WHITE)
    screen.blit(text_surf, (size[0]//2 - text_surf.get_width()//2, y_off))

while True:
    screen.fill(INDIGO)
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            
            if estado == "MENU":
                # Detectar selección de rondas (reemplazo simple por teclado o clic en área)
                # Por simplicidad, usaremos teclas 1, 3, 5, 0 para configurar:
                pass
            
            if estado == "ILUMINADO":
                if target_rect["rect"].collidepoint(mouse_pos):
                    reaccion = (current_time - tiempo_inicio_luz) / 1000.0
                    tiempos_reaccion.append(reaccion)
                    ronda_actual += 1
                    
                    if ronda_actual >= rondas_totales:
                        # Cálculo del promedio interno
                        promedio = sum(tiempos_reaccion) / len(tiempos_reaccion)
                        estado = "FINALIZADO"
                    else:
                        estado = "ESPERANDO"
                        tiempo_aparicion = current_time + random.randint(1000, 3000)

        if event.type == pygame.KEYDOWN and estado == "MENU":
            if event.key == pygame.K_1: rondas_totales = 1
            if event.key == pygame.K_3: rondas_totales = 3
            if event.key == pygame.K_5: rondas_totales = 5
            if event.key == pygame.K_0: rondas_totales = 10
            
            if rondas_totales > 0:
                estado = "ESPERANDO"
                ronda_actual = 0
                tiempos_reaccion = []
                tiempo_aparicion = current_time + random.randint(1000, 3000)

    # Lógica de dibujo y estados
    if estado == "MENU":
        mostrar_texto("Selecciona Rondas: Presiona 1, 3, 5 o 0 (para 10)", 300)
    
    elif estado == "ESPERANDO":
        # Dibujar cuadros normales
        for r in rects:
            pygame.draw.rect(screen, r["color"], r["rect"])
        
        if current_time >= tiempo_aparicion:
            target_rect = random.choice(rects)
            tiempo_inicio_luz = pygame.time.get_ticks()
            estado = "ILUMINADO"
            
    elif estado == "ILUMINADO":
        for r in rects:
            color = r["bright"] if r == target_rect else r["color"]
            pygame.draw.rect(screen, color, r["rect"])
            
    elif estado == "FINALIZADO":
        mostrar_texto("¡Juego Terminado!", 300)
        mostrar_texto("Presiona R para reiniciar", 350)
        if pygame.key.get_pressed()[pygame.K_r]:
            estado = "MENU"
            rondas_totales = 0

    pygame.display.flip()
    clock.tick(60)