from datetime import datetime

class NodoAVL:
    def __init__(self, temperatura, fecha):
        # cada nodo guarda su temperatura y su fecha
        self.temperatura = temperatura
        self.fecha = datetime.strptime(fecha, "%d/%m/%Y")  # convierte el string de la fecha en datetime
        #crea los hijos
        self.izquierdo = None
        self.derecho = None
        # crea la altura
        self.altura = 1
        # Valores mínimo y máximo del subárbol 
        self.min_subarbol = temperatura
        self.max_subarbol = temperatura

class AVL:
    def __init__(self):
        # se crea el arbol vacio
        self.raiz = None

    def _altura(self, nodo):
        # devuelve la altura del nodo
        return nodo.altura if nodo else 0

    def _actualizar_altura_y_extremos(self, nodo):
        # Recalcula la altura, el mínimo y el máximo del subárbol del nodo
        if not nodo:
            return

        # altura = la altura del nodo + la altura max de sus hijos
        altura_izq = self._altura(nodo.izquierdo)
        altura_der = self._altura(nodo.derecho)
        nodo.altura = 1 + max(altura_izq, altura_der)

        # calcula los valores de temperatura mínimo y máximo del subárbol
        valores = [nodo.temperatura]  # arranca con la temperatura del nodo
        if nodo.izquierdo:
            # agrega extremos del subárbol izquierdo
            valores += [nodo.izquierdo.min_subarbol, nodo.izquierdo.max_subarbol]
        if nodo.derecho:
            # agrega extremos del subárbol derecho
            valores += [nodo.derecho.min_subarbol, nodo.derecho.max_subarbol]
        
        # actualiza los extremos del subárbol actual
        nodo.min_subarbol, nodo.max_subarbol = min(valores), max(valores)

    def _balance(self, nodo):
        # devuelve el factor de balance (altura izquierda - altura derecha)
        # si está entre -1 y 1, el nodo está balanceado
        if not nodo:
            return 0
        return self._altura(nodo.izquierdo) - self._altura(nodo.derecho)

    def _separar_fecha(self, fecha):
        #convierte la fecha a datetime
        return datetime.strptime(fecha, "%d/%m/%Y") if isinstance(fecha, str) else fecha

    # rotaciones
    def _rotacion_derecha(self, y):
        x, T2 = y.izquierdo, y.izquierdo.derecho  # se guardan las referencias
        x.derecho, y.izquierdo = y, T2            # se hace la rotación
        # se actualizan alturas y extremos
        self._actualizar_altura_y_extremos(y)
        self._actualizar_altura_y_extremos(x)
        return x  # devuelve el nuevo nodo raíz del subárbol rotado

    def _rotacion_izquierda(self, x):
        y, T2 = x.derecho, x.derecho.izquierdo
        y.izquierdo, x.derecho = x, T2
        # se actualizan alturas y extremos
        self._actualizar_altura_y_extremos(x)
        self._actualizar_altura_y_extremos(y)
        return y  # devuelve el nuevo nodo raíz del subárbol rotado

    def _insertar(self, nodo, temperatura, fecha):
        fecha_dt = self._separar_fecha(fecha)
        
        #si el nodo está vacío, crea un nuevo nodo
        if not nodo:
            return NodoAVL(temperatura, fecha)

        #si la fecha es menor, insertar en el subárbol izquierdo
        if fecha_dt < nodo.fecha:
            nodo.izquierdo = self._insertar(nodo.izquierdo, temperatura, fecha)
        #si la fecha es mayor, insertar en el subárbol derecho
        elif fecha_dt > nodo.fecha:
            nodo.derecho = self._insertar(nodo.derecho, temperatura, fecha)
        else:
            #si la fecha ya existe, actualiza la temperatura
            nodo.temperatura = temperatura
            return nodo

        #actualiza altura y extremos después de insertar
        self._actualizar_altura_y_extremos(nodo)
        
        #calcula el factor de balance para ver si hace flata reequilibrar
        balance = self._balance(nodo)

        #balanceo
        # desequilibrio izquierda-izquierda
        if balance > 1 and fecha_dt < nodo.izquierdo.fecha:
            return self._rotacion_derecha(nodo)
        #desequilibrio derecha-derecha
        if balance < -1 and fecha_dt > nodo.derecho.fecha:
            return self._rotacion_izquierda(nodo)
        #desequilibrio izquierda-derecha
        if balance > 1 and fecha_dt > nodo.izquierdo.fecha:
            nodo.izquierdo = self._rotacion_izquierda(nodo.izquierdo)
            return self._rotacion_derecha(nodo)
        #desequilibrio derecha-izquierda
        if balance < -1 and fecha_dt < nodo.derecho.fecha:
            nodo.derecho = self._rotacion_derecha(nodo.derecho)
            return self._rotacion_izquierda(nodo)

        return nodo

    def _borrar(self, nodo, fecha_dt):
        if not nodo:
            return None

        # recorre al subarbol que corresponde
        if fecha_dt < nodo.fecha:
            nodo.izquierdo = self._borrar(nodo.izquierdo, fecha_dt)
        elif fecha_dt > nodo.fecha:
            nodo.derecho = self._borrar(nodo.derecho, fecha_dt)
        else:
            # encontro el nodo que se va a borrar
            if not nodo.izquierdo:
                #solo hijo derecho o ninguno
                return nodo.derecho
            if not nodo.derecho:
                #solo hijo izquierdo
                return nodo.izquierdo

            #si tiene dos hijos, busca el sucesor inorden (el más chico del subárbol derecho)
            sucesor = nodo.derecho
            while sucesor.izquierdo:
                sucesor = sucesor.izquierdo
            
            # copia los datos del sucesor al nodo actual
            nodo.temperatura, nodo.fecha = sucesor.temperatura, sucesor.fecha
            # elimina el sucesor del subárbol derecho
            nodo.derecho = self._borrar(nodo.derecho, sucesor.fecha)

        # actualiza la altura y lo extremos
        self._actualizar_altura_y_extremos(nodo)
        balance = self._balance(nodo)

        #reebalanceo despues de la eliminacion
        # izquierda-izquierda
        if balance > 1 and self._balance(nodo.izquierdo) >= 0:
            return self._rotacion_derecha(nodo)
        # izquierda-derecha
        if balance > 1 and self._balance(nodo.izquierdo) < 0:
            nodo.izquierdo = self._rotacion_izquierda(nodo.izquierdo)
            return self._rotacion_derecha(nodo)
        # derecha-derecha
        if balance < -1 and self._balance(nodo.derecho) <= 0:
            return self._rotacion_izquierda(nodo)
        # derecha-izquierda
        if balance < -1 and self._balance(nodo.derecho) > 0:
            nodo.derecho = self._rotacion_derecha(nodo.derecho)
            return self._rotacion_izquierda(nodo)

        return nodo
