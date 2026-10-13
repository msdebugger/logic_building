"""
Q65: Replace negatives with 0 Write a Python script that iterates through a list of integers and replaces every negative number found in the list with the value 0. Example: numbers = [5, -3, 8, -1, 0, -10, 12] -> [5, 0, 8, 0, 0, 0, 12].

"""

nums = [5, -3, 8, -1, 0, -10, 12]


for i in range(len(nums)):
    if nums[i] < 0:
        nums[i] = 0
print(nums)        