class Vertice:
    def __init__(self, clave):
        self.id = clave
        self.conectadoA = {}
        self.distancia = float('inf')  # distancia usada por Prim
        self.predecesor = None         # vértice anterior en el MST
    def __lt__(self, other): #compara vertice
        return self.distancia < other.distancia

    def agregarVecino(self, vecino, ponderacion=0):
        self.conectadoA[vecino] = ponderacion
    
    def obtenerConexiones(self):
        return self.conectadoA.keys()
    
    def obtenerId(self):
        return self.id
    
    def obtenerPonderacion(self, vecino):
        return self.conectadoA[vecino]

    def asignarDistancia(self, dist):
        self.distancia = dist

    def obtenerDistancia(self):
        return self.distancia

    def asignarPredecesor(self, pred):
        self.predecesor = pred

    def obtenerPredecesor(self):
        return self.predecesor


class Grafo:
    def __init__(self):
        self.listaVertices = {}  # Diccionario de vértices: clave -> objeto Vertice
        self.numVertices = 0     # Contador de vértices en el grafo

    def agregarVertice(self, clave):
        if clave in self.listaVertices:  # Si el vértice ya existe, se devuelve
            return self.listaVertices[clave]
        nuevoVertice = Vertice(clave)  # Crear un nuevo vértice
        self.listaVertices[clave] = nuevoVertice  # Agregarlo al diccionario
        self.numVertices += 1  # Incrementar el contador de vértices
        return nuevoVertice

    # Método para obtener un vértice por su clave
    def obtenerVertice(self, n):
        return self.listaVertices.get(n)  # Devuelve None si no existe

    # Método para agregar una arista entre dos vértices con un peso opcional
    def agregarArista(self, de_, a, ponderacion=0):
        if de_ not in self.listaVertices:  # Si el vértice de origen no existe, se crea
            self.agregarVertice(de_)
        if a not in self.listaVertices:  # Si el vértice destino no existe, se crea
            self.agregarVertice(a)
        # Agregar la conexión en ambos sentidos (grafo no dirigido)
        self.listaVertices[de_].agregarVecino(self.listaVertices[a], ponderacion)
        self.listaVertices[a].agregarVecino(self.listaVertices[de_], ponderacion)

    # Devuelve todas las claves de los vértices del grafo
    def obtenerVertices(self):
        return self.listaVertices.keys()
    
    def __contains__(self, n):
        return n in self.listaVertices

    # Permite iterar directamente sobre los vértices del grafo
    def __iter__(self):
        return iter(self.listaVertices.values())
    
def leer_aldedas(file_path="aldeas.txt"):
    grafo = Grafo()
    with open(file_path, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if linea.strip() == "":
                continue
            partes = linea.strip().split(",")
            if len(partes) == 3:
                origen = partes[0].strip()
                destino = partes[1].strip()
                distancia = int(partes[2].strip())
                grafo.agregarArista(origen, destino, distancia)
    return grafo


