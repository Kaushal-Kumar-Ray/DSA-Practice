class Solution:
    def minJumps(self, arr):
        n = len(arr)
        if n <= 1:
            return 0
        jumps = 0
        m_range = 0
        c_range = 0
        for i in range(n - 1):
            m_range = max(m_range, arr[i] + i)
            if i == c_range:
                if m_range <= i:
                    return -1
                jumps += 1
                c_range = m_range
        return jumps

# Input from user
arr = list(map(int, input("Enter array: ").split()))

# Call the function
print("Minimum jumps:", Solution().minJumps(arr))
