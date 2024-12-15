def analyze_performance(graph, results):
    metrics = {
        "latency": [],
        "throughput": [],
        "routing_overhead": 0
    }
    for source, distances in results.items():
        total_distance = sum(distances.values())
        metrics['latency'].append(total_distance / len(distances))
    metrics['routing_overhead'] = len(graph.edges) * 2  # Example overhead calculation
    print("Performance Metrics:", metrics)


def analyze_complex_performance(graph, results, packets_per_second=100, packet_size=1000):
    """
    Analyze network performance for metrics like latency, throughput, and routing overhead.

    :param graph: NetworkX graph with weighted edges.
    :param results: Routing results (shortest paths or distance metrics).
    :param packets_per_second: Number of packets sent per second.
    :param packet_size: Size of each packet in bytes.
    """
    metrics = {
        "latency": [],
        "throughput": 0,
        "routing_overhead": 0
    }

    total_data_transferred = 0  # in bytes
    total_time = 0  # in seconds

    for source, distances in results.items():
        for destination, distance in distances.items():
            if source != destination:
                # Transmission time (data size / link bandwidth)
                link_bandwidth = 100e6  # 100 Mbps default (example)
                transmission_time = (packet_size * 8) / link_bandwidth  # seconds

                # Propagation delay based on "distance"
                propagation_delay = distance * 0.01  # Example: 10 ms per unit distance

                # Total time per packet
                total_time_per_packet = transmission_time + propagation_delay

                # Update total time and data transferred
                total_time += total_time_per_packet * packets_per_second
                total_data_transferred += packets_per_second * packet_size

    # Calculate throughput in Mbps
    if total_time > 0:
        metrics['throughput'] = (total_data_transferred * 8) / (total_time * 1e6)  # Mbps

    # Routing overhead (example calculation)
    metrics['routing_overhead'] = len(graph.edges) * 2  # Example: twice the number of edges

    # Example Latency Calculation (average distance)
    avg_latency = sum(sum(distances.values()) for distances in results.values()) / (len(graph.nodes) ** 2)
    metrics['latency'] = avg_latency

    print("Performance Metrics:", metrics)

def analyze_utilization_performance(graph, results, packets_per_second=100, packet_size=1000):
    """
    Analyze network performance for metrics like latency, throughput, routing overhead, and network utilization.

    :param graph: NetworkX graph with weighted edges.
    :param results: Routing results (shortest paths or distance metrics).
    :param packets_per_second: Number of packets sent per second.
    :param packet_size: Size of each packet in bytes.
    """
    metrics = {
        "latency": [],
        "throughput": 0,
        "routing_overhead": 0,
        "network_utilization": 0
    }

    total_data_transferred = 0  # in bytes
    total_time = 0  # in seconds
    total_available_bandwidth = 0  # in bps

    for u, v, data in graph.edges(data=True):
        # Assume a default bandwidth for each link (e.g., 100 Mbps)
        bandwidth = data.get('bandwidth', 100e6)  # Default 100 Mbps
        total_available_bandwidth += bandwidth

    for source, distances in results.items():
        for destination, distance in distances.items():
            if source != destination:
                # Transmission time (data size / link bandwidth)
                link_bandwidth = 100e6  # 100 Mbps default (example)
                transmission_time = (packet_size * 8) / link_bandwidth  # seconds

                # Propagation delay based on "distance"
                propagation_delay = distance * 0.01  # Example: 10 ms per unit distance

                # Total time per packet
                total_time_per_packet = transmission_time + propagation_delay

                # Update total time and data transferred
                total_time += total_time_per_packet * packets_per_second
                total_data_transferred += packets_per_second * packet_size * distance  # Data * number of hops

    # Calculate throughput in Mbps
    if total_time > 0:
        metrics['throughput'] = (total_data_transferred * 8) / (total_time * 1e6)  # Mbps

    # Calculate network utilization
    if total_available_bandwidth > 0:
        metrics['network_utilization'] = (total_data_transferred * 8) / total_available_bandwidth  # Ratio

    # Routing overhead (example calculation)
    metrics['routing_overhead'] = len(graph.edges) * 2  # Example: twice the number of edges

    # Example Latency Calculation (average distance)
    avg_latency = sum(sum(distances.values()) for distances in results.values()) / (len(graph.nodes) ** 2)
    metrics['latency'] = avg_latency

    print("Performance Metrics:", metrics)


def analyze_performance_pvr(graph, pvr_results, packets_per_second=100, packet_size=1000):
    """
    Analyze network performance for Path Vector Routing (PVR) results.
    
    :param graph: NetworkX graph with weighted edges.
    :param pvr_results: Results from the Path Vector Routing algorithm.
        Format: {node: (distance_dict, path_dict)}
    :param packets_per_second: Number of packets sent per second (default: 100).
    :param packet_size: Size of each packet in bytes (default: 1000 bytes).
    :return: Dictionary of performance metrics.
    """
    metrics = {
        "latency": 0,
        "throughput": 0,
        "routing_overhead)": 0,
        "network_utilization": 0
    }
    
    total_latency = 0
    total_data_transferred = 0  # In bytes
    total_time = 0  # In seconds
    total_available_bandwidth = 0  # In bps

    num_node_pairs = 0

    # Calculate total available bandwidth
    for u, v, data in graph.edges(data=True):
        # Assume default bandwidth of 100 Mbps if not provided
        bandwidth = data.get('bandwidth', 100e6)  # Default bandwidth in bps
        total_available_bandwidth += bandwidth

    # Process PVR results for performance metrics
    for source, (distances, paths) in pvr_results.items():
        for destination, distance in distances.items():
            if source != destination:
                num_node_pairs += 1
                # Accumulate latency (sum of distances)
                total_latency += distance

                # Transmission time
                link_bandwidth = 100e6  # Assume 100 Mbps for simplicity
                transmission_time = (packet_size * 8) / link_bandwidth  # seconds

                # Propagation delay based on distance
                propagation_delay = distance * 0.01  # Example: 10 ms per unit distance

                # Total time per packet
                total_time_per_packet = transmission_time + propagation_delay

                # Update total time and data transferred
                total_time += total_time_per_packet * packets_per_second
                total_data_transferred += packets_per_second * packet_size

    # Calculate latency (average)
    if num_node_pairs > 0:
        metrics["latency"] = (total_latency / num_node_pairs) * 10  # Convert to ms

    # Calculate throughput (in Mbps)
    if total_time > 0:
        metrics["throughput"] = (total_data_transferred * 8) / (total_time * 1e6)  # Mbps

    # Calculate network utilization (%)
    if total_available_bandwidth > 0:
        metrics["network_utilization"] = ((total_data_transferred * 8) / total_available_bandwidth) * 100  # Percentage

    # Calculate routing overhead (packets)
    num_nodes = len(graph.nodes)
    num_edges = len(graph.edges)
    # Assume routing overhead as the number of messages exchanged to build routing tables
    metrics["routing_overhead"] = num_nodes * num_edges * 2  # Example assumption

    # Return metrics
    print("Performance Metrics:", metrics)

