"""
Q66: Using list comprehension, create a list of squares of all odd numbers from 1 to 20. Expected output: [1, 9, 25, 49, 81, 121, 169, 225, 289, 361].
"""



nums = [i * i for i in range(1, 21) if i % 2 == 1]
print(nums)
    