class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        res = [-1] * n  # default is -1
        stack = []
        
        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            # Pop smaller or equal elements from stack
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            
            # If stack not empty, top is next greater
            if stack:
                res[i] = stack[-1]
            
            # Push current element to stack
            stack.append(arr[i])
        
        return res


# Example usage
arr = [1, 3, 2, 4]
sol = Solution()
print(sol.nextLargerElement(arr))  # Output: [3, 4, 4, -1]
