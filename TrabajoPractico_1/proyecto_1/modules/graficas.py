import time
import matplotlib.pyplot as plt
import numpy as np

from modules.lista_doblemente import ListaDoblementeEnlazada  

def medir_tiempo_len(lista):
    inicio = time.perf_counter()
    _ = len(lista)
    fin = time.perf_counter()
    return fin - inicio

def medir_tiempo_copiar(lista):
    inicio = time.perf_counter()
    _ = lista.copiar()   
    fin = time.perf_counter()
    return fin - inicio

def medir_tiempo_invertir(lista):
    inicio = time.perf_counter()
    _ = lista.invertir() 
    fin = time.perf_counter()
    return fin - inicio


tamanios = np.arange(10, 1001, 50) 
tiempos_len = []
tiempos_copiar = []
tiempos_invertir = []

for n in tamanios:
    lista = ListaDoblementeEnlazada()
    for i in range(n):
        lista.insertar(i)  
    tiempos_len.append(medir_tiempo_len(lista))
    tiempos_copiar.append(medir_tiempo_copiar(lista))
    tiempos_invertir.append(medir_tiempo_invertir(lista))

    # Gráfica
plt.plot(tamanios, tiempos_len, label="len(lista)")
plt.plot(tamanios, tiempos_copiar, label="copiar()")
plt.plot(tamanios, tiempos_invertir, label="invertir()")
plt.xlabel("Tamaño de la lista (n)")
plt.ylabel("Tiempo (segundos)")
plt.title("Tiempo real de ejecución de operaciones")
plt.legend()
plt.grid(True)
plt.show()