class Solution:
    def missingNum(self, arr):
        n = len(arr) + 1  # Because one number is missing
        total = n * (n + 1) // 2
        return total - sum(arr)

# User input
user_input = input("Enter the array elements separated by spaces: ")
arr = list(map(int, user_input.strip().split()))

solution = Solution()
print("Missing number is:", solution.missingNum(arr))
