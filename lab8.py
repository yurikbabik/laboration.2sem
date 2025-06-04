import csv
import matplotlib.pyplot as plt
import networkx as nx

class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            self.parent[root2] = root1
            return True
        return False

def read_communication_data(filename):
    edges = []
    nodes = set()
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 3:
                continue
            k1, k2, dist = row[0].strip(), row[1].strip(), int(row[2].strip())
            edges.append((dist, k1, k2))
            nodes.update([k1, k2])
    return list(nodes), edges

def bubble_sort_edges(edges):
    n = len(edges)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (edges[j][0], edges[j][1], edges[j][2]) > (edges[j + 1][0], edges[j + 1][1], edges[j + 1][2]):
                edges[j], edges[j + 1] = edges[j + 1], edges[j]

def draw_graph(title, edges, highlight_edges=None):
    G = nx.Graph()
    for dist, k1, k2 in edges:
        G.add_edge(k1, k2, weight=dist)

    pos = nx.spring_layout(G)
    edge_labels = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}

    plt.figure(figsize=(8, 6))
    plt.title(title)


    nx.draw(G, pos, with_labels=True, node_color="skyblue", edge_color="gray", node_size=1500, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)


    if highlight_edges:
        mst_edges = [(k1, k2) for (k1, k2, _) in highlight_edges]
        nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color="red", width=3)

    plt.show()

def minimum_fiber_length(filename):
    nodes, edges = read_communication_data(filename)

    print("Оригінальний граф (ребра):")
    for dist, k1, k2 in edges:
        print(f"{k1} - {k2} : {dist}")

    draw_graph("Оригінальний граф", edges)

    uf = UnionFind(nodes)
    total_length = 0
    edge_count = 0
    mst_edges = []

    bubble_sort_edges(edges)

    for dist, k1, k2 in edges:
        if uf.union(k1, k2):
            total_length += dist
            edge_count += 1
            mst_edges.append((k1, k2, dist))
            if edge_count == len(nodes) - 1:
                break

    if edge_count != len(nodes) - 1:
        print("Неможливо з’єднати всі колодязі.")
        return -1

    print("\nМінімальне остовне дерево (ребра):")
    for k1, k2, dist in mst_edges:
        print(f"{k1} - {k2} : {dist}")

    draw_graph("Мінімальне остовне дерево (Крускал)", edges, highlight_edges=mst_edges)

    return total_length


if __name__ == "__main__":
    filename = "test_data.csv"
    result = minimum_fiber_length(filename)
    if result != -1:
        print(f"\nМінімальна довжина кабелю: {result}")










