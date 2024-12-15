import networkx as nx
import random
import matplotlib.pyplot as plt

class NetworkTopology:
    def __init__(self, topology_type, num_nodes):
        self.topology_type = topology_type
        self.num_nodes = num_nodes
        self.graph = self.create_topology()

    def create_topology(self):
        if self.topology_type == "linear":
            return nx.path_graph(self.num_nodes)
        elif self.topology_type == "star":
            return nx.star_graph(self.num_nodes - 1)
        elif self.topology_type == "mesh":
            return nx.complete_graph(self.num_nodes)
        elif self.topology_type == "ring":
            return nx.cycle_graph(self.num_nodes)
        elif self.topology_type == "tree":
            return nx.balanced_tree(2, int(self.num_nodes ** 0.5))  # Binary tree
        elif self.topology_type == "grid":
            side = int(self.num_nodes ** 0.5)
            return nx.grid_2d_graph(side, side)
        else:
            raise ValueError("Unsupported topology type")

    def add_random_weights(self, min_cost=1, max_cost=10):
        for u, v in self.graph.edges():
            self.graph[u][v]['weight'] = random.randint(min_cost, max_cost)
    
    def add_constant_weights(self, constant_weight):
        for u, v in self.graph.edges():
            self.graph[u][v]['weight'] = constant_weight

    def display(self):
        print(f"Topology: {self.topology_type}")
        print(f"Nodes: {list(self.graph.nodes)}")
        print(f"Edges: {list(self.graph.edges(data=True))}")

# Example usage:
# topology = NetworkTopology("mesh", 6)
# topology.add_weights()
# topology.display()
# nx.draw(topology.graph, with_labels=True, font_weight='bold')
# plt.show()