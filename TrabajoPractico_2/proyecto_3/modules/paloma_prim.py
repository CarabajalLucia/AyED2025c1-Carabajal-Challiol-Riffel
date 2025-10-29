import sys
from modules.cola_prioridades import ColaPrioridad

def prim(grafo, inicio_nombre):
    inicio = grafo.obtenerVertice(inicio_nombre)
    cp = ColaPrioridad()

    for v in grafo:
        v.asignarDistancia(sys.maxsize)
        v.asignarPredecesor(None)

    inicio.asignarDistancia(0)
    cp.construirMonticulo([(v.obtenerDistancia(), v) for v in grafo])

    while not cp.estaVacia():
        verticeActual = cp.eliminarMin()
        for verticeSiguiente in verticeActual.obtenerConexiones():
            nuevoCosto = verticeActual.obtenerPonderacion(verticeSiguiente)
            if verticeSiguiente in cp and nuevoCosto < verticeSiguiente.obtenerDistancia():
                verticeSiguiente.asignarPredecesor(verticeActual)
                verticeSiguiente.asignarDistancia(nuevoCosto)
                cp.decrementarClave(verticeSiguiente, nuevoCosto)

    padres = {}
    envios = {}
    total_distancia = 0

    for v in grafo:
        if v.obtenerPredecesor():
            padres[v.obtenerId()] = v.obtenerPredecesor().obtenerId()
            envios.setdefault(v.obtenerPredecesor().obtenerId(), []).append(v.obtenerId())
            total_distancia += v.obtenerDistancia()
        else:
            padres[v.obtenerId()] = None

    return padres, envios, total_distancia
