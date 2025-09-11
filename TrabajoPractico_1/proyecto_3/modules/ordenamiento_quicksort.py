import random
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return quicksort(izquierda) + medio + quicksort(derecha)


if __name__ == '__main__': 
    lista = [random.choice([-1, 1]) * random.randint(10000, 99999) for _ in range(500)]
    lista_sorted = sorted(lista)
    lista_ordenada = quicksort(lista)
    print(lista_ordenada)

    if lista_ordenada == lista_sorted:
        print("La lista se ordenó correctamente")
    else:
        print("la lista está desordenada")