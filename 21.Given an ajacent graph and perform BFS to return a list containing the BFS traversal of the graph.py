from collections import deque

class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        V = len(adj)
        visited = [False] * V
        q = deque()
        result = []

        # Start from vertex 0
        q.append(0)
        visited[0] = True

        while q:
            node = q.popleft()
            result.append(node)

            # Traverse neighbors in the same order as given
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    q.append(nei)

        return result


# Example usage with user input:
V = int(input("Enter number of vertices: "))
adj = []
for i in range(V):
    row = list(map(int, input(f"Enter neighbors of vertex {i}: ").split()))
    adj.append(row)

sol = Solution()
print("BFS Traversal:", sol.bfs(adj))
