from collections import defaultdict

class Solution:
    def isCycle(self, V, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * V

        def dfs(node, parent):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
            return False

        for i in range(V):
            if not visited[i]:
                if dfs(i, -1):
                    return True
        return False


# 🔽 User Input Section
V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

edges = []
print("Enter the edges (u v) one per line:")
for _ in range(E):
    u, v = map(int, input().split())
    edges.append([u, v])

# 🚀 Check for cycle
sol = Solution()
has_cycle = sol.isCycle(V, edges)
print("Cycle detected!" if has_cycle else "No cycle in the graph.")
