import time
import pandas as pd
from src.topology import NetworkTopology
from src.algorithms.distance_vector import DistanceVectorRouting
from src.algorithms.link_state import LinkStateRouting
from src.algorithms.path_vector import PathVectorRouting
from analysis.analyze import analyze_utilization_performance, analyze_performance_pvr

# Define the topologies and number of nodes
# TOPOLOGIES = ["linear", "star", "mesh", "ring", "grid"]
TOPOLOGIES = ["tree"]
NODE_RANGES = range(10, 110, 10)

# Initialize a list to store results
results = []

# Loop through each topology and number of nodes
for topology_type in TOPOLOGIES:
    for num_nodes in NODE_RANGES:
        print(f"Running for topology: {topology_type}, #nodes: {num_nodes}")

        # Create the topology with constant weights
        topology = NetworkTopology(topology_type, num_nodes)
        topology.add_random_weights(min_cost=1, max_cost=10)  # Random weight example

        # Initialize algorithms
        dvr = DistanceVectorRouting(topology.graph)
        lsr = LinkStateRouting(topology.graph)
        pvr = PathVectorRouting(topology.graph)

        # Distance Vector Routing
        print(f"Running Distance Vector Algorithm for {topology_type}, #nodes: {num_nodes}", end = " | ")
        start_time = time.time()
        result_dvr = dvr.run()
        end_time = time.time()
        print("Done Running", end = " | ")
        elapsed_time = end_time - start_time
        metrics = analyze_utilization_performance(topology.graph, result_dvr)
        print("Done Analyzing")
        results.append({
            "Topology": topology_type, "Number of Nodes": num_nodes, "Algorithm": "Distance Vector",
            "Latency (ms)": metrics["latency"], "Throughput (Mbps)": metrics["throughput"],
            "Routing Overhead (packets)": metrics["routing_overhead"],
            "Network Utilization (%)": metrics["network_utilization"],
            "Execution Time (s)": elapsed_time, "Weights": "random"
        })


        # Link State Routing
        print(f"Running Link State Algorithm for {topology_type}, #nodes: {num_nodes}", end = " | ")
        start_time = time.time()
        result_lsr = lsr.run()
        end_time = time.time()
        print("Done Running", end = " | ")
        elapsed_time = end_time - start_time
        metrics = analyze_utilization_performance(topology.graph, result_lsr)
        print("Done Analyzing")
        results.append({
            "Topology": topology_type, "Number of Nodes": num_nodes, "Algorithm": "Link State",
            "Latency (ms)": metrics["latency"], "Throughput (Mbps)": metrics["throughput"],
            "Routing Overhead (packets)": metrics["routing_overhead"],
            "Network Utilization (%)": metrics["network_utilization"],
            "Execution Time (s)": elapsed_time, "Weights": "random"
        })

        # Path Vector Routing
        print(f"Running Path Vector Algorithm for {topology_type}, nodes: {num_nodes}", end = " | ")
        start_time = time.time()
        result_pvr = pvr.run()
        end_time = time.time()
        print("Done Running", end = " | ")
        elapsed_time = end_time - start_time
        metrics = analyze_performance_pvr(topology.graph, result_pvr)
        print("Done Analyzing")
        results.append({
            "Topology": topology_type, "Number of Nodes": num_nodes, "Algorithm": "Path Vector",
            "Latency (ms)": metrics["latency"], "Throughput (Mbps)": metrics["throughput"],
            "Routing Overhead (packets)": metrics["routing_overhead"],
            "Network Utilization (%)": metrics["network_utilization"],
            "Execution Time (s)": elapsed_time, "Weights": "random"
        })

        print("------------------------------------------------------------------------------------")

        # # Optionally: Use random weights for additional testing
        # topology.add_weights(min_cost=1, max_cost=10)  # Random weights example

        # # Distance Vector Routing with random weights
        # start_time = time.time()
        # result_dvr = dvr.run()
        # end_time = time.time()
        # elapsed_time = end_time - start_time
        # metrics = analyze_performance(topology.graph, result_dvr)
        # results.append({
        #     "Topology": topology_type, "Number of Nodes": num_nodes, "Algorithm": "Distance Vector",
        #     "Latency (ms)": metrics["latency (ms)"], "Throughput (Mbps)": metrics["throughput (Mbps)"],
        #     "Routing Overhead (packets)": metrics["routing_overhead (packets)"],
        #     "Network Utilization (%)": metrics["network_utilization (%)"],
        #     "Execution Time (s)": elapsed_time, "Weights": "random"
        # })

        # # Link State Routing with random weights
        # start_time = time.time()
        # result_lsr = lsr.run()
        # end_time = time.time()
        # elapsed_time = end_time - start_time
        # metrics = analyze_performance(topology.graph, result_lsr)
        # results.append({
        #     "Topology": topology_type, "Number of Nodes": num_nodes, "Algorithm": "Link State",
        #     "Latency (ms)": metrics["latency (ms)"], "Throughput (Mbps)": metrics["throughput (Mbps)"],
        #     "Routing Overhead (packets)": metrics["routing_overhead (packets)"],
        #     "Network Utilization (%)": metrics["network_utilization (%)"],
        #     "Execution Time (s)": elapsed_time, "Weights": "random"
        # })

        # # Path Vector Routing with random weights
        # start_time = time.time()
        # result_pvr = pvr.run()
        # end_time = time.time()
        # elapsed_time = end_time - start_time
        # metrics = analyze_performance(topology.graph, result_pvr)
        # results.append({
        #     "Topology": topology_type, "Number of Nodes": num_nodes, "Algorithm": "Path Vector",
        #     "Latency (ms)": metrics["latency (ms)"], "Throughput (Mbps)": metrics["throughput (Mbps)"],
        #     "Routing Overhead (packets)": metrics["routing_overhead (packets)"],
        #     "Network Utilization (%)": metrics["network_utilization (%)"],
        #     "Execution Time (s)": elapsed_time, "Weights": "random"
        # })

# Convert results to a DataFrame and save to CSV
results_df = pd.DataFrame(results)
results_df.to_csv("./routing_data/routing_algorithm_results_random_weights_tree.csv", index=False)

print("Simulation complete. Results saved to routing_algorithm_results.csv")
