"""
Q77: Take 5 numbers as input from the user, store them in a tuple, and print the tuple along with its minimum and maximum  
"""

nums = []

for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    nums.append(num)

numbers = tuple(nums)

print("Tuple:", numbers)
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))