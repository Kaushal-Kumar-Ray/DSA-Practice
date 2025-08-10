class Solution:
    def knapsack(self, W, val, wt):
        n = len(val)
        dp = [[0] * (W + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(1, W + 1):
                if wt[i-1] <= w:  
                    dp[i][w] = max(val[i-1] + dp[i-1][w - wt[i-1]], dp[i-1][w])
                else:
                    dp[i][w] = dp[i-1][w]

        return dp[n][W]


# Taking user input
W = int(input("Enter knapsack capacity: "))
n = int(input("Enter number of items: "))

val = list(map(int, input("Enter values: ").split()))
wt = list(map(int, input("Enter weights: ").split()))

solution = Solution()
result = solution.knapsack(W, val, wt)
print("Maximum value:", result)
