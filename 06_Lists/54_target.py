"""
Q54: Check for Target Existence Write a program that takes a list and a target number. Use a loop to determine if the target number exists in the list. Do not use the in operator.
"""

nums = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    nums.append(num)
print(nums)
target = int(input("Enter target number: "))

found = False

for i in nums:
    if i == target:
        found = True 
        break


if found == True:
    print("Element exists")
else:
    print("Element does not exists")    

