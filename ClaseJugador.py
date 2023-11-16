class Jugador:
    def __init__(self):
        self.__nombre = ""
        self.__rango = 0

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_rango(self):
        return self.__rango

    def set_rango(self, rango):
        self.__rango = rango

    