# -*- coding: utf-8 -*-
"""
Created on Thu May  2 15:43:55 2019

@author: preet
"""

from graphTheory2 import Graph


g1 = { "a" : ["d"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : []
}

g2 = { "a" : ["d","f"],
       "b" : ["c"],
       "c" : ["b", "c", "d", "e"],
       "d" : ["a", "c"],
       "e" : ["c"],
       "f" : ["a"]
}

g3 = { "a" : ["d","f"],
       "b" : ["c","b"],
       "c" : ["b", "c", "d", "e"],
       "d" : ["a", "c"],
       "e" : ["c"],
       "f" : ["a"]
}

graph = Graph(g1)
print(str(graph))
print(graph.is_connected())

graph = Graph(g2)
print(str(graph))
print(graph.is_connected())

graph = Graph(g3)
print(str(graph))
print(graph.is_connected())

