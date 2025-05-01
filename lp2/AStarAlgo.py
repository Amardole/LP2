import heapq
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2)],
    'E': [('B', 5), ('G', 1)],
    'F': [('C', 3)],
    'G': [('E', 1)]
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 2,
    'F': 6,
    'G': 0
}

def a_star_search(start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic[start], 0, start, [start]))  
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            print(f"Path found: {' -> '.join(path)} with cost: {g}")
            return

        if current in visited:
            continue

        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                total_cost = g + cost
                estimated_cost = total_cost + heuristic[neighbor]
                heapq.heappush(open_list, (estimated_cost, total_cost, neighbor, path + [neighbor]))

    print("No path found.")

start_node = 'A'
goal_node = 'G'

print(f"A* Search from {start_node} to {goal_node}:")
a_star_search(start_node, goal_node)
