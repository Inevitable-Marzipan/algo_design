class UnionFind:
    def __init__(self):
        self.parents = dict()
        self.ranks = dict()
        self.vertices = set()
        self.size = 0

    def add_vertex(self, vertex):
        self.vertices.add(vertex)
        self.parents[vertex] = vertex
        self.ranks[vertex] = 0
        self.size += 1

    def path_compress_find(self, vertex):
        if vertex == '361':
            #breakpoint()
            pass
        parent = self.parents[vertex]
        if parent == vertex:
            return vertex

        vertices_to_compress = [vertex]

        def find(v):

            parent = self.parents[v]
            if parent == v:
                return parent
            else:
                vertices_to_compress.append(v)
                root = find(parent)
            return root

        if self.parents[parent] == parent:
            return parent
        else:
            root = find(parent)

        for v in vertices_to_compress:
            if v == '361':
                #breakpoint()
                pass
            self.parents[v] = root

        return root

    def union(self, v1, v2):
        root1 = self.path_compress_find(v1)
        root2 = self.path_compress_find(v2)
        rank1 = self.ranks[root1]
        rank2 = self.ranks[root2]

        if rank1 > rank2:
            if root2 == '361':
                #breakpoint()
                pass
            self.parents[root2] = root1
        elif rank2 > rank1:
            if root1 == '361':
                #breakpoint()
                pass
            self.parents[root1] = root2
        else:
            if root2 == '361':
                #breakpoint()
                pass
            self.parents[root2] = root1
            self.ranks[root1] += 1
