import sys
from collections import defaultdict


MAX = 1000000


def load_graph(filename):
    """
    Assumes graph is symmetric
    """

    graph = defaultdict(list)
    with open(filename, 'r') as f:
        for line in f:
            line = line.split('\t')
            line.remove('\n')
            u = line.pop(0)
            line = list(map(lambda x: x.split(','), line))
            for v, dist in line:
                graph[u].append((int(dist), v))

    return graph


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


def dijkstra(graph, source):

    # initialize heap
    heap = MinHeap()
    for idx, vertex in enumerate(graph.keys()):
        node = [MAX, vertex]
        heap.array.append(node)
        heap.pos[vertex] = idx
    heap.size = len(heap.array)

    distances = defaultdict(lambda: MAX)
    heap.decrease_key(source, 0)
    distances[source] = 0

    while not heap.is_empty():
        min_node = heap.extract_min()
        distances[min_node[1]] = min_node[0]
        distance_neighbour = graph[min_node[1]]

        for distance, neighbour in distance_neighbour:
            if heap.is_in_heap(neighbour):
                new_distance = distances[min_node[1]] + distance
                if new_distance < distances[neighbour]:
                    distances[neighbour] = new_distance
                    heap.decrease_key(neighbour, new_distance)

    return distances


def main():
    filename = 'dijkstraData.txt'
    graph = load_graph(filename)
    source = '1'
    distances = dijkstra(graph, source)
    print(distances['7'])
    print(distances['37'])
    print(distances['59'])
    print(distances['82'])
    print(distances['99'])
    print(distances['115'])
    print(distances['133'])
    print(distances['165'])
    print(distances['188'])
    print(distances['197'])
if __name__ == '__main__':
    main()
