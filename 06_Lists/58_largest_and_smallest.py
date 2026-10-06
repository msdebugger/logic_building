"""
Q58: Find largest & smallest without built-ins Find the largest and smallest number in a list without using built-in functions like max() or min(). Hint: use a loop and a variable to track the current largest/smallest as you go through the list. Example: if the list is [3, 1, 4, 1, 5], the largest is 5 and smallest is 1.
"""
nums = [0, 1, 4, 1, 50]

smallest = nums[0]
largest = nums[0]

for i in range(len(nums)):
    if nums[i] > largest:
        largest = nums[i]

    if nums[i] < smallest:
        smallest = nums[i]
print(smallest)                
print(largest)