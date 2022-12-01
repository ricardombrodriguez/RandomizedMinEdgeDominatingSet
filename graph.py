# @Author: Ricardo Rodriguez

from constants import *
from random import randint, seed
from math import sqrt

seed(SEED)

class Graph:

    def __init__(self, num_vertices, edge_percentage):

        self.num_vertices = num_vertices
        self.edge_percentage = edge_percentage
        self.create_vertices()
        self.create_edges()

    def create_vertices(self):
        self.vertices = {}
        for i in range(self.num_vertices):
            while True:
                x, y = randint(MIN_AXIS_VALUE,MAX_AXIS_VALUE), randint(MIN_AXIS_VALUE,MAX_AXIS_VALUE)
                if not ((x,y) in self.vertices.values()) and self.is_distant(x,y):
                    self.vertices[i+1] = (x,y)
                    break
    
    def is_distant(self,x,y):
        distances = [ sqrt((x-v[0])**2 + (y-v[1])**2) for v in self.vertices.values()]
        return all(d > 1 for d in distances)

    def create_edges(self):

        min_edges_graph = self.num_vertices - 1
        max_edges_graph = self.num_vertices * (self.num_vertices - 1) / 2 
        num_edges =  max( [round((self.edge_percentage * max_edges_graph) / 100), min_edges_graph] )
        unconnected_vertices = list(self.vertices.keys())
        self.adjacency_list = {}

        for i in range(num_edges):
            while 1:
                e1 = randint(1,self.num_vertices) if not unconnected_vertices else unconnected_vertices.pop(randint(0,len(unconnected_vertices)-1))
                e2 = randint(1,self.num_vertices) if not unconnected_vertices or len(unconnected_vertices) == 1 else unconnected_vertices.pop(randint(0,len(unconnected_vertices)-1))

                if not (e1 == e2 or (self.adjacency_list and ( ( e1 in self.adjacency_list and e2 in self.adjacency_list[e1] ) or ( e2 in self.adjacency_list and e1 in self.adjacency_list[e2] ) ) )):
                    if e1 not in self.adjacency_list:
                        self.adjacency_list[e1] = [e2]
                    else:
                        self.adjacency_list[e1] += [e2]
                    if e2 not in self.adjacency_list:
                        self.adjacency_list[e2] = [e1]
                    else:
                        self.adjacency_list[e2] += [e1]
                    break
                elif e1 == e2:
                    unconnected_vertices.append(e1)


        self.edges = []
        [ self.edges.append((v1,v2)) for v1, edge_list in self.adjacency_list.items() for v2 in edge_list if (v2,v1) not in self.edges ]
