import random
def counting_sort(lista, exp):
    n = len(lista)
    salida = [0] * n        
    conteo = [0] * 10      

    for i in range(n):
        indice = (lista[i] // exp) % 10
        conteo[indice] += 1

    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    i = n - 1
    while i >= 0:
        indice = (lista[i] // exp) % 10
        salida[conteo[indice] - 1] = lista[i]
        conteo[indice] -= 1
        i -= 1

    for i in range(n):
        lista[i] = salida[i]

def ordenamiento_por_residuos(lista):
    max_num = max(lista)
    exp = 1
    while max_num // exp > 0: #// division
        counting_sort(lista, exp)
        exp *= 10
    return lista

if __name__ == '__main__':

    #lista = [random.choice([-1, 1]) * random.randint(10000, 99999) for _ in range(5)] No funciona para numeros negativos
    lista = [random.randint(10000, 99999) for _ in range(500)]
    lista_sorted = sorted(lista)
    lista_ordenada = ordenamiento_por_residuos(lista)
    print(lista_ordenada)

    if lista_ordenada == lista_sorted:
        print("La lista se ordeno correctamente")
    else:
        print("la lista esta desordenada")
    
