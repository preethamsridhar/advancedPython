# -*- coding: utf-8 -*-
"""
Created on Thu May  2 17:15:23 2019

@author: preet
"""
import networkx as nx
import matplotlib.pyplot as plt

G = nx.path_graph(4)
cities = {
        0: "Toronto",
        1: "London",
        2: "Berlin",
        3: "New York"
        }
H = nx.relabel_nodes(G, cities)

print("Nodes of graph:")
print(H.nodes())

print("Edges of graph:")
print(H.edges())
nx.draw(G)
nx.draw(H)

plt.savefig("path_graph_cities.png")
plt.show()
