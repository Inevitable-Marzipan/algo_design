from collections import defaultdict
import copy


def load_graph_file(filename):
    connections = []
    with open(filename, 'r') as f:
        for line in f:
            u, v = line.strip().split(' ')
            connections.append((u, v))
    
    return connections

def create_graph(connections):
    graph = defaultdict(set)
    vertices = set()
    for connection in connections:
        u, v = connection
        graph[u].add(v)
        vertices.add(u)
        vertices.add(v)
    
    for vertex in list(vertices):
        if len(graph[vertex]) == 0:
            graph[vertex] = set()
    
    return graph

def reverse_graph(graph):
    new_graph = defaultdict(set)
    vertices = set()
    for u, vs in graph.items():
        for v in vs:
            new_graph[v].add(u)
            vertices.add(u)
            vertices.add(v)
    
    for vertex in list(vertices):
        if len(new_graph[vertex]) == 0:
            new_graph[vertex] = set()
    return new_graph


def dfs(graph, vertex, visited):
    visited_vertices = []
    stack = [vertex]

    while (len(stack)):
        working_vertex = stack[-1]
        
        has_unexplored_neighbours = False
        for neighbour in graph[working_vertex]:
            if neighbour not in visited:
                has_unexplored_neighbours = True
                stack.append(neighbour)
                visited.add(neighbour)
        
        if not has_unexplored_neighbours:
            adding = stack.pop()
            visited_vertices.append(adding)
    
    return visited_vertices

def dfs_orders(graph):
    """
    Runs dfs over vertices in the graph in a loop
    such that dfs is run on all vertices.

    Returns an ordered list of vertices corresponding to
    their finish times
    """

    stack = []
    visited = set()
    for vertex in graph.keys():
        if vertex not in visited:
            visited.add(vertex)
            visited_vertices = dfs(graph, vertex, visited)
            stack += visited_vertices

    return stack


def kosaraju(graph):
    """
    Takes in a directed graph object
    and returns a dictionary of strongly connected components
    """
    reversed_graph = reverse_graph(graph)
    stack_orders = dfs_orders(reversed_graph)

    counter = 0
    visited = set()
    scc_dict = dict()
    for vertex in reversed(stack_orders):
        if vertex not in visited:
            visited.add(vertex)
            nodes = dfs(graph, vertex, visited)
            scc_dict[counter] = nodes
            counter += 1

    return scc_dict

def main():
    filename = 'SCC.txt'
    connections = load_graph_file(filename)
      
    graph = create_graph(connections)
    sccs = kosaraju(graph)
    
    scc_sizes = sccs.values()
    vals = sorted(map(len, scc_sizes), reverse=True)
    print(vals[:10])

if __name__ == '__main__':
    main()