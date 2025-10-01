class Monticulo_binario:
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamañoactual = 0
    def infilArriba(self, i):
        while i // 2 > 0:
            if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            i = i // 2

    def insertar(self, elemento):
        self.listaMonticulo.append(elemento) 
        self.tamañoactual = self.tamañoactual +1
        self.infilArriba(self.tamañoactual)             #recoloca hacia arriba

    def infiltAbajo(self,i):
        while (i * 2) <= self.tamañoactual:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i] > self.listaMonticulo[hm]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm

    def hijoMin(self,i):
        if i * 2 + 1 > self.tamañoactual:
            return i * 2
        else:
            if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
            
    def extraer_min(self): # extrae el elemento de mayor prioridad
        minimo = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamañoactual]
        self.tamañoactual = self.tamañoactual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return minimo
    
    