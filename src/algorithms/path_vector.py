class PathVectorRouting:
    def __init__(self, graph):
        self.graph = graph

    def path_vector(self, source):
        paths = {node: [] for node in self.graph.nodes}
        paths[source] = [source]
        distance = {node: float('inf') for node in self.graph.nodes}
        distance[source] = 0
        for _ in range(len(self.graph.nodes) - 1):
            for u, v, data in self.graph.edges(data=True):
                if distance[u] + data['weight'] < distance[v]:
                    distance[v] = distance[u] + data['weight']
                    paths[v] = paths[u] + [v]
                if distance[v] + data['weight'] < distance[u]:
                    distance[u] = distance[v] + data['weight']
                    paths[u] = paths[v] + [u]
        return distance, paths

    def run(self):
        results = {}
        for node in self.graph.nodes:
            results[node] = self.path_vector(node)
        return results

# Example usage:
# pvr = PathVectorRouting(topology.graph)
# result = pvr.run()
# print("Path Vector Results:", result)
