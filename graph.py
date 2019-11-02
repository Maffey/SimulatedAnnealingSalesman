from collections import defaultdict
from typing import Dict, Any


class Graph:
    edges: Dict[str, list]
    weights: Dict[tuple, int]

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

    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight


'''
Code for operating on graphs. Not used in annealing approach.
# Initiate the main graph
graph = Graph()

# Set up graph with edges
for edge in edges_odd_index:
    graph.add_edge(*edge)
'''
