import sys
from collections import defaultdict


def load_graph(filename):

    graph = defaultdict(list)
    with open(filename, 'r') as f:
        for line_num, line in enumerate(f):
            if line_num == 0:
                num_nodes, num_edges = list(map(int, str.strip(line).split(' ')))
                continue
            line = str.strip(line).split(' ')
            u, v, dist = line
            graph[u].append((v, int(dist)))
            graph[v].append((u, int(dist)))
    return num_nodes, num_edges, graph


class MinHeap:

    def __init__(self):
        self.array = []
        self.pos = {}
        self.size = 0

    def parent(self, idx):
        return (idx - 1) // 2

    def children(self, idx):
        left_idx = (idx * 2) + 1
        right_idx = (idx * 2) + 2
        return (left_idx, right_idx)

    def get_min_child(self, node):
        left_idx, right_idx = self.children(node)
        possible_children = []
        for child in [left_idx, right_idx]:
            if child < self.size:
                possible_children.append(child)
        if len(possible_children) == 0:
            return None
        else:
            return min(possible_children, key=(lambda x: self.array[x][0]))

    def exchange(self, idx1, idx2):

        v1 = self.array[idx1][1]
        v2 = self.array[idx2][1]
        # Switch in array
        t = self.array[idx1]
        self.array[idx1] = self.array[idx2]
        self.array[idx2] = t

        # switch in position
        self.pos[v1] = idx2
        self.pos[v2] = idx1

    def extract_min(self):

        if self.size == 0:
            return

        min_node = self.array[0]
        self.exchange(0, self.size - 1)
        self.size -= 1
        p = 0
        while p < self.size:
            curr_key = self.array[p][0]

            min_child_idx = self.get_min_child(p)
            if min_child_idx is None:
                break
            min_child_node = self.array[min_child_idx]

            if min_child_node[0] >= curr_key:
                break
            else:
                self.exchange(min_child_idx, p)
                p = min_child_idx

        return min_node

    def decrease_key(self, v, new_key):
        idx = self.pos[v]
        self.array[idx][0] = new_key

        while idx > 0:
            curr_key = self.array[idx][0]
            parent_idx = self.parent(idx)
            parent_key = self.array[parent_idx][0]

            if curr_key >= parent_key:
                break
            else:
                self.exchange(idx, parent_idx)
                idx = parent_idx

    def is_in_heap(self, v):
        pos = self.pos[v]
        if pos < self.size:
            return True
        else:
            return False

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False


def prims_minimum_spanning(graph):

    heap = MinHeap()
    for idx, vertex in enumerate(graph.keys()):
        node = [sys.maxsize, vertex]
        heap.array.append(node)
        heap.pos[vertex] = idx
    heap.size = len(heap.array)

    source = list(graph.keys())[0]
    heap.decrease_key(source, 0)

    tree_edges = []
    while not heap.is_empty():
        min_node = heap.extract_min()
        distance, first_vertex = min_node
        if first_vertex != source:
            other_vertex = [vertex for vertex, dist in graph[first_vertex]
                            if ((dist == distance) & (not heap.is_in_heap(vertex)))][0]
            tree_edges.append((first_vertex, other_vertex))
        neighbours = graph[min_node[1]]
        for neighbour, distance in neighbours:
            if heap.is_in_heap(neighbour):
                curr_distance = heap.array[heap.pos[neighbour]][0]
                if distance < curr_distance:
                    heap.decrease_key(neighbour, distance)

    return tree_edges


def calculate_tree_cost(graph, edges):
    cost = 0
    for edge in edges:
        first_vertex, second_vertex = edge
        edge_weight = [weight for vertex, weight in graph[first_vertex] if vertex == second_vertex][0]
        cost += edge_weight
    return cost


def main():
    filename = 'edges.txt'
    _, _, graph = load_graph(filename)
    edges = prims_minimum_spanning(graph)
    cost = calculate_tree_cost(graph, edges)
    print(cost)

if __name__ == '__main__':
    main()
