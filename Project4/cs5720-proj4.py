import os
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
from heapq import heappop, heappush

# Load graphs and perform basic analysis
def count_nodes_and_edges(file_path):
    graph_matrix = pd.read_csv(file_path, header=None)
    num_nodes = graph_matrix.shape[0]
    num_edges = (graph_matrix != -1).sum().sum() // 2  # Undirected graph
    return num_nodes, num_edges

# graphs the relationship between the size of the node and edge sets
def graph_relationship(edges, nodes, type):
    plt.plot(nodes, edges, linestyle='None', marker='o')
    plt.ylabel("Number of Edges")
    plt.xlabel("Number of Vertices")
    plt.title("Relationship between The Number of Edges and Nodes: " + type)
    plt.savefig("edge_vertex_relationship_"+ type)
    plt.close()

# graphs the relationship between the size of the node and edge sets as compared to the max number of edges possible
def graph_relationship_max(edges, nodes, max_edges, type):
    plt.plot(nodes, edges, linestyle='None', marker='o')
    plt.plot(nodes, max_edges, linestyle='None', marker='o', color='red')
    plt.ylabel("Number of Edges")
    plt.xlabel("Number of Vertices")
    plt.title("Relationship between The Number of Edges and Nodes Compared to Max Edges: " + type)
    plt.savefig("edge_vertex_max_relationship_"+ type)
    plt.close()

# Prim's Algorithm (Adjacency Matrix + Unordered Priority Queue)
def prim_mst(matrix):
    n = len(matrix)  # Number of vertices
    visited = [False] * n   # Track visited nodes
    mst_weight = 0          # Total weight of the MST
    edge_list = []          # Unordered array-based priority queue

    # Start from the first node (index 0)
    visited[0] = True
    for j in range(n):
        if matrix[0][j] != -1:  # Add all edges from the first node
            edge_list.append((matrix[0][j], 0, j))  # (weight, from, to)

    while edge_list:
        # Find the minimum weight edge in the unordered edge list
        min_weight, u, v = min(edge_list, key=lambda x: x[0])
        edge_list.remove((min_weight, u, v))  # Remove the selected edge from the list

        # Skip if the target node is already visited
        if visited[v]:
            continue

        # Add the edge to the MST
        mst_weight += min_weight
        visited[v] = True

        # Add all edges from the newly added vertex
        for w in range(n):
            if not visited[w] and matrix[v][w] != -1:
                edge_list.append((matrix[v][w], v, w))

    return mst_weight

# Kruskal's Algorithm
def kruskal_mst(matrix):
    num_nodes = len(matrix)
    edges = []
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if matrix[i][j] != -1:
                edges.append((matrix[i][j], i, j))
    edges.sort()
    parent = list(range(num_nodes))

    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        root_x, root_y = find(x), find(y)
        if root_x != root_y:
            parent[root_y] = root_x

    total_weight = 0
    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            total_weight += weight
    return total_weight

# Timing Analysis
def timing_analysis(func, matrix):
    start = time.time()
    func(matrix)
    return time.time() - start

# Paths and Setup
data_path = "graphs"
results = {"Graph": [], "Nodes": [], "Edges": [], "Prim MST": [], "Kruskal MST": [], "Prim Time": [], "Kruskal Time": []}

for graph_type in ["type-1", "type-2", "type-3"]:
    type_path = os.path.join(data_path, graph_type.replace("-", "_"))
    node_set = []
    edge_set = []
    max_edges = []
    for file_name in os.listdir(type_path):
        graph_path = os.path.join(type_path, file_name)
        graph_matrix = pd.read_csv(graph_path, header=None).to_numpy()
        
        nodes, edges = count_nodes_and_edges(graph_path)
        node_set.append(nodes)
        edge_set.append(edges)
        max_edges.append(0.5*nodes*(nodes-1))
        
        prim_weight = prim_mst(graph_matrix)
        kruskal_weight = kruskal_mst(graph_matrix)
        prim_time = timing_analysis(prim_mst, graph_matrix)
        kruskal_time = timing_analysis(kruskal_mst, graph_matrix)
        
        results["Graph"].append(f"{graph_type} - {file_name}")
        results["Nodes"].append(nodes)
        results["Edges"].append(edges)
        results["Prim MST"].append(prim_weight)
        results["Kruskal MST"].append(kruskal_weight)
        results["Prim Time"].append(prim_time)
        results["Kruskal Time"].append(kruskal_time)

    graph_relationship(edge_set, node_set, graph_type)
    graph_relationship_max(edge_set, node_set, max_edges, graph_type)

# Save Results
results_df = pd.DataFrame(results)
results_df = results_df.sort_values(by="Graph")
results_df.to_csv("graph-analysis-results.csv", index=False)

# Plotting
for graph_type in ["type-1", "type-2", "type-3"]:
    subset = results_df[results_df["Graph"].str.contains(graph_type)]

    plt.figure()
    plt.title(f"Timing Analysis: {graph_type}")
    plt.plot(subset["Graph"], subset["Prim Time"], label="Prim")
    plt.plot(subset["Graph"], subset["Kruskal Time"], label="Kruskal")
    plt.xlabel("Graph")
    plt.ylabel("Time (s)")
    plt.legend()
    plt.xticks(rotation=45, fontsize=8)
    plt.tight_layout()
    plt.savefig(f"timing-analysis-{graph_type}.png")
