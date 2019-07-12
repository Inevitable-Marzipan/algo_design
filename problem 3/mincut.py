import random
import copy

random.seed(20)

def load_graph_file(filename):
    graph = dict()

    with open(filename, 'r') as f:
        for line in f:
            line = line.split('\t')
            line.remove('\n')
            line = [int(val) for val in line]
            vertex = line[0]
            graph[vertex] = list(set(line[1:]))

    return graph


cuts = []
def karger_min_cut(graph):
    graph = copy.deepcopy(graph)
    
    while(len(graph) > 2):
        u = random.choice(list(graph.keys()))
        v = random.choice(list(graph[u]))

        contract(graph, u, v)
    mincut = len(graph[list(graph.keys())[0]])
    cuts.append(mincut)
    print(graph)
    return graph


def contract(graph, u, v):
    for node in graph[v]:
        if node != u:
            graph[u].append(node)
        graph[node].remove(v)
        if node != u:
            graph[node].append(u)
    del graph[v]


def Main():
    filename = 'kargerMinCut.txt'
    graph = load_graph_file(filename)
    for _ in range(1):
        karger_min_cut(graph)
    print(min(cuts))

if __name__ == '__main__':
    Main()