import pandas as pd
import networkx as nx
import numpy as np

# Step 1: Load dataset info
df = pd.DataFrame([
    ('Facebook Northwestern University', '', 'socfb-Northwestern25/socfb-Northwestern25.edges.gz'),
    ('IMDB movies and actors', '', 'imdb/actors_movies.edges.gz'),
    ('IMDB actors costar', 'W', 'imdb/actors_costar.edges.gz'),
    ('Twitter US politics', 'DW', 'icwsm_polarization/retweet-digraph.edges.gz'),
    ('Enron Email', 'DW', 'email-Enron/email-Enron.edges.gz'),
    ('Enron Executive Email', '', 'ia-enron-only/ia-enron-only.edges'),
    ('Wikipedia math', 'D', 'enwiki_math/enwiki_math.edges.gz'),
    ('Internet routers', '', 'tech-RL-caida/tech-RL-caida.edges.gz'),
    ('US air transportation', '', 'openflights/openflights_usa.edges.gz'),
    ('World air transportation', '', 'openflights/openflights_world.edges.gz'),
    ('Yeast protein interactions', '', 'bio-yeast-protein-inter/bio-yeast-protein-inter.edges'),
    ('C. elegans brain', 'DW', 'celegansneural/celegansneural.edges'),
    ('Everglades ecological food web', 'DW', 'eco-everglades/eco-everglades.edges'),
], columns=['Name', 'Type', 'File'])

# Step 2: Load Wikipedia math network
file_path = df[df['Name'] == 'Wikipedia math']['File'].values[0]
G = nx.read_edgelist(file_path, create_using=nx.DiGraph())

# Step 3: Basic properties
n_nodes = G.number_of_nodes()
n_edges = G.number_of_edges()

# 1. Average in-degree and out-degree
avg_in = n_edges / n_nodes
avg_out = avg_in  # always equal in directed graphs

print(f"1. Average in-degree: {avg_in:.2f}")
print(f"   Average out-degree: {avg_out:.2f}")
print("   ➤ These are always equal in directed graphs because each edge adds one in and one out.")

# 2. Node with highest in-degree
in_deg = dict(G.in_degree())
max_in_node = max(in_deg, key=in_deg.get)
print(f"\n2. Node with highest in-degree: {max_in_node} ({in_deg[max_in_node]} incoming links)")

# 3. Node with highest out-degree
out_deg = dict(G.out_degree())
max_out_node = max(out_deg, key=out_deg.get)
print(f"\n3. Node with highest out-degree: {max_out_node} ({out_deg[max_out_node]} outgoing links)")

# 4. Compare max in-degree and out-degree
max_in = max(in_deg.values())
max_out = max(out_deg.values())
print(f"\n4. Max in-degree: {max_in}")
print(f"   Max out-degree: {max_out}")
print("   ➤ Usually, web graphs show higher in-degrees for popular pages, due to many inbound links.")

# 5. In-degree heterogeneity
in_deg_values = np.array(list(in_deg.values()))
H_in = np.sqrt(np.mean(in_deg_values**2)) / np.mean(in_deg_values)
print(f"\n5. In-degree heterogeneity: {H_in:.2f}")

# 6. Out-degree heterogeneity
out_deg_values = np.array(list(out_deg.values()))
H_out = np.sqrt(np.mean(out_deg_values**2)) / np.mean(out_deg_values)
print(f"6. Out-degree heterogeneity: {H_out:.2f}")
