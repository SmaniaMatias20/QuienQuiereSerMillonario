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


def configurar_ventana(alto, ancho, icono: pygame.image, titulo):
    ventana = pygame.display.set_mode((ancho, alto))                                 
    pygame.display.set_caption(titulo)                                        
    pygame.display.set_icon(icono) 

    return ventana 

def actualizar_ventana(ventana: pygame.Surface, pregunta: dict, opciones: list, indice):
    aplicar_imagenes(ventana)
    mostrar_pregunta(ventana, pregunta)
    mostrar_opciones(ventana, opciones)
    mostrar_rangos(ventana, rangos[indice])
    
def aplicar_imagenes(ventana: pygame.Surface):
    ventana.blit(lista_de_imagenes[0], [0, 0])
    ventana.blit(lista_de_imagenes[1], [480, 125])
    ventana.blit(lista_de_imagenes[3], [650, 50])
    ventana.blit(lista_de_imagenes[4], [45, 395])
    ventana.blit(lista_de_imagenes[4], [45, 445])
    ventana.blit(lista_de_imagenes[4], [345, 395])
    ventana.blit(lista_de_imagenes[4], [345, 445])
    ventana.blit(lista_de_imagenes[5], [35, 320])

def filtrar_pregunta(banco_de_preguntas: list, dificultad: int):
    preguntas_por_dificultad = []
    
    for pregunta in banco_de_preguntas:
        if pregunta["dificultad"] == dificultad:
            preguntas_por_dificultad.append(pregunta)

    indice_aleatorio = random.randint(0, len(preguntas_por_dificultad)-1)
    
    return preguntas_por_dificultad[indice_aleatorio]
    
def mostrar_pregunta(ventana: pygame.Surface, pregunta: dict):
    aplicar_texto(ventana, pregunta["pregunta"], 50, 340, lista_de_colores[4])
    
def mostrar_opciones(ventana: pygame.Surface, opciones: list):
    aplicar_texto(ventana, opciones[0], 50, 410, lista_de_colores[4])
    aplicar_texto(ventana, opciones[1], 50, 460, lista_de_colores[4])
    aplicar_texto(ventana, opciones[2], 350, 410, lista_de_colores[4])
    aplicar_texto(ventana, opciones[3], 350, 460, lista_de_colores[4])
       
def mezclar_opciones(opciones: list):
    random.shuffle(opciones)
    
    return opciones

def verificar_respuesta(pregunta: dict):
    # Comparo la respuesta correcta con las opciones y retorno las coordenadas de la misma.
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
    posicion_mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if posicion_mouse[0] > rectangulo[0] and posicion_mouse[0] < rectangulo[1] and posicion_mouse[1] > rectangulo[2] and posicion_mouse[1] < rectangulo[3]:
                return True
            else:
                return False

def mostrar_rangos(ventana: pygame.Surface, valor_rango: int):
    ubicacion_x = 700
    ubicacion_y = 130
    for rango in reversed(rangos):
        rango = str(rango)
        if valor_rango == int(rango):
            color_texto = lista_de_colores[0]
            dibujar_rectangulo(ventana, lista_de_colores[4], ubicacion_x-50, ubicacion_y, 225, 15)
        else:
            color_texto = lista_de_colores[4] 

        aplicar_texto(ventana, f"${rango}", ubicacion_x, ubicacion_y, color_texto)
        ubicacion_y += 20

def dibujar_rectangulo(ventana: pygame.Surface, color, ubicacion_x: int, ubicacion_y: int, ancho: int, alto: int, borde = 0):
    pygame.draw.rect(ventana, color, (ubicacion_x, ubicacion_y, ancho, alto), borde)
      
def sanitizar_string(valor_str:str):
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
    nombre_ingresado = prompt(title = "Registro", prompt = "Ingrese su nombre")
    nombre = sanitizar_string(nombre_ingresado)

    jugador = Jugador("", 0)
    jugador.set_nombre(nombre)
    jugador.set_rango(rango)
    return jugador

def guardar_puntuacion(jugador: Jugador):
    with open("archivos/puntuaciones.csv", "a", encoding="UTF8") as archivo:
        mensaje = f"{jugador.get_nombre()}, ${jugador.get_rango()}\n"
        archivo.write(mensaje)

def continuar_partida(ventana: pygame.Surface, indice):

    if rangos[indice] == 1000 or rangos[indice] == 32000:
        ventana.blit(lista_de_imagenes[6], [250, 100])
        aplicar_texto(ventana, f"¡Has llegado a ${rangos[indice]}!", 270, 160, lista_de_colores[0])
        aplicar_texto(ventana, "Para salir presione ESC", 270, 180, lista_de_colores[0])

        tecla_presionada = pygame.key.get_pressed()
        if tecla_presionada[pygame.K_ESCAPE]: 
            return False
        else:
            return 1
    else:
        return True

def crear_texto(mensaje: str, color: list):
    mi_fuente = pygame.font.Font(None, 20)
    mensaje = mi_fuente.render(mensaje, 0, color)

    return mensaje

def aplicar_texto(ventana: pygame.Surface, mensaje: str, ubicacion_x: int, ubicacion_y: int, color: list):
    mensaje_creado = crear_texto(mensaje, color)
    ventana.blit(mensaje_creado, (ubicacion_x, ubicacion_y))
            