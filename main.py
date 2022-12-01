# @Author: Ricardo Rodriguez

from graph import Graph
from constants import *
from problem import Problem

import os

import networkx as nx
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def create_graphs():

    if not os.path.exists("graphs"):
        os.makedirs("graphs")

    if not os.path.exists('results.txt'):
        os.mknod('results.txt')
        with open('results.txt', 'a') as results:
            results.write("{: <12} | {: <10} | {: <15} | {: <16} | {: >20}\n".format("Search type","Vertices","Edge percentage","Basic operations","Time (s)"))

    vertices = MIN_GRAPH_VERTICES
    
    while 1:
        for edge_percentage in MAX_NUMBER_EDGES:
            print()
            print(f"num vertices: {vertices} | edge percentage: {edge_percentage}%)")
            g = Graph(vertices,edge_percentage)
            greedy = Problem(g,"greedy")
            save_result(greedy,edge_percentage)
            save_graph(greedy,edge_percentage)
            exaustive = Problem(g,"exaustive")
            save_result(exaustive,edge_percentage)
            save_graph(exaustive,edge_percentage)
        vertices += 1 

def save_result(p, edge_percentage):
    with open('results.txt', 'a') as results:
        results.write("{: <12} | {: <10} | {: <15} | {: <16} | {: >20}\n".format(p.type,len(p.graph.vertices),edge_percentage,p.counter,p.time))


def save_graph(p, edge_percentage):
    
    vertices, edges = p.graph.vertices, p.graph.edges
    result = p.result

    # Create networkx graph and add nodes and edges (characteristics vary if it belongs to the min_edge_dominating_set or not!)
    g = nx.Graph()
    [ g.add_node(v_id, pos=coords) for v_id, coords in vertices.items() ]
    [ g.add_edge(edge[0],edge[1],color='r',weight=1) for edge in edges if edge not in result]
    [ g.add_edge(edge[0],edge[1],color='g',weight=2) for edge in result ]

    # Create graph drawing and store it
    f = plt.figure()
    edges = g.edges()
    colors = [g[u][v]['color'] for u,v in edges]
    weights = [g[u][v]['weight'] for u,v in edges]
    nx.draw(g, nx.get_node_attributes(g, 'pos'), edge_color=colors, width=weights, with_labels=True, node_size=400)
    f.savefig(f"graphs/V{len(vertices)}_{edge_percentage}%_{p.type}.png")
    plt.close('all')


if __name__ == "__main__":
    create_graphs()