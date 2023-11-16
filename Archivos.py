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
    except json.decoder.JSONDecodeError:
        print("Error al decodificar el archivo JSON")
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except Exception:
        print("Otro error inesperado")



def agregar_pregunta(pregunta: dict, nombre_archivo: str):
    """
    Brief: 
        Guarda una pregunta en un archivo, en este caso JSON.
    Parametros:
        - pregunta (dict): La pregunta a guardar.
        - nombre_archivo (str): El nombre del archivo donde se va a guardar.
    Retorno:
        - Sin retorno.
    """ 
    with open(nombre_archivo, 'a', encoding="utf-8") as archivo:
        json.dump(pregunta, archivo, indent=4, ensure_ascii = False)
