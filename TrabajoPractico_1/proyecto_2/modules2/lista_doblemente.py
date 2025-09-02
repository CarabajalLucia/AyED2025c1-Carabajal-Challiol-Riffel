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
        if posicion < 0:
            posicion = self.tamanio + posicion

        if posicion < 0 or posicion > self.tamanio:
            raise IndexError("Posición fuera de rango")
        if posicion == 0:
            dato = self.cabeza.dato 
            self.cabeza = self.cabeza.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            else:
                self.cola = None
        elif posicion == self.tamanio -1:
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
            actual.anterior ,actual.siguiente =actual.siguiente , actual.anterior 
            actual = actual.anterior
        return self
    
    def concatenar(self, otralista):
        if otralista.esta_vacia():
            return self

        actual = otralista.cabeza
        while actual:
            self.insertar(actual.dato)
            actual = actual.siguiente

        return self

    def __len__(self):
        return self.tamanio
    
    def __add__(self, otralista):
        nueva = self.copiar()
        nueva.concatenar(otralista.copiar())
        return nueva 
    
    def __iter__(self):
        actual = self.cabeza
        for i in range(self.tamanio):
            yield actual.dato
            actual = actual.siguiente

#graficas
import matplotlib.pyplot as plt
import numpy as np

n = np.arange(1, 101)  # de 1 a 100 elementos

len_op = np.ones_like(n)  # O(1)
copiar_op = n             # O(n)
invertir_op = n         # O(n)

plt.plot(n, len_op, label="len() O(1)")
plt.plot(n, copiar_op, label="copiar() O(n)")
plt.plot(n, invertir_op, label="invertir() O(n)", linestyle="--")

plt.xlabel("Tamaño de la lista (n)")
plt.ylabel("Tiempo relativo")
plt.title("Complejidad temporal de operaciones")
plt.legend()
plt.grid(True)
plt.show()
 
#explicar resultados y orden de complejidad 

#pruebas
"""lista = ListaDoblementeEnlazada()
lista.agregar_al_inicio(10)
lista.agregar_al_inicio("listaa")

lista.agregar_al_inicio(11)
print(list(lista))

lista2 = ListaDoblementeEnlazada()
lista2.agregar_al_inicio(55)
print(list(lista2))
lista3 = lista.concatenar(lista2)
print(list(lista3))
print(list(lista))

"""