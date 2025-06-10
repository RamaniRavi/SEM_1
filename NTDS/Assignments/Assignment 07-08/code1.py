import networkx as nx
import random

# Load the Facebook graph
G = nx.read_edgelist(r"D:\Koblenz\Sem1\NTDS\Assignments\Assignment 07-08\socfb-Northwestern25.edgelist", nodetype=int, create_using=nx.Graph())

# Use the largest connected component to avoid "no path" errors
if not nx.is_connected(G):
    largest_cc = max(nx.connected_components(G), key=len)
    G = G.subgraph(largest_cc).copy()

# Step 1: Get node list
nodes = list(G.nodes())

# Step 2: Randomly sample 1000 unique node pairs
sampled_pairs = random.sample([(u, v) for u in nodes for v in nodes if u < v], 1000)

# Step 3: Compute shortest path lengths for each pair
path_lengths = []
for u, v in sampled_pairs:
    try:
        length = nx.shortest_path_length(G, source=u, target=v)
        path_lengths.append(length)
    except nx.NetworkXNoPath:
        continue  # skip if no path exists

# Step 4: Compute average
if path_lengths:
    avg_length = sum(path_lengths) / len(path_lengths)
    print(f"Estimated average shortest path length: {avg_length:.4f}")
else:
    print("No valid paths found in the sample.")

