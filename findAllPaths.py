# -*- coding: utf-8 -*-
"""
Created on Thu May  2 13:00:01 2019

@author: preet
"""

from graphTheory2 import Graph

g = { "a" : ["d", "f"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : ["d"]
    }

graph = Graph(g)

print(str(graph))

print('All paths from vertex "a" to vertex "b":')
path = graph.find_all_paths('a', 'b')
print(path)

print('All paths from vertex "a" to vertex "f":')
path = graph.find_all_paths('a', 'f')
print(path)

print('All paths from vertex "c" to vertex "c":')
path = graph.find_all_paths('c', 'c')
print(path)