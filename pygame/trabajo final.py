import pygame
import sys
import random

pygame.init()

size = (475, 850)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Juego de Reacción")

INDIGO = (75, 0, 130)

GOLD = (255, 215, 0)
L_GOLD = (255, 240, 150)

DODGER_BLUE = (30, 144, 255)
L_DODGER_BLUE = (150, 200, 255)

SEA_GREEN = (60, 179, 113)
L_SEA_GREEN = (150, 230, 180)

TOMATO = (255, 99, 71)
L_TOMATO = (255, 180, 160)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

rects = [
    {"id": 0, "color": GOLD, "bright": L_GOLD,
     "rect": pygame.Rect(52, 50, 180, 350)},

    {"id": 1, "color": DODGER_BLUE, "bright": L_DODGER_BLUE,
     "rect": pygame.Rect(52, 420, 180, 350)},

    {"id": 2, "color": SEA_GREEN, "bright": L_SEA_GREEN,
     "rect": pygame.Rect(250, 50, 180, 350)},

    {"id": 3, "color": TOMATO, "bright": L_TOMATO,
     "rect": pygame.Rect(250, 420, 180, 350)}
]

font = pygame.font.SysFont("verdana", 24)
font_big = pygame.font.SysFont("verdana", 30, True)

clock = pygame.time.Clock()

rondas_totales = 0
ronda_actual = 0

tiempos_reaccion = []

historial_partidas = []

estado = "MENU"

target_rect = None

tiempo_inicio_luz = 0
tiempo_aparicion = 0

boton_reinicio = pygame.Rect(80, 580, 320, 70)

