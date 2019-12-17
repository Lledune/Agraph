import community
import networkx as nx
import matplotlib.pyplot as plt
import os
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
G = nx.read_gexf(dataOne, relabel=True)
#first compute the best partition
#partition = community.best_partition(G)
D = community.generate_dendrogram(G)
D = G
partition = community.best_partition(D)

#drawing
size = float(len(set(partition.values())))
pos = nx.circular_layout(G)
count = 0.
for com in set(partition.values()) :
    count = count + 1.
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 20,
                                node_color = str(count / size))


nx.draw_networkx_edges(G, pos, alpha=0.5)
nx.draw_networkx_labels(G, pos)
plt.show()