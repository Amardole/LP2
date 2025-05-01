from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def dfs(graph, vertex, visited):
    if vertex not in visited:
        print(vertex, end=' ')
        visited.add(vertex)
        for neighbor in graph[vertex]:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            queue.extend(graph[vertex])

print("DFS Traversal starting from vertex A:")
dfs(graph, 'A', set())

print("\n\nBFS Traversal starting from vertex A:")
bfs(graph, 'A')
