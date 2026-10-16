"""
Q69: Given a 3x3 matrix as input, print its lower triangle. Replace all elements in the upper triangle (above the main diagonal) with an asterisk (*). Input: [[1,2,3],[4,5,6],[7,8,9]] -> Output rows: '1**', '45*', '789'.
"""

nums = [[1,2,3],
        [4,5,6],
        [7,8,9]]

for i in range(len(nums)):
    for j in range(len(nums[i])):
        if j > i:
            print("*", end="")
        else:
            print(nums[i][j], end="")
    print()    


