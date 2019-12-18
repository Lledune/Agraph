import community
import networkx as nx
import matplotlib.pyplot as plt
import os
from matplotlib.colors import ListedColormap
import palettable
#paths names
dirname = os.path.dirname(__file__)
dataOne = 'c:/users/lucien/desktop/agraph/data/lesmiserables.gexf'
dataTwo = os.path.join(dirname, 'data/airlines-sample.gexf')
dataThree = 'c:/users/lucien/desktop/agraph/data/karate.gml'
dirDic = {
    "Les miserables" : dataOne,
    "Airlines" : dataTwo,
    "Karate" : dataThree
}

#better with karate_graph() as defined in networkx example.
#erdos renyi don't have true community structure
G = nx.read_gml(dataThree, label=None)
cmap = ListedColormap(palettable.matplotlib.Viridis_20.mpl_colors, N = len(G))

#first compute the best partition
#partition = community.best_partition(G)
D = community.generate_dendrogram(G)
D = G
partition = community.best_partition(D)


from operator import itemgetter
degrees = nx.degree_centrality(G)
nx.set_node_attributes(G, values = degrees, name = 'degreeTest')
nNodes = len(G)
maxdeg = max(degrees.values())
mindeg = min(degrees.values())


#lenpalette is the number of colors in palette
def normalize(val, max, min):
    val = ((val-min)/max)
    return val

#m is default size
def normalizeSize(val, max, min, m):
    val = ((val-min)/max)*m
    return val

displayedNodes = []
nodeColors = []
nodeSizes = []
for node, data in G.nodes(data = True):
    if(data['degreeTest'] > 0.2):
        displayedNodes.append(node)
        nodeColors.append(normalize(data['degreeTest'], maxdeg, mindeg))
        nodeSizes.append((normalizeSize(data['degreeTest'], maxdeg, mindeg, 500) + 1))

G = G.subgraph(displayedNodes)
pos = nx.circular_layout(G)


nx.draw(G, vmax = 1, vmin = 0, cmap = plt.cm.viridis, with_labels=False, node_size = nodeSizes, node_color = nodeColors, nodelist = displayedNodes)
plt.show()
