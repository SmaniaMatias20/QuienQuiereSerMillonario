import pygame as py
import os

def cargar_imagen(path, tamaño: tuple):
    imagen = py.image.load(path)
    imagen = py.transform.scale(imagen, tamaño)

    return imagen

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

SONIDO_FONDO = os.path.join('sonidos', 'sonido.mp3')

IMAGEN_FONDO = os.path.join('imagenes','imagen.png')
IMAGEN_CONDUCTOR = os.path.join('imagenes', 'azzaro.png')
IMAGEN_ICONO = os.path.join('imagenes','icono.png')
IMAGEN_RANGOS = os.path.join('imagenes', 'rangos.png')
IMAGEN_RESPUESTA = os.path.join('imagenes', 'respuesta.png')
IMAGEN_PREGUNTA = os.path.join('imagenes', 'pregunta.png')
IMAGEN_MENSAJE = os.path.join('imagenes', 'mensaje.png')
IMAGEN_COMODIN = os.path.join('imagenes', 'comodin.png')

imagen_fondo = cargar_imagen(IMAGEN_FONDO, (900, 500))
imagen_conductor = cargar_imagen(IMAGEN_CONDUCTOR, (120, 200))
imagen_rangos = cargar_imagen(IMAGEN_RANGOS, (225, 450))
imagen_respuesta = cargar_imagen(IMAGEN_RESPUESTA, (260, 40))
imagen_pregunta = cargar_imagen(IMAGEN_PREGUNTA, (600, 60))
imagen_comodin = cargar_imagen(IMAGEN_COMODIN, (100, 50))