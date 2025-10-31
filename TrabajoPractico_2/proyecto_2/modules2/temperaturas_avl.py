from modules2.AVL import AVL                
import matplotlib.pyplot as plt             
import networkx as nx                       

class Temperaturas_DB(AVL):                
    def __init__(self):
        super().__init__()                  # Llama al constructor de la clase padre para inicializar self.raiz
        self._cantidad = 0                  # lleva la cuenta de cuantos datos se cargaron

    # Funciones principales
    def guardar_temperatura(self, temperatura, fecha):
        if self.devolver_temperatura(fecha) is None:
            # Si no existe la fecha, inserta y aumenta el contador
            self.raiz = self._insertar(self.raiz, temperatura, fecha)
            self._cantidad += 1
        else:
            # Si ya existe, actualiza la temperatura
            self.raiz = self._insertar(self.raiz, temperatura, fecha)

    def devolver_temperatura(self, fecha):
        # devuelve la temperatura en la fecha indicada
        fecha_dt = self._separar_fecha(fecha)  # con la funcion del avl convierte de strings a datetime la fecha
        nodo = self.raiz                       # empieza por la raiza
        while nodo:
            if fecha_dt < nodo.fecha:         # cuando la fecha buscada es menor, va al subárbol izquierdo
                nodo = nodo.izquierdo
            elif fecha_dt > nodo.fecha:       # si es mayor, va al subárbol derecho
                nodo = nodo.derecho
            else:
                return nodo.temperatura       # cuando encuentra la fecha, devuelve la temperatura
        return None                            # si no la encuentra da None

    def borrar_temperatura(self, fecha):
        # borra la temperatura en esa fecha (si existe), y le saca uno al contador
        if self.devolver_temperatura(fecha) is not None:
            self.raiz = self._borrar(self.raiz, self._separar_fecha(fecha))
            self._cantidad -= 1

    def cantidad_muestras(self):
        # da la cantidad de muestras cargadas
        return self._cantidad

    # temepraturas en rangos
    def _extremo_en_rango(self, nodo, f1, f2, tipo):
        if not nodo:
            return float('-inf') if tipo == "max" else float('inf')

        if nodo.fecha < f1:
            # si la fecha del nodo es menor que el rango, todo el subárbol izquierdo se descarta y va a la derecha
            return self._extremo_en_rango(nodo.derecho, f1, f2, tipo)
        if nodo.fecha > f2:
            # si la fecha del nodo es mayor que el rango, todo el subárbol derecho se descarta y va a la izquierda
            return self._extremo_en_rango(nodo.izquierdo, f1, f2, tipo)

        # si la fecha del nodo está entre el rango, se miran los dos subarboles y se compra con el nodo
        izq = self._extremo_en_rango(nodo.izquierdo, f1, f2, tipo)
        der = self._extremo_en_rango(nodo.derecho, f1, f2, tipo)
        # si tipo == "max" devuelve el máximo entre el nodo y los resultados de subárboles, si no el mínimo
        return max(nodo.temperatura, izq, der) if tipo == "max" else min(nodo.temperatura, izq, der)

    def max_temp_rango(self, f1, f2):
        return self._extremo_en_rango(self.raiz, self._separar_fecha(f1), self._separar_fecha(f2), "max")

    def min_temp_rango(self, f1, f2):
        return self._extremo_en_rango(self.raiz, self._separar_fecha(f1), self._separar_fecha(f2), "min")

    def devolver_temperaturas(self, f1, f2):
        # Devuelve una lista de las temperaturas en el rango indicado
        f1, f2 = self._separar_fecha(f1), self._separar_fecha(f2)  # convierte strings a datetime
        lista = []
        self._listar_en_rango(self.raiz, f1, f2, lista)             # va completando la lista
        return lista

    def _listar_en_rango(self, nodo, f1, f2, lista):
        # recorre el arbol y agrega a la lista las fechas que esten el el rango indicado
        if not nodo:
            return
        if nodo.fecha > f1:
            # recorre solo a la izquierda si hay nodos mayores a f1
            self._listar_en_rango(nodo.izquierdo, f1, f2, lista)
        if f1 <= nodo.fecha <= f2:
            # si el nodo esta en el rango, lo pasa nuevamente a string y lo agrega a la lista
            lista.append(f"{nodo.fecha.strftime('%d/%m/%Y')}: {nodo.temperatura} ºC")
        if nodo.fecha < f2:
            # recorre solo derecha si hay nodos menores a f2
            self._listar_en_rango(nodo.derecho, f1, f2, lista)

    # Carga de archivo
    def cargar_archivo(self, ruta_archivo):
        # abre el archivo y por cada linea de fecha llama a guardar temperatura
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()            
                if not linea:
                    continue                     
                fecha_str, temp_str = linea.split(";")   
                self.guardar_temperatura(float(temp_str), fecha_str)  # carga la muestra

    # grafica del árbol
    def graficar_arbol(self):
        # Dibuja el árbol usando networkx para la estructura y matplotlib para mostrarlo
        if not self.raiz:
            print("El árbol está vacío.")
            return

        G = nx.DiGraph()                         # Grafo dirigido para representar padre->hijo
        self._agregar_nodos_edges(self.raiz, G)  # Rellena el grafo con nodos y aristas
        pos = self._generar_posiciones(self.raiz) # Genera posiciones x,y para cada nodo
        # crea etiquetas con fecha y temperatura para mostrar en cada nodo
        etiquetas = {n: f"{n.fecha.strftime('%d/%m/%Y')}\n{n.temperatura}°C" for n in G.nodes()}

        plt.figure(figsize=(10, 6))              # Crea la figura
        # Dibuja el grafico
        nx.draw(G, pos, with_labels=True, labels=etiquetas, node_size=1600,
                node_color="skyblue", font_size=8, font_weight="bold", arrows=False)
        plt.title("Árbol AVL de Temperaturas", fontsize=12, fontweight="bold")
        plt.show()                               # Muestra la figura en pantalla

    def _agregar_nodos_edges(self, nodo, G):
        if not nodo:
            return
        G.add_node(nodo)                          
        if nodo.izquierdo:
            G.add_edge(nodo, nodo.izquierdo)     
            self._agregar_nodos_edges(nodo.izquierdo, G)  
        if nodo.derecho:
            G.add_edge(nodo, nodo.derecho)      
            self._agregar_nodos_edges(nodo.derecho, G)    #

    def _generar_posiciones(self, nodo, x=0, y=0, dx=1.0, pos=None): 
        if pos is None:
            pos = {}
        pos[nodo] = (x, -y)                      
        if nodo.izquierdo:
            self._generar_posiciones(nodo.izquierdo, x - dx, y + 1, dx / 1.8, pos)
        if nodo.derecho:
            self._generar_posiciones(nodo.derecho, x + dx, y + 1, dx / 1.8, pos)
        return pos                             
