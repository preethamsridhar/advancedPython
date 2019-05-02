# -*- coding: utf-8 -*-
"""
Created on Thu May  2 16:25:56 2019

@author: preet
"""

from graphTheory2 import Graph

g = { "a" : ["c"],
      "b" : ["c","e","f"],
      "c" : ["a","b","d","e"],
      "d" : ["c"],
      "e" : ["b","c","f"],
      "f" : ["b","e"]
}

graph = Graph(g)
diameter = graph.diameter()
print(diameter)