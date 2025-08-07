class Solution:
    def perfectSum(self, arr, target):
        n = len(arr)
        
        # Initialize DP table
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        
        # There's one subset (empty set) for sum = 0
        for i in range(n + 1):
            dp[i][0] = 1
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(target + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - arr[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[n][target]
# 🚀 User Input
arr_input = input("Enter array elements (space-separated): ")
target = int(input("Enter target sum: "))

arr = list(map(int, arr_input.strip().split()))
sol = Solution()
print("Number of subsets with sum equal to target:", sol.perfectSum(arr, target))
