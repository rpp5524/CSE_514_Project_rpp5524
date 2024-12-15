from src.topology import NetworkTopology
from src.algorithms.distance_vector import DistanceVectorRouting
from src.algorithms.link_state import LinkStateRouting
from src.algorithms.path_vector import PathVectorRouting
from analysis.analyze import analyze_performance, analyze_complex_performance, analyze_utilization_performance, analyze_performance_pvr

import time

topology = NetworkTopology("mesh", 100)
topology.add_constant_weights(10)
# print("hello")
dvr = DistanceVectorRouting(topology.graph)
lsr = LinkStateRouting(topology.graph)
pvr = PathVectorRouting(topology.graph)

start_time = time.time()
result_dvr = dvr.run()
# result_lsr = lsr.run()

# result_pvr = pvr.run()
end_time = time.time()

# print("Distance Vector Results:", result_dvr)
# print("Distance Vector Results:", result_lsr)
# print("Distance Vector Results:", result_pvr)

# analyze_utilization_performance(topology.graph, result_dvr)
# analyze_utilization_performance(topology.graph, result_lsr)
analyze_utilization_performance(topology.graph, result_dvr)