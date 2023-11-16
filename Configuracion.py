from tkinter.simpledialog import askstring as prompt
from Archivos import *
from ClaseJugador import *
from Multimedia import *
import pygame as py
import random
import sys


rangos = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
comodin = {"50-50": "activo"}

banco_de_preguntas = cargar_preguntas()

def configurar_ventana(alto: int, ancho: int, imagen_icono: py.Surface, titulo: str):
    """
    Brief: 
        Configura una ventana.
    Parametros:
        - alto (int): El alto de la ventana.
        - ancho (int): El ancho de la ventana.
        - icono (py.Surface): El path del icono de la ventana.
        - titulo (str): El titulo de la ventana.
    Retorno:
        - ventana.
    """
    ventana = py.display.set_mode((ancho, alto))                                 
    py.display.set_caption(titulo)                                        
    py.display.set_icon(imagen_icono) 

    return ventana 

def menu_intro():
    """
    Brief: 
        Crea una ventana de menu.
    Parametros:
        - Sin parametros.
    Retorno:
        - True.
    """
    VENTANA_MENU = configurar_ventana(500, 500, imagen_icono, "Menu")

    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                sys.exit()
            elif event.type == py.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = py.mouse.get_pos()
                if rect_boton.collidepoint(mouse_x, mouse_y):
                    return True
                    
        VENTANA_MENU.blit(imagen_menu, [0, 0])
        rect_boton = VENTANA_MENU.blit(boton_comenzar, [50, 300])

        py.display.flip()    

def actualizar_ventana(ventana: py.Surface, pregunta: dict, opciones: list, indice: int):
    """
    Brief: 
        Actualiza la ventana, aplicando las imagenes y mostrando tanto las preguntas como las respuestas.
    Parametros:
        - ventana (pygame.Surface): Ventana a actualizar.
        - pregunta (dict): Pregunta a mostrar en la ventana.
        - opciones (list): Opciones a mostrar en la ventana.
        - indice (int): El indice de la lista de rangos. 
    Retorno:
        - Sin retorno.
    """
    rectangulos_opciones = aplicar_imagenes(ventana)
    mostrar_pregunta(ventana, pregunta)
    mostrar_opciones(ventana, opciones, pregunta)
    mostrar_rangos(ventana, rangos[indice], 700, 130)
    respuesta = elegir_respuesta(ventana, pregunta, rectangulos_opciones)

    return respuesta
    
    
def aplicar_imagenes(ventana: py.Surface):
    """
    Brief: 
        Muestra las imagenes en pantalla.
    Parametros:
        - ventana (pygame.Surface): Ventana donde se mostraran las imagenes.
    Retorno:
        - rectangulos.
    """
    ventana.blit(imagen_fondo, [0, 0])
    ventana.blit(imagen_conductor, [480, 125])
    ventana.blit(imagen_rangos, [650, 50])
    ventana.blit(imagen_pregunta, [35, 320])
    primer_rect = ventana.blit(imagen_respuesta, [45, 395])
    segundo_rect = ventana.blit(imagen_respuesta, [45, 445])
    tercer_rect = ventana.blit(imagen_respuesta, [345, 395])
    cuarto_rect = ventana.blit(imagen_respuesta, [345, 445])

    rects_opciones = {
        "primer_rect": primer_rect,
        "segundo_rect": segundo_rect,
        "tercer_rect": tercer_rect,
        "cuarto_rect": cuarto_rect,
    }

    return rects_opciones

def aplicar_comodin(ventana: py.Surface):
    """
    Brief: 
        Muestra el comodin en pantalla
    Parametros:
        - ventana (pygame.Surface): Ventana donde se mostrara el comodin.
    Retorno:
        - rectangulo.
    """
    if comodin["50-50"] == "activo":
        rect_comodin = ventana.blit(imagen_comodin, [10, 10])
    else:
        rect_comodin = ventana.blit(py.Surface((50,50)), [10, 10])

    return rect_comodin


def filtrar_pregunta(banco_de_preguntas: list, dificultad: int):
    """
    Brief: 
        Filtra las preguntas por dificultad.
    Parametros:
        - banco_de_preguntas (list): Lista con las preguntas.
        - dificultad (int): Dificultad de la pregunta a filtrar.
    Retorno:
        - Una pregunta aleatoria con la dificultad pedida.
    """
    preguntas_por_dificultad = []
     
    for pregunta in banco_de_preguntas:
        if pregunta["dificultad"] == dificultad:
            preguntas_por_dificultad.append(pregunta)
    
    indice_aleatorio = random.randint(0, len(preguntas_por_dificultad)-1)
    
    return preguntas_por_dificultad[indice_aleatorio]
    
