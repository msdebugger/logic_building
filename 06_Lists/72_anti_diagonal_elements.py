"""
Q72: Given a 3x3 matrix, print only the anti-diagonal (top-right to bottom-left) elements and replace everything else with an asterisk (*). Input: [[1,2,3],[4,5,6],[7,8,9]] -> Output rows: '**3', '*5*', '7**'.
"""
nums = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(nums)):
    for j in range(len(nums[i])):
        if i + j != len(nums-1):
            nums[i][j] = "*"

for row in nums:
    print("".join(map(str, row)))       
