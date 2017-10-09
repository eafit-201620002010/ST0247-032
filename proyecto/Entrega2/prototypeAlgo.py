from collections import defaultdict
import math

"""
Title: IMPLEMENTING DJIKSTRA'S SHORTEST PATH ALGORITHM WITH PYTHON
Author: Ben Keen
Date: 11th January 2017
Code Version: 
Avaibility: http://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/
"""


class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}
        #AQUI
        self.grafo = defaultdict(dict)
    
    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.weights[(from_node, to_node)] = weight
        #AQUI
        self.grafo[from_node][to_node] = weight

graph = Graph()
"""
edges = [
    ('X', 'A', 7),
    ('X', 'B', 2),
    ('X', 'C', 3),
    ('X', 'E', 4),
    ('A', 'D', 3),
    ('B', 'A', 4),
    ('B', 'D', 4),
    ('B', 'H', 5),
    ('D', 'F', 1),
    ('F', 'H', 3),
    ('H', 'G', 2),
    ('G', 'Y', 2),
]
"""
edges = [
    ('10000', '1', 10),
    ('10000', '3', 14),
    ('10000', '4', 10),
    ('1', '10000', 10),
    ('1', '2', 7),
    ('1', '3', 12),
    ('1', '4', 15),
    ('2', '1', 7),
    ('2', '3', 20),
    ('3', '10000', 14),
    ('3', '1', 12),
    ('3', '2', 20),
    ('3', '4', 8),
    ('4', '10000', 10),
    ('4', '1', 15),
    ('4', '3', 8),
    ('X', 'A', 7),
    ('X', 'B', 2),
    ('X', 'C', 3),
    ('X', 'E', 4),
    ('A', 'D', 3),
    ('B', 'A', 4),
    ('B', 'D', 4),
    ('B', 'H', 5),
    ('D', 'F', 1),
    ('F', 'H', 3),
    ('H', 'G', 2),
    ('G', 'Y', 2)
]

for edge in edges:
    graph.add_edge(*edge)

def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        #AQUI
        destinations = list(graph.grafo[current_node].keys())
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            #AQUI
            weight = graph.grafo[current_node][next_node] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    #print("weight3 ",weight)
    return path,weight


#print(dijsktra(graph, 'X','Y'))
#print(dijsktra(graph, 'X','B'))
#print(dijsktra(graph, '1','4'))