class NodoAVL: 
    def __init__(self, temperatura, fecha):
        self.temperatura = temperatura
        self.fecha = fecha
        self.izquierdo = None
        self.derecho = None
        self.altura = 1
        self.min_subarbol = temperatura
        self.max_subarbol = temperatura
