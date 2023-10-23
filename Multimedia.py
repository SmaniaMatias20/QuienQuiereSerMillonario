import json
import pygame

def definir_colores():
    """
    Brief: 
        Define colores.
    Parametros:
        - Sin parametros.
    Retorno:
        - Una lista de colores.
    """ 
    NEGRO      = (  0,   0,   0)
    ROJO       = (255,   0,   0)
    VERDE      = (  2,  47,  30)
    AZUL       = ( 11,  57,  94)
    BLANCO     = (255, 255, 255)

    lista_de_colores = [NEGRO, ROJO, VERDE, AZUL, BLANCO]

    return lista_de_colores

def cargar_imagenes():
    """
    Brief: 
        Carga y redimenciona las imagenes.
    Parametros:
        - Sin parametros.
    Retorno:
        - Una lista de imagenes.
    """ 
    imagen_de_fondo = pygame.image.load("imagenes/imagen.png")
    imagen_de_fondo = pygame.transform.scale(imagen_de_fondo, (900, 500)) 

    imagen_conductor = pygame.image.load("imagenes/azzaro.png")
    imagen_conductor = pygame.transform.scale(imagen_conductor, (120, 200))

    imagen_icono = pygame.image.load("imagenes/icono.png") 

    imagen_rangos = pygame.image.load("imagenes/rangos.png")
    imagen_rangos = pygame.transform.scale(imagen_rangos, (225, 450))

    imagen_respuesta = pygame.image.load("imagenes/respuesta.png")
    imagen_respuesta = pygame.transform.scale(imagen_respuesta, (260, 40))

    imagen_pregunta = pygame.image.load("imagenes/pregunta.png")
    imagen_pregunta = pygame.transform.scale(imagen_pregunta, (600, 60))

    imagen_mensaje = pygame.image.load("imagenes/mensaje.png")
    imagen_mensaje = pygame.transform.scale(imagen_mensaje, (200, 200))

    lista_de_imagenes = [imagen_de_fondo, imagen_conductor, imagen_icono, imagen_rangos, imagen_respuesta, imagen_pregunta, imagen_mensaje]

    return lista_de_imagenes

def cargar_sonido():
    """
    Brief: 
        Carga los sonidos.
    Parametros:
        - Sin parametros.
    Retorno:
        - Un sonido.
    """ 
    sonido = pygame.mixer.Sound("sonidos/sonido.mp3")

    return sonido

def cargar_preguntas():
    """
    Brief: 
        Carga los preguntas del archivo json.
    Parametros:
        - Sin parametros.
    Retorno:
        - El banco de preguntas.
    """ 
    banco_de_preguntas = []

    with open("archivos/preguntas.json", "r", encoding="UTF8") as archivo:
        banco_de_preguntas = json.load(archivo)

    return banco_de_preguntas