class Solution:
    def sort012(self, arr):
        low = 0
        mid = 0
        high = len(arr) - 1

        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:  # arr[mid] == 2
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
        return arr

# 🚀 User input
user_input = input("Enter array elements (only 0s, 1s, and 2s) separated by spaces: ")
arr = list(map(int, user_input.strip().split()))

# ✅ Run the sort
solution = Solution()
sorted_arr = solution.sort012(arr)

print("Sorted array:", sorted_arr)
