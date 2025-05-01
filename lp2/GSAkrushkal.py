
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u
            return True
        return False

def kruskal(graph_edges, vertices):
    ds = DisjointSet(vertices)
    mst = []
    total_cost = 0

    graph_edges.sort(key=lambda x: x[2])

    for u, v, weight in graph_edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

    print("Minimum Spanning Tree edges and weights:")
    for u, v, w in mst:
        print(f"{u} - {v} : {w}")
    print("Total cost of MST:", total_cost)

edges = [
    ('A', 'B', 2),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 1),
    ('C', 'D', 4)
]

vertices = ['A', 'B', 'C', 'D']

print("Kruskal's Algorithm - MST:")
kruskal(edges, vertices)
