import csv
import sys
from ClaseJugador import *
from Multimedia import *
from tkinter.simpledialog import askstring as prompt
import pygame
import random
import re

rangos = [100,200,300,500,1000,2000,4000,8000,16000,32000,64000,125000,250000,500000,1000000]

lista_de_colores = definir_colores()
lista_de_imagenes = cargar_imagenes()
banco_de_preguntas = cargar_preguntas()

def configurar_ventana(alto: int, ancho: int, icono: pygame.image, titulo: str):
    """
    Brief: 
        Configura una ventana.
    Parametros:
        - alto (int): El alto de la ventana.
        - ancho (int): El ancho de la ventana.
        - icono (pygame.image): El icono de la ventana.
        - titulo (str): El titulo de la ventana.
    Retorno:
        - ventana.
    """
    ventana = pygame.display.set_mode((ancho, alto))                                 
    pygame.display.set_caption(titulo)                                        
    pygame.display.set_icon(icono) 

    return ventana 

def actualizar_ventana(ventana: pygame.Surface, pregunta: dict, opciones: list, indice: int):
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
    aplicar_imagenes(ventana)
    mostrar_pregunta(ventana, pregunta)
    mostrar_opciones(ventana, opciones)
    mostrar_rangos(ventana, rangos[indice], 700, 130)
    
def aplicar_imagenes(ventana: pygame.Surface):
    """
    Brief: 
        Muestra las imagenes en pantalla.
    Parametros:
        - ventana (pygame.Surface): Ventana donde se mostraran las imagenes.
    Retorno:
        - Sin retorno.
    """
    ventana.blit(lista_de_imagenes[0], [0, 0])
    ventana.blit(lista_de_imagenes[1], [480, 125])
    ventana.blit(lista_de_imagenes[3], [650, 50])
    ventana.blit(lista_de_imagenes[4], [45, 395])
    ventana.blit(lista_de_imagenes[4], [45, 445])
    ventana.blit(lista_de_imagenes[4], [345, 395])
    ventana.blit(lista_de_imagenes[4], [345, 445])
    ventana.blit(lista_de_imagenes[5], [35, 320])

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
    
def mostrar_pregunta(ventana: pygame.Surface, pregunta: dict):
    """
    Brief: 
        Muestra una pregunta en la ventana.
    Parametros:
        - ventana (pygame.Surface): Ventana donde se va a mostrar la pregunta.
        - pregunta (dict): Pregunta que se va a mostrar en la ventana.
    Retorno:
        - Sin retorno.
    """
    aplicar_texto(ventana, pregunta["pregunta"], 50, 340, lista_de_colores[4], 12, "Arial Black")
    
def mostrar_opciones(ventana: pygame.Surface, opciones: list):
    """
    Brief: 
        Muestra las opciones en la ventana.
    Parametros:
        - ventana (pygame.Surface): Ventana donde se van a mostrar las opciones.
        - opciones (list): Opciones que se van a mostrar en la ventana.
    Retorno:
        - Sin retorno.
    """
    aplicar_texto(ventana, opciones[0], 50, 410, lista_de_colores[4], 12, "Arial Black")
    aplicar_texto(ventana, opciones[1], 50, 460, lista_de_colores[4], 12, "Arial Black")
    aplicar_texto(ventana, opciones[2], 350, 410, lista_de_colores[4], 12, "Arial Black")
    aplicar_texto(ventana, opciones[3], 350, 460, lista_de_colores[4], 12, "Arial Black")
       
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

def verificar_respuesta(pregunta: dict):
    """
    Brief: 
        Verifica las coordenadas donde se encuentra la respuesta correcta.
    Parametros:
        - pregunta: dict: Pregunta que se va a analizar.
    Retorno:
        - respuesta
    """
    if pregunta["respuesta_correcta"] == pregunta["opciones"][0]:
        rectangulo = [50, 310, 400, 430]
    elif pregunta["respuesta_correcta"] == pregunta["opciones"][1]:
        rectangulo = [50, 310, 450, 480]
    elif pregunta["respuesta_correcta"] == pregunta["opciones"][2]:
        rectangulo = [350, 610, 400, 430]
    else:
        rectangulo = [350, 610, 450, 480]
    
    respuesta = elegir_respuesta(rectangulo) 
    return respuesta  
     
