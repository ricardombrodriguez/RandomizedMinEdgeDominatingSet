# @Author: Ricardo Rodriguez

from itertools import chain, combinations
from time import time
from random import randint, choice
from math import log10
from copy import deepcopy

class Problem:

    def __init__(self, graph, search_type):

        self.iterations = 0
        self.type = search_type
        self.graph = graph
        start = time()
        result = self.greedy_search(self.graph.adjacency_list) if search_type == "greedy" else \
                                       self.exaustive_search() if search_type == "exaustive" else \
                                       self.randomized_search()
        self.result = result[0]
        self.counter = result[1]
        self.time = time()-start
        print(f"{search_type} time: {time()-start} | counter: {self.counter}")
        

    def exaustive_search(self):
        
        basic_operations = 0
        for subset in self.generate_subsets(self.graph.edges):
            self.iterations += 1
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
            self.iterations = 1
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

    def randomized_search(self):

        counter = 0
        iteration = 0
        best_result = []
        self.iterations = self.get_randomized_iterations(self.graph.edges)
        while iteration < self.iterations:
            result, iteration_counter = self.random_iteration(adjacency_list=deepcopy(self.graph.adjacency_list))
            best_result = result if len(result) < len(best_result) or not best_result else best_result
            iteration += 1
            counter += iteration_counter
        print("counter", counter)
        print(self.iterations)
        return (best_result, counter)

    def random_iteration(self, adjacency_list):

        result = []
        counter = 0
        remaining_vertices = len(adjacency_list.keys())
        counter += 2
        while remaining_vertices:
            v1 = choice(list(adjacency_list.keys()))
            v2 = adjacency_list[v1][randint(0,len(adjacency_list[v1])-1)]
            edge = (v1,v2) 
            removed_list = set(adjacency_list.pop(v1,[]) + adjacency_list.pop(v2,[]))
            remaining_vertices -= 2
            neighbours = removed_list - {v1,v2}
            for k in neighbours:
                if k in adjacency_list and edge[0] in adjacency_list[k]:
                    adjacency_list[k].remove(edge[0])
                if k in adjacency_list and edge[1] in adjacency_list[k]:
                    adjacency_list[k].remove(edge[1])
                if not adjacency_list[k]:
                    del adjacency_list[k]    
                    remaining_vertices -= 1
                counter += 3
            result.append(edge)
            counter += 13
        return result, counter
        

    def get_randomized_iterations(self, edges):
        num_edge_combinations = 2**len(edges) - 1
        iterations = max([ 5, round( 0.1 * log10(num_edge_combinations) ) ])
        return iterations



    def verify_edge_dominating_set(self, edges, edge):

        remaining_edges = [ e for e in edges if e[0] not in edge and e[1] not in edge ]
        remaining_adjacency_list = { e[0] : [e[1]] for e in remaining_edges }
        for e in remaining_edges:
            if e[0] not in remaining_adjacency_list:
                remaining_adjacency_list[e[0]] = [e[1]]
            else:
                remaining_adjacency_list[e[0]] += [e[1]]    
        return remaining_adjacency_list