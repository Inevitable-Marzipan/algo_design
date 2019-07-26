import sys
from collections import defaultdict, namedtuple
from unionfind import UnionFind
Edge = namedtuple('Edge', ['u', 'v', 'dist'])


def load_graph(filename):

    edges = []
    vertices = set()
    with open(filename, 'r') as f:
        for line_num, line in enumerate(f):
            if line_num == 0:
                num_vertices = int(str.strip(line))
                continue
            line = str.strip(line).split(' ')
            u, v, dist = line
            edge = Edge(u, v, int(dist))
            edges.append(edge)
            vertices.add(u)
            vertices.add(v)
    assert len(vertices) == num_vertices

    return edges, vertices


def max_space_clustering(edges, vertices, clusters):
    union_find = UnionFind()
    for vertex in vertices:
        union_find.add_vertex(vertex)
    edges = sorted(edges, key=(lambda x: x.dist))

    e = 0
    for edge in edges:
        rootu = union_find.path_compress_find(edge.u)
        rootv = union_find.path_compress_find(edge.v)

        if e == len(vertices) - clusters:
            if rootu != rootv:
                max_spacing = edge.dist
                break
            else:
                continue

        if rootu == rootv:
            continue
        else:
            union_find.union(edge.u, edge.v)
            e += 1

    root_parents = dict()
    for vertex in list(vertices):
        root_parents[vertex] = union_find.path_compress_find(vertex)

    return root_parents, max_spacing


def main():
    filename = 'clustering1.txt'
    edges, vertices = load_graph(filename)
    clusters = 4
    root_parents, max_spacing = max_space_clustering(edges, vertices, clusters)
    roots = set(root_parents.values())
    print(roots)
    print(max_spacing)

if __name__ == '__main__':
    main()