def elegir_respuesta(rectangulo: list):
    """
    Brief: 
        Evalua las coordenadas donde se produce el evento.
    Parametros:
        - rectangulo (list): Coordenadas de la respuesta correcta.
    Retorno:
        - True.
        - False.
    """
    posicion_mouse = pygame.mouse.get_pos()        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if posicion_mouse[0] > rectangulo[0] and posicion_mouse[0] < rectangulo[1] and posicion_mouse[1] > rectangulo[2] and posicion_mouse[1] < rectangulo[3]:
                return True
            else:
                return False

def mostrar_rangos(ventana: pygame.Surface, valor_rango: int, ubicacion_x: int, ubicacion_y: int):
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
        rango = str(rango)
        if valor_rango == int(rango):
            color_texto = lista_de_colores[0]
            dibujar_rectangulo(ventana, lista_de_colores[4], ubicacion_x-50, ubicacion_y, 225, 15)
        else:
            color_texto = lista_de_colores[4] 

        aplicar_texto(ventana, f"${rango}", ubicacion_x, ubicacion_y, color_texto, 12, "Arial Black")
        ubicacion_y += 20

def dibujar_rectangulo(ventana: pygame.Surface, color: tuple, ubicacion_x: int, ubicacion_y: int, ancho: int, alto: int, borde: int = 0):
    """
    Brief: 
        Dibuja un rectangulo en la ventana.
    Parametros:
        - ventana (pygame.Surface): Ventana del juego.
        - color (tuple): Un color especifico.
        - ubicacion_x (int): Ubicacion en el eje x.
        - ubicacion_y (int): Ubicacion en el eje y.
        - ancho (int): Ancho del rectangulo. 
        - alto (int): Largo del rectangulo.
        - borde (int): Borde del rectangulo, inicializado en 0. 
    Retorno:
        - Sin retorno.
    """
    pygame.draw.rect(ventana, color, (ubicacion_x, ubicacion_y, ancho, alto), borde)
      
def sanitizar_string(valor_str:str):
    """
    Brief: 
        Sanitiza el string recibido por parametro.
    Parametros:
        - valor_str (str): El string a sanitizar.
    Retorno:
        - valor_str
        - "N/A"
    """
    try:
        if type(valor_str) == str and len(valor_str) != 0:
            valor_str = re.sub("[0-9]", "", valor_str)
            valor_str = valor_str.title()
            valor_str = valor_str.strip()
            return valor_str
        else:
            return "N/A"
    except ValueError:
        return "N/A"
    except Exception:
        return "N/A"        

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

    jugador = Jugador("", 0)
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

def continuar_partida(ventana: pygame.Surface, indice: int):
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
        ventana.blit(lista_de_imagenes[6], [250, 100])
        aplicar_texto(ventana, f"¡Has llegado a ${rangos[indice]}!", 270, 160, lista_de_colores[0], 12, "Arial Black")
        aplicar_texto(ventana, "Para salir presione ESC", 270, 180, lista_de_colores[0], 12, "Arial Black")

        tecla_presionada = pygame.key.get_pressed()
        if tecla_presionada[pygame.K_ESCAPE]: 
            return False
        else:
            return 1
    else:
        return True

def crear_texto(mensaje: str, color: tuple, tamaño: int, fuente: str):
    """
    Brief: 
        Crea un texto.
    Parametros:
        - mensaje (str): El mensaje del texto.
        - color (tuple): Un color especifico.
        - tamaño (int): El tamaño del texto.
        - fuente (str): La fuente del texto.
    Retorno:
        - Un mensaje.
    """
    mi_fuente = pygame.font.SysFont(fuente, tamaño)
    mensaje = mi_fuente.render(mensaje, 0, color)

    return mensaje

def aplicar_texto(ventana: pygame.Surface, mensaje: str, ubicacion_x: int, ubicacion_y: int, color: list, tamaño: int, fuente: str = ""):
    """
    Brief: 
        Aplica el texto creado a la ventana.
    Parametros:
        - ventana (pygame.surface): La ventana del juego.
        - mensaje (str): El mensaje del texto.
        - ubicacion_x (int): Ubicacion en el eje x.
        - ubicacion_y (int): Ubicacion en el eje y.
        - color (tuple): Un color especifico.
        - tamaño (int): El tamaño del texto.
        - fuente (str): La fuente del texto.
    Retorno:
        - Sin retorno.
    """
    mensaje_creado = crear_texto(mensaje, color, tamaño, fuente)
    ventana.blit(mensaje_creado, (ubicacion_x, ubicacion_y))
            
