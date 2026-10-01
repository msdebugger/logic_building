"""
Q53: Find the Largest Element Given a list of numbers, write Python code using a loop to find and print the largest element. Do not use the built-in max() function.
"""

nums = [1, 9, 7, 3, 2, 10]

largest = 0
for i in range(1, len(nums)):
    if nums[i] > largest:
        largest = nums[i]
print(largest)