def mostrar_pregunta(ventana: py.Surface, pregunta: dict):
    """
    Brief: 
        Muestra una pregunta en la ventana.
    Parametros:
        - ventana (pygame.Surface): Ventana donde se va a mostrar la pregunta.
        - pregunta (dict): Pregunta que se va a mostrar en la ventana.
    Retorno:
        - Sin retorno.
    """
    aplicar_texto(ventana, pregunta["pregunta"], 50, 340, BLANCO, 12, "Arial Black")
    
def mostrar_opciones(ventana: py.Surface, opciones: list, pregunta: dict):
    """
    Brief: 
        Muestra las opciones en la ventana.
    Parametros:
        - ventana (pygame.Surface): Ventana donde se van a mostrar las opciones.
        - opciones (list): Opciones que se van a mostrar en la ventana.
    Retorno:
        - Sin retorno.
    """
    match comodin["50-50"]:
        case "usado":
            if pregunta["respuesta_correcta"] == opciones[0]:
                aplicar_texto(ventana, opciones[0], 50, 410, BLANCO, 12, "Arial Black")
                aplicar_texto(ventana, opciones[3], 350, 460, BLANCO, 12, "Arial Black")
            elif pregunta["respuesta_correcta"] == opciones[1]:
                aplicar_texto(ventana, opciones[1], 50, 460, BLANCO, 12, "Arial Black")
                aplicar_texto(ventana, opciones[3], 350, 460, BLANCO, 12, "Arial Black") 
            elif pregunta["respuesta_correcta"] == opciones[2]:
                aplicar_texto(ventana, opciones[1], 50, 460, BLANCO, 12, "Arial Black")
                aplicar_texto(ventana, opciones[2], 350, 410, BLANCO, 12, "Arial Black")
            else:
                aplicar_texto(ventana, opciones[0], 50, 410, BLANCO, 12, "Arial Black")
                aplicar_texto(ventana, opciones[3], 350, 460, BLANCO, 12, "Arial Black")

            comodin["50-50"] == "desactivo"
        case _: 
            aplicar_texto(ventana, opciones[0], 50, 410, BLANCO, 12, "Arial Black")
            aplicar_texto(ventana, opciones[1], 50, 460, BLANCO, 12, "Arial Black")
            aplicar_texto(ventana, opciones[2], 350, 410, BLANCO, 12, "Arial Black")
            aplicar_texto(ventana, opciones[3], 350, 460, BLANCO, 12, "Arial Black")

  
def mezclar_opciones(opciones: list):
    """
    Brief: 
        Mezcla las opciones de las preguntas.
    Parametros:
        - opciones (list): Lista con las opciones.
    Retorno:
        - opciones.
    """
    random.shuffle(opciones)
    
    return opciones

def verificar_respuesta(pregunta: dict, rects_opciones: dict):
    """
    Brief: 
        Verifica las coordenadas donde se encuentra la respuesta correcta.
    Parametros:
        - pregunta (dict): Pregunta que se va a analizar.
        - rects_opciones (dict): Los rectangulos de las opciones bliteadas en pantalla.
    Retorno:
        - respuesta
    """
    if pregunta["respuesta_correcta"] == pregunta["opciones"][0]:
        coord_correcta = rects_opciones["primer_rect"]
    elif pregunta["respuesta_correcta"] == pregunta["opciones"][1]:
        coord_correcta = rects_opciones["segundo_rect"]
    elif pregunta["respuesta_correcta"] == pregunta["opciones"][2]:
        coord_correcta = rects_opciones["tercer_rect"]
    else:
        coord_correcta = rects_opciones["cuarto_rect"]
  
    return coord_correcta  
     
