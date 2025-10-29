from modules.paloma_prim import prim
from modules.grafo import Grafo, leer_aldedas
import networkx as nx
import matplotlib.pyplot as plt
import itertools


grafo = leer_aldedas("aldeas.txt")
inicio = "Peligros"
padres, envios, total_distancia = prim(grafo, inicio)
print("Aldeas en orden alfabético:")
for aldea in sorted(grafo.obtenerVertices()):
    print(aldea)

print("\nEnvío de noticias más eficiente:")
for aldea in sorted(grafo.obtenerVertices()):
    receptor = padres.get(aldea)
    enviados = envios.get(aldea, [])
    print(f"\n Aldea: {aldea}")
    if receptor:
        print(f"   Recibe de: {receptor}")
    else:
        print(f"   Recibe de: --- (es el origen)")
    if enviados:
        print(f"   Envía a: {', '.join(enviados)}")
    else:
        print(f"   Envía a ninguna")

print(f"\nDistancia total recorrida por las palomas: {total_distancia} leguas")

# Gráfico
G = nx.DiGraph()
for aldea in padres.keys():
    G.add_node(aldea)

for origen, destinos in envios.items():
    for destino in destinos:
        G.add_edge(origen, destino)

# Layout tipo fuerza
pos = nx.spring_layout(G, k=2.0, iterations=200, seed=42)

plt.figure(figsize=(14,10))

# Nodos: verde para origen, azul para resto
node_colors = ["green" if n == inicio else "skyblue" for n in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_size=1200, node_color=node_colors)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

# Colores para los caminos (un color distinto por cada origen)
colors = itertools.cycle(["red", "blue", "orange", "purple", "brown", "pink", "cyan", "magenta", "olive"])

# Dibujar aristas con colores distintos por cada rama
for origen, destinos in envios.items():
    color = next(colors)
    for destino in destinos:
        nx.draw_networkx_edges(G, pos, edgelist=[(origen, destino)],
                               arrowstyle="->", arrowsize=20, edge_color=color, width=2)

plt.title("Flujo de noticias entre aldeas (MST)", fontsize=16)
plt.axis('off')
plt.show() 