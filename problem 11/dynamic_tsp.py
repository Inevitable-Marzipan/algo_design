from collections import namedtuple
from itertools import combinations

Vertex = namedtuple('Vertex', ['x', 'y'])

def load_file(filename):

    vertices = []

    with open(filename, 'r') as f:
        for line_num, line in enumerate(f):
            if line_num == 0:
                n = int(line.strip())
                continue
            x, y = map(float, line.strip().split(' '))
            # rename vertices so they are 0 indexed
            vertex = Vertex(x, y)
            vertices.append(vertex)

    assert len(vertices) == n
    
    return vertices

def euclidian_distance(v1, v2):
    return ((v1.x - v2.x) ** 2 + (v1.y - v2.y) ** 2) ** (1/2)

def tsp(vertices):
    n = len(vertices)
    v0 = 0
    dists = [[euclidian_distance(x, y) for x in vertices] for y in vertices]

    #initialize values, use first vertex (zero index) as source
    # c indexed by set of vertices included and last vertex tuple
    c = dict()
    for i in range(1, n):
        S = frozenset([v0, i])
        c[(S, i)] = (euclidian_distance(vertices[v0], vertices[i]), [v0, i])
    

    for num_vertices in range(2, n):
        print(num_vertices)
        c_prime = dict()
        Ss = [frozenset(s | {v0}) for s in list(map(set,combinations(range(1, n), num_vertices)))]
        for S in Ss:
            for v1 in S - {v0}:
                c_prime[(S, v1)] = min([(c[(S - {v1}, v2)][0] + dists[v1][v2], c[(S - {v1}, v2)][1] + [v1])
                                           for v2 in S
                                           if (v2 != v0) & (v2 != v1) ])
        c = c_prime
    
    all_vertices = frozenset(range(len(vertices)))
    min_tsp = min([(c[all_vertices, v][0] + dists[v][v0], c[all_vertices, v][1] + [v0]) for v in range(num_vertices) if v != v0])
    return min_tsp


def main():
    filename = 'tsp.txt'
    vertices = load_file(filename)
    dist, path  = tsp(vertices)
    print(dist)
    print(path)




if __name__ == '__main__':
    main()