def elegir_respuesta(ventana: py.Surface, pregunta: dict, rects_opciones: dict):
    """
    Brief: 
        Evalua las coordenadas donde se produce el evento.
    Parametros:
        - ventana (py.Surface): Ventana del juego.
        - pregunta (dict): pregunta actual.
        - rects_opciones (dict): rectangulos de las opciones
    Retorno:
        - True.
        - False.
    """
    coord_correcta = verificar_respuesta(pregunta, rects_opciones)
    coord_comodin = aplicar_comodin(ventana)
       
    for event in py.event.get():
        if event.type == py.QUIT:
            sys.exit()
        elif event.type == py.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = py.mouse.get_pos()  
            if coord_comodin.collidepoint(mouse_x, mouse_y):
                comodin["50-50"] = "usado"    
            elif coord_correcta.collidepoint(mouse_x, mouse_y):
                return True
            else:
                return False

def mostrar_rangos(ventana: py.Surface, valor_rango: int, ubicacion_x: int, ubicacion_y: int):
    """
    Brief: 
        Muestra los rangos en la ventana.
    Parametros:
        - ventana (pygame.Surface): Ventana del juego.
        - valor_rango (int): Rango que se va a mostrar.
        - ubicacion_x (int): Ubicacion en el eje x.
        - ubicacion_y (int): Ubicacion en el eje y.
    Retorno:
        - Sin retorno.
    """
    for rango in reversed(rangos):
        if valor_rango == rango:
            color_texto = NEGRO
            dibujar_rectangulo(ventana, BLANCO, ubicacion_x-50, ubicacion_y, 225, 15)
        else:
            if rango == 1000 or rango == 32000:
                color_texto = CIAN 
            else:
                color_texto = BLANCO 


        aplicar_texto(ventana, f"${rango}", ubicacion_x, ubicacion_y, color_texto, 12, "Arial Black")
        ubicacion_y += 20

def cargar_jugador(rango: int):
    """
    Brief: 
        Carga los datos del jugador.
    Parametros:
        - rango (int): El puntaje que logro alcanzar el jugador.
    Retorno:
        - jugador
    """
    nombre_ingresado = prompt(title = "Registro", prompt = f"¡El juego ha finalizado, ha ganado ${rango}! \nIngrese su nombre: ")
    nombre = sanitizar_string(nombre_ingresado)

    jugador = Jugador()
    jugador.set_nombre(nombre)
    jugador.set_rango(rango)

    return jugador

def guardar_puntuacion(rango: int):
    """
    Brief: 
        Guarda los datos y la puntuacion del jugador.
    Parametros:
        - rango (int): El puntaje que logro alcanzar el jugador. 
    Retorno:
        - Sin retorno.
    """
    jugador = cargar_jugador(rango)

    with open("archivos/puntuaciones.csv", "a", encoding="UTF8") as archivo:
        mensaje = f"{jugador.get_nombre()}, ${jugador.get_rango()}\n"
        archivo.write(mensaje)

def continuar_partida(ventana: py.Surface, indice: int):
    """
    Brief: 
        Una vez llegado a cierto rango, le pregunta al jugador si desea continuar o retirarse con lo que tiene.
    Parametros:
        - ventana (pygame.Surface): Ventana de la partida.
        - rango (int): El puntaje que logro alcanzar el jugador. 
    Retorno:
        - True.
        - False.
        - 1
    """
    if rangos[indice] == 1000 or rangos[indice] == 32000:
        ventana.blit(imagen_mensaje, [250, 100])
        aplicar_texto(ventana, f"¡Has llegado a ${rangos[indice]}!", 270, 160, NEGRO, 12, "Arial Black")
        aplicar_texto(ventana, "Para salir presione ESC", 270, 180, NEGRO, 12, "Arial Black")

        tecla_presionada = py.key.get_pressed()
        if tecla_presionada[py.K_ESCAPE]: 
            return False
        else:
            return 1
    else:
        return True

def mostrar_tiempo(ventana: py.surface, tiempo_maximo: int):
    """
    Brief: 
        Muestra el temporizador en pantalla.
    Parametros:
        - ventana (pygame.Surface): La ventana del juego.
        - tiempo_maximo (int): El tiempo que tenemos para responder.
    Retorno:
        - segundos
    """
    tiempo_actual = py.time.get_ticks()
    tiempo_restante = max(tiempo_maximo - tiempo_actual, 0)

    segundos_restantes = tiempo_restante // 1000
    minutos = segundos_restantes // 60
    segundos = segundos_restantes % 60

    mensaje = f"{minutos:02}:{segundos:02}"
    
    aplicar_texto(ventana, mensaje, 350, 10, BLANCO, 30, "Arial Black")

    return segundos
    

