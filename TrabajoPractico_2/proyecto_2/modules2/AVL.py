from datetime import datetime

class NodoAVL:
    def __init__(self, clave, valor):
        self.clave = clave          # se usa para ordenar
        self.valor = valor          # es el valor asociado a esa clave
        self.izquierdo = None       
        self.derecho = None         
        self.altura = 1             # altura del nodo


class AVL:
    def __init__(self):
        self.raiz = None  # inicia con el arbol vacio

    def _altura(self, nodo):
        return nodo.altura if nodo else 0 # devuleve la altura del nodo

    def _balance(self, nodo):
        return self._altura(nodo.izquierdo) - self._altura(nodo.derecho) if nodo else 0 # devuelve el factor de balance (altura izquierda - derecha)

    def _actualizar_altura(self, nodo):
        nodo.altura = 1 + max(self._altura(nodo.izquierdo), self._altura(nodo.derecho)) # recalcula la atura del nodo 

    def _rotacion_derecha(self, y):
        x = y.izquierdo
        T2 = x.derecho
        # rota
        x.derecho = y
        y.izquierdo = T2
        # actualiza alturas
        self._actualizar_altura(y)
        self._actualizar_altura(x)
        return x  # cambia la raiz

    def _rotacion_izquierda(self, x):
        y = x.derecho
        T2 = y.izquierdo
        # Rota
        y.izquierdo = x
        x.derecho = T2
        # actualiza alturas
        self._actualizar_altura(x)
        self._actualizar_altura(y)
        return y  # cambia la raiz


    def insertar(self, clave, valor):
        self.raiz = self._insertar(self.raiz, clave, valor) #inserta la clave y su valor en el arbol

    def _insertar(self, nodo, clave, valor):
        if not nodo:
            return NodoAVL(clave, valor)

        # inserta recurvivamente segun la clave
        if clave < nodo.clave:
            nodo.izquierdo = self._insertar(nodo.izquierdo, clave, valor)
        elif clave > nodo.clave:
            nodo.derecho = self._insertar(nodo.derecho, clave, valor)
        else:
            # actualiza el valor segun la clave
            nodo.valor = valor
            return nodo

        # actualiza la altur
        self._actualizar_altura(nodo)

        # calcula el factor de balance
        balance = self._balance(nodo)

        # aca comprueb los distintos casos de desequilibrio
        # izq - izq
        if balance > 1 and clave < nodo.izquierdo.clave:
            return self._rotacion_derecha(nodo)
        # der - der
        if balance < -1 and clave > nodo.derecho.clave:
            return self._rotacion_izquierda(nodo)
        # izq - der
        if balance > 1 and clave > nodo.izquierdo.clave:
            nodo.izquierdo = self._rotacion_izquierda(nodo.izquierdo)
            return self._rotacion_derecha(nodo)
        # der - izq
        if balance < -1 and clave < nodo.derecho.clave:
            nodo.derecho = self._rotacion_derecha(nodo.derecho)
            return self._rotacion_izquierda(nodo)

        return nodo

    def buscar(self, clave):                      #devuelve el valor asociado a una clave (None, si no existe)
        nodo = self.raiz
        while nodo:
            if clave < nodo.clave:               
                nodo = nodo.izquierdo
            elif clave > nodo.clave:
                nodo = nodo.derecho
            else:
                return nodo.valor
        return None

    def _inorden_rango(self, nodo, c1, c2, lista):      #agrega a la lista las tuplas (clave, valor) entre c1 y c2
        if not nodo:
            return
        if nodo.clave > c1:
            self._inorden_rango(nodo.izquierdo, c1, c2, lista)
        if c1 <= nodo.clave <= c2:
            lista.append((nodo.clave, nodo.valor))
        if nodo.clave < c2:
            self._inorden_rango(nodo.derecho, c1, c2, lista)

    def elementos_en_rango(self, c1, c2): #devuelve la lista en el rango indicado
        lista = []
        self._inorden_rango(self.raiz, c1, c2, lista)
        return lista
