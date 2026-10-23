"""
Q71: Given a 3x3 matrix, print only the main diagonal elements and replace everything else with an asterisk (*). Input: [[1,2,3],[4,5,6],[7,8,9]] -> Output rows: '1**', '*5*', '**9'.
"""
nums = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(nums)):
    for j in range(len(nums[i])):
        if i != j:
            nums[i][j] = "*"

for row in nums:
    print("".join(map(str, row)))       
