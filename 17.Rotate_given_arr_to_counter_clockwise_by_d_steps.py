class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n  # handle cases where d > n

        # Step 1: Reverse first d elements
        arr[:d] = reversed(arr[:d])
        # Step 2: Reverse the remaining elements
        arr[d:] = reversed(arr[d:])
        # Step 3: Reverse the whole array
        arr[:] = reversed(arr)

# 🚀 Taking user input
arr = list(map(int, input("Enter array elements: ").split()))
d = int(input("Enter rotation steps: "))

sol = Solution()
sol.rotateArr(arr, d)
print("Rotated Array:", arr)
