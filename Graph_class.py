class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, node_id, data=None):
        self.nodes[node_id] = data

    def add_edge(self, source_id, target_id, weight=1):
        self.edges.setdefault(source_id, []).append((target_id, weight))

    def __str__(self):
        return f"Nodes: {self.nodes}\nEdges: {self.edges}"

graph = Graph()
graph.add_node("A", {"name": "Alice"})
graph.add_node("B", {"name": "Bob"})
graph.add_edge("A", "B", 5)
print(graph)
