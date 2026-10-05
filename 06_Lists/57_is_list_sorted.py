"""
Q57: Check if a List is Sorted Write a program that takes a list of numbers and, using a loop, determines whether it is sorted in ascending order. Print True if it is sorted, and False otherwise. Do not use built-in sort or sorted() functions for checking.

"""
nums = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    nums.append(num)

print(nums)    
is_sorted = True

for j in range(1, len(nums)):
    if nums[j - 1] > nums[j]:
        is_sorted = False
        break
print(is_sorted)