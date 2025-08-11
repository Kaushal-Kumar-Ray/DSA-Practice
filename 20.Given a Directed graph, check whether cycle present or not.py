class Solution:
    def isCycle(self, V, edges):
        # Build adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)

        visited = [0] * V  # 0 = unvisited, 1 = visiting, 2 = visited

        def dfs(node):
            if visited[node] == 1:  # Found a back edge → cycle
                return True
            if visited[node] == 2:  # Already processed → no cycle here
                return False

            visited[node] = 1  # Mark as visiting
            for nei in adj[node]:
                if dfs(nei):
                    return True
            visited[node] = 2  # Mark as fully processed
            return False

        for i in range(V):
            if visited[i] == 0:
                if dfs(i):
                    return True
        return False


# --- User Input ---
V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))
edges = []
print("Enter each edge as: u v")
for _ in range(E):
    u, v = map(int, input().split())
    edges.append((u, v))

sol = Solution()
print("Cycle Present?" , sol.isCycle(V, edges))


"""
Enter number of vertices: 4
Enter number of edges: 4
Enter each edge as: u v
0 1
1 2
2 0
2 3
Cycle Present? True


"""