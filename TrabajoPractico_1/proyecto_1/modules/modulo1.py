class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0
    
    def esta_vacia(self):
        return self.tamanio == 0

    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo (dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamanio += 1 
    
    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo (dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamanio += 1 
    
    def insertar(self, dato, posicion = None):
        if posicion is None:
            self.agregar_al_final(dato)
            return
        if posicion < 0 or posicion > self.tamanio:
            raise IndexError("Posición fuera de rango")
        if posicion == 0:
            self.agregar_al_inicio(dato)
        elif posicion == self.tamanio:
            self.agregar_al_final(dato)
        else:
            nuevo = Nodo(dato)
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            anterior = actual.anterior
            nuevo.anterior = anterior
            nuevo.siguiente = actual
            anterior.siguiente = nuevo
            actual.anterior = nuevo
            self.tamanio += 1
    

    def extraer(self, posicion = None):
        if self.esta_vacia():
            raise IndexError("lista vacia")
        if posicion is None:
            posicion = self.tamanio -1
        if posicion < 0 or posicion > self.tamanio:
            raise IndexError("Posición fuera de rango")
        if posicion == 0:
            dato = self.cabeza.dato 
            self.cabeza = self.cabeza.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            else:
                self.cola = None
        if posicion == self.tamanio -1:
            dato=self.cola.dato
            self.cola = self.cola.anterior
            if self.cola:
                self.cola.siguiente = None
            else:
                self.cabeza = None
        else:
            actual = self.cabeza
            for i in range(posicion):
                actual = actual.siguiente
                dato = actual.dato
                anterior = actual.anterior
                siguiente = actual.siguiente
                anterior.siguiente = siguiente
                siguiente.anterior = anterior
        self.tamanio -= 1
        return dato
    
    def copiar(self):
        copia= ListaDoblementeEnlazada()
        actual = self.cabeza
        while actual is not None:
            copia.agregar_al_final(actual.dato)
            actual=actual.siguiente
        return copia
    
    def invertir(self):
        actual = self.cabeza
        self.cabeza, self.cola = self.cola , self.cabeza 
        while actual:
            actual.anterio ,actual.siguiente =actual.siguiente , actual.anterior 
            actual = actual.anterior
        return self
    def concatenar (self, Otralista):
        if Otralista.esta_vacia():
            return 0
        if self.esta_vacia ():
            self.cabeza=Otralista.cabeza 
            self.cola=Otralista.cola
        else:
            self.cola.siguiente=Otralista.cola
            Otralista.cabeza.anterior=self.cola
            self.cola=Otralista.cola
        self.tamanio+=Otralista.tamanio
        return self
     
        
    