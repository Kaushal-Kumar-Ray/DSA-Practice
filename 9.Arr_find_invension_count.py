class Solution:
    def inversionCount(self, arr):
        count = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    count += 1
        return count

# 🚀 Input from user
user_input = input("Enter array elements separated by space: ")
arr = list(map(int, user_input.strip().split()))

sol = Solution()
print("Inversion Count:", sol.inversionCount(arr))
