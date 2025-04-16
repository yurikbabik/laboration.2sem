def has_cycle(graph):
    visited = set()

    def dfs(vertex, parent):
        visited.add(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                if dfs(neighbor, vertex):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True
    return False


def read_graph(filename):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = list(map(int, line.strip().split()))
            node = parts[0]
            neighbors = parts[1:]
            graph[node] = neighbors
    return graph


def write_result(filename, result):
    with open(filename, 'w') as file:
        file.write(str(result))


if __name__ == "__main__":
    graph = read_graph('input.txt')
    result = has_cycle(graph)
    write_result('output.txt', result)
