import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (1, 3), (1, 4)])
nx.draw(G, with_labels=True, font_weight='bold')

plt.show()
