class LinkStateRouting:
    def __init__(self, graph):
        self.graph = graph

    def dijkstra(self, source):
        unvisited = set(self.graph.nodes)
        distance = {node: float('inf') for node in self.graph.nodes}
        distance[source] = 0
        while unvisited:
            current_node = min(unvisited, key=lambda node: distance[node])
            unvisited.remove(current_node)
            for neighbor in self.graph.neighbors(current_node):
                weight = self.graph[current_node][neighbor]['weight']
                if distance[current_node] + weight < distance[neighbor]:
                    distance[neighbor] = distance[current_node] + weight
        return distance

    def run(self):
        results = {}
        for node in self.graph.nodes:
            results[node] = self.dijkstra(node)
        return results

# Example usage:
# lsr = LinkStateRouting(topology.graph)
# result = lsr.run()
# print("Link State Results:", result)
