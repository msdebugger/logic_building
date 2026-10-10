"""
Q62: Separate evens and odds Separate a list of integers into two distinct lists: one containing all the even numbers and the other containing all the odd numbers. Example: numbers = [1..10] -> evens = [2,4,6,8,10], odds = [1,3,5,7,9].
"""

nums = [10, 3, 4, 5, 30, 22]

evens = []
odds = []

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        evens.append(nums[i])
    else:
        odds.append(nums[i])

print(f"Even list: {evens}")            
print(f"Odds list: {odds}")            