class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        if n == 1:
            return 0

        arr.sort()  # Step 1: Sort the array

        # Step 2: Initialize result with max difference before any changes
        result = arr[-1] - arr[0]

        # Step 3: Try modifying elements with +k and -k and track the min diff
        for i in range(1, n):
            if arr[i] - k < 0:
                continue  # Skip if subtraction makes value negative

            min_elem = min(arr[0] + k, arr[i] - k)
            max_elem = max(arr[i - 1] + k, arr[-1] - k)
            result = min(result, max_elem - min_elem)

        return result
user_input = input("Enter tower heights separated by spaces: ")
arr = list(map(int, user_input.strip().split()))
k = int(input("Enter the value of k: "))

sol = Solution()
print("Minimum possible difference:", sol.getMinDiff(arr, k))
