import pygame as py
import re

def cargar_imagen(path: str, tamaño: tuple):
    """
    Brief: 
        Carga las imagenes.
    Parametros:
        - path (str): El path de la imagen a cargar.
        - tamaño (tuple): El tamaño que necesitamos reescalar la imagen.
    Retorno:
        - imagen
    """ 
    imagen = py.image.load(path)
    imagen = py.transform.scale(imagen, tamaño)

    return imagen

def cargar_sonido(path: str):
    sonido = py.mixer.Sound(path)
    sonido.set_volume(0.2)
    sonido.play(-1)

def dibujar_rectangulo(ventana: py.Surface, color: tuple, ubicacion_x: int, ubicacion_y: int, ancho: int, alto: int, borde: int = 0):
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
    py.draw.rect(ventana, color, (ubicacion_x, ubicacion_y, ancho, alto), borde)

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
    mi_fuente = py.font.SysFont(fuente, tamaño)
    mensaje_creado = mi_fuente.render(mensaje, 0, color)

    return mensaje_creado

def aplicar_texto(ventana: py.Surface, mensaje: str, ubicacion_x: int, ubicacion_y: int, color: list, tamaño: int, fuente: str = ""):
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
    if type(valor_str) == str:
        cadena = re.sub("[0-9]+", "", valor_str)
        cadena = cadena.title()
        nombre = cadena.strip()
        if len(nombre) != 0:
            return nombre
        else:
            return "N/A"
    else:
        return "N/A"


ROJO      = (255,   0,   0)
VERDE     = (  0, 255,   0)
AZUL      = (  0,   0, 255)
AMARILLO  = (255, 255,   0)
MAGENTA   = (255,   0, 255)
CIAN      = (  0, 255, 255)
BLANCO    = (255, 255, 255)
NEGRO     = (  0,   0,   0)
GRIS      = (128, 128, 128)
NARANJA   = (255, 165,   0)
ROSA      = (255, 192, 203)
VIOLETA   = (138, 43 , 226)
 
imagen_fondo = cargar_imagen('imagenes\imagen.png', (900, 500))
imagen_icono = cargar_imagen('imagenes\icono.png', (50, 50))
imagen_conductor = cargar_imagen('imagenes\\azzaro.png', (120, 200))
imagen_rangos = cargar_imagen('imagenes\\rangos.png', (225, 450))
imagen_respuesta = cargar_imagen('imagenes\\respuesta.png', (260, 40))
imagen_pregunta = cargar_imagen('imagenes\pregunta.png', (600, 60))
imagen_mensaje = cargar_imagen('imagenes\mensaje.png', (200, 200))
imagen_comodin = cargar_imagen('imagenes\comodin.png', (100, 50))
imagen_menu = cargar_imagen('imagenes\menu.png', (500, 500))
boton_comenzar = cargar_imagen('imagenes\start.png', (150, 50))
