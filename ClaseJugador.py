class Jugador:
    def __init__(self, nombre: str, rango: int):
        self.__nombre = nombre
        self.__rango = rango

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_rango(self):
        return self.__rango

    def set_rango(self, rango):
        self.__rango = rango

    