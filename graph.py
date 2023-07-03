# non-directed graph
class Graph:
    def __init__(self):
        self.adjacent_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacent_list:
            self.adjacent_list[vertex] = []

    def add_edge(self, v1, v2):
        if v1 in self.adjacent_list and v2 in self.adjacent_list:
            self.adjacent_list[v1].append(v2)
            self.adjacent_list[v2].append(v1)

    def display(self):
        for v in self.adjacent_list:
            neighbours = ",".join(self.adjacent_list[v])
            print(f"{v}:{neighbours}")


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
graph.display()
"""
Output: A:B,C
B:A,D
C:A,E
D:B
E:C
"""
