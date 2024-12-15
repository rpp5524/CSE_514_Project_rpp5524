class DistanceVectorRouting:
    def __init__(self, graph):
        self.graph = graph
        self.num_nodes = len(graph.nodes)
        self.distances = {node: {neighbor: float('inf') for neighbor in graph.nodes} for node in graph.nodes}
        for node in graph.nodes:
            self.distances[node][node] = 0
        for u, v, data in graph.edges(data=True):
            self.distances[u][v] = data['weight']
            self.distances[v][u] = data['weight']

    def bellman_ford(self, source):
        distance = {node: float('inf') for node in self.graph.nodes}
        distance[source] = 0
        for _ in range(self.num_nodes - 1):
            for u, v, data in self.graph.edges(data=True):
                if distance[u] + data['weight'] < distance[v]:
                    distance[v] = distance[u] + data['weight']
                if distance[v] + data['weight'] < distance[u]:
                    distance[u] = distance[v] + data['weight']
        return distance

    def run(self):
        results = {}
        for node in self.graph.nodes:
            results[node] = self.bellman_ford(node)
        return results

# Example usage:
# dvr = DistanceVectorRouting(topology.graph)
# result = dvr.run()
# print("Distance Vector Results:", result)
