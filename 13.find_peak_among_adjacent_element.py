class Solution:   
    def peakElement(self, arr):
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Get neighbors safely using -inf for out-of-bound
            left = arr[mid - 1] if mid - 1 >= 0 else float('-inf')
            right = arr[mid + 1] if mid + 1 < len(arr) else float('-inf')
            
            if arr[mid] >= left and arr[mid] >= right:
                return mid  # Peak found
            
            elif arr[mid] < right:
                low = mid + 1
            else:
                high = mid - 1
arr = [10, 20, 15, 2, 23, 90, 80]
sol = Solution()
index = sol.peakElement(arr)
print("true" if (index == 0 or index == len(arr) - 1 or arr[index] > arr[index - 1] and arr[index] > arr[index + 1]) else "false")
