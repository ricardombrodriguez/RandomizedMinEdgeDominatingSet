import matplotlib.pyplot as plt
from math import log10

types = ["randomized","greedy","exaustive","n x 2^n"]

basic_operations = {
    "randomized" : [],
    "greedy" : [],
    "exaustive" : [],
    "n x 2^n" : []
}

tested_solutions = {
    "randomized" : [],
    "greedy" : [],
    "exaustive" : [],
    "n x 2^n" : []
}


elapsed_times = {
    "randomized" : [],
    "greedy" : [],
    "exaustive" : [],
    "n x 2^n" : []
}

solutions_length = {
    "randomized" : [],
    "greedy" : [],
    "exaustive" : [],
    "n x 2^n" : []
}

vertices = []

with open("./results.txt") as file:

    file.readline()

    for line in file:
        if not line.strip():
            continue
        line = line.rstrip().split("|")
        method = line[0].strip()
        vertexes = int(line[1].strip())
        edge_percentage = float(line[2].strip())
        basic_operation = int(line[3].strip())
        solution_length = int(line[4].strip())
        tested_solution = int(line[5].strip())
        elapsed_time = float(line[6].strip())

        if edge_percentage == 75:
            if vertexes not in vertices:
                vertices.append(vertexes) 
            basic_operations[method].append(basic_operation)
            tested_solutions[method].append(tested_solution)
            elapsed_times[method].append(elapsed_time)
            solutions_length[method].append(solution_length)

for method in types:
    len_vertices = len(vertices)
    len_elapsed = len(elapsed_times[method])
    if len(vertices) != len(elapsed_times[method]):
        missing_elements = len_vertices - len_elapsed
        basic_operations[method].extend([None for i in range(missing_elements)])
        tested_solutions[method].extend([None for i in range(missing_elements)])
        elapsed_times[method].extend([None for i in range(missing_elements)])
        solutions_length[method].extend([None for i in range(missing_elements)])

# Nx2^N
basic_operations["n x 2^n"] = [log10( 2**int(n*(n-1)/2))  for n in vertices]
tested_solutions["n x 2^n"] = [log10( 2**int(n*(n-1)/2))  for n in vertices]
elapsed_times["n x 2^n"] = [log10( 2**int(n*(n-1)/2)) for n in vertices]
solutions_length["n x 2^n"] = [log10( 2**int(n*(n-1)/2))  for n in vertices]


# elapsed times:
f1 = plt.figure()
for method in elapsed_times:
    plt.plot(vertices, elapsed_times[method], label=method)
plt.title('Elapsed times for different search methods')
plt.xlabel('Number of vertices (for 75% edge percentage)')
plt.ylabel('Elapsed time (seconds)')
plt.legend()
f1.savefig(f"elapsed_times.png")

# configurations testes:
f2 = plt.figure()
for method in tested_solutions:
    plt.plot(vertices, tested_solutions[method], label=method)
plt.title('Candidate solutions for different search methods')
plt.xlabel('Number of vertices (for 75% edge percentage)')
plt.ylabel('Number of tested configurations')
plt.legend()
f2.savefig(f"tested_solutions.png")

# elapsed times:
f3 = plt.figure()
for method in basic_operations:
    plt.plot(vertices, basic_operations[method], label=method)
plt.title('Number of basic operations for different search methods')
plt.xlabel('Number of vertices (for 75% edge percentage)')
plt.ylabel('Num. of basic operations')
plt.legend()
f3.savefig(f"basic_operations.png")