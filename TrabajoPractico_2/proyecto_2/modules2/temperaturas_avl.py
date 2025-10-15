from modules2.AVL import NodoAVL
from datetime import datetime  # Importamos datetime para manejar fechas
#  Clase principal Temperaturas_DB 
class Temperaturas_DB:
    def __init__(self):
        # Nodo raíz del árbol AVL (empieza vacío)
        self.raiz = None
        # Contador de cuántas mediciones (muestras) hay en la base de datos
        self._cantidad = 0

    # FUNCIONES AUXILIARES 
    def _altura(self, nodo):
        # Devuelve la altura del nodo si existe, o 0 si es None
        return nodo.altura if nodo else 0

    def _actualizar_altura_y_extremos(self, nodo):
        # Actualiza la altura, temperatura mínima y máxima del subárbol que parte de este nodo
        if not nodo:
            return

        # La altura es 1 más que la máxima altura de sus hijos
        nodo.altura = 1 + max(self._altura(nodo.izquierdo), self._altura(nodo.derecho))

        # Guardamos todas las temperaturas relevantes (del nodo y de sus subárboles)
        valores = [nodo.temperatura]
        if nodo.izquierdo:
            valores.append(nodo.izquierdo.min_subarbol)
            valores.append(nodo.izquierdo.max_subarbol)
        if nodo.derecho:
            valores.append(nodo.derecho.min_subarbol)
            valores.append(nodo.derecho.max_subarbol)
        nodo.min_subarbol = min(valores)
        nodo.max_subarbol = max(valores)

    def _balance(self, nodo):
        # Calcula el factor de balance del nodo (altura izquierda - altura derecha)
        return self._altura(nodo.izquierdo) - self._altura(nodo.derecho) if nodo else 0

    # ROTACIONES AVL 
    def _rotacion_derecha(self, y):
        x = y.izquierdo
        T2 = x.derecho
        x.derecho = y
        y.izquierdo = T2
        self._actualizar_altura_y_extremos(y)
        self._actualizar_altura_y_extremos(x)
        return x

    def _rotacion_izquierda(self, x):
        y = x.derecho
        T2 = y.izquierdo
        y.izquierdo = x
        x.derecho = T2
        self._actualizar_altura_y_extremos(x)
        self._actualizar_altura_y_extremos(y)
        return y

    #INSERCIÓN EN EL ÁRBOL
    def guardar_temperatura(self, temperatura, fecha):
        # Inserta una nueva temperatura en el árbol AVL
        self.raiz = self._insertar(self.raiz, temperatura, fecha)
        self._cantidad += 1

    def _insertar(self, nodo, temperatura, fecha):
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")

        if not nodo:
            return NodoAVL(temperatura, fecha)

        if fecha_dt < nodo.fecha:
            nodo.izquierdo = self._insertar(nodo.izquierdo, temperatura, fecha)
        elif fecha_dt > nodo.fecha:
            nodo.derecho = self._insertar(nodo.derecho, temperatura, fecha)
        else:
            nodo.temperatura = temperatura
            return nodo

        self._actualizar_altura_y_extremos(nodo)
        balance = self._balance(nodo)

        # Casos de desbalance
        if balance > 1 and fecha_dt < nodo.izquierdo.fecha:
            return self._rotacion_derecha(nodo)
        if balance < -1 and fecha_dt > nodo.derecho.fecha:
            return self._rotacion_izquierda(nodo)
        if balance > 1 and fecha_dt > nodo.izquierdo.fecha:
            nodo.izquierdo = self._rotacion_izquierda(nodo.izquierdo)
            return self._rotacion_derecha(nodo)
        if balance < -1 and fecha_dt < nodo.derecho.fecha:
            nodo.derecho = self._rotacion_derecha(nodo.derecho)
            return self._rotacion_izquierda(nodo)

        return nodo
