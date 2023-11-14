import json


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
    try:
        with open("archivos/preguntas.json", "r", encoding="UTF8") as archivo:
            banco_de_preguntas = json.load(archivo)
            
        return banco_de_preguntas
    except json.decoder.JSONDecodeError as e:
        print(f"Error al decodificar el archivo JSON: {e}")
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except Exception:
        print("Otro error inesperado")


def agregar_pregunta():
    pass
