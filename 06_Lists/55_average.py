"""
Q55: Calculate the Average Given a list of numbers, use a loop to calculate and print their average. You can use len() to get the count of elements, but avoid using sum() for the total. Format the average to two decimal places.

"""

nums = [3, 4, 60, 40, 50]

total = 0

for i in nums:
    total+= i
average = total/len(nums)
print(f"Total is {total}, and Average is {average:.2f}")        
