from datetime import datetime  # Importamos datetime para manejar fechas

class NodoAVL:
    def __init__(self, temperatura, fecha):
        # Guarda la temperatura medida (dato flotante)
        self.temperatura = temperatura
        # Convierte la fecha (string) al formato datetime para poder compararla fácilmente
        self.fecha = datetime.strptime(fecha, "%d/%m/%Y")
        # Puntero al hijo izquierdo
        self.izquierdo = None
        # Puntero al hijo derecho
        self.derecho = None
        # Altura del nodo dentro del árbol (necesaria para balancear el AVL)
        self.altura = 1
        # Valor mínimo de temperatura dentro del subárbol que tiene este nodo como raíz
        self.min_subarbol = temperatura
        # Valor máximo de temperatura dentro del subárbol que tiene este nodo como raíz
        self.max_subarbol = temperatura