class Solution:
    def majorityElement(self, arr):
        count = 0
        candidate = None

        # Phase 1: Find a candidate
        for num in arr:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        # Phase 2: Verify the candidate
        if arr.count(candidate) > len(arr) // 2:
            return candidate
        else:
            return -1


# 🔽 User input section
user_input = input("Enter array elements separated by spaces: ")
arr = list(map(int, user_input.strip().split()))

# 🔍 Use the class method to find majority element
solution = Solution()
result = solution.majorityElement(arr)

if result != -1:
    print("The majority element is:", result)
else:
    print("There is no majority element in the array.",result)
