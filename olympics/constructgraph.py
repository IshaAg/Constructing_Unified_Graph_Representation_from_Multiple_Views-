import networkx as nx
from neighbour import *
g=nx.Graph()
node=[i for i in range(1,465)]
g.add_nodes_from(node)
from graphedges import *
g.add_edges_from(graphedges)
import matplotlib.pyplot as plt
nx.draw(g)
plt.savefig("file.png")
plt.show()
