import heapq

def dijkstra(graph, start):
    distances = {v: float('inf') for v in graph}
    distances[start] = 0
    queue = [(0, start)]
    path_tree = {}

    while queue:
        current_distance, u = heapq.heappop(queue)
        if current_distance > distances[u]:
            continue
        for v, weight in graph[u].items():
            distance = current_distance + weight
            if distance < distances[v]:
                distances[v], path_tree[v] = distance, u
                heapq.heappush(queue, (distance, v))

    return distances, path_tree

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}
distances, path_tree = dijkstra(graph, 'A')
print(distances)