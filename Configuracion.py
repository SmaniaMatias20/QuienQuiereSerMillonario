from tkinter.simpledialog import askstring as prompt
from archivos.Archivos import *
from ClaseJugador import *
from Multimedia import *
import pygame
import random
import re
import sys


rangos = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
comodin = {"50-50": "activo"}

banco_de_preguntas = cargar_preguntas()




def configurar_ventana(alto: int, ancho: int, icono, titulo: str):
    """
    Brief: 
        Configura una ventana.
    Parametros:
        - alto (int): El alto de la ventana.
        - ancho (int): El ancho de la ventana.
        - icono: El path del icono de la ventana.
        - titulo (str): El titulo de la ventana.
    Retorno:
        - ventana.
    """
    imagen_icono = cargar_imagen(icono, (50, 50))

    ventana = pygame.display.set_mode((ancho, alto))                                 
    pygame.display.set_caption(titulo)                                        
    pygame.display.set_icon(imagen_icono) 

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
    mostrar_opciones(ventana, opciones, pregunta)
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
    ventana.blit(imagen_fondo, [0, 0])
    ventana.blit(imagen_conductor, [480, 125])
    ventana.blit(imagen_rangos, [650, 50])
    ventana.blit(imagen_respuesta, [45, 395])
    ventana.blit(imagen_respuesta, [45, 445])
    ventana.blit(imagen_respuesta, [345, 395])
    ventana.blit(imagen_respuesta, [345, 445])
    ventana.blit(imagen_pregunta, [35, 320])

    if comodin["50-50"] == "activo":
        ventana.blit(imagen_comodin, [10, 10])

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
    aplicar_texto(ventana, pregunta["pregunta"], 50, 340, BLANCO, 12, "Arial Black")
    
def mostrar_opciones(ventana: pygame.Surface, opciones: list, pregunta: dict):
    """
    Brief: 
        Muestra las opciones en la ventana.
    Parametros:
        - ventana (pygame.Surface): Ventana donde se van a mostrar las opciones.
        - opciones (list): Opciones que se van a mostrar en la ventana.
    Retorno:
        - Sin retorno.
    """

    if comodin["50-50"] != "usado":
        aplicar_texto(ventana, opciones[0], 50, 410, BLANCO, 12, "Arial Black")
        aplicar_texto(ventana, opciones[1], 50, 460, BLANCO, 12, "Arial Black")
        aplicar_texto(ventana, opciones[2], 350, 410, BLANCO, 12, "Arial Black")
        aplicar_texto(ventana, opciones[3], 350, 460, BLANCO, 12, "Arial Black")
    elif comodin["50-50"] == "usado":
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
        coord_correcta = {
            "left" : 50,
            "right" : 310,
            "bottom" : 400,
            "top" : 430
        }
    elif pregunta["respuesta_correcta"] == pregunta["opciones"][1]:
        coord_correcta = {
            "left" : 50,
            "right" : 310,
            "bottom" : 450,
            "top" : 480
        }
    elif pregunta["respuesta_correcta"] == pregunta["opciones"][2]:
        coord_correcta = {
            "left" : 350,
            "right" : 610,
            "bottom" : 400,
            "top" : 430
        }
    else:
        coord_correcta = {
            "left" : 350,
            "right" : 610,
            "bottom" : 450,
            "top" : 480
        }
  
    respuesta = elegir_respuesta(coord_correcta) 
    return respuesta  
     
def elegir_respuesta(coor_correcta: list):
    """
    Brief: 
        Evalua las coordenadas donde se produce el evento.
    Parametros:
        - rectangulo (list): Coordenadas de la respuesta correcta.
    Retorno:
        - True.
        - False.
    """
    coor_comodin = {
            "right" : 110,
            "left" : 10,
            "bottom" : 60,
            "top" : 10
        }

    x, y = pygame.mouse.get_pos()        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if coor_comodin["right"] > x > coor_comodin["left"] and coor_comodin["bottom"] > y > coor_comodin["top"] and comodin["50-50"] == "activo":
                comodin["50-50"] = "usado"    
            elif coor_correcta["right"] > x > coor_correcta["left"] and coor_correcta["top"] > y > coor_correcta["bottom"]:
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
        Sanitiza el string recibido.
    Parametros:
        - valor_str (str): El string a sanitizar.
    Retorno:
        - valor_str
        - "N/A"
    """

    if type(valor_str) == str:
        valor_str = re.sub("[0-9]+", "", valor_str)
        valor_str = valor_str.title()
        valor_str = valor_str.strip()
        if len(valor_str) != 0:
            return valor_str
        else:
            return "N/A"
    else:
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
        imagen_mensaje = cargar_imagen(IMAGEN_MENSAJE, (200, 200))
        ventana.blit(imagen_mensaje, [250, 100])
        aplicar_texto(ventana, f"¡Has llegado a ${rangos[indice]}!", 270, 160, NEGRO, 12, "Arial Black")
        aplicar_texto(ventana, "Para salir presione ESC", 270, 180, NEGRO, 12, "Arial Black")

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

def mostrar_tiempo(ventana: pygame.surface, tiempo_maximo):
    tiempo_actual = pygame.time.get_ticks()
    tiempo_restante = max(tiempo_maximo - tiempo_actual, 0)


    segundos_restantes = tiempo_restante // 1000
    minutos = segundos_restantes // 60
    segundos = segundos_restantes % 60

    mensaje = f"{minutos:02}:{segundos:02}"
    
    aplicar_texto(ventana, mensaje, 350, 10, BLANCO, 30, "Arial Black")

    return segundos
    