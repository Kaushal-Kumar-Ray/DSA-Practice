class Solution:
    def minimumPlatform(self, arr, dep):
        arr.sort()
        dep.sort()

        n = len(arr)
        i = 1
        j = 0

        platforms_needed = 1
        max_platforms = 1

        while i < n and j < n:
            if arr[i] <= dep[j]:
                platforms_needed += 1
                i += 1
            else:
                platforms_needed -= 1
                j += 1

            max_platforms = max(max_platforms, platforms_needed)

        return max_platforms

# 🚀 User Input Section
arr_input = input("Enter arrival times (24hr format, space-separated, e.g., 900 940 950): ")
dep_input = input("Enter departure times (24hr format, space-separated, e.g., 910 1200 1120): ")

# Convert input strings to integer lists
arr = list(map(int, arr_input.strip().split()))
dep = list(map(int, dep_input.strip().split()))

# Check lengths match
if len(arr) != len(dep):
    print("Error: Arrival and departure lists must be of the same length.")
else:
    sol = Solution()
    result = sol.minimumPlatform(arr, dep)
    print("Minimum number of platforms required:", result)
