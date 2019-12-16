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

G = nx.barabasi_albert_graph(10, 2)
nodeList = list(G.nodes)
degreeList = G.degree()

pos = nx.drawing.spiral_layout(G)
nx.draw_networkx(G, pos=pos, node_size = degreeList)
plt.axis('off')
plt.show()
