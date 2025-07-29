from typing import List

class Solution:
    def subarraySum(self, arr: List[int], target: int) -> List[int]:
        left = 0
        current_sum = 0

        for right in range(len(arr)):
            current_sum += arr[right]

            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1

            if current_sum == target:
                return [left , right ]

        return [-1]

# 🚫 No __main__ block
user_input = input("Enter numbers separated by spaces: ")
arr = list(map(int, user_input.strip().split()))
target = int(input("Enter the target sum: "))

solution = Solution()
result = solution.subarraySum(arr, target)

print(f"Subarray that sums to {target}: {result}")
