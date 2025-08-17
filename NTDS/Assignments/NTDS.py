import networkx as nx

# Load the graph
G = nx.read_graphml('D:\Koblenz\Sem1\WIR\Exercise\Assignment 02\enwiki_math.graphml', node_type=int)
if not isinstance(G, nx.DiGraph):
    G = nx.DiGraph(G)

# Function to compute heterogeneity parameter
def heterogeneity_parameter(degree_sequence):
    avg_k = sum(degree_sequence) / len(degree_sequence)
    avg_k_squared = sum(k**2 for k in degree_sequence) / len(degree_sequence)
    H = avg_k_squared / (avg_k ** 2)
    return H

# In-degree distribution
in_degrees = [d for n, d in G.in_degree()]
H_in = heterogeneity_parameter(in_degrees)

# Out-degree distribution
out_degrees = [d for n, d in G.out_degree()]
H_out = heterogeneity_parameter(out_degrees)

print(f"Heterogeneity (In-degree): {H_in:.4f}")
print(f"Heterogeneity (Out-degree): {H_out:.4f}")
