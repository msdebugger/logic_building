"""
Q73: Given a 4x4 matrix, print only the border elements and replace the inner elements with an asterisk (*). Input rows 1-4,5-8,9-12,13-16 -> Output rows: '1 2 3 4', '5 * * 8', '9 * * 12', '13 14 15 16'.
"""

nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

for i in range(len(nums)):
    for j in range(len(nums[i])):
        if not (i == 0 or i == len(nums) - 1 or j == 0 or j == len(nums[i]) - 1):
            nums[i][j] = "*"

for row in nums:
    print(*row)