class Solution:
    # Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        total_sum = sum(arr)
        left_sum = 0

        for i in range(len(arr)):
            # total_sum - arr[i] is now the sum on the right of index i
            if left_sum == total_sum - left_sum - arr[i]:
                return i  # index where left_sum == right_sum
            left_sum += arr[i]

        return -1  # if no equilibrium index is found
arr = list(map(int, input("Enter array elements separated by space: ").split()))
sol = Solution()
res = sol.findEquilibrium(arr)
print("Equilibrium Index:" if res != -1 else "No Equilibrium Point", res)
