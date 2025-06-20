import networkx as nx

def average_neighbor_degree(G, node):
    neighbors = list(G.neighbors(node))
    if not neighbors:
        return 0
    neighbor_degrees = [G.degree(n) for n in neighbors]
    return sum(neighbor_degrees) / len(neighbor_degrees)

graph_path = "openflights_usa.graphml"
G = nx.read_graphml(graph_path)

average_node_degree = sum(dict(G.degree()).values()) / G.number_of_nodes()
average_neighbor_degrees = [average_neighbor_degree(G, node) for node in G.nodes()]
average_neighbor_degree_overall = sum(average_neighbor_degrees) / len(average_neighbor_degrees)

# Print results
print(f"Average node degree: {average_node_degree:.2f}")
print(f"Average neighbor degree: {average_neighbor_degree_overall:.2f}")

if average_neighbor_degree_overall > average_node_degree:
    print("The Friendship Paradox holds: neighbors tend to have more connections.")
else:
    print("The Friendship Paradox does not hold in this case.")
