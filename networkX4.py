# -*- coding: utf-8 -*-
"""
Created on Thu May  2 17:27:50 2019

@author: preet
"""

import networkx as nx

# =============================================================================
# G = nx.path_graph(10)
# mapping = dict(zip(G.nodes(),"abcde" ))
# nx.relabel_nodes(G, mapping, copy=False)
# 
# print("Nodes of graph:")
# print(G.nodes())
# =============================================================================

G = nx.path_graph(10)

def mapping(x):
    return x + 100

nx.relabel_nodes(G, mapping, copy=False)

print("Nodes of graph:")
print(G.nodes())