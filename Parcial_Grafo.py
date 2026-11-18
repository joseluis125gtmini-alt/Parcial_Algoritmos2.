import matplotlib.pyplot as plt
import networkx as nx

# 1. Crear un grafo dirigido (DiGraph)
G = nx.DiGraph()

# 2. Definir los vértices (nodos)
vertices = [1, 2, 3, 4, 5, 6]
G.add_nodes_from(vertices)

# 3. Definir las 8 aristas dirigidas EXACTAS del PDF
aristas = [
    (1, 2),
    (1, 3),
    (6, 1),  
    (2, 4),
    (3, 4),
    (3, 5),
    (4, 6),  
    (5, 4),
]
G.add_edges_from(aristas)

# --- REPRESENTACIÓN ALGORÍTMICA EN CONSOLA ---
print("=== INTERPRETACIÓN DEL GRAFO ===")
print(f"Vértices ({G.number_of_nodes()}): {list(G.nodes())}")
print(f"Aristas ({G.number_of_edges()}): {list(G.edges())}")
print(f"¿Es un grafo dirigido?: {'Sí' if G.is_directed() else 'No'}")

print("\nLista de Adyacencia:")
for nodo in G.nodes():
    print(f"  {nodo} -> {list(G.neighbors(nodo))}")

# --- GRAFICACIÓN EXACTA A LA IMAGEN ---
posiciones = {
    1: (0.0, 2.0),  # Arriba centro
    3: (-1.3, 1.1),  # Izquierda arriba
    2: (1.4, 1.2),  # Derecha arriba (ligeramente más abierto para que pase la línea 1->6)
    4: (0.0, 0.2),  # Centro
    5: (-1.3, -0.7),  # Izquierda abajo
    6: (1.3, -0.7),  # Derecha abajo
}

plt.figure(figsize=(6, 5))

nx.draw(
    G,
    pos=posiciones,
    with_labels=True,
    node_color="#1f4e78",
    node_size=950,
    font_color="white",
    font_weight="bold",
    font_size=12,
    edge_color="#262626",
    width=1.5,
    arrows=True,
    arrowstyle="-|>",
    arrowsize=18,
)

plt.xlim(-2.0, 2.1)
plt.ylim(-1.4, 2.7)
plt.axis("off")
plt.tight_layout()
plt.show()