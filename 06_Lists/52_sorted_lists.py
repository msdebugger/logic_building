"""
Q52: Sorted Lists
Create a list of numbers (e.g., [5, 2, 8, 1, 9, 3]). Print the list in ascending order and then in descending order using the sorted() function. After printing, verify and print the original list to confirm it remains unchanged.

"""

nums = [1, 8, 9, 3, 6]

print(sorted(nums))
print(sorted(nums, reverse=True))

print(nums)