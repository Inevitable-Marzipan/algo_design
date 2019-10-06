import argparse
from collections import namedtuple
from math import inf

parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str,
                    help='input file')

args = parser.parse_args()

Edge = namedtuple('Edge', ['source', 'target', 'weight'])

def read_file(filename):
    edges = []

    with open(filename, 'r') as f:
        for line_num, line in enumerate(f):
            if line_num == 0:
                n, m = map(int, line.strip().split(' '))
                continue
            source, target, weight = map(int, line.strip().split(' '))
            # rename vertices so they are 0 indexed
            source -= 1
            target -= 1
            edge = Edge(source, target, weight)
            edges.append(edge)
    
    return n, m, edges


def floyd_warshall(n, edges):
    # initialize distance matrix
    distances = [[0 if i == j else inf for j in range(n)] for i in range(n)]
    for edge in edges:
        source, target, weight = edge
        distances[source][target] = min(distances[source][target], weight)
    

    # Run algorithm
    for v in range(n):
        if v % 10 == 0:
            print(v)
        prev_distances = distances
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(prev_distances[i][j],
                                      prev_distances[i][v] + prev_distances[v][j])



    return distances

def main():
     filename = args.filename
     n, m, edges = read_file(filename)
     distances = floyd_warshall(n, edges)

     neg_cost_cycle = False
     min_val = inf
     for i in range(n):
         for j in range(n):
             if distances[i][j] < min_val:
                 min_val = distances[i][j]
             if (i == j) and distances[i][j] < 0:
                 neg_cost_cycle = True
    
     print('Negative cost cycle exists:', neg_cost_cycle)
     print('Minimum distance:', min_val)


if __name__ == '__main__':
    main()

# g1 has negative cost cycle