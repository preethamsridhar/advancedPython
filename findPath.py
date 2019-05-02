# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:01:51 2019

@author: preet
"""

from graphTheory2 import Graph

g = { "a" : ["c","d", "f"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : ["a"]
    }

graph = Graph(g)

# =============================================================================
# print("Vertices of graph:", end=" ")
# print(graph.vertices())
# 
# print("Edges of graph:", end=" ")
# print(graph.edges())
# =============================================================================

print(str(graph))

print('Find the path from vertex "a" to vertex "b":')
path = graph.find_path('a', 'b')
print(path)

print('Find the path from vertex "a" to vertex "f":')
path = graph.find_path('a', 'f')
print(path)

print('Find the path from vertex "c" to vertex "c":')
path = graph.find_path('c','c')
print(path)

