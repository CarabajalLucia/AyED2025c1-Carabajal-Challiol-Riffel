from modules.monticulo_binario import Monticulo_binario

class ColaPrioridad:
    def __init__(self):
        self.monticulo = Monticulo_binario()
        self.elementos = {}  # referencia rápida: vértice -> prioridad

    def construirMonticulo(self, lista):
        # Insertamos uno por uno porque Monticulo_binario no tiene construirMonticulo()
        for prioridad, vertice in lista:
            self.monticulo.insertar((prioridad, vertice))
            self.elementos[vertice] = prioridad

    def estaVacia(self):
        return self.monticulo.tamañoactual == 0  # usa "tamañoactual"

    def eliminarMin(self):
        # usa extraer_min()
        prioridad, vertice = self.monticulo.extraer_min()
        self.elementos.pop(vertice, None)
        return vertice

    def decrementarClave(self, vertice, nuevaPrioridad): #cambia la prioridad de un vertice en la cola, chequear el orden
        self.elementos[vertice] = nuevaPrioridad
        nueva_lista = [(p, v) for v, p in self.elementos.items()]
        self.monticulo = Monticulo_binario()
        for prioridad, vert in nueva_lista:    
            self.monticulo.insertar((prioridad, vert))

    def __contains__(self, vertice): #chequea que el vertice siga o no en la cola, permite que utilicemos in 
        return vertice in self.elementos
    

    