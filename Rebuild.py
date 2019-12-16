import matplotlib.pyplot as plt
import networkx as nx
import os
#paths names
dirname = os.path.dirname(__file__)
dataOne = os.path.join(dirname, 'data/lesmiserables.gexf')
dataTwo = os.path.join(dirname, 'data/airlines-sample.gexf')
dataThree = os.path.join(dirname, 'data/codeminer.gexf')
dirDic = {
    "Les miserables" : dataOne,
    "Airlines" : dataTwo,
    "Code-miner" : dataThree
}

G = nx.read_gexf(dataOne)
# position is stored as node attribute data for random_geometric_graph
pos = nx.get_node_attributes(G, 'pos')

G = nx.random_geometric_graph(200, 0.125)
# position is stored as node attribute data for random_geometric_graph
pos = nx.get_node_attributes(G, 'pos')

# find node near center (0.5,0.5)
dmin = 1
ncenter = 0
for n in pos:
    x, y = pos[n]
    d = (x - 0.5)**2 + (y - 0.5)**2
    if d < dmin:
        ncenter = n
        dmin = d

plt.figure(figsize=(8, 8))
nx.draw_networkx_edges(G, pos, alpha=0.4)
nx.draw_networkx_nodes(G, pos)

plt.xlim(-0.05, 1.05)
plt.ylim(-0.05, 1.05)
plt.axis('off')
plt.show()