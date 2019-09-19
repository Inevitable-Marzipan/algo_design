from unionfind import UnionFind

def load_graph(filename):
    with open(filename, 'r') as f:
        graph_nodes = set()

        for line_num, line in enumerate(f):
            if line_num == 0:
                parsed_line = (line).split()
                num_nodes, len_code = map(int, parsed_line)
            else:
                digits = line.strip().split()
                digits = ''.join(digits)
                graph_nodes.add(digits)
    
    return num_nodes, len_code, graph_nodes

def generate_neighbours(code):
    neighbours = set()
    for split in range(len(code)):
        pre = code[:split]
        post = code[split + 1:]
        swap = code[split]
        if swap == '1':
            swapped = '0'
        elif swap == '0':
            swapped = '1'
        else:
            raise ValueError(f'Unexpected token {swap}')
        new_neighbour = pre + swapped + post
        neighbours.add(new_neighbour)
    
    return neighbours

def generate_second_neighbours(code):
    neighbours = set()
    for split in range(len(code)):
        pre = code[:split]
        swap = code[split]
        if swap == '1':
            swapped = '0'
        elif swap == '0':
            swapped = '1'
        else:
            raise ValueError(f'Unexpected value {swap} \
                               only expecting 0s or 1s')
        post = code[split + 1:]
        new_neighbour = pre + swapped + post
        neighbours.add(new_neighbour)
        post_neighbours = generate_neighbours(post)

        for post_neighbour in list(post_neighbours):
            new_neighbour = pre + swapped + post_neighbour
            neighbours.add(new_neighbour)

    return neighbours

def get_clusters_two_spaces(graph_nodes):
    union_find = UnionFind()
    for vertex in list(graph_nodes):
        union_find.add_vertex(vertex)
    clusters = len(graph_nodes)
    for u in list(graph_nodes):   

        u_neighbours = set(generate_neighbours(u))
        u_second_neighbours = set()
        u_second_neighbours = u_second_neighbours.union(u_neighbours)
        for neighbour in u_neighbours:
            next_neighbours = generate_neighbours(neighbour)
            u_second_neighbours = u_second_neighbours.union(next_neighbours)

        #u_second_neighbours = generate_second_neighbours(u)

        actual_neighbours = set(u_second_neighbours).intersection(graph_nodes)
        
        
        for v in actual_neighbours:
            if u == v:
                continue
            root_u = union_find.path_compress_find(u)
            root_v = union_find.path_compress_find(v)
            if root_u == root_v:
                continue
            else:
                clusters -= 1
                union_find.union(root_u, root_v)
    
    return union_find, clusters


def main():
    filename = 'clustering_big.txt'
    num_nodes, len_code, graph_nodes = load_graph(filename)
    print(num_nodes, len_code)
    #graph_nodes = ['1010', '0101', '1100', '1001']
    uf, clusters = get_clusters_two_spaces(graph_nodes)
    print(clusters)
    
    


if __name__ == '__main__':
    main()