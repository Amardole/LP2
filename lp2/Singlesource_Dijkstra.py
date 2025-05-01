
INF = 999999

def dijkstra(graph, start):
    n = len(graph)
    visited = [False] * n
    distance = [INF] * n
    distance[start] = 0

    for _ in range(n):
        min_dist = INF
        u = -1
        for i in range(n):
            if not visited[i] and distance[i] < min_dist:
                min_dist = distance[i]
                u = i

        visited[u] = True

        for v in range(n):
            if graph[u][v] and not visited[v]:
                if distance[v] > distance[u] + graph[u][v]:
                    distance[v] = distance[u] + graph[u][v]

    print("Vertex \t Distance from Source")
    for i in range(n):
        print(f"{i} \t {distance[i]}")

graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

dijkstra(graph, 0)
