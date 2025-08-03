def isCycle(V, edges):
    from collections import defaultdict

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for i in range(V):
        if i not in visited:
            if dfs(i, -1):
                return True
    return False

# 💻 Input
V = 4
edges = [[0, 1], [0, 2], [1, 2], [2, 3]]

# 🚀 Output
print("Cycle found!" if isCycle(V, edges) else "No cycle.")
