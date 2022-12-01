# @Author: Ricardo Rodriguez

from itertools import chain, combinations
from time import time

class Problem:

    def __init__(self, graph, search_type):

        self.type = search_type
        self.graph = graph
        start = time()
        result = self.greedy_search(self.graph.adjacency_list) if search_type == "greedy" else self.exaustive_search()
        self.result = result[0]
        self.counter = result[1]
        self.time = time()-start
        print(f"{search_type} time: {time()-start} | counter: {self.counter}")
        

    def exaustive_search(self):
        basic_operations = 0
        for subset in self.generate_subsets(self.graph.edges):
            remaining_edges = self.graph.edges
            for edge in subset:
                basic_operations += 1
                remaining_edges = [ e for e in list(remaining_edges) if e[0] not in edge and e[1] not in edge ]
                if not remaining_edges:
                    return (subset, basic_operations)

    
    def generate_subsets(self, edges):
        for subset in chain.from_iterable(combinations(edges, num) for num in range(len(edges)+1)):
            yield subset


    def greedy_search(self, adjacency_list, counter=0):

        if counter == 0:
            adjacency_list = dict(sorted(adjacency_list.items(), key=lambda x : len(x[1]), reverse=True))
            for data in list(adjacency_list.items()):
                adjacency_list[data[0]] = sorted(data[1], key = lambda x : len(adjacency_list[x]), reverse=True)

        edges = []
        [ edges.append((v1,v2)) for v1, edge_list in adjacency_list.items() for v2 in edge_list if (v2,v1) not in edges ]

        while edges:
            counter += 1
            edge = edges.pop(0)
            adjacency_list = self.verify_edge_dominating_set(edges,edge)
            if not adjacency_list:
                return ([edge], counter)                                                   
            greedy = self.greedy_search(adjacency_list, counter)
            return ( [edge] + greedy[0], greedy[1])


    def verify_edge_dominating_set(self, edges, edge):

        remaining_edges = [ e for e in edges if e[0] not in edge and e[1] not in edge ]
        remaining_adjacency_list = { e[0] : [e[1]] for e in remaining_edges }
        for e in remaining_edges:
            if e[0] not in remaining_adjacency_list:
                remaining_adjacency_list[e[0]] = [e[1]]
            else:
                remaining_adjacency_list[e[0]] += [e[1]]    
        return remaining_adjacency_list