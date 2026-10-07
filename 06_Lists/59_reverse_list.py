"""
Q59: Reverse a list manually Reverse a list without using the .reverse() method or list slicing ([::-1]). Hint: swap elements from both ends of the list using a loop. Example: [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1].
"""

nums = [1, 2, 3, 4, 5]

i = 0
j = len(nums)-1

for i in range(len(nums) // 2):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

    j -= 1

print(nums)