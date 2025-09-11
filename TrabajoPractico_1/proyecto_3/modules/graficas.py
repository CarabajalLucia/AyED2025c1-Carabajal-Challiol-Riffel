from matplotlib import pyplot as plt
from modules.tiempos import medir_tiempos
from modules.ordenamiento_burbuja import ordenamiento_burbuja
from modules.ordenamiento_quicksort import quicksort
from modules.ordenamiento_por_residuos import ordenamiento_por_residuos

# Lista global de métodos de ordenamiento
lista_metodos_ord = [ordenamiento_burbuja, quicksort, ordenamiento_por_residuos, sorted]

def graficar_tiempos():
    tamanos = [1, 10, 100, 200, 500, 700, 1000]
    plt.figure(figsize=(10, 6))
    for metodo_ord in lista_metodos_ord:
        tiempos = medir_tiempos(metodo_ord, tamanos)
        plt.plot(tamanos, tiempos, marker='o', label=metodo_ord.__name__)
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparación de tiempos de ordenamiento')
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == '__main__':
    graficar_tiempos()

