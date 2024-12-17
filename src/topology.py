import networkx as nx
import random
import matplotlib.pyplot as plt
import math

class NetworkTopology:
    def __init__(self, topology_type, num_nodes):
        self.topology_type = topology_type
        self.num_nodes = num_nodes
        self.graph = self.create_topology()
        self.positions = None  # For geographic positioning if needed

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

    def add_realistic_weights(self, max_coord=100):
        """
        Add weights based on a combination of geographic distance, congestion, and bandwidth.
        """
        # Assign random positions to nodes
        self.positions = {node: (random.randint(0, max_coord), random.randint(0, max_coord)) for node in self.graph.nodes()}
        
        for u, v in self.graph.edges():
            # Calculate geographic distance
            x1, y1 = self.positions[u]
            x2, y2 = self.positions[v]
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            # Add congestion and bandwidth factors
            bandwidth = random.choice([50, 100, 500])  # Mbps
            congestion = random.uniform(1, 3)  # Congestion factor multiplier
            
            # Weight formula: distance + (congestion / bandwidth)
            weight = distance + (congestion / bandwidth)
            self.graph[u][v]['weight'] = round(weight, 2)

    def display(self):
        print(f"Topology: {self.topology_type}")
        print(f"Nodes: {list(self.graph.nodes)}")
        print(f"Edges: {list(self.graph.edges(data=True))}")

    def draw_topology(self):
        """
        Draw the graph with weights.
        """
        pos = self.positions if self.positions else nx.spring_layout(self.graph)  # Use assigned positions if available
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw(self.graph, pos, with_labels=True, node_size=500, node_color='lightblue')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)

# Example usage:
# topology = NetworkTopology("mesh", 6)
# topology.add_weights()
# topology.display()
# nx.draw(topology.graph, with_labels=True, font_weight='bold')
# plt.show()