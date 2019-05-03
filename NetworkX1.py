# -*- coding: utf-8 -*-
"""
Created on Thu May  2 16:53:57 2019

@author: preet
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node("a")
G.add_nodes_from(["b", "c"])

G.add_edge(1, 2)
edge = ("d", "e")
G.add_edge(*edge)

edge = ("a", "b")
G.add_edges_from([edge])

G.add_edges_from([("a", "c"), ("c", "d"), ("a", 1), (1, "d"), ("a", 2)])

print(G.nodes())
print(G.edges())

nx.draw(G)
plt.savefig("simple_path.png")
plt.show()
