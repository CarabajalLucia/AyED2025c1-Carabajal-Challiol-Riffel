class Monticulo_binario:
    def __init__(self):
        # Lista que almacena los elementos del montículo; índice 0 no se usa para simplificar cálculos
        self.listaMonticulo = [0]
        # Contador del número actual de elementos en el montículo
        self.tamañoactual = 0

    def infilArriba(self, i):
        # Reorganiza el elemento en la posición i hacia arriba para mantener la propiedad del montículo
        while i // 2 > 0:  # mientras no se llegue a la raíz
            if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
                # Intercambia el elemento con su padre si es menor (mayor prioridad)
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            i = i // 2  # sube un nivel en el árbol

    def insertar(self, elemento):
        # Añade un nuevo elemento al final del montículo
        self.listaMonticulo.append(elemento) 
        self.tamañoactual = self.tamañoactual +1
        # Reorganiza hacia arriba para mantener la propiedad del montículo
        self.infilArriba(self.tamañoactual)             

    def infiltAbajo(self,i):
        # Reorganiza el elemento en la posición i hacia abajo para mantener la propiedad del montículo
        while (i * 2) <= self.tamañoactual:  # mientras tenga al menos un hijo
            hm = self.hijoMin(i)  # obtiene el hijo de menor valor (mayor prioridad)
            if self.listaMonticulo[i] > self.listaMonticulo[hm]:
                # Intercambia el elemento con su hijo menor si es mayor
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm  # baja un nivel en el árbol

    def hijoMin(self,i):
        # Devuelve el índice del hijo con menor valor (mayor prioridad)
        if i * 2 + 1 > self.tamañoactual:
            # Solo tiene hijo izquierdo
            return i * 2
        else:
            # Tiene ambos hijos, devuelve el que sea menor
            if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
            

    def extraer_min(self): # extrae el elemento de mayor prioridad
        # La raíz siempre tiene el menor valor (mayor prioridad)
        minimo = self.listaMonticulo[1]
        # Coloca el último elemento en la raíz
        self.listaMonticulo[1] = self.listaMonticulo[self.tamañoactual]
        self.tamañoactual = self.tamañoactual - 1  # disminuye tamaño del montículo
        self.listaMonticulo.pop()  # elimina el último elemento (ya movido a la raíz)
        # Reorganiza hacia abajo para mantener la propiedad del montículo
        self.infiltAbajo(1)
        return minimo  # devuelve el elemento de mayor prioridad
