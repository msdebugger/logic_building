"""
Q78: Write a function get_stats(nums) that takes a tuple of numbers
and returns a tuple containing the sum, average, minimum, and maximum.
Unpack the returned tuple and print each value.
"""

def get_stats(nums):
    total = sum(nums)
    average = total / len(nums)
    minimum = min(nums)
    maximum = max(nums)

    return (total, average, minimum, maximum)


nums = (10, 20, 30, 40, 50)

total, average, minimum, maximum = get_stats(nums)

print("Sum:", total)
print("Average:", average)
print("Minimum:", minimum)
print("Maximum:", maximum)