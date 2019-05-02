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
    
    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """
        find all the paths from start vertex to end_vertex in graph
        """
        graph = self.__graph_dict
        path = path + [start_vertex]
        
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, end_vertex, path)
                
                for p in extended_paths:
                    paths.append(p)
                    
        return paths
    
    
    def vertex_degree(self, vertex):
        """
        The degree sum formula (Handshaking lemma): 
        ∑v ∈ Vdeg(v) = 2 |E| 
        This means that the sum of degrees of all the vertices is equal to the number of edges multiplied by 2.
        We can conclude that the number of vertices with odd degree has to be even. This statement is known as 
        the handshaking lemma. The name "handshaking lemma" stems from a popular mathematical problem: In any 
        group of people the number of people who have shaken hands with an odd number of other people from the 
        group is even. 
        
           
        The degree of a vertex is the number of edges connecting it, i.e. the number of adjacent vertices,
        Loops are counted double i.e. every occurence of vertex in the list of adjacent vertices
        """
        adj_vertices = self.__graph_dict[vertex]
        degree = len(adj_vertices) + adj_vertices.count(vertex)
        return degree
    
    
    def find_isolated_vertices(self):
        graph = self.__graph_dict
        isolated = []
        for vertex in graph:
            print(isolated, vertex)
            if not graph[vertex]:
                isolated += [vertex]
        return isolated
    
    def delta(self):
        minimum = 10000000
        for vertex in self.__graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree < minimum: 
                minimum = vertex_degree
        return minimum
    
    
    def Delta(self):
        maximum = 0
        for vertex in self.__graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree > maximum: 
                maximum = vertex_degree
        return maximum
    
    def degree_sequence(self):
        seq = []
        for vertex in self.__graph_dict:
            seq += [self.vertex_degree(vertex)]
        seq.sort(reverse=True)
        return seq
    
    def density(self):
        """ method to calculate the density of graph"""
        g = self.__graph_dict
        V = len(self.vertices())
        E = len(self.edges())
        return 2.0 * E/ (V * (V - 1))
        
    def is_connected(self, vertices_encountered=None, start_vertex=None):
        """ determines if the graph is connected"""
        if vertices_encountered is None:
            vertices_encountered = set()
            
        gdict = self.__graph_dict
        vertices = list(gdict.keys()) 
        if not start_vertex:
            start_vertex = vertices[0]
        vertices_encountered.add(start_vertex)
        if len(vertices_encountered) != len(vertices):
            for vertex in gdict[start_vertex]:
                if vertex not in vertices_encountered:
                    if self.is_connected(vertices_encountered, vertex):
                        return True
        else:
            return True
        return False
    
    def diameter(self):
        v = self.vertices()
        pairs = [(v[i], v[j]) for i in range(len(v) - 1) for j in range(i+1, len(v))]
        smallest_paths = []
        for (s, e) in pairs:
            paths = self.find_all_paths(s, e)
            smallest = sorted(paths, key=len)[0]
            smallest_paths.append(smallest)
            
        print(smallest_paths)    
        smallest_paths.sort(key=len)
        # longest path is at the end of list, 
        # i.e. diameter corresponds to the length of this path
        
        diameter = len(smallest_paths[-1]) - 1
        return diameter
        
    
    @staticmethod
    def erdos_gallai(deg_sequence):
        if sum(deg_sequence) % 2:
            return False
        for k in range(1, len(deg_sequence) + 1):
            left = sum(deg_sequence[:k])
            right = k * (k -1) + sum([min(x, k) for x in deg_sequence[k:]])
            if left > right:
                return False
        return True
    
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

    print("vertex degree of c:")    
    print(graph.vertex_degree('c'))    

    print(str(graph))

    
        
    
    
    
    
    
    
    
    
    
    
    