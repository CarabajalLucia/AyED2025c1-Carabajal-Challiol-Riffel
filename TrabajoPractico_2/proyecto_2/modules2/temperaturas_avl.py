from datetime import datetime
from modules2.AVL import AVL
import matplotlib.pyplot as plt
import networkx as nx


class Temperaturas_DB:
    def __init__(self):
        self.arbol = AVL()        
        self._cantidad = 0         # cuenta las muestras cargadas


    def _convertir_fecha(self, fecha):
        return datetime.strptime(fecha, "%d/%m/%Y")     #convierte la fecha de string  a datetime

    def guardar_temperatura(self, temperatura, fecha):  #guarda o actualiza la temperatura en la fecha que se indique
        fecha_dt = self._convertir_fecha(fecha)
        if self.devolver_temperatura(fecha) is None:
            self._cantidad += 1
        self.arbol.insertar(fecha_dt, temperatura)

    def devolver_temperatura(self, fecha):               #devuelve la temperatura registrada en esa fecha
        return self.arbol.buscar(self._convertir_fecha(fecha))

    def cantidad_muestras(self):                         #devuelve la cantidad de muestras cargadas
        return self._cantidad


    def devolver_temperaturas(self, f1, f2): #devuelve la lista de temperaturas en esa fecha
        f1, f2 = self._convertir_fecha(f1), self._convertir_fecha(f2)
        datos = self.arbol.elementos_en_rango(f1, f2)
        return [f"{f.strftime('%d/%m/%Y')}: {t} ºC" for f, t in datos]

    def max_temp_rango(self, f1, f2):       #devuelve la temperatura maxima en el rango indicado
        f1, f2 = self._convertir_fecha(f1), self._convertir_fecha(f2)
        datos = self.arbol.elementos_en_rango(f1, f2)
        return max(t for _, t in datos) if datos else None

    def min_temp_rango(self, f1, f2):      #devuelve la temperatura minima en el rango indicado
        f1, f2 = self._convertir_fecha(f1), self._convertir_fecha(f2)
        datos = self.arbol.elementos_en_rango(f1, f2)
        return min(t for _, t in datos) if datos else None


    def cargar_archivo(self, ruta_archivo):     #lee el archivo que tiene las muestras
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                fecha_str, temp_str = linea.split(";")
                self.guardar_temperatura(float(temp_str), fecha_str)

   
    def graficar_arbol(self):   #muestra el arbol graficamente 
        if not self.arbol.raiz:
            print("El árbol está vacío.")
            return

        G = nx.DiGraph()
        self._agregar_nodos_edges(self.arbol.raiz, G)
        pos = self._generar_posiciones(self.arbol.raiz)
        etiquetas = {n: f"{n.clave.strftime('%d/%m/%Y')}\n{n.valor}°C" for n in G.nodes()}

        plt.figure(figsize=(10, 6))
        nx.draw(G, pos, with_labels=True, labels=etiquetas, node_size=1600,
                node_color="skyblue", font_size=8, font_weight="bold", arrows=False)
        plt.title("Árbol AVL de Temperaturas", fontsize=12, fontweight="bold")
        plt.show()

    def _agregar_nodos_edges(self, nodo, G):
        if not nodo:
            return
        G.add_node(nodo)
        if nodo.izquierdo:
            G.add_edge(nodo, nodo.izquierdo)
            self._agregar_nodos_edges(nodo.izquierdo, G)
        if nodo.derecho:
            G.add_edge(nodo, nodo.derecho)
            self._agregar_nodos_edges(nodo.derecho, G)

    def _generar_posiciones(self, nodo, x=0, y=0, dx=1.0, pos=None):
        if pos is None:
            pos = {}
        pos[nodo] = (x, -y)
        if nodo.izquierdo:
            self._generar_posiciones(nodo.izquierdo, x - dx, y + 1, dx / 1.8, pos)
        if nodo.derecho:
            self._generar_posiciones(nodo.derecho, x + dx, y + 1, dx / 1.8, pos)
        return pos
