import networkx as nx
import numpy as np

G = nx.read_edgelist(r"D:\Koblenz\Sem1\NTDS\Assignments\Assignment 07-08\socfb-Northwestern25.edgelist", nodetype=int, create_using=nx.Graph())

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
print(f"Facebook Graph - Nodes: {num_nodes}, Edges: {num_edges}")

G_random = nx.gnm_random_graph(num_nodes, num_edges)
print(f"Random Graph - Nodes: {G_random.number_of_nodes()}, Edges: {G_random.number_of_edges()}")

# -------------------------------------------------
# Get degrees of all nodes in the random graph
degrees = [d for n, d in G_random.degree()]

# Compute the 95th percentile
percentile_95 = np.percentile(degrees, 95)

print(f"95th percentile degree in the random network: {percentile_95}")

# --------------------------------------------------
avg_clustering = nx.average_clustering(G_random)
print(f"Average clustering coefficient of the random network: {avg_clustering:.4f}")
