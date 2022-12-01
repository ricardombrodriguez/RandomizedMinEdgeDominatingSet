# MinEdgeDominatingSet

Advanced Algorithms (AA) first project.

## Introduction

Design and test an exhaustive search algorithm to solve one of the following graph problems, as well as another method using a greedy heuristics.

Afterwards, analyze the computational complexity of the developed algorithms. To accomplish that:
- Perform a formal computational complexity analysis of the algorithms.
- Carry out a sequence of experiments, for successively larger problem instances, to register and analyze (1) the number of basic operations carried out, (2) the execution time and (3) the number of solutions / configurations tested.
- Compare the results of the experimental and the formal analysis.
- Determine the largest graph that you can process on your computer, without taking too much
time.
- Estimate the execution time that would be required by much larger problem instances.
- Write a report (8 pages, max.). 

## Graphs for the Computational Experiments
The graph instances used in the computational experiments should represent the following scenario:
- graph vertices are 2D points on the XOY plane, with integer valued coordinates between 1 and 20 (could be bigger if vertices don't fit the canvas).
- graph vertices should neither be coincident nor too close.
- the number of edges sharing a vertex is randomly determined.

Generate successively larger random graphs, with 4, 5, 6, … vertices, using your student number as seed.
Use 12.5%, 25%, 50% and 75% of the maximum number of edges for the number of vertices.

## My Problem

Find a minimum edge dominating set for a given undirected graph G(V, E), with n vertices and m edges. An edge dominating set of G is a subset D of edges, such that every edge not in D is adjacent to, at least, one edge in D. A minimum edge dominating set is an edge dominating set of smallest possible size.

## Results

Methodologies and results are described in the project report.