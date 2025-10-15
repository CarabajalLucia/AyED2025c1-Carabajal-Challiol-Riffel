from modules2.AVL import NodoAVL
from datetime import datetime

class Temperaturas_DB:
    def __init__(self):
        # Nodo raíz del árbol AVL (inicialmente vacío)
        self.raiz = None
        # Contador de cuántas mediciones hay en la base de datos
        self._cantidad = 0

    # FUNCIONES AUXILIARES 
    def _altura(self, nodo):
        if nodo:
            return nodo.altura
        else:
            return 0

    def _actualizar_altura_y_extremos(self, nodo):
        if not nodo:
            return
        
        # Altura = 1 + altura máxima de sus hijos
        altura_izq = self._altura(nodo.izquierdo)
        altura_der = self._altura(nodo.derecho)
        nodo.altura = 1 + max(altura_izq, altura_der)

        # Recolecta temperaturas relevantes del nodo y sus hijos
        valores = [nodo.temperatura]
        if nodo.izquierdo:
            valores.append(nodo.izquierdo.min_subarbol)
            valores.append(nodo.izquierdo.max_subarbol)
        if nodo.derecho:
            valores.append(nodo.derecho.min_subarbol)
            valores.append(nodo.derecho.max_subarbol)

        # Asigna los valores mínimo y máximo al nodo
        nodo.min_subarbol = min(valores)
        nodo.max_subarbol = max(valores)

    def _balance(self, nodo):
        if not nodo:
            return 0
        altura_izq = self._altura(nodo.izquierdo)
        altura_der = self._altura(nodo.derecho)
        return altura_izq - altura_der

    # ROTACIONES AVL 
    def _rotacion_derecha(self, y):
        x = y.izquierdo
        T2 = x.derecho

        # Rotación
        x.derecho = y
        y.izquierdo = T2

        # Actualizamos altura y extremos
        self._actualizar_altura_y_extremos(y)
        self._actualizar_altura_y_extremos(x)

        return x

    def _rotacion_izquierda(self, x):
        y = x.derecho
        T2 = y.izquierdo

        # Rotación
        y.izquierdo = x
        x.derecho = T2

        # Actualizamos altura y extremos
        self._actualizar_altura_y_extremos(x)
        self._actualizar_altura_y_extremos(y)

        return y

    #  INSERCIÓN 
    def guardar_temperatura(self, temperatura, fecha):
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

        # Rebalanceo
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

    #  BÚSQUEDA 
    def devolver_temperatura(self, fecha):
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        nodo = self.raiz

        while nodo:
            if fecha_dt < nodo.fecha:
                nodo = nodo.izquierdo
            elif fecha_dt > nodo.fecha:
                nodo = nodo.derecho
            else:
                return nodo.temperatura

        return None

    #  MÁXIMO Y MÍNIMO EN RANGO 
    def max_temp_rango(self, fecha1, fecha2):
        f1 = datetime.strptime(fecha1, "%d/%m/%Y")
        f2 = datetime.strptime(fecha2, "%d/%m/%Y")
        return self._max_en_rango(self.raiz, f1, f2)

    def _max_en_rango(self, nodo, f1, f2):
        if not nodo:
            return float('-inf')

        if nodo.fecha < f1:
            return self._max_en_rango(nodo.derecho, f1, f2)

        if nodo.fecha > f2:
            return self._max_en_rango(nodo.izquierdo, f1, f2)

        max_izq = self._max_en_rango(nodo.izquierdo, f1, f2)
        max_der = self._max_en_rango(nodo.derecho, f1, f2)
        return max(nodo.temperatura, max_izq, max_der)

    def min_temp_rango(self, fecha1, fecha2):
        f1 = datetime.strptime(fecha1, "%d/%m/%Y")
        f2 = datetime.strptime(fecha2, "%d/%m/%Y")
        return self._min_en_rango(self.raiz, f1, f2)

    def _min_en_rango(self, nodo, f1, f2):
        if not nodo:
            return float('inf')

        if nodo.fecha < f1:
            return self._min_en_rango(nodo.derecho, f1, f2)

        if nodo.fecha > f2:
            return self._min_en_rango(nodo.izquierdo, f1, f2)

        min_izq = self._min_en_rango(nodo.izquierdo, f1, f2)
        min_der = self._min_en_rango(nodo.derecho, f1, f2)
        return min(nodo.temperatura, min_izq, min_der)

    def temp_extremos_rango(self, fecha1, fecha2):
        min_temp = self.min_temp_rango(fecha1, fecha2)
        max_temp = self.max_temp_rango(fecha1, fecha2)
        return (min_temp, max_temp)

    #  LISTAR TEMPERATURAS EN RANGO 
    def devolver_temperaturas(self, fecha1, fecha2):
        f1 = datetime.strptime(fecha1, "%d/%m/%Y")
        f2 = datetime.strptime(fecha2, "%d/%m/%Y")
        resultado = []
        self._listar_en_rango(self.raiz, f1, f2, resultado)
        return resultado

    def _listar_en_rango(self, nodo, f1, f2, lista):
        if not nodo:
            return

        if nodo.fecha > f1:
            self._listar_en_rango(nodo.izquierdo, f1, f2, lista)

        if f1 <= nodo.fecha <= f2:
            fecha_str = nodo.fecha.strftime("%d/%m/%Y")
            lista.append(f"{fecha_str}: {nodo.temperatura} ºC")

        if nodo.fecha < f2:
            self._listar_en_rango(nodo.derecho, f1, f2, lista)

    # ELIMINACIÓN
    def borrar_temperatura(self, fecha):
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        self.raiz = self._borrar(self.raiz, fecha_dt)
        self._cantidad -= 1

    def _borrar(self, nodo, fecha_dt):
        if not nodo:
            return None

        if fecha_dt < nodo.fecha:
            nodo.izquierdo = self._borrar(nodo.izquierdo, fecha_dt)
        elif fecha_dt > nodo.fecha:
            nodo.derecho = self._borrar(nodo.derecho, fecha_dt)
        else:
            # Nodo con uno o ningún hijo
            if not nodo.izquierdo:
                return nodo.derecho
            if not nodo.derecho:
                return nodo.izquierdo

            # Nodo con dos hijos
            temp = nodo.derecho
            while temp.izquierdo:
                temp = temp.izquierdo

            nodo.temperatura = temp.temperatura
            nodo.fecha = temp.fecha
            nodo.derecho = self._borrar(nodo.derecho, temp.fecha)

        self._actualizar_altura_y_extremos(nodo)
        balance = self._balance(nodo)

        # Rebalanceo después de eliminación
        if balance > 1 and self._balance(nodo.izquierdo) >= 0:
            return self._rotacion_derecha(nodo)

        if balance > 1 and self._balance(nodo.izquierdo) < 0:
            nodo.izquierdo = self._rotacion_izquierda(nodo.izquierdo)
            return self._rotacion_derecha(nodo)

        if balance < -1 and self._balance(nodo.derecho) <= 0:
            return self._rotacion_izquierda(nodo)

        if balance < -1 and self._balance(nodo.derecho) > 0:
            nodo.derecho = self._rotacion_derecha(nodo.derecho)
            return self._rotacion_izquierda(nodo)

        return nodo

    # CANTIDAD DE MUESTRAS 
    def cantidad_muestras(self):
        return self._cantidad
