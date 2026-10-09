"""
Q61: Remove duplicates, preserve order Given a list, remove all duplicate elements while preserving the original order of the unique items. Example: data = [10, 20, 30, 20, 10, 40, 50, 40] -> [10, 20, 30, 40, 50].
"""
nums = [10, 20, 30, 10, 40, 50, 40]


# data = []

# for i in range(len(nums)):
#     if nums[i] not in data:
#         data.append(nums[i])
# print(data)        

i = 0
while i < len(nums):
    if nums[i] in nums[:i]:
        nums.pop(i)
    else: 
        i += 1    

print(nums)


