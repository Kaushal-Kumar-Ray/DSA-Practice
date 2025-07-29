import heapq

class Solution:

    def kthSmallest(self, arr, k):
        # Convert arr to a min-heap
        heapq.heapify(arr)

        # Pop k-1 smallest elements
        for _ in range(k - 1):
            heapq.heappop(arr)

        # The k-th smallest is now on top
        return heapq.heappop(arr)
user_input = input("Enter array elements: ")
arr = list(map(int, user_input.strip().split()))
k = int(input("Enter k: "))

sol = Solution()
print("K-th smallest element is:", sol.kthSmallest(arr, k))
