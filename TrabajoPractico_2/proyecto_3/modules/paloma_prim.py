from modules.grafo import Grafo
import heapq #ordena la ponderacion de menor a mayor

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

def prim(grafo, inicio_id):
    visitadas = set()
    padres = {inicio_id: None}
    envios = {i.obtenerId(): [] for i in grafo}
    total_distancia = 0

    visitadas.add(inicio_id)
    heap = []
    for vecino in grafo.obtenerVertice(inicio_id).obtenerConexiones():
        heapq.heappush(heap, (grafo.obtenerVertice(inicio_id).obtenerPonderacion(vecino),
                              inicio_id,
                              vecino.obtenerId()))

    while heap:
        dist, origen, destino = heapq.heappop(heap)
        if destino not in visitadas:
            visitadas.add(destino)
            padres[destino] = origen
            envios[origen].append(destino)
            total_distancia += dist

            for vecino in grafo.obtenerVertice(destino).obtenerConexiones():
                if vecino.obtenerId() not in visitadas:
                    heapq.heappush(heap, (grafo.obtenerVertice(destino).obtenerPonderacion(vecino),
                                          destino,
                                          vecino.obtenerId()))

    return padres, envios, total_distancia
