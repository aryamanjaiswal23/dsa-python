from collections import deque
import heapq


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        traversal = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                traversal.append(vertex)
                queue.extend(self.adjacency_list[vertex])

        return traversal

    def dfs(self, start_vertex):
        visited = set()
        stack = [start_vertex]
        traversal = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                traversal.append(vertex)
                stack.extend(self.adjacency_list[vertex])

        return traversal

    def dijkstra(self, start_vertex):
        distances = {vertex: float("inf") for vertex in self.adjacency_list}
        distances[start_vertex] = 0

        heap = [(0, start_vertex)]

        while heap:
            current_distance, current_vertex = heapq.heappop(heap)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor in self.adjacency_list[current_vertex]:
                distance = current_distance + 1  # Assuming unit weight edges
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))

        return distances


graph = Graph()

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "E")
graph.add_edge("D", "E")

bfs_traversal = graph.bfs("A")
print("BFS Traversal:", bfs_traversal)  # Output: ['A', 'B', 'C', 'D', 'E']

dfs_traversal = graph.dfs("A")
print("DFS Traversal:", dfs_traversal)  # Output: ['A', 'C', 'E', 'D', 'B']

dijkstra_distances = graph.dijkstra("A")
print(
    "Dijkstra's Distances:", dijkstra_distances
)  # Output: {'A': 0, 'B': 1, 'C': 1, 'D': 2, 'E': 2}
