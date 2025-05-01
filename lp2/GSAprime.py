import heapq

def prim_mst(graph, start):
    visited = set()
    min_heap = [(0, start)]  
    mst_cost = 0
    mst_edges = []

    while min_heap:
        cost, u = heapq.heappop(min_heap)
        if u not in visited:
            visited.add(u)
            mst_cost += cost

            if cost != 0:
                mst_edges.append((u, cost))

            for v, weight in graph[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (weight, v))

    print("Minimum Spanning Tree edges and their weights:")
    for edge in mst_edges:
        print(f"{edge[0]} - weight: {edge[1]}")
    print("Total cost of MST:", mst_cost)

graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

print("Prim's Algorithm - MST from starting node A:")
prim_mst(graph, 'A')
