# CSE_514_rpp5524
This is a github repository for CSE 514 Computer Networks Final Project for Fall 2024
- Name: Rohan Prasad
- PSU ID: 980707395
- PSU email: rpp5524@psu.edu

# Routing Algorithms Simulation

## Overview

This project simulates various routing algorithms for the CSE 514 Final Project, focusing on implementation, optimization and comparing the efficiency and accuracy of algorithms like Dijkstra's, Bellman-Ford, and A* in different network scenarios.

## Structure
```
.
├── README.md
├── analysis
│   ├── __pycache__
│   │   └── analyze.cpython-311.pyc
│   └── analyze.py
├── main.py
├── src
│   ├── __pycache__
│   │   └── topology.cpython-311.pyc
│   ├── algorithms
│   │   ├── __pycache__
│   │   │   ├── distance_vector.cpython-311.pyc
│   │   │   ├── link_state.cpython-311.pyc
│   │   │   └── path_vector.cpython-311.pyc
│   │   ├── distance_vector.py
│   │   ├── link_state.py
│   │   └── path_vector.py
└──-└── topology.py
```

## Base Algorithms
- **Distance Vector Algorithm**: Shortest path for graphs with non-negative weights.
- **Link State Algorithm**: Shortest path even with negative weights.

## Algorithms they constitute
- **Dijkstra's Algorithm**: Shortest path for graphs with non-negative weights.
- **Bellman-Ford Algorithm**: Shortest path even with negative weights.
- **Algorithms**: Optimized implementations on different topologies.

The simulation evaluates these algorithms on diverse network topologies (linear, star, mesh, ring, tree, grid, and hybrid). Key performance metrics—**latency**, **throughput**, **routing overhead**, and **network utilization**—are calculated to compare the efficiency and adaptability of the algorithms under varying network conditions.

---

## **Features**
1. **Simulation of Topologies**:
   - Linear
   - Star
   - Mesh
   - Ring
   - Tree
   - Grid
   - Hybrid

2. **Performance Metrics**:
   - **Latency (ms)**: Average time for data to travel between nodes.
   - **Throughput (Mbps)**: Rate of successful data delivery.
   - **Routing Overhead (packets)**: Total control message overhead for routing.
   - **Network Utilization (%)**: Percentage of bandwidth used effectively.

## Setup

### Prerequisites

- Python 3.8+
- NumPy
- more (yet to be decided)

To install dependencies, run:
```bash
pip install networkx matplotlib
```

### Installation

```bash
git clone https://github.com/YourGitHub/CSE514_RoutingAlgorithms.git
cd CSE_514_rpp5524
```
Install dependencies
```bash
pip install -r requirements.txt
```

## Analysis
For detailed results, see the final project report in the docs directory.

## Extending the Project
- Add Custom Topologies: Add a new topology in network_topologies.py by extending the NetworkTopology class.

- Implement New Algorithms: Create a new routing algorithm class in routing_algorithms.py and implement its logic.

- Experiment with Parameters: Modify link weights, node density, or packet transmission rates to test algorithm behavior under different conditions.

## Contributors
- [Rohan Prasad](https://github.com/rpp5524)


