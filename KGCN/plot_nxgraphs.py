import matplotlib.pyplot as plt 
import networkx as nx 
import os
import sys
from pathlib import Path
PATH = os.getcwd() #+'\data\\'
SAVEPATH = PATH + "/nx_2class_500n2500/"

scn_idx = 1972
graph = nx.read_gpickle(str(SAVEPATH) + "graph_" + str(scn_idx) + ".gpickle")

new_graph = nx.Graph(graph)
nx.draw(new_graph, with_labels=True)
plt.show()