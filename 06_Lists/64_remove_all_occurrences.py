"""
Q64: Remove all occurrences of a value Given a list of numbers (which may contain duplicates), write a Python script that takes an integer as input from the user and removes all occurrences of that integer from the list. Example: my_list = [10, 20, 10, 30, 20, 10, 40], if user enters 10 -> [20, 30, 20, 40].
"""

nums = [10, 20, 10, 30, 20, 10, 10]

target = int(input("Enter number: "))

i = 0

while i < len(nums):
    if nums[i] == target:
        nums.pop(i)
    else:
        i += 1

print(nums) 