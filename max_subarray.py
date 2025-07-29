# Take input from the user
user_input = input("Enter integers separated by spaces: ")
arr = list(map(int, user_input.strip().split()))

# Kadane's Algorithm
max_sum = float('-inf')
current_sum = 0

for num in arr:
    current_sum += num
    if current_sum > max_sum:
        max_sum = current_sum
    if current_sum < 0:
        current_sum = 0

print("Maximum subarray sum is:", max_sum)

