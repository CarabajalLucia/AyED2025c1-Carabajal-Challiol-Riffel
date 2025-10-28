class Vertice:
    def __init__(self, clave):
        self.id = clave  # Identificador del vértice
        self.conectadoA = {}  # Diccionario de vecinos y sus ponderaciones

    # Método para agregar un vecino con un peso opcional (por defecto 0)
    def agregarVecino(self, vecino, ponderacion=0):
        self.conectadoA[vecino] = ponderacion

    # Representación en texto del vértice y sus conexiones
    def __str__(self):
        return f"{self.id} conectadoA: {[i.id for i in self.conectadoA]}"

    # Devuelve los vértices vecinos del vértice actual
    def obtenerConexiones(self):
        return self.conectadoA.keys()

    # Devuelve el id del vértice
    def obtenerId(self):
        return self.id

    # Devuelve la ponderación (peso) de la arista hacia un vecino
    def obtenerPonderacion(self, vecino):
        return self.conectadoA[vecino]


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

    # Permite iterar directamente sobre los vértices del grafo
    def __iter__(self):
        return iter(self.listaVertices.values())
