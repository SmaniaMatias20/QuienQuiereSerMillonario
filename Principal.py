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
         
    actualizar_ventana(ventana, pregunta, opciones, indice)

    respuesta = verificar_respuesta(pregunta)
    
    continuar = None
    continuar = continuar_partida(ventana, indice)
    
    if respuesta == True and continuar == True:
        indice = indice + 1
        if indice >= len(rangos):
            # Gano el millon
            guardar_puntuacion(rangos[indice-1])
            break
        pregunta = filtrar_pregunta(banco_de_preguntas, rangos[indice])
        opciones = mezclar_opciones(pregunta["opciones"])
    elif respuesta == False or continuar == False:
        # Fin del juego
        if continuar == False:
            guardar_puntuacion(rangos[indice])
            break
        elif respuesta == False:
            guardar_puntuacion(0)
            break
    
    reloj.tick(60)
    pygame.display.flip()

pygame.quit()
