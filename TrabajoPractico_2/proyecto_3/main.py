from modules.paloma_prim import leer_aldedas, prim
from modules.grafo import Grafo
import networkx as nx
import matplotlib.pyplot as plt

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

#Grafica
G = nx.DiGraph()
for aldea in padres.keys():
    G.add_node(aldea)
for origen, destinos in envios.items():
    for destino in destinos:
        G.add_edge(origen, destino)

pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(12,8))
nx.draw_networkx_nodes(G, pos, node_size=1000, node_color="skyblue")
nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")
nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=20, edge_color="red", width=2)
plt.title("Flujo de noticias entre aldeas (MST)")
plt.axis('off')
plt.show()
