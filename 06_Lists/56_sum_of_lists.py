"""
Q56: Element-wise Sum of Two Lists Given two lists of the same length, write Python code using a loop to create a new list where each element is the sum of the corresponding elements from both original lists.
"""

nums1 = [10, 20, 30, 40, 50]
nums2 = [20, 30, 40, 50, 60]
nums = []

for i in range(len(nums1)):
    total = nums1[i] + nums2[i]
    nums.append(total)
print(nums)    