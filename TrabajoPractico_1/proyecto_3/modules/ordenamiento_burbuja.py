import random
def ordenamiento_burbuja (lista):
    intercambiado = True 
    num_pasadas = len(lista)-1
    while num_pasadas > 0 and intercambiado:
        intercambiado = False
        for j in range(num_pasadas):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambiado = True
        num_pasadas -= 1
    return lista

if __name__ == '__main__':
 
    lista = [random.choice([-1, 1]) * random.randint(10000, 99999) for _ in range(500)]
    lista_sorted = sorted(lista)
    lista_ordenada = ordenamiento_burbuja(lista)
    print(lista_ordenada)

    if lista_ordenada == lista_sorted:
        print("La lista se ordenó correctamente")
    else:
        print("la lista está desordenada")


