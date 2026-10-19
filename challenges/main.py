# Read n
n = int(input())

# Read the list of numbers
# Convert the space-separated string of numbers into a list of integers
nums_str = input().split()
nums = [int(x) for x in nums_str]

# Your code to find the missing number goes here
# Hint: Think about the sum of numbers in the full range [0, n] and the sum of numbers in the given list.
for i in range(n + 1):
    if i not in nums:
        print(i)
        break

# Print the missing number
# print(missing_number)