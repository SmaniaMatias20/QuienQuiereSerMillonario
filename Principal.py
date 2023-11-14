from Configuracion import *
from Multimedia import *
from ClaseJugador import *
import pygame as py


pygame.init()

reloj = py.time.Clock()  
tiempo_maximo = pygame.time.get_ticks() + 30 * 1000

ventana = configurar_ventana(500, 900, IMAGEN_ICONO, "¿Quien quiere ser millonario?")

indice_de_rango = 0
pregunta = filtrar_pregunta(banco_de_preguntas, rangos[indice_de_rango])
opciones = mezclar_opciones(pregunta["opciones"])

while True:

    actualizar_ventana(ventana, pregunta, opciones, indice_de_rango)

    respuesta = verificar_respuesta(pregunta)
    
    continuar = None
    continuar = continuar_partida(ventana, indice_de_rango)

    tiempo_restante = mostrar_tiempo(ventana, tiempo_maximo)
    
    if respuesta == True and continuar == True:
        
        indice_de_rango = indice_de_rango + 1
        if indice_de_rango >= len(rangos):
            # Gano el millon
            guardar_puntuacion(rangos[indice_de_rango-1])
            break
        pregunta = filtrar_pregunta(banco_de_preguntas, rangos[indice_de_rango])
        opciones = mezclar_opciones(pregunta["opciones"])

        tiempo_maximo = pygame.time.get_ticks() + 30 * 1000

        if comodin["50-50"] == "usado":
            comodin["50-50"] = "desactivo"

    elif respuesta == False or tiempo_restante == 0:
        guardar_puntuacion(0)
        break
    elif continuar == False: 
        guardar_puntuacion(rangos[indice_de_rango])
        break

    reloj.tick(60)
    pygame.display.flip()

pygame.quit()