def mostrar_texto(txt, y_off, fuente=font, color=WHITE):

    text_surf = fuente.render(txt, True, color)

    screen.blit(
        text_surf,
        (size[0] // 2 - text_surf.get_width() // 2, y_off)
    )

while True:

    screen.fill(INDIGO)

    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            mouse_pos = event.pos

            if estado == "ILUMINADO":

                if target_rect["rect"].collidepoint(mouse_pos):

                    reaccion = (
                        current_time - tiempo_inicio_luz
                    )

                    tiempos_reaccion.append(reaccion)

                    ronda_actual += 1

                    if ronda_actual >= rondas_totales:

                        promedio = (
                            sum(tiempos_reaccion)
                            / len(tiempos_reaccion)
                        )

                        historial_partidas.append({
                            "rondas": rondas_totales,
                            "promedio": round(promedio),
                            "mejor": round(min(tiempos_reaccion))
                        })

                        estado = "FINALIZADO"

                    else:

                        estado = "ESPERANDO"

                        tiempo_aparicion = (
                            current_time
                            + random.randint(1000, 3000)
                        )

            elif estado == "FINALIZADO":

                if boton_reinicio.collidepoint(mouse_pos):

                    estado = "MENU"

                    rondas_totales = 0
                    ronda_actual = 0

                    tiempos_reaccion = []

        if event.type == pygame.KEYDOWN and estado == "MENU":

            if event.key == pygame.K_1:
                rondas_totales = 1

            if event.key == pygame.K_3:
                rondas_totales = 3

            if event.key == pygame.K_5:
                rondas_totales = 5

            if event.key == pygame.K_0:
                rondas_totales = 10

            if rondas_totales > 0:

                estado = "ESPERANDO"

                ronda_actual = 0

                tiempos_reaccion = []

                tiempo_aparicion = (
                    current_time
                    + random.randint(1000, 3000)
                )

    if estado == "MENU":

        pygame.draw.rect(screen, (95, 20, 160), (25, 40, 425, 760), border_radius=25)

        
        titulo = pygame.font.SysFont("verdana", 54, True)

        mostrar_texto(
            "ClicQuest",
            90,
            titulo,
            GOLD
        )

        
        mostrar_texto(
            "Juego de Reacción",
            170,
            font_big,
            WHITE
        )

        mostrar_texto(
            "Presiona una tecla para elegir rondas",
            230,
            font,
            L_GOLD
        )

        
        cuadros = [
            {"x": 70, "y": 330, "w": 140, "h": 120, "txt": "1"},
            {"x": 260, "y": 330, "w": 140, "h": 120, "txt": "3"},
            {"x": 170, "y": 500, "w": 140, "h": 120, "txt": "5"},
        ]

        for c in cuadros:

            
            pygame.draw.rect(
                screen,
                WHITE,
                (c["x"], c["y"], c["w"], c["h"]),
                border_radius=20
            )

            
            pygame.draw.rect(
                screen,
                GOLD,
                (c["x"], c["y"], c["w"], c["h"]),
                5,
                border_radius=20
            )

            
            numero = pygame.font.SysFont("verdana", 42, True)

            texto_num = numero.render(
                c["txt"],
                True,
                INDIGO
            )

            screen.blit(
                texto_num,
                (
                    c["x"] + c["w"]//2 - texto_num.get_width()//2,
                    c["y"] + 15
                )
            )

            
            texto_rondas = font.render(
                "Rondas",
                True,
                BLACK
            )

            screen.blit(
                texto_rondas,
                (
                    c["x"] + c["w"]//2 - texto_rondas.get_width()//2,
                    c["y"] + 75
                )
            )

        
        mostrar_texto(
            "Teclas: 1 - 3 - 5",
            690,
            font_big,
            L_SEA_GREEN
        )

    elif estado == "ESPERANDO":

        for r in rects:

            pygame.draw.rect(
                screen,
                r["color"],
                r["rect"]
            )

        if current_time >= tiempo_aparicion:

            target_rect = random.choice(rects)

            tiempo_inicio_luz = pygame.time.get_ticks()

            estado = "ILUMINADO"

    elif estado == "ILUMINADO":

        for r in rects:

            color = (
                r["bright"]
                if r == target_rect
                else r["color"]
            )

            pygame.draw.rect(
                screen,
                color,
                r["rect"]
            )

    elif estado == "FINALIZADO":

        screen.fill(INDIGO)

        pygame.draw.rect(
            screen,
            WHITE,
            (45, 70, 380, 480)
        )

        pygame.draw.line(
            screen,
            BLACK,
            (45, 210),
            (425, 210),
            5
        )

        texto_rondas = font_big.render(
            f"Rondas Realizadas: {rondas_totales}",
            True,
            BLACK
        )

        screen.blit(texto_rondas, (60, 70))

        texto_promedio = font_big.render(
            f"Promedio: {round(promedio)} ms",
            True,
            BLACK
        )

        screen.blit(texto_promedio, (60,150))

        titulo = font_big.render(
            "Mejores Resultados",
            True,
            BLACK
        )

        screen.blit(titulo, (60, 220))

        titulo2 = font_big.render(
            "registrados:",
            True,
            BLACK
        )

        screen.blit(titulo2, (60, 250))

        mejores = sorted(tiempos_reaccion)

        y = 305

        for i in range(len(mejores)):

            texto = font.render(
                f"{i+1}. {round(mejores[i])} ms",
                True,
                BLACK
            )

            screen.blit(texto, (60, y))

            y += 40

        pygame.draw.rect(
            screen,
            GREEN,
            boton_reinicio
        )

        texto_boton = font_big.render(
            "Volver a intentar",
            True,
            WHITE
        )

        screen.blit(texto_boton, (100, 600))

        titulo_historial = font_big.render(
            "Historial de partidas",
            True,
            WHITE
        )

        screen.blit(titulo_historial, (70, 680))

        y_historial = 750

        for i in range(len(historial_partidas)):

            partida = historial_partidas[i]

            texto_historial = font.render(
                f"Partida {i+1}: "
                f"{partida['promedio']}ms | "
                f"Mejor: {partida['mejor']}ms",
                True,
                WHITE
            )

            screen.blit(texto_historial, (20, y_historial))

            y_historial += 30

    pygame.display.flip()

    clock.tick(30)