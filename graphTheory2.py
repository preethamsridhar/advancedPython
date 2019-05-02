# -*- coding: utf-8 -*-
"""
Created on Wed May  1 19:10:05 2019

@author: preet
"""
class Graph(object):
    
    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict
        
    def vertices(self):
        return list(self.__graph_dict.keys())
    
    def edges(self):
        return self.__generate_edges()
    
    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []
    
    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]
        
    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]: 
                if {vertex, neighbour} not in edges:
                    edges.append({vertex, neighbour})
        return edges
              
    def __str__(self):
        res = ">>>\n"
        res += "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        res += "\n>>>"
        return res
    
    def find_path(self, start_vertex, end_vertex, path=None):
        """
        Find a path from start_vertex to end_vertex
        """
        if path == None:
            path = []
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)
                if extended_path:
                    return extended_path
        return None
    
if __name__ == "__main__":
    g = { 
        "a" : ["d"],
        "b" : ["c"],
        "c" : ["b", "c", "d", "e"],
        "d" : ["a", "c"],
        "e" : ["c"],
        "f" : []
    }
    
    graph = Graph(g)
    
    print("Vertices of graph:")
    print(graph.vertices())
    
    print("\nEdges of graph:")
    print(graph.edges())
    
    print("\nAdd Vertex:")
    graph.add_vertex("z")
    
    print("\nVertices of graph:")
    print(graph.vertices())
    
    print("\nAdd an edge")
    graph.add_edge({"a", "z"})
    
    print("\nVertices of graph:")
    print(graph.vertices())
    
    print("\nEdges of the graph")
    print(graph.edges())
    
    print('\nAdding an edge {"x","y"} with new vertices:')
    graph.add_edge({"x", "y"})
    
    print("\nVertices of a graph:")
    print(graph.vertices())
    print("\nEdges of a graph:")
    print(graph.edges())
    
    print(str(graph))

    
        
    
    
    
    
    
    
    
    
    
    
    