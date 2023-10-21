from Configuracion import *
from Multimedia import *
from ClaseJugador import *
import pygame, sys


pygame.init()

reloj = pygame.time.Clock() 
sonido = cargar_sonido()
# sonido.play(-1) 
ventana = configurar_ventana(500, 900, lista_de_imagenes[2], "¿Quien quiere ser millonario?")

indice = 0
pregunta = filtrar_pregunta(banco_de_preguntas, rangos[indice])
opciones = mezclar_opciones(pregunta["opciones"])

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
     
    actualizar_ventana(ventana, pregunta, opciones, indice)

    respuesta = verificar_respuesta(pregunta)
    
    continuar = ""
    continuar = continuar_partida(ventana, indice)
    
    if respuesta == True and continuar == True:
        indice = indice + 1
        if indice >= len(rangos):
            # Gano el millon
            jugador = cargar_jugador(rangos[indice-1])
            guardar_puntuacion(jugador)
            break
        pregunta = filtrar_pregunta(banco_de_preguntas, rangos[indice])
        opciones = mezclar_opciones(pregunta["opciones"])
    elif respuesta == False or continuar == False:
        # Fin del juego
        if continuar == False:
            jugador = cargar_jugador(rangos[indice])
            guardar_puntuacion(jugador)
            break
        elif respuesta == False:
            jugador = cargar_jugador(0)
            guardar_puntuacion(jugador)
            break
    


    reloj.tick(60)
    pygame.display.flip()

pygame.quit()
