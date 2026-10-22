"""
Q70: Given a 3x3 matrix, print its upper triangle. Replace all elements in the lower triangle (below the main diagonal) with an asterisk (*). Input: [[1,2,3],[4,5,6],[7,8,9]] -> Output rows: '123', '*56', '**9'.
"""

nums = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(nums)):
    for j in range(len(nums[i])):
        if j < i:
            nums[i][j] = "*"

for row in nums:
    print("".join(map(str, row)))
