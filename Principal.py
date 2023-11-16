from Configuracion import *
from Multimedia import *
from ClaseJugador import *
import pygame as py

py.init()

jugar = menu_intro()

reloj = py.time.Clock()  

VENTANA = configurar_ventana(500, 900, imagen_icono, "¿Quien quiere ser millonario?")
cargar_sonido("sonidos\sonido.mp3")

indice_de_rango = 0
pregunta = filtrar_pregunta(banco_de_preguntas, rangos[indice_de_rango])
opciones = mezclar_opciones(pregunta["opciones"])

tiempo_maximo = py.time.get_ticks() + 30 * 1000
while jugar:

    respuesta = actualizar_ventana(VENTANA, pregunta, opciones, indice_de_rango)

    continuar = None
    continuar = continuar_partida(VENTANA, indice_de_rango)

    tiempo_restante = mostrar_tiempo(VENTANA, tiempo_maximo)
    
    if respuesta == True and continuar == True:
        
        indice_de_rango = indice_de_rango + 1
        if indice_de_rango >= len(rangos):
            # Gano el millon
            guardar_puntuacion(rangos[indice_de_rango-1])
            break
        pregunta = filtrar_pregunta(banco_de_preguntas, rangos[indice_de_rango])
        opciones = mezclar_opciones(pregunta["opciones"])

        tiempo_maximo = py.time.get_ticks() + 30 * 1000

        if comodin["50-50"] == "usado":
            comodin["50-50"] = "desactivo"

    elif respuesta == False or tiempo_restante == 0:
        guardar_puntuacion(0)
        break
    elif continuar == False: 
        guardar_puntuacion(rangos[indice_de_rango])
        break

    reloj.tick(60)
    py.display.flip()

py.quit()
