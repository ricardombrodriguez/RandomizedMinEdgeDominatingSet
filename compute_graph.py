# Used to solve the generated graphs given by the professor

# @Author: Ricardo Rodriguez

from graph import Graph
from constants import *
from problem import Problem
from time import time


def compute_graph(filename):
    g = read_file(filename)
    start = time()
    randomized = Problem(g, "randomized")
    elapsed_time = time() - start
    store_result(filename, randomized, elapsed_time)


def store_result(filename, randomized, elapsed_time):
    with open('pointers/results.txt', 'a') as results:
        results.write("{: <14} | {: <10} | {: <16} | {: <15} | {: <25} | {: >20}\n".format(filename.split("/")[1],randomized.graph.num_vertices,randomized.counter,len(randomized.result),elapsed_time,randomized.iterations))


def read_file(filename):

    g = Graph()

    with open(filename,'r') as f:

        lines = f.readlines()
        g.num_vertices = int(lines[2].strip())
        g.edges = []
        g.adjacency_list = {}
        for line in lines[4:]:
            v1 = line.split()[0]
            v2 = line.split()[1]
            g.edges.append((v1,v2))
            if v1 not in g.adjacency_list:
                g.adjacency_list[v1] = [v2]
            else:
                g.adjacency_list[v1] += [v2]
            if v2 not in g.adjacency_list:
                g.adjacency_list[v2] = [v1]
            else:
                g.adjacency_list[v2] += [v1]

    return g

if __name__ == "__main__":
    files = ["SWtinyG.txt","SWmediumG.txt","SWlargeG.txt"]
    with open('pointers/results.txt', 'a') as results:
        results.write("{: <14} | {: <10} | {: <16} | {: <15} | {: <25} | {: >20}\n".format("File","Vertices","Basic Operations","Solution Length","Elapsed Time","Iterations"))
    for f in files:
        compute_graph(f"pointers/{f}")